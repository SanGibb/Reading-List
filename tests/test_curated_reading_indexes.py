"""Reader-facing regression checks for the retrospective curation sidecar."""

from __future__ import annotations

import copy
import json
from pathlib import Path
import re
import subprocess
import sys
import tempfile
import unittest

from scripts.render_reading_indexes import BRANCH_DIRECTORIES, build_indexes


REPOSITORY = Path(__file__).resolve().parents[1]
RENDERER = REPOSITORY / "scripts/render_reading_indexes.py"
REORGANIZER = REPOSITORY / "scripts/reorganize_library.py"
DATE = "2026-10-20"


def folded_section(page: str, summary: str) -> str:
    """Return the complete collapsed section, including any nested sections."""
    position = page.index(summary)
    opening = page.rfind("<details>", 0, position)
    if opening < 0:
        raise AssertionError(f"Section is not folded: {summary}")
    depth = 0
    for match in re.finditer(r"<details\b[^>]*>|</details>", page[opening:]):
        depth += -1 if match.group() == "</details>" else 1
        if depth == 0:
            return page[opening:opening + match.end()]
    raise AssertionError(f"Unclosed details section: {summary}")


def link_depth(page: str, link: str) -> int:
    """A link inside a closed details element is not visible by default."""
    position = page.index(link)
    tags = re.findall(r"<details\b[^>]*>|</details>", page[:position])
    return sum(-1 if tag == "</details>" else 1 for tag in tags)


class CuratedReadingIndexTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.artifact = f"reports/reorganization/{DATE}/branch-X.json"
        self.registry = {
            "updated": DATE,
            "branches": [{"id": branch, "name": f"Branch {branch}", "papers": []}
                         for branch in "ABCDE"],
        }
        self.papers = []
        decisions = ("priority", "reference", "undecided", "source_issue")
        titles = ("Released Protocol", "Distinct Baseline", "Unwatched Simulator", "Mismatched Source")
        roles = ("current", "alternative", "unreviewed", "unreviewed")
        scores = ((4, 5, 4), (3, 4, 3), (4, 4, 3), (None, None, 1))
        self.frontiers = {
            "lifecycle_schema_version": 1, "updated": DATE,
            "tasks": [self.make_task("controlled-evaluation", "Controlled evaluation"),
                      self.make_task("pending-simulation", "Pending simulation")],
        }
        self.review = {
            "review_schema_version": 1, "policy_version": 2,
            "review_date": DATE, "reviews": [],
        }
        self.audit = {"review_date": DATE, "branches": ["A"], "reviews": []}
        for number, (decision, title, role, score) in enumerate(zip(decisions, titles, roles, scores)):
            task = self.frontiers["tasks"][number // 2]
            paper = {
                "title": title, "year": 2026,
                "url": f"https://example.edu/papers/{number}",
                "deep_dive_path": f"paper_reads/{BRANCH_DIRECTORIES['A']}/paper-{number}.md",
                "data": "Fixed held-out task records.", "method": "Source-defined evaluation procedure.",
                "task": task["title"], "source_quality": "primary",
                "impact_score": score[0], "project_relevance_score": score[1],
                "evidence_strength": score[2], "demo_score": 3,
                "visual_quality_score": 0 if decision == "priority" else 4,
                "visual_quality_decision": "not_applicable" if decision == "priority" else "strong",
                "visual_inspection_status": "legacy_claim",
                "curation_status": decision, "task_ids": [task["task_id"]],
            }
            self.papers.append(paper)
            self.registry["branches"][0]["papers"].append(paper)
            reason = f"{title}: task-specific reassessment with its uncertainty retained."
            evidence = {
                "source_url": paper["url"], "locator": "Section 3, fixed evaluation protocol",
                "claim": f"The primary source identifies the scope of {title}.",
                "source_quality": "primary", "status": "verified",
            }
            membership = {"paper_url": paper["url"], "role": role, "reason": reason}
            if role != "unreviewed":
                membership.update(reviewed_on=DATE, evidence=[copy.deepcopy(evidence)])
            task["members"].append(membership)
            row = {
                "paper_url": paper["url"], "decision": decision,
                "impact_score": score[0], "project_relevance_score": score[1],
                "evidence_strength": score[2], "reason": reason,
                "revisit_trigger": f"Revisit {title} when its missing protocol or source evidence changes.",
                "task_ids": [task["task_id"]], "review_artifact": self.artifact,
            }
            if decision == "undecided":
                row["dossier_path"] = f"undecided/{DATE}/LIB-A-paper-{number}.md"
            self.review["reviews"].append(row)
            audit = dict(
                copy.deepcopy(row), title=title, branch="A", role=role,
                task_id=task["task_id"], task_title=task["title"], scope=copy.deepcopy(task["scope"]),
                material_difference=f"The task-specific difference for {title} remains explicit.",
                requires_visual_review=decision == "undecided",
                requires_temporal_demo=decision == "undecided",
                visual_status="not_inspected" if decision == "undecided" else "not_applicable",
                visual_quality_score=0,
                visual_quality_decision="undecided" if decision == "undecided" else "not_applicable",
                inspection_evidence=[], sources=[evidence],
                not_applicable_reason="This recommendation uses the released metric protocol, not generated motion or robot execution quality.",
            )
            if decision == "source_issue":
                audit.update(
                    actual_source_title="A different paper at the original URL",
                    corrected_source_url="https://example.edu/corrected-paper",
                )
            self.audit["reviews"].append(audit)
            path = self.root / paper["deep_dive_path"]
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(f"# {title}\n\nOriginal collected analysis for paper {number}.\n")
        dossier = self.root / self.review["reviews"][2]["dossier_path"]
        dossier.parent.mkdir(parents=True, exist_ok=True)
        dossier.write_text("Local-only pending temporal inspection; no viewing claim.\n")
        self.write_sources()

    @staticmethod
    def make_task(task_id: str, title: str) -> dict:
        return {
            "task_id": task_id, "title": title, "branch": "A",
            "scope": {
                "input": "A fixed task configuration and model outputs.",
                "output": "Task-specific scores and failure records.",
                "setting": "A held-out controlled simulation task.",
                "protocol": "The same split, input conditions, budget and metric definitions.",
            },
            "members": [],
        }

    def write_sources(self) -> None:
        for relative, value in (
            ("data/papers.seed.json", self.registry),
            ("data/task_frontiers.seed.json", self.frontiers),
            ("data/library_review.seed.json", self.review),
            (self.artifact, self.audit),
        ):
            path = self.root / relative
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(json.dumps(value, ensure_ascii=False))

    def render(self, *arguments: str) -> subprocess.CompletedProcess:
        return subprocess.run(
            [sys.executable, str(RENDERER), "--root", str(self.root), *arguments],
            text=True, capture_output=True, check=False,
        )

    def indexes(self) -> dict[Path, str]:
        return build_indexes(self.registry, self.frontiers, self.root)

    def add_later_admission(self) -> dict:
        """Add an independently admitted v2 paper without editing the dated review."""
        paper = copy.deepcopy(self.papers[0])
        paper.pop("curation_status")
        paper.update(
            title="Later Accepted Work", url="https://example.edu/papers/later",
            deep_dive_path=f"paper_reads/{BRANCH_DIRECTORIES['A']}/later.md",
            acceptance_policy_version=2, branch="A", venue="arXiv",
            novelty="A substantial improvement under the same task and budget.",
            project_relevance="A directly reusable controlled evaluation interface.",
            impact_score=4, project_relevance_score=5, evidence_strength=4,
            requires_visual_review=False, requires_temporal_demo=False,
            not_applicable_reason="Admission uses the released evaluation protocol rather than generated motion quality.",
        )
        self.registry["branches"][0]["papers"].append(paper)
        self.frontiers["tasks"][0]["members"].append({
            "paper_url": paper["url"], "role": "current",
            "reason": "A separately admitted, source-backed starting point for this task.",
            "reviewed_on": "2026-10-21",
            "evidence": [{
                "source_url": paper["url"], "locator": "Table 4, matched split and budget",
                "claim": "The new protocol has controlled improvements and documents deployment costs.",
                "source_quality": "primary", "status": "verified",
            }],
        })
        self.registry["updated"] = self.frontiers["updated"] = "2026-10-21"
        (self.root / paper["deep_dive_path"]).write_text(
            "# Later Accepted Work\n\nacceptance_policy_version: 2\n\n"
            "The separately validated admission and matched task evidence are retained here.\n"
        )
        self.write_current_sources()
        return paper

    def write_current_sources(self) -> None:
        for relative, value in (("data/papers.seed.json", self.registry),
                                ("data/task_frontiers.seed.json", self.frontiers)):
            (self.root / relative).write_text(json.dumps(value, ensure_ascii=False))

    def test_eight_indexes_preserve_every_paper_once_but_only_priorities_are_unfolded(self) -> None:
        indexes = self.indexes()
        expected = {self.root / "paper_reads" / directory / "README.md"
                    for directory in BRANCH_DIRECTORIES.values()}
        expected.update(self.root / f"paper_reads/{name}" for name in
                        ("README.md", "task_frontiers.md", "library_review.md"))
        self.assertEqual(set(indexes), expected)
        for path in (self.root / "paper_reads/README.md",
                     self.root / "paper_reads" / BRANCH_DIRECTORIES["A"] / "README.md"):
            page = indexes[path]
            self.assertNotIn("<details open", page)
            self.assertEqual(page.count("<details>"), page.count("</details>"))
            for number, paper in enumerate(self.papers):
                link = f"[{paper['title']}]({Path(paper['deep_dive_path']).name})" if path.parent.name == BRANCH_DIRECTORIES["A"] else f"[{paper['title']}]({BRANCH_DIRECTORIES['A']}/paper-{number}.md)"
                with self.subTest(index=path.name, paper=paper["title"]):
                    self.assertEqual(page.count(link), 1)
                    self.assertEqual(link_depth(page, link) == 0, number == 0)

    def test_pending_tasks_are_folded_and_source_problems_are_never_current(self) -> None:
        indexes = self.indexes()
        page = indexes[self.root / "paper_reads/task_frontiers.md"]
        pending = folded_section(page, "<summary>待补证任务：Pending simulation（2 篇）</summary>")
        self.assertIn("Unwatched Simulator", pending)
        self.assertIn("Mismatched Source", pending)
        self.assertNotIn("任务角色：当前主推荐", pending)
        self.assertIn("来源待修复", pending)
        self.assertIn("待视觉复核", pending)
        self.assertIn("当前主推荐 1；并列备选 1；历史基线 0；未审查 2", page)
        main = indexes[self.root / "paper_reads/README.md"]
        source_line = next(line for line in main.splitlines() if line.startswith("- [Mismatched Source]"))
        self.assertIn("来源待修复", source_line)
        self.assertNotIn("当前主推荐", source_line)

    def test_full_review_keeps_scores_audit_links_and_original_source_correction(self) -> None:
        audit_before = (self.root / self.artifact).read_bytes()
        page = self.indexes()[self.root / "paper_reads/library_review.md"]
        issue = folded_section(page, "<summary>来源待修复（1 篇）</summary>")
        self.assertIn("本轮结论：来源待修复", issue)
        self.assertIn("未定 / 未定 / 1", issue)
        self.assertIn("https://example.edu/corrected-paper", issue)
        self.assertIn(self.papers[3]["url"], issue)
        self.assertIn("../" + self.artifact, issue)
        self.assertNotIn("任务角色：当前主推荐", issue)
        for paper in self.papers:
            link = f"[{paper['title']}]({BRANCH_DIRECTORIES['A']}/{Path(paper['deep_dive_path']).name})"
            self.assertEqual(page.count(link), 1)
        self.assertEqual((self.root / self.artifact).read_bytes(), audit_before)

    def test_check_detects_missing_or_stale_curated_indexes_without_writing(self) -> None:
        missing = self.render("--check")
        self.assertEqual(missing.returncode, 1)
        self.assertFalse((self.root / "paper_reads/library_review.md").exists())
        generated = self.render()
        self.assertEqual(generated.returncode, 0, generated.stderr)
        self.assertEqual(self.render("--check").returncode, 0)
        expected = self.indexes()
        self.assertEqual(len(expected), 8)
        path = self.root / "paper_reads/library_review.md"
        path.write_text("Existing review awaiting regeneration.\n")
        snapshot = {path: path.read_bytes() for path in expected}
        stale = self.render("--check")
        self.assertEqual(stale.returncode, 1)
        self.assertIn("paper_reads/library_review.md", stale.stderr)
        self.assertEqual(snapshot, {path: path.read_bytes() for path in expected})

    def test_disagreeing_sidecar_audit_or_registry_refuses_all_output_writes(self) -> None:
        self.assertEqual(self.render().returncode, 0)
        outputs = self.indexes()
        snapshot = {path: path.read_bytes() for path in outputs}
        baseline = copy.deepcopy((self.registry, self.review, self.audit))
        for changed_source in ("summary reason", "audit score", "registry status"):
            with self.subTest(source=changed_source):
                self.registry, self.review, self.audit = copy.deepcopy(baseline)
                if changed_source == "summary reason":
                    self.review["reviews"][0]["reason"] = "Summary changed without its source audit."
                elif changed_source == "audit score":
                    self.audit["reviews"][0]["evidence_strength"] = 5
                else:
                    self.registry["branches"][0]["papers"][0]["curation_status"] = "watchlist"
                self.write_sources()
                for arguments in ((), ("--check",)):
                    result = self.render(*arguments)
                    self.assertEqual(result.returncode, 1, result.stdout)
                    self.assertIn("library review", result.stderr)
                    self.assertEqual(snapshot, {path: path.read_bytes() for path in outputs})

    def test_temporal_claims_cannot_use_not_applicable_or_a_static_figure(self) -> None:
        audit = self.audit["reviews"][0]
        audit["requires_temporal_demo"] = True
        self.write_sources()
        with self.assertRaisesRegex(ValueError, "temporal evidence cannot waive visual review"):
            self.indexes()
        audit.update(requires_visual_review=True, visual_status="verified",
                     visual_quality_score=3, visual_quality_decision="adequate", inspection_evidence=[{
            "url": "https://example.edu/media/figure-3.png", "modality": "paper_figure",
            "locator": "Figure 3", "observation": "Only an initial and final static state are visible.",
            "limitations": "Contact, motion and action following cannot be judged from these states.",
        }])
        self.papers[0].update(visual_quality_score=3, visual_quality_decision="adequate")
        self.write_sources()
        with self.assertRaisesRegex(ValueError, "needs temporal inspection"):
            self.indexes()
        audit["inspection_evidence"] = [{
            "url": "https://example.edu/media/rollout.mp4", "modality": "video",
            "locator": "00:00-00:06, complete controlled rollout",
            "observation": "The commanded object moves and settles after release in this inspected clip.",
            "limitations": "One inspected trial does not establish performance across all tasks.",
        }]
        self.write_sources()
        self.assertEqual(len(self.indexes()), 8)

    def test_reorganization_preserves_source_issue_identity_and_historical_analysis(self) -> None:
        paper = self.papers[3]
        original_url = paper["url"]
        original_labels = {key: paper[key] for key in (
            "source_quality", "evidence_strength", "demo_score", "visual_quality_score",
            "visual_quality_decision", "visual_inspection_status",
        )}
        audit_before = (self.root / self.artifact).read_bytes()
        deep_path = self.root / paper["deep_dive_path"]
        original_analysis = deep_path.read_text().split("\n", 1)[1]
        result = subprocess.run(
            [sys.executable, str(REORGANIZER), "--root", str(self.root), "--date", DATE],
            text=True, capture_output=True, check=False,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        registry = json.loads((self.root / "data/papers.seed.json").read_text())
        preserved = next(p for branch in registry["branches"] for p in branch["papers"] if p["url"] == original_url)
        self.assertEqual(preserved["curation_status"], "source_issue")
        self.assertEqual(preserved["source_quality"], "unverified")
        self.assertEqual(preserved["deep_dive_path"], paper["deep_dive_path"])
        self.assertEqual(preserved["historical_acceptance"], original_labels)
        self.assertIn(original_analysis, deep_path.read_text())
        self.assertIn("来源待修复", deep_path.read_text())
        self.assertEqual((self.root / self.artifact).read_bytes(), audit_before)
        audit = json.loads((self.root / self.artifact).read_text())["reviews"][3]
        self.assertEqual(audit["paper_url"], original_url)
        self.assertEqual(audit["actual_source_title"], "A different paper at the original URL")
        self.assertEqual(audit["corrected_source_url"], "https://example.edu/corrected-paper")
        managed_paths = [self.root / name for name in (
            "data/papers.seed.json", "data/task_frontiers.seed.json", "data/library_review.seed.json",
        )]
        managed_paths.extend(self.root / paper["deep_dive_path"] for paper in self.papers)
        snapshot = {path: path.read_bytes() for path in managed_paths}
        repeated = subprocess.run(
            [sys.executable, str(REORGANIZER), "--root", str(self.root), "--date", DATE],
            text=True, capture_output=True, check=False,
        )
        self.assertEqual(repeated.returncode, 0, repeated.stderr)
        self.assertEqual(snapshot, {path: path.read_bytes() for path in managed_paths})
        self.assertEqual((self.root / self.artifact).read_bytes(), audit_before)
        self.assertEqual(self.render().returncode, 0)
        rendered = (self.root / "paper_reads/library_review.md").read_text()
        self.assertIn(audit["corrected_source_url"], rendered)

    def test_later_v2_admission_is_visible_without_rewriting_the_dated_review(self) -> None:
        review_path = self.root / "data/library_review.seed.json"
        audit_path = self.root / self.artifact
        snapshot = {path: path.read_bytes() for path in (review_path, audit_path)}
        paper = self.add_later_admission()
        indexes = self.indexes()
        main = indexes[self.root / "paper_reads/README.md"]
        link = f"[{paper['title']}]({BRANCH_DIRECTORIES['A']}/later.md)"
        self.assertEqual(main.count(link), 1)
        self.assertEqual(link_depth(main, link), 0)
        task_page = indexes[self.root / "paper_reads/task_frontiers.md"]
        self.assertIn("#### Later Accepted Work", task_page)
        review_page = indexes[self.root / "paper_reads/library_review.md"]
        self.assertIn("此次复审后按新版标准收录", review_page)
        self.assertIn(link, review_page)
        self.assertEqual(len(json.loads(review_path.read_text())["reviews"]), 4)
        self.assertNotIn(paper["url"], review_path.read_text())
        self.assertEqual(snapshot, {path: path.read_bytes() for path in snapshot})
        self.assertEqual(self.render().returncode, 0)
        self.assertEqual(self.render("--check").returncode, 0)

    def test_evidence_backed_successor_folds_old_priority_without_changing_its_review(self) -> None:
        review_path = self.root / "data/library_review.seed.json"
        audit_path = self.root / self.artifact
        snapshot = {path: path.read_bytes() for path in (review_path, audit_path)}
        successor = self.add_later_admission()
        predecessor = self.frontiers["tasks"][0]["members"][0]
        predecessor.update(
            role="historical", superseded_by=successor["url"], reviewed_on="2026-10-21",
            reason="Matched task evidence supports the successor while retaining this original baseline.",
            comparison={
                "same_task": True, "comparable_protocol": True, "no_material_regression": True,
                "improvements": "Table 4 reports a substantial controlled gain on the same split and budget.",
                "tradeoffs": "Table 5 preserves runtime, availability and all decision-relevant capabilities.",
                "retained_value": "The original released protocol remains useful for lineage and baseline reproduction.",
            },
        )
        predecessor["evidence"].append({
            "source_url": successor["url"], "locator": "Tables 4-5, controlled task and cost comparison",
            "claim": "The successor improves the same protocol without material runtime or capability regression.",
            "source_quality": "primary", "status": "verified",
        })
        self.write_current_sources()
        indexes = self.indexes()
        for path in (self.root / "paper_reads/README.md",
                     self.root / "paper_reads" / BRANCH_DIRECTORIES["A"] / "README.md"):
            page = indexes[path]
            line = next(line for line in page.splitlines() if line.startswith("- [Released Protocol]"))
            self.assertIn("参考备选", line)
            self.assertIn("历史基线", line)
            self.assertNotIn("优先阅读", line)
            self.assertNotIn("当前主推荐", line)
            self.assertGreater(link_depth(page, line), 0)
            future_line = next(line for line in page.splitlines() if line.startswith("- [Later Accepted Work]"))
            self.assertEqual(link_depth(page, future_line), 0)
        task_page = indexes[self.root / "paper_reads/task_frontiers.md"]
        history = folded_section(task_page, "<summary>历史基线：Released Protocol（2026）</summary>")
        self.assertIn("后继：[Later Accepted Work]", history)
        self.assertIn("保留价值", history)
        self.assertEqual(self.papers[0]["curation_status"], "priority")
        self.assertEqual(self.review["reviews"][0]["decision"], "priority")
        self.assertEqual(snapshot, {path: path.read_bytes() for path in snapshot})

    def test_an_unreviewed_preexisting_paper_cannot_use_the_later_admission_exception(self) -> None:
        self.add_later_admission()
        self.review["reviews"] = [row for row in self.review["reviews"]
                                   if row["paper_url"] != self.papers[1]["url"]]
        self.write_sources()
        with self.assertRaisesRegex(ValueError, "cover every pre-existing registry paper"):
            self.indexes()
        result = self.render()
        self.assertEqual(result.returncode, 1)
        self.assertFalse((self.root / "paper_reads/README.md").exists())


if __name__ == "__main__":
    unittest.main()
