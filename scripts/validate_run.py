#!/usr/bin/env python3
"""Validate a consolidated file-driven literature run."""

from __future__ import annotations

import json
import os
import re
import sys
from pathlib import Path
from typing import Any


BRANCHES = {"A", "B", "C", "D", "E"}
CANDIDATE_RE = re.compile(r"^CAND-\d{4}$")
MIN_YEAR = 2024

JSON_FILES = [
    "00_run_plan.json",
    "01_discovery.json",
    "02_evidence.json",
    "03_review.json",
    "05_registry_patch.json",
]

REQUIRED_REGISTRY_FIELDS = {
    "title",
    "year",
    "venue",
    "url",
    "data",
    "method",
    "task",
    "novelty",
    "project_relevance",
    "source_quality",
    "demo_score",
    "visual_quality_score",
    "visual_quality_decision",
    "evidence_strength",
}

VISUAL_DECISIONS = {"strong", "adequate", "weak", "undecided", "not_applicable"}
FOLLOW_SOURCE_STATUSES = {"checked", "spot_checked", "unreachable", "skipped"}

DEEP_DIVE_REQUIRED_SECTIONS = [
    "## Source Links",
    "## TL;DR",
    "## Novelty",
    "## Contributions",
    "## Task",
    "## Data",
    "## Method",
    "## Key Figures / Architecture",
    "## Evidence Trail",
    "## Evidence",
    "## Limitations",
    "## Project Relevance",
    "## Reproduction / Follow-up",
]


def load_json(path: Path, errors: list[str]) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text())
    except Exception as exc:  # noqa: BLE001
        errors.append(f"{path.name} is not valid JSON: {exc}")
        return {}
    if not isinstance(value, dict):
        errors.append(f"{path.name} must contain a JSON object")
        return {}
    return value


def require(obj: dict[str, Any], field: str, label: str, errors: list[str]) -> Any:
    if field not in obj:
        errors.append(f"{label} missing required field `{field}`")
        return None
    return obj[field]


def validate_score(value: Any, label: str, errors: list[str]) -> None:
    if not isinstance(value, int) or not 0 <= value <= 5:
        errors.append(f"{label} must be an integer from 0 to 5")


def validate_deep_dive(path: Path, cid: str, paper: dict[str, Any], errors: list[str]) -> None:
    if not path.exists():
        errors.append(f"registry addition {cid} needs paper deep dive: {path}")
        return

    text = path.read_text()
    if len(text.strip()) < 1200:
        errors.append(f"paper deep dive {cid} is too short to be useful")
    for section in DEEP_DIVE_REQUIRED_SECTIONS:
        if section not in text:
            errors.append(f"paper deep dive {cid} missing required section: {section}")
    url = paper.get("url")
    if isinstance(url, str) and url and url not in text:
        errors.append(f"paper deep dive {cid} must include original paper URL")
    if "figure_status:" not in text:
        errors.append(f"paper deep dive {cid} must include figure_status in Key Figures / Architecture")


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: validate_run.py YYYY-MM-DD", file=sys.stderr)
        return 2

    run_id = sys.argv[1]
    root = Path(__file__).resolve().parents[1]
    run_dir = root / "reports" / "runs" / run_id
    errors: list[str] = []

    if not run_dir.exists():
        print(f"Run directory does not exist: {run_dir}", file=sys.stderr)
        return 1

    data: dict[str, dict[str, Any]] = {}
    for name in JSON_FILES:
        path = run_dir / name
        if not path.exists():
            errors.append(f"missing required artifact: {name}")
            continue
        artifact = load_json(path, errors)
        data[name] = artifact
        if artifact.get("run_id") != run_id:
            errors.append(f"{name} run_id must be {run_id}")

    run_plan = data.get("00_run_plan.json", {})
    if run_plan.get("minimum_year") != MIN_YEAR:
        errors.append(f"00_run_plan.json minimum_year must be {MIN_YEAR}")
    branches = run_plan.get("branches")
    if branches is not None and set(branches) != BRANCHES:
        errors.append(f"00_run_plan.json branches must be {sorted(BRANCHES)}")
    follow_sources_path = run_plan.get("follow_sources_path")
    follow_source_ids: set[str] = set()
    if not isinstance(follow_sources_path, str) or not follow_sources_path:
        errors.append("00_run_plan.json missing required field `follow_sources_path`")
    else:
        follow_path = root / follow_sources_path
        if not follow_path.exists():
            errors.append(f"follow_sources_path does not exist: {follow_sources_path}")
        else:
            follow_doc = load_json(follow_path, errors)
            for collection_name in ["source_groups", "meta_sources"]:
                collection = follow_doc.get(collection_name, [])
                if not isinstance(collection, list):
                    errors.append(f"{follow_sources_path} `{collection_name}` must be a list")
                    continue
                for source in collection:
                    if isinstance(source, dict) and isinstance(source.get("id"), str):
                        follow_source_ids.add(source["id"])

    report = run_dir / "04_editor_report.md"
    if not report.exists():
        errors.append("missing required artifact: 04_editor_report.md")
    elif not report.read_text().strip():
        errors.append("04_editor_report.md must not be empty")

    manifest = run_dir / "run_manifest.json"
    if not manifest.exists():
        errors.append("missing required artifact: run_manifest.json")
    else:
        manifest_data = load_json(manifest, errors)
        if manifest_data.get("run_id") != run_id:
            errors.append("run_manifest.json run_id mismatch")

    discovery_doc = data.get("01_discovery.json", {})
    followed_sources_checked = discovery_doc.get("followed_sources_checked", [])
    if not isinstance(followed_sources_checked, list):
        errors.append("01_discovery.json `followed_sources_checked` must be a list")
        followed_sources_checked = []
    for item in followed_sources_checked:
        if not isinstance(item, dict):
            errors.append("followed source check entries must be objects")
            continue
        source_id = require(item, "source_id", "followed source check", errors)
        status = require(item, "status", f"followed source check {source_id}", errors)
        require(item, "notes", f"followed source check {source_id}", errors)
        if status not in FOLLOW_SOURCE_STATUSES:
            errors.append(f"followed source check {source_id} has invalid status: {status}")
        if follow_source_ids and source_id not in follow_source_ids:
            errors.append(f"followed source check references unknown source_id: {source_id}")

    candidates = discovery_doc.get("candidates", [])
    if not isinstance(candidates, list):
        errors.append("01_discovery.json `candidates` must be a list")
        candidates = []

    candidate_ids: set[str] = set()
    for item in candidates:
        if not isinstance(item, dict):
            errors.append("candidate entries must be objects")
            continue
        cid = require(item, "candidate_id", "candidate", errors)
        require(item, "title", f"candidate {cid}", errors)
        require(item, "source_url", f"candidate {cid}", errors)
        require(item, "source_type", f"candidate {cid}", errors)
        require(item, "why_candidate", f"candidate {cid}", errors)
        if isinstance(cid, str) and not CANDIDATE_RE.match(cid):
            errors.append(f"invalid candidate id: {cid}")
        if cid in candidate_ids:
            errors.append(f"duplicate candidate id: {cid}")
        if isinstance(cid, str):
            candidate_ids.add(cid)
        branch_hint = item.get("branch_hint")
        if branch_hint not in BRANCHES:
            errors.append(f"candidate {cid} has invalid branch_hint: {branch_hint}")

    triage = discovery_doc.get("triage", [])
    if not isinstance(triage, list):
        errors.append("01_discovery.json `triage` must be a list")
        triage = []

    decisions: dict[str, str] = {}
    for item in triage:
        if not isinstance(item, dict):
            errors.append("triage entries must be objects")
            continue
        cid = require(item, "candidate_id", "triage item", errors)
        decision = require(item, "decision", f"triage {cid}", errors)
        require(item, "reason", f"triage {cid}", errors)
        validate_score(item.get("impact_prior"), f"triage {cid} impact_prior", errors)
        validate_score(item.get("project_relevance_prior"), f"triage {cid} project_relevance_prior", errors)
        if cid not in candidate_ids:
            errors.append(f"triage references unknown candidate: {cid}")
        if decision not in {"analyze", "watchlist", "reject"}:
            errors.append(f"triage {cid} has invalid decision: {decision}")
        if isinstance(cid, str) and isinstance(decision, str):
            decisions[cid] = decision
        primary_branch = item.get("primary_branch")
        if decision == "analyze" and primary_branch not in BRANCHES:
            errors.append(f"triage {cid} analyze decision needs valid primary_branch")

    evidence_doc = data.get("02_evidence.json", {})
    paper_cards = evidence_doc.get("paper_cards", [])
    if not isinstance(paper_cards, list):
        errors.append("02_evidence.json `paper_cards` must be a list")
        paper_cards = []

    paper_card_ids: set[str] = set()
    for card in paper_cards:
        if not isinstance(card, dict):
            errors.append("paper cards must be objects")
            continue
        cid = require(card, "candidate_id", "paper card", errors)
        if cid not in candidate_ids:
            errors.append(f"paper card references unknown candidate: {cid}")
        if decisions.get(cid) != "analyze":
            errors.append(f"paper card {cid} is not allowed unless triage decision is analyze")
        for field in [
            "title",
            "year",
            "venue",
            "url",
            "primary_branch",
            "secondary_branches",
            "data",
            "method",
            "task",
            "novelty",
            "evidence",
            "limitations",
            "project_relevance",
        ]:
            require(card, field, f"paper card {cid}", errors)
        if card.get("primary_branch") not in BRANCHES:
            errors.append(f"paper card {cid} has invalid primary_branch")
        year = card.get("year")
        if not isinstance(year, int) or year < MIN_YEAR:
            errors.append(f"paper card {cid} year must be >= {MIN_YEAR}")
        if isinstance(cid, str):
            paper_card_ids.add(cid)

    demo_cards = evidence_doc.get("demo_cards", [])
    if not isinstance(demo_cards, list):
        errors.append("02_evidence.json `demo_cards` must be a list")
        demo_cards = []

    for card in demo_cards:
        if not isinstance(card, dict):
            errors.append("demo cards must be objects")
            continue
        cid = require(card, "candidate_id", "demo card", errors)
        if cid not in candidate_ids:
            errors.append(f"demo card references unknown candidate: {cid}")
        if decisions.get(cid) == "reject":
            errors.append(f"demo card {cid} cannot reference rejected candidate")
        validate_score(card.get("demo_score"), f"demo card {cid} demo_score", errors)
        require(card, "verification_status", f"demo card {cid}", errors)
        require(card, "demo_notes", f"demo card {cid}", errors)

    review_doc = data.get("03_review.json", {})
    visual_cards = review_doc.get("visual_cards", [])
    if not isinstance(visual_cards, list):
        errors.append("03_review.json `visual_cards` must be a list")
        visual_cards = []

    undecided_ids: set[str] = set()
    visual_card_ids: set[str] = set()
    for card in visual_cards:
        if not isinstance(card, dict):
            errors.append("visual cards must be objects")
            continue
        cid = require(card, "candidate_id", "visual card", errors)
        if cid not in candidate_ids:
            errors.append(f"visual card references unknown candidate: {cid}")
        if decisions.get(cid) == "reject":
            errors.append(f"visual card {cid} cannot reference rejected candidate")
        require(card, "visual_materials", f"visual card {cid}", errors)
        require(card, "inspected_modalities", f"visual card {cid}", errors)
        validate_score(card.get("visual_quality_score"), f"visual card {cid} visual_quality_score", errors)
        visual_decision = require(card, "visual_quality_decision", f"visual card {cid}", errors)
        if visual_decision not in VISUAL_DECISIONS:
            errors.append(f"visual card {cid} has invalid visual_quality_decision")
        require(card, "visual_notes", f"visual card {cid}", errors)
        require(card, "failure_modes", f"visual card {cid}", errors)
        needs_human = require(card, "needs_human_decision", f"visual card {cid}", errors)
        require(card, "undecided_reason", f"visual card {cid}", errors)
        if not isinstance(needs_human, bool):
            errors.append(f"visual card {cid} needs_human_decision must be boolean")
        if visual_decision == "undecided" or needs_human is True:
            if isinstance(cid, str):
                undecided_ids.add(cid)
                dossier = root / "undecided" / run_id / f"{cid}.md"
                if os.environ.get("REQUIRE_UNDECIDED_DOSSIERS") == "1" and not dossier.exists():
                    errors.append(f"undecided candidate {cid} needs dossier: {dossier.relative_to(root)}")
        if isinstance(cid, str):
            visual_card_ids.add(cid)

    for cid in paper_card_ids:
        if cid not in visual_card_ids:
            errors.append(f"paper card {cid} must have a visual quality card")

    quality_review = review_doc.get("quality_review", [])
    if not isinstance(quality_review, list):
        errors.append("03_review.json `quality_review` must be a list")
        quality_review = []

    accepted_ids: set[str] = set()
    blocked_ids: set[str] = set()
    for item in quality_review:
        if not isinstance(item, dict):
            errors.append("quality review entries must be objects")
            continue
        cid = require(item, "candidate_id", "quality review item", errors)
        decision = require(item, "review_decision", f"quality review {cid}", errors)
        require(item, "issues", f"quality review {cid}", errors)
        require(item, "required_fixes", f"quality review {cid}", errors)
        if cid not in candidate_ids:
            errors.append(f"quality review references unknown candidate: {cid}")
        if decision not in {"pass", "needs_revision", "block"}:
            errors.append(f"quality review {cid} has invalid review_decision")
        accepted = item.get("accepted_for_registry")
        if not isinstance(accepted, bool):
            errors.append(f"quality review {cid} accepted_for_registry must be boolean")
        if accepted:
            accepted_ids.add(cid)
            if decision != "pass":
                errors.append(f"quality review {cid} cannot accept unless review_decision is pass")
            if cid not in paper_card_ids:
                errors.append(f"quality review {cid} cannot accept without a paper card")
            if cid in undecided_ids:
                errors.append(f"quality review {cid} cannot accept an undecided visual-quality candidate")
        if decision == "block" and isinstance(cid, str):
            blocked_ids.add(cid)

    patch_doc = data.get("05_registry_patch.json", {})
    assignments = patch_doc.get("branch_assignments", [])
    if not isinstance(assignments, list):
        errors.append("05_registry_patch.json `branch_assignments` must be a list")
        assignments = []
    for item in assignments:
        if not isinstance(item, dict):
            errors.append("branch assignments must be objects")
            continue
        cid = item.get("candidate_id")
        if cid not in candidate_ids:
            errors.append(f"taxonomy assignment references unknown candidate: {cid}")
        if item.get("primary_branch") not in BRANCHES:
            errors.append(f"taxonomy assignment {cid} has invalid primary_branch")
        validate_score(item.get("taxonomy_confidence"), f"taxonomy {cid} confidence", errors)

    proposals = patch_doc.get("taxonomy_change_proposals", [])
    if not isinstance(proposals, list):
        errors.append("05_registry_patch.json `taxonomy_change_proposals` must be a list")
        proposals = []
    for proposal in proposals:
        if not isinstance(proposal, dict):
            errors.append("taxonomy proposals must be objects")
            continue
        if proposal.get("status") != "proposal_only":
            errors.append("taxonomy proposals must have status proposal_only")

    additions = patch_doc.get("registry_additions", [])
    if not isinstance(additions, list):
        errors.append("05_registry_patch.json `registry_additions` must be a list")
        additions = []
    for item in additions:
        if not isinstance(item, dict):
            errors.append("registry additions must be objects")
            continue
        cid = require(item, "candidate_id", "registry addition", errors)
        branch = require(item, "branch", f"registry addition {cid}", errors)
        deep_dive_path = require(item, "deep_dive_path", f"registry addition {cid}", errors)
        paper = require(item, "paper", f"registry addition {cid}", errors)
        if cid not in accepted_ids:
            errors.append(f"registry addition {cid} is not accepted by quality review")
        if cid in blocked_ids:
            errors.append(f"registry addition {cid} is blocked by quality review")
        if decisions.get(cid) in {"reject", "watchlist"}:
            errors.append(f"registry addition {cid} cannot come from {decisions.get(cid)} candidate")
        if cid in undecided_ids:
            errors.append(f"registry addition {cid} cannot include undecided visual-quality candidate")
        if branch not in BRANCHES:
            errors.append(f"registry addition {cid} has invalid branch")
        if not isinstance(paper, dict):
            errors.append(f"registry addition {cid} paper must be object")
        else:
            missing = sorted(REQUIRED_REGISTRY_FIELDS - set(paper))
            if missing:
                errors.append(f"registry addition {cid} missing paper fields: {', '.join(missing)}")
            year = paper.get("year")
            if not isinstance(year, int) or year < MIN_YEAR:
                errors.append(f"registry addition {cid} paper year must be >= {MIN_YEAR}")
            if isinstance(cid, str) and isinstance(deep_dive_path, str):
                deep_dive_rel = Path(deep_dive_path)
                if deep_dive_rel.is_absolute() or ".." in deep_dive_rel.parts:
                    errors.append(f"registry addition {cid} deep_dive_path must be a safe relative path")
                elif not deep_dive_path.startswith("paper_reads/"):
                    errors.append(f"registry addition {cid} deep_dive_path must live under paper_reads/")
                else:
                    validate_deep_dive(root / deep_dive_rel, cid, paper, errors)

    if errors:
        print("Run validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Run validation passed: {run_id}")
    print(f"- candidates: {len(candidate_ids)}")
    print(f"- analyzed: {len(paper_card_ids)}")
    print(f"- accepted for registry: {len(accepted_ids)}")
    print(f"- registry additions: {len(additions)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
