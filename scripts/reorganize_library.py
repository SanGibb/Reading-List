#!/usr/bin/env python3
"""Apply human/source-backed branch reviews without deleting collected papers.

This integrates already written audit judgments. It does not infer scores,
recommendations, scientific superiority, or source verification from metadata.
"""

from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import re

if __package__:
    from .library_review import DECISION_LABELS, validate_library_review
    from .task_lifecycle import iso_date, validate_task_frontiers
else:
    from library_review import DECISION_LABELS, validate_library_review
    from task_lifecycle import iso_date, validate_task_frontiers


def write_json(path: Path, value: dict) -> None:
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n")


def review_anchor(ref: str) -> str:
    return "paper-" + hashlib.sha256(ref.encode()).hexdigest()[:12]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--date", required=True)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    root = args.root.resolve()
    if not iso_date(args.date):
        parser.error("--date must be YYYY-MM-DD")
    audit_dir = root / "reports/reorganization" / args.date
    registry = json.loads((root / "data/papers.seed.json").read_text())
    papers = {p["url"]: p for b in registry["branches"] for p in b["papers"]}
    audited: dict[str, tuple[dict, str]] = {}
    for path in sorted(audit_dir.glob("branch-*.json")):
        doc = json.loads(path.read_text())
        if doc.get("review_date") != args.date:
            raise ValueError(f"Review date mismatch: {path}")
        for row in doc["reviews"]:
            ref = row["paper_url"]
            if ref not in papers or ref in audited:
                raise ValueError(f"Unknown or duplicated reviewed paper: {ref}")
            if row.get("title") != papers[ref]["title"]:
                raise ValueError(f"Review title mismatch: {ref}")
            audited[ref] = (row, path.relative_to(root).as_posix())
    if set(audited) != set(papers):
        raise ValueError(f"Full review required: {len(set(papers)-set(audited))} records missing")

    merge_path = audit_dir / "task-merge-plan.json"
    assignments = {}
    if merge_path.is_file():
        merge = json.loads(merge_path.read_text())
        for task in merge["tasks"]:
            for ref in task["paper_urls"]:
                if ref not in papers or ref in assignments:
                    raise ValueError(f"Invalid/duplicate task assignment: {ref}")
                assignments[ref] = {key: task[key] for key in ("task_id", "title", "branch", "scope")}
        if set(assignments) != set(papers):
            raise ValueError("Task-merge plan must cover every retained paper exactly once")

    tasks: dict[str, dict] = {}
    review_rows = []
    for ref, paper in papers.items():
        row, artifact = audited[ref]
        decision = row["decision"]
        if decision not in DECISION_LABELS:
            raise ValueError(f"Invalid decision: {ref}")
        descriptor = assignments.get(ref, {"task_id": row["task_id"], "title": row["task_title"], "branch": row["branch"], "scope": row["scope"]})
        tid = descriptor["task_id"]
        if tid not in tasks:
            tasks[tid] = dict(descriptor, members=[])
        elif any(tasks[tid][key] != descriptor[key] for key in descriptor):
            raise ValueError(f"Conflicting task definitions for {tid}; reconcile the reviews first")
        member = {"paper_url": ref, "role": row["role"], "reason": row["reason"]}
        if row["role"] != "unreviewed":
            member["reviewed_on"] = args.date
            member["evidence"] = [dict(s) for s in row["sources"] if s.get("status") == "verified"]
        if row["role"] == "historical":
            member.update({"superseded_by": row["superseded_by"], "comparison": row["comparison"]})
        tasks[tid]["members"].append(member)

        record = {key: row.get(key) for key in (
            "paper_url", "decision", "impact_score", "project_relevance_score", "evidence_strength", "reason", "revisit_trigger"
        )}
        record.update({"task_ids": [tid], "task_title": descriptor["title"], "review_artifact": artifact})
        if decision == "undecided":
            slug = Path(paper["deep_dive_path"]).stem
            record["dossier_path"] = f"undecided/{args.date}/LIB-{row['branch']}-{slug}.md"
        review_rows.append(record)

        # Preserve what the old admissions claimed, while making current evidence
        # uncertainty explicit in the live record and in the reader-facing banner.
        paper.setdefault("historical_acceptance", {key: paper.get(key) for key in (
            "source_quality", "evidence_strength", "demo_score", "visual_quality_score", "visual_quality_decision", "visual_inspection_status"
        )})
        paper.update({
            "curation_status": decision,
            "curation_policy_version": 2,
            "curation_reviewed_on": args.date,
            "curation_review_path": "paper_reads/library_review.md#" + review_anchor(ref),
            "task_ids": [tid],
            "evidence_strength": row.get("evidence_strength") if isinstance(row.get("evidence_strength"), int) else 0,
        })
        for key in ("impact_score", "project_relevance_score"):
            if type(row.get(key)) is int:
                paper[key] = row[key]
        has_verified_source = any(s.get("status") == "verified" for s in row.get("sources", []))
        paper["source_quality"] = "unverified" if decision == "source_issue" or not has_verified_source else "primary_or_official"
        if decision == "source_issue":
            paper["demo_score"] = 0
        if row.get("requires_visual_review"):
            score, verdict = row.get("visual_quality_score"), row.get("visual_quality_decision")
            visually_passed = (row.get("visual_status") == "verified" and decision != "undecided"
                               and type(score) is int and 3 <= score <= 5
                               and ((verdict == "adequate" and score == 3) or (verdict == "strong" and score >= 4)))
            if visually_passed:
                paper["visual_quality_score"] = score
                paper["visual_quality_decision"] = verdict
                paper["visual_inspection_status"] = f"inspected_in_reassessment_{args.date}"
            else:
                paper.update({"visual_quality_score": 0, "visual_quality_decision": "undecided", "visual_inspection_status": f"not_verified_in_reassessment_{args.date}"})
        else:
            paper.update({"visual_quality_score": 0, "visual_quality_decision": "not_applicable", "visual_inspection_status": f"protocol_only_reassessment_{args.date}"})

    registry["updated"] = args.date
    frontiers = {"lifecycle_schema_version": 1, "updated": args.date, "tasks": sorted(tasks.values(), key=lambda t: t["task_id"])}
    review = {"review_schema_version": 1, "policy_version": 2, "review_date": args.date,
              "review_scope": "user_requested_existing_library_reassessment", "reviews": review_rows}
    if assignments:
        review["task_assignment_artifact"] = merge_path.relative_to(root).as_posix()
    errors = validate_task_frontiers(frontiers, registry, root) + validate_library_review(review, registry, frontiers, root)
    # Local dossiers are generated below from the reviewed record plus the retained
    # original analysis, so the pre-write check does not require them yet.
    errors = [error for error in errors if "needs local dossier:" not in error]
    if errors:
        raise ValueError("\n".join(errors))

    for record in review_rows:
        ref = record["paper_url"]
        decision = record["decision"]
        paper = papers[ref]
        row, artifact = audited[ref]
        path = root / paper["deep_dive_path"]
        original = path.read_text()
        clean = re.sub(r"\n<!-- curation-review:start -->.*?<!-- curation-review:end -->\n", "\n", original, flags=re.S)
        first, _, rest = clean.partition("\n")
        rest = rest.lstrip("\n")
        clean = first + "\n\n" + rest
        relative = "../library_review.md#" + review_anchor(ref)
        message = row["reason"].replace("\n", " ")
        banner = ("\n<!-- curation-review:start -->\n"
                  f"> {args.date} 按新版标准复审：**{DECISION_LABELS[record['decision']]}**。{message}\n> "
                  f"[本次来源、分数与任务判断]({relative})。下文保留原精读；旧验收标签不代表本次重新通过，所有实验仍为作者报告。\n"
                  )
        if decision == "priority":
            scores = " / ".join(str(record[key]) for key in ("impact_score", "project_relevance_score", "evidence_strength"))
            banner += f">\n> **本轮准入依据**（技术贡献 / 直接相关性 / 证据：{scores}）：{row['material_difference']}\n"
            for item in row.get("sources", []):
                banner += f"> - [{item['locator']}]({item['source_url']})：{item['claim']}（{item['status']}）。\n"
            banner += ">\n> 引用指标、发布规模和比较结果时，以以上已定位来源和本次复审限制为准，不沿用下文旧概括。\n"
        elif decision == "source_issue" and row.get("corrected_source_url"):
            banner += f">\n> 身份纠错线索：[原始/官方入口]({row['corrected_source_url']})；此线索不代表已重新通过准入。\n"
        banner += "<!-- curation-review:end -->\n"
        updated = first + "\n" + banner + "\n" + rest
        if updated != original:
            path.write_text(updated)
        if record["decision"] == "undecided":
            dossier = root / record["dossier_path"]
            dossier.parent.mkdir(parents=True, exist_ok=True)
            sources = "\n".join(f"- {s['source_url']} — {s['locator']}: {s['claim']} ({s['status']})" for s in row.get("sources", []))
            dossier.write_text(
                f"# 本地待定复审：{paper['title']}\n\ndecision: undecided_visual_quality\nreview_date: {args.date}\n"
                f"paper_url: {ref}\n\n## 本轮判断与来源\n\n{row['reason']}\n\n{sources}\n\n"
                f"## 任务与实质增量\n\n- task_id: {record['task_ids'][0]}\n- 原复审细分范围：{row['task_id']}\n- 任务：{paper['task']}\n"
                f"- 方法：{paper['method']}\n- 数据：{paper['data']}\n- 新增量：{row['material_difference']}\n\n"
                f"## 视觉与证据缺口\n\n状态：{row['visual_status']}。本轮未确认的动态质量不继承旧 strong/adequate。"
                f"\n\n需要补充：{row['revisit_trigger']}\n\n## 人工决策\n\n"
                "- 接受：实际检查代表性时序/交互材料后，记录时间段、动作/接触/一致性及失败覆盖，并重新确认三项四分门槛。\n"
                "- 拒绝：可见质量或任务可用性不满足要求，或方法/相关性不足。\n"
                "- 继续观察：材料不可访问、样例不足或仍无法判断。\n\n"
                "## 原精读快照（历史分析，不作为本轮通过证据）\n\n" + clean
            )
    write_json(root / "data/papers.seed.json", registry)
    write_json(root / "data/task_frontiers.seed.json", frontiers)
    write_json(root / "data/library_review.seed.json", review)
    counts = Counter(row["decision"] for row in review_rows)
    source_issues = [row for row in review_rows if row["decision"] == "source_issue"]
    summary = [f"# {args.date} Existing Library Reorganization", "",
               "This is an explicit, user-requested retrospective reassessment, not a weekly expansion or an independent reproduction.", "",
               f"All {len(papers)} records and deep dives are preserved; {len(tasks)} concrete task groups cover the complete inventory.", "",
               "| Review outcome | Count |", "|---|---:|"]
    summary += [f"| {DECISION_LABELS[key]} | {counts[key]} |" for key in DECISION_LABELS]
    summary += ["", "Only priority entries are shown as current recommendations. Reference status does not mean renewed v2 admission. Uncertainty is not proof that a paper is bad.", "",
                "## Source issues", ""]
    summary += [f"- **{papers[row['paper_url']]['title']}** — {row['reason']}" for row in source_issues] or ["None found."]
    summary += ["", "## Evidence and scope", "",
                "Each paper has a branch-audit record with fresh source checks, task scope, final scores or explicit unknowns, and a decision/revisit trigger. Original admission runs remain unchanged. Source verification is not independent reproduction; linked videos are not watched videos.", "",
                "Current registry fields describe this reassessment; historical_acceptance preserves the original source/visual/evidence labels. Undecided dossiers are local-only and remain outside publication.", "",
                "No supersession is inferred from age, version numbers or unmatched benchmark scores. Any historical task link must satisfy the separate comparable-protocol/no-regression evidence gates.", "",
                "## Entry points", "", "- [Curated reading and full review](../../../paper_reads/library_review.md)",
                "- [Task frontiers](../../../paper_reads/task_frontiers.md)", "",
                "## Validation", "", "Run the full tests, regenerate indexes, and use REQUIRE_UNDECIDED_DOSSIERS=1 python3 scripts/validate_all.py before publication."]
    (audit_dir / "summary.md").write_text("\n".join(summary) + "\n")
    print(f"Applied {len(review_rows)} source-backed review records across {len(tasks)} tasks: {dict(counts)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
