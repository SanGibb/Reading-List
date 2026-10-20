"""Retrospective curation is separate from the immutable original admission runs."""

from __future__ import annotations

import json
from pathlib import Path

if __package__:
    from .task_lifecycle import iso_date, text, url
else:
    from task_lifecycle import iso_date, text, url


DECISION_LABELS = {
    "priority": "优先阅读",
    "reference": "参考备选",
    "watchlist": "观察名单",
    "undecided": "待视觉复核",
    "source_issue": "来源待修复",
}


def validate_library_review(review: dict, registry: dict, frontiers: dict, root: Path | None = None) -> list[str]:
    errors: list[str] = []
    if not isinstance(review, dict) or review.get("review_schema_version") != 1 or review.get("policy_version") != 2:
        return ["library review needs review_schema_version: 1 and policy_version: 2"]
    if not iso_date(review.get("review_date")):
        errors.append("library review needs an ISO review_date")
    papers = {p["url"]: p for b in registry.get("branches", []) for p in b.get("papers", [])}
    memberships = {
        (t["task_id"], m["paper_url"]): m for t in frontiers.get("tasks", []) for m in t.get("members", [])
    }
    rows = review.get("reviews")
    if not isinstance(rows, list):
        return errors + ["library review reviews must be an array"]
    seen = set()
    audits: dict[str, dict] = {}
    for row in rows:
        if not isinstance(row, dict):
            errors.append("library review entries must be objects")
            continue
        ref = row.get("paper_url")
        if not isinstance(ref, str) or ref not in papers:
            errors.append(f"library review references unknown paper: {ref}")
            continue
        if ref in seen:
            errors.append(f"duplicate library review: {ref}")
        seen.add(ref)
        label = f"library review {ref}"
        decision = row.get("decision")
        if decision not in DECISION_LABELS:
            errors.append(f"{label} has invalid decision")
        if not text(row.get("reason")) or not text(row.get("revisit_trigger")):
            errors.append(f"{label} needs reason and revisit_trigger")
        for key in ("impact_score", "project_relevance_score", "evidence_strength"):
            value = row.get(key)
            if value is not None and (type(value) is not int or not 0 <= value <= 5):
                errors.append(f"{label} {key} must be null or an integer 0-5")
        ids = row.get("task_ids")
        if not isinstance(ids, list) or not ids or any(not isinstance(tid, str) for tid in ids):
            errors.append(f"{label} needs real task_ids")
            ids = []
        elif len(ids) != len(set(ids)) or any((tid, ref) not in memberships for tid in ids):
            errors.append(f"{label} has unknown or duplicate task memberships")
        if papers[ref].get("curation_status") != decision or papers[ref].get("task_ids") != ids:
            errors.append(f"{label} must agree with current registry curation status/task_ids")
        audit_path = row.get("review_artifact")
        audit = None
        if not isinstance(audit_path, str) or not audit_path.startswith("reports/reorganization/") or ".." in Path(audit_path).parts:
            errors.append(f"{label} needs a safe review_artifact path")
        elif root is not None:
            path = (root / audit_path).resolve()
            if not path.is_relative_to(root.resolve()):
                errors.append(f"{label} audit escapes the repository")
            else:
                try:
                    if audit_path not in audits:
                        doc = json.loads(path.read_text())
                        audits[audit_path] = {r["paper_url"]: r for r in doc["reviews"]}
                    audit = audits[audit_path].get(ref)
                except (OSError, ValueError, KeyError, TypeError):
                    errors.append(f"{label} cannot read its review artifact")
                if not audit:
                    errors.append(f"{label} is missing from its review artifact")
                elif any(audit.get(key) != row.get(key) for key in ("decision", "impact_score", "project_relevance_score", "evidence_strength", "reason")):
                    errors.append(f"{label} disagrees with its review artifact")
        if decision == "priority":
            if any(type(row.get(k)) is not int or row[k] < 4 for k in ("impact_score", "project_relevance_score", "evidence_strength")):
                errors.append(f"{label} priority requires all three final scores >=4")
            if papers[ref].get("source_quality") not in {"primary", "official", "primary_or_official"}:
                errors.append(f"{label} priority needs a primary/official current registry source")
            if any(papers[ref].get(k) != row.get(k) for k in ("impact_score", "project_relevance_score", "evidence_strength")):
                errors.append(f"{label} final registry scores must match the review")
            if any(memberships.get((tid, ref), {}).get("role") not in {"current", "alternative", "historical"} for tid in ids):
                errors.append(f"{label} priority needs a supported reviewed task role")
            if audit is not None:
                if type(audit.get("requires_visual_review")) is not bool or type(audit.get("requires_temporal_demo")) is not bool:
                    errors.append(f"{label} priority needs explicit visual/temporal requirements")
                if audit.get("requires_temporal_demo") and not audit.get("requires_visual_review"):
                    errors.append(f"{label} temporal evidence cannot waive visual review")
                sources = audit.get("sources", [])
                if not any(s.get("status") == "verified" and s.get("source_quality") in {"primary", "official", "primary_or_official"} and url(s.get("source_url")) and text(s.get("locator")) and text(s.get("claim")) for s in sources):
                    errors.append(f"{label} priority needs verified official source traces")
                if audit.get("requires_visual_review"):
                    inspected = audit.get("inspection_evidence", [])
                    score, verdict = audit.get("visual_quality_score"), audit.get("visual_quality_decision")
                    if type(score) is not int or not 3 <= score <= 5 or verdict not in {"adequate", "strong"} or (verdict == "adequate" and score != 3) or (verdict == "strong" and score < 4):
                        errors.append(f"{label} needs adequate/3 or strong/4-5 visual quality")
                    if papers[ref].get("visual_quality_score") != score or papers[ref].get("visual_quality_decision") != verdict:
                        errors.append(f"{label} registry visual verdict must match inspected evidence")
                    if audit.get("visual_status") != "verified" or not inspected:
                        errors.append(f"{label} priority requires actual visual inspection")
                    for item in inspected:
                        if not isinstance(item, dict) or not url(item.get("url")) or any(not text(item.get(k)) for k in ("locator", "observation", "limitations")):
                            errors.append(f"{label} visual inspection needs URL, locator, observation, and limits")
                    if audit.get("requires_temporal_demo") and not any(i.get("modality") in {"video", "gif", "interactive_demo"} for i in inspected):
                        errors.append(f"{label} priority needs temporal inspection")
                else:
                    if audit.get("visual_status") != "not_applicable" or not text(audit.get("not_applicable_reason")):
                        errors.append(f"{label} non-visual priority needs not_applicable rationale")
                    if papers[ref].get("visual_quality_score") != 0 or papers[ref].get("visual_quality_decision") != "not_applicable":
                        errors.append(f"{label} non-visual registry verdict must be not_applicable/0")
        elif any(memberships.get((tid, ref), {}).get("role") == "current" for tid in ids):
            errors.append(f"{label} a non-priority entry cannot be presented as current")
        if decision == "undecided":
            dossier = row.get("dossier_path")
            if not isinstance(dossier, str) or not dossier.startswith("undecided/") or ".." in Path(dossier).parts:
                errors.append(f"{label} needs a local-only undecided dossier path")
            elif root is not None:
                import os
                if os.environ.get("REQUIRE_UNDECIDED_DOSSIERS") == "1" and not (root / dossier).is_file():
                    errors.append(f"{label} needs local dossier: {dossier}")
    # This is a dated retrospective snapshot. Later, separately validated v2
    # admissions need not rewrite its original 168 judgments.
    missing = set(papers) - seen
    unsupported = {ref for ref in missing if papers[ref].get("acceptance_policy_version") != 2 or papers[ref].get("curation_status") not in {None, "priority"}}
    if unsupported:
        errors.append(f"library review must cover every pre-existing registry paper exactly once (missing {len(unsupported)})")
    return errors
