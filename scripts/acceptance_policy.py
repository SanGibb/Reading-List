"""Mechanical checks for selective collection policy v2; historical runs stay intact."""

from __future__ import annotations

import json
from datetime import date, datetime, timedelta
from pathlib import Path
from typing import Any
from urllib.parse import urlparse


POLICY_VERSION = 2
EFFECTIVE_DATE = "2026-10-20"
BRANCHES = set("ABCDE")
MIN_ACCEPTANCE_SCORE = 4
OFFICIAL_SOURCES = {"primary", "official", "primary_or_official"}
SELECTION_BASES = {
    "new_capability", "substantial_improvement", "reusable_infrastructure", "decisive_evaluation"
}
TEMPORAL_MODALITIES = {"video", "gif", "interactive_demo"}
INSPECTION_MODALITIES = TEMPORAL_MODALITIES | {"paper_figure", "image"}
PLACEHOLDER_QUERIES = {
    "fixed follow sources", "newly influential 2024+ omissions", "broad primary-source search"
}


def nonempty(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def http_url(value: Any) -> bool:
    if not isinstance(value, str):
        return False
    parsed = urlparse(value)
    return parsed.scheme in {"http", "https"} and bool(parsed.netloc)


def timestamp(value: Any) -> bool:
    if not nonempty(value):
        return False
    try:
        return datetime.fromisoformat(value.replace("Z", "+00:00")).tzinfo is not None
    except ValueError:
        return False


def text_fields(obj: dict, fields: tuple[str, ...], label: str, errors: list[str]) -> None:
    for key in fields:
        if not nonempty(obj.get(key)):
            errors.append(f"{label} needs non-empty {key}")


def final_scores(obj: dict, label: str, errors: list[str]) -> None:
    for field in ("impact_score", "project_relevance_score", "evidence_strength"):
        value = obj.get(field)
        if type(value) is not int or not MIN_ACCEPTANCE_SCORE <= value <= 5:
            errors.append(f"{label} {field} must be an integer >= 4 and <= 5")


def validate_policy_paper(paper: dict, label: str, errors: list[str]) -> None:
    """Validate explicitly v2 registry entries without reclassifying older papers."""
    version = paper.get("acceptance_policy_version")
    if version is None:
        return
    if type(version) is not int or version != POLICY_VERSION:
        errors.append(f"{label} acceptance_policy_version must be 2")
        return
    text_fields(paper, ("title", "venue", "data", "method", "task", "novelty", "project_relevance"), label, errors)
    if type(paper.get("year")) is not int or paper["year"] < 2024:
        errors.append(f"{label} year must be >= 2024")
    if not http_url(paper.get("url")):
        errors.append(f"{label} needs a valid primary/official URL")
    final_scores(paper, label, errors)
    if paper.get("source_quality") not in OFFICIAL_SOURCES:
        errors.append(f"{label} source_quality must be primary or official")
    for key in ("requires_visual_review", "requires_temporal_demo"):
        if type(paper.get(key)) is not bool:
            errors.append(f"{label} {key} must be boolean")
    required = paper.get("requires_visual_review")
    temporal = paper.get("requires_temporal_demo")
    decision = paper.get("visual_quality_decision")
    score = paper.get("visual_quality_score")
    if temporal and not required:
        errors.append(f"{label} temporal demo requires visual review")
    if required:
        if decision not in {"strong", "adequate"}:
            errors.append(f"{label} requires strong or adequate visual quality")
        if type(score) is not int or score < 3 or score > 5:
            errors.append(f"{label} visual_quality_score must be >= 3 and <= 5")
        if decision == "strong" and (type(score) is not int or score < 4):
            errors.append(f"{label} strong visual quality requires score >= 4")
        if decision == "adequate" and score != 3:
            errors.append(f"{label} adequate visual quality requires score 3")
    elif required is False and (decision != "not_applicable" or type(score) is not int or score != 0):
        errors.append(f"{label} non-visual work needs not_applicable with score 0")


def validate_policy_run(run_id: str, artifacts: dict[str, dict], root: Path, errors: list[str]) -> None:
    """Enforce v2 on new runs, including zero-addition weeks and update/no-op runs."""
    plan = artifacts.get("00_run_plan.json", {})
    version = plan.get("acceptance_policy_version")
    if run_id < EFFECTIVE_DATE and version is None:
        return
    if type(version) is not int or version != POLICY_VERSION:
        errors.append(f"runs from {EFFECTIVE_DATE} require acceptance_policy_version: 2")
        return
    try:
        run_date = date.fromisoformat(run_id)
    except ValueError:
        errors.append("v2 run_id must be an ISO date")
        return
    if plan.get("follow_sources_path") != "data/follow_sources.seed.json":
        errors.append("v2 follow_sources_path must be data/follow_sources.seed.json")
    if plan.get("known_registry_path", "data/papers.seed.json") != "data/papers.seed.json":
        errors.append("v2 known_registry_path must be data/papers.seed.json")

    discovery = artifacts.get("01_discovery.json", {})
    evidence = artifacts.get("02_evidence.json", {})
    review = artifacts.get("03_review.json", {})
    patch = artifacts.get("05_registry_patch.json", {})
    candidates = discovery.get("candidates", [])
    triage = discovery.get("triage", [])
    paper_cards = evidence.get("paper_cards", [])
    visuals = review.get("visual_cards", [])
    reviews = review.get("quality_review", [])
    if not all(isinstance(items, list) for items in (candidates, triage, paper_cards, visuals, reviews)):
        return  # The structural validator reports malformed collections.

    def index(items: list, label: str) -> dict:
        result = {}
        for item in items:
            if not isinstance(item, dict) or not nonempty(item.get("candidate_id")):
                continue
            cid = item["candidate_id"]
            if cid in result:
                errors.append(f"duplicate {label} for {cid}")
            result[cid] = item
        return result

    candidate_map = index(candidates, "candidate")
    triage_map = index(triage, "triage")
    paper_map = index(paper_cards, "paper card")
    visual_map = index(visuals, "visual card")
    review_map = index(reviews, "quality review")
    if set(candidate_map) != set(triage_map):
        errors.append("v2 discovery needs exactly one triage decision per candidate")

    # Real execution logs distinguish broad discovery from a hand-picked final list.
    queries = discovery.get("query_log")
    if not isinstance(queries, list) or not queries:
        errors.append("v2 discovery needs a non-empty query_log")
        queries = []
    query_map: dict[str, dict] = {}
    covered: dict[str, set[str]] = {branch: set() for branch in BRANCHES}
    executed_queries: dict[str, set[str]] = {branch: set() for branch in BRANCHES}
    for query in queries:
        if not isinstance(query, dict):
            errors.append("query_log entries must be objects")
            continue
        qid = query.get("query_id")
        branch = query.get("branch")
        label = f"query {qid}"
        text_fields(query, ("query_id", "query", "stop_reason"), label, errors)
        if not nonempty(qid):
            continue
        if qid in query_map:
            errors.append(f"duplicate query_id: {qid}")
        query_map[qid] = query
        if branch not in BRANCHES:
            errors.append(f"{label} needs valid branch")
            continue
        text = query.get("query", "")
        if isinstance(text, str):
            if text.lower().strip() in PLACEHOLDER_QUERIES or "primary-source sweep" in text.lower():
                errors.append(f"{label} must record actual search terms, not a placeholder")
            executed_queries[branch].add(text)
        basis = query.get("date_basis")
        if basis not in {"submitted", "updated", "release", "backfill", "citation"}:
            errors.append(f"{label} has invalid date_basis")
        else:
            covered[branch].add(basis)
        if not http_url(query.get("source_url")) or not timestamp(query.get("executed_at")):
            errors.append(f"{label} needs source_url and timezone-aware executed_at")
        elif abs((datetime.fromisoformat(query["executed_at"].replace("Z", "+00:00")).date() - run_date).days) > 1:
            errors.append(f"{label} executed_at must be within one calendar day of the run")
        try:
            start = date.fromisoformat(query.get("date_from", ""))
            end = date.fromisoformat(query.get("date_to", ""))
            if start > end:
                raise ValueError
            if basis in {"submitted", "updated"} and (end - start).days < 13:
                errors.append(f"{label} must cover at least 14 calendar days")
            if basis == "release" and (end - start).days < 44:
                errors.append(f"{label} must cover at least 45 calendar days of releases")
            if basis in {"submitted", "updated", "release"} and not run_date - timedelta(days=1) <= end <= run_date:
                errors.append(f"{label} date_to must reach the run date or previous day")
        except (ValueError, TypeError):
            errors.append(f"{label} needs ordered ISO date_from/date_to")
        for field, minimum in (("results_reviewed", 0), ("pages_checked", 1)):
            value = query.get(field)
            if type(value) is not int or value < minimum:
                errors.append(f"{label} needs integer {field} >= {minimum}")
        ids = query.get("candidate_ids")
        if not isinstance(ids, list) or any(not isinstance(cid, str) or cid not in candidate_map for cid in ids):
            errors.append(f"{label} candidate_ids must refer to discovered candidates")
    branch_queries = plan.get("branch_queries", {})
    for branch in sorted(BRANCHES):
        planned = branch_queries.get(branch) if isinstance(branch_queries, dict) else None
        if not isinstance(planned, list) or not planned or any(not nonempty(q) for q in planned):
            errors.append(f"v2 branch {branch} needs actual branch_queries")
        elif any(q not in executed_queries[branch] for q in planned):
            errors.append(f"v2 branch {branch} has planned queries missing from query_log")
        if not {"submitted", "updated", "release"} <= covered[branch]:
            errors.append(f"v2 branch {branch} must check submitted, updated, and release windows")
    for cid, candidate in candidate_map.items():
        qid = candidate.get("query_id")
        query = query_map.get(qid) if isinstance(qid, str) else None
        if not query or cid not in query.get("candidate_ids", []):
            errors.append(f"candidate {cid} needs a bidirectional query_id trace")

    follow_path = root / "data/follow_sources.seed.json"
    try:
        follow = json.loads(follow_path.read_text())
    except (OSError, ValueError):
        errors.append("v2 cannot load follow-source coverage requirements")
        follow = {}
    core_ids = {
        item["id"] for collection in ("source_groups", "meta_sources")
        for item in follow.get(collection, []) if isinstance(item, dict) and item.get("priority") == "core"
    }
    checks = discovery.get("followed_sources_checked", [])
    seen_sources = set()
    for check in checks if isinstance(checks, list) else []:
        if not isinstance(check, dict):
            continue
        sid = check.get("source_id")
        if sid in seen_sources:
            errors.append(f"duplicate follow-source check: {sid}")
        seen_sources.add(sid)
        status = check.get("status")
        text_fields(check, ("notes",), f"follow source {sid}", errors)
        if status in {"checked", "spot_checked", "unreachable"}:
            urls = check.get("urls_checked")
            values = list(urls.values()) if isinstance(urls, dict) else urls
            if not isinstance(values, list) or not values or not all(http_url(url) for url in values):
                errors.append(f"follow source {sid} needs actual urls_checked")
            if not timestamp(check.get("checked_at")):
                errors.append(f"follow source {sid} needs timezone-aware checked_at")
        if status in {"checked", "spot_checked"} and not http_url(check.get("evidence_url")):
            errors.append(f"follow source {sid} needs evidence_url")
        if sid in core_ids and status in {"skipped", "unreachable"}:
            text_fields(check, ("retry_trigger",), f"follow source {sid}", errors)
    if missing := core_ids - seen_sources:
        errors.append(f"v2 follow-source coverage missing core groups: {', '.join(sorted(missing))}")

    for cid, item in triage_map.items():
        if item.get("decision") == "watchlist":
            text_fields(item, ("revisit_trigger",), f"watchlist {cid}", errors)
    for cid, visual in visual_map.items():
        if visual.get("visual_quality_decision") == "undecided":
            if visual.get("needs_human_decision") is not True:
                errors.append(f"undecided {cid} must set needs_human_decision true")
            if triage_map.get(cid, {}).get("decision") != "analyze":
                errors.append(f"undecided {cid} needs analyzed evidence and a local dossier")
            if cid not in paper_map:
                errors.append(f"undecided {cid} needs a paper evidence card")

    accepted = {cid for cid, item in review_map.items() if item.get("accepted_for_registry") is True}
    for cid in accepted:
        item = review_map[cid]
        label = f"accepted {cid}"
        final_scores(item, label, errors)
        text_fields(item, ("acceptance_rationale",), label, errors)
        if item.get("selection_basis") not in SELECTION_BASES:
            errors.append(f"{label} needs a concrete selection_basis")
        comparison = item.get("comparison_to_registry")
        if not isinstance(comparison, dict):
            errors.append(f"{label} needs comparison_to_registry")
        else:
            text_fields(comparison, ("closest_paper", "material_difference", "why_new_entry"), label, errors)
        if triage_map.get(cid, {}).get("source_quality") not in OFFICIAL_SOURCES:
            errors.append(f"{label} source_quality must be primary or official")
        card = paper_map.get(cid, {})
        visual = visual_map.get(cid, {})
        if not http_url(candidate_map.get(cid, {}).get("source_url")) or not http_url(card.get("url")):
            errors.append(f"{label} needs valid primary/official candidate and paper URLs")
        if visual.get("needs_human_decision") is True:
            errors.append(f"{label} cannot require a pending human decision")
        for key in ("requires_visual_review", "requires_temporal_demo"):
            if type(card.get(key)) is not bool:
                errors.append(f"paper card {cid} needs boolean {key}")
        synthetic_paper = dict(card, **{key: item.get(key) for key in ("impact_score", "project_relevance_score", "evidence_strength")})
        synthetic_paper.update({
            "acceptance_policy_version": 2,
            "source_quality": triage_map.get(cid, {}).get("source_quality"),
            "visual_quality_decision": visual.get("visual_quality_decision"),
            "visual_quality_score": visual.get("visual_quality_score"),
        })
        validate_policy_paper(synthetic_paper, label, errors)
        claims = card.get("claim_checks", [])
        used = [claim for claim in claims if isinstance(claim, dict) and claim.get("used_for_acceptance", True)] if isinstance(claims, list) else []
        if not used or any(claim.get("status") != "verified" or not http_url(claim.get("source")) or not nonempty(claim.get("claim")) for claim in used):
            errors.append(f"{label} needs verified primary-source claim_checks for acceptance")
        if card.get("requires_visual_review") is False:
            text_fields(visual, ("not_applicable_reason",), label, errors)
        if card.get("requires_visual_review") is True:
            inspections = visual.get("inspection_evidence")
            if not isinstance(inspections, list) or not inspections:
                errors.append(f"{label} needs actual inspection_evidence")
                inspections = []
            modalities = set()
            for inspection in inspections:
                if not isinstance(inspection, dict):
                    errors.append(f"{label} inspection_evidence entries must be objects")
                    continue
                text_fields(inspection, ("locator", "observation", "limitations"), label, errors)
                if not http_url(inspection.get("url")) or inspection.get("modality") not in INSPECTION_MODALITIES:
                    errors.append(f"{label} inspection needs official media URL and modality")
                else:
                    modalities.add(inspection["modality"])
            if card.get("requires_temporal_demo") and not modalities & TEMPORAL_MODALITIES:
                errors.append(f"{label} needs inspected temporal demo evidence")

    # Every passed candidate has exactly one editor disposition, not just additions -> passed.
    dispositions: dict[str, str] = {}
    existing_urls: set[str] = set()
    if any(patch.get(kind) for kind in ("registry_updates", "registry_noops")):
        try:
            registry = json.loads((root / "data/papers.seed.json").read_text())
            existing_urls = {
                paper["url"] for branch in registry.get("branches", [])
                for paper in branch.get("papers", []) if http_url(paper.get("url"))
            }
        except (OSError, ValueError, TypeError, KeyError):
            errors.append("v2 updates/no-ops need an inspectable existing registry")
    for kind in ("registry_additions", "registry_updates", "registry_noops"):
        for item in patch.get(kind, []) if isinstance(patch.get(kind, []), list) else []:
            if not isinstance(item, dict):
                errors.append(f"v2 {kind} entries must be objects")
                continue
            cid = item.get("candidate_id")
            if cid not in accepted:
                errors.append(f"{kind} {cid} is not an accepted candidate")
            if cid in dispositions:
                errors.append(f"accepted {cid} has duplicate editor dispositions")
            if isinstance(cid, str):
                dispositions[cid] = kind
            if kind != "registry_additions":
                text_fields(item, ("reason",), f"{kind} {cid}", errors)
                target = item.get("existing_paper_url")
                if not http_url(target) or target not in existing_urls:
                    errors.append(f"{kind} {cid} must target an existing_paper_url in the registry")
                if "paper" not in item:
                    continue
                if kind == "registry_noops":
                    errors.append(f"registry_noops {cid} cannot carry a paper mutation")
            paper = item.get("paper")
            if not isinstance(paper, dict):
                if kind == "registry_updates":
                    errors.append(f"registry_updates {cid} paper must be an object when provided")
                continue
            if paper.get("acceptance_policy_version") != POLICY_VERSION:
                errors.append(f"registry addition {cid} must declare acceptance_policy_version: 2")
            validate_policy_paper(paper, f"registry addition {cid}", errors)
            final = review_map.get(cid, {})
            visual = visual_map.get(cid, {})
            card = paper_map.get(cid, {})
            for key in ("impact_score", "project_relevance_score", "evidence_strength"):
                if paper.get(key) != final.get(key):
                    errors.append(f"registry addition {cid} {key} must match final review")
            for key in ("visual_quality_score", "visual_quality_decision"):
                if paper.get(key) != visual.get(key):
                    errors.append(f"registry addition {cid} {key} must match visual review")
            for key in ("requires_visual_review", "requires_temporal_demo"):
                if paper.get(key) != card.get(key):
                    errors.append(f"registry addition {cid} {key} must match paper card")
    if missing := accepted - set(dispositions):
        errors.append(f"accepted candidates missing editor disposition: {', '.join(sorted(missing))}")
