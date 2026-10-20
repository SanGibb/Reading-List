"""Behavioral checks for complete indexes and task-scoped history rendering."""

from __future__ import annotations

import copy
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

from scripts.render_reading_indexes import BRANCH_DIRECTORIES, build_indexes, paper_anchor


RENDERER = Path(__file__).resolve().parents[1] / "scripts/render_reading_indexes.py"


def registry_fixture(count: int = 5) -> dict:
    branches = [{"id": branch, "name": f"Branch {branch}", "papers": []} for branch in "ABCDE"]
    for number in range(count):
        branch = branches[number % 5]
        branch["papers"].append({
            "title": f"Paper {number}",
            "year": 2024 + number % 3,
            "url": f"https://example.edu/papers/{number}",
            "deep_dive_path": f"paper_reads/{BRANCH_DIRECTORIES[branch['id']]}/paper-{number}.md",
        })
    return {"branches": branches}


def member(number: int, role: str = "unreviewed", successor: int | None = None) -> dict:
    record = {
        "paper_url": f"https://example.edu/papers/{number}",
        "role": role,
        "reason": f"Task-specific judgment for Paper {number}.",
    }
    if role != "unreviewed":
        record.update({
            "reviewed_on": "2026-10-20",
            "evidence": [{
                "source_url": f"https://example.edu/papers/{number}",
                "locator": "Table 2, matched held-out task and compute budget",
                "claim": f"Paper {number} supports this task-specific comparison.",
                "source_quality": "official",
                "status": "verified",
            }],
        })
    if role == "historical":
        record.update({
            "superseded_by": f"https://example.edu/papers/{successor}",
            "comparison": {
                "same_task": True,
                "comparable_protocol": True,
                "no_material_regression": True,
                "improvements": f"Successor improves controlled performance over Paper {number}.",
                "tradeoffs": "No material regression within this task and protocol; broader settings remain untested.",
                "retained_value": f"Paper {number} remains a reproducible historical baseline.",
            },
        })
    return record


def task(task_id: str, members: list[dict]) -> dict:
    return {
        "task_id": task_id,
        "title": f"Task {task_id}",
        "branch": "A",
        "scope": {
            "input": "Matched observation and instruction.",
            "output": "Executable articulated asset.",
            "setting": "Held-out cabinet manipulation in the same simulator.",
            "protocol": "Same split, input observations, hardware budget and success metric.",
        },
        "members": members,
    }


def frontiers_fixture() -> dict:
    return {
        "lifecycle_schema_version": 1,
        "updated": "2026-10-20",
        "tasks": [
            task("asset-generation", [member(0, "historical", 1), member(1, "historical", 2), member(2, "current"), member(3)]),
            task("efficient-generation", [member(0, "current"), member(3, "alternative")]),
        ],
    }


class ReadingIndexTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.registry = registry_fixture()
        self.frontiers = frontiers_fixture()
        self.write_fixture()

    def write_fixture(self) -> None:
        (self.root / "data").mkdir(exist_ok=True)
        (self.root / "data/papers.seed.json").write_text(json.dumps(self.registry))
        (self.root / "data/task_frontiers.seed.json").write_text(json.dumps(self.frontiers))
        for branch in self.registry["branches"]:
            for paper in branch["papers"]:
                path = self.root / paper["deep_dive_path"]
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(f"# {paper['title']}\n")

    def run_cli(self, *arguments: str) -> subprocess.CompletedProcess:
        return subprocess.run(
            [sys.executable, str(RENDERER), "--root", str(self.root), *arguments],
            text=True, capture_output=True, check=False,
        )

    def test_multilevel_history_is_folded_under_current_with_reverse_links(self) -> None:
        page = build_indexes(self.registry, self.frontiers, self.root)[self.root / "paper_reads/task_frontiers.md"]
        current = page.index("#### Paper 2")
        middle = page.index("<summary>历史基线：Paper 1")
        oldest = page.index("<summary>历史基线：Paper 0")
        first_close = page.index("</details>")
        self.assertLess(current, middle)
        self.assertLess(middle, oldest)
        self.assertLess(oldest, first_close)
        self.assertEqual(page.count("<summary>历史基线："), 2)
        self.assertEqual(page.count("<details>"), page.count("</details>"))
        self.assertIn(f"后继：[Paper 2](#{paper_anchor('asset-generation', 'https://example.edu/papers/2')})", page)
        self.assertIn(f"后继：[Paper 1](#{paper_anchor('asset-generation', 'https://example.edu/papers/1')})", page)
        for label in ("归档原因", "证据", "保留价值", "实质改进", "取舍与适用边界"):
            self.assertIn(label, page[middle:first_close])
        self.assertIn("Paper 0 remains a reproducible historical baseline.", page)

    def test_historical_in_one_task_remains_current_in_another_and_fully_listed(self) -> None:
        indexes = build_indexes(self.registry, self.frontiers, self.root)
        main = indexes[self.root / "paper_reads/README.md"]
        line = next(line for line in main.splitlines() if line.startswith("- [Paper 0]"))
        self.assertIn("Task asset-generation：历史基线", line)
        self.assertIn("Task efficient-generation：当前主推荐", line)
        self.assertEqual(main.count("- [Paper 0]"), 1)
        branch = indexes[self.root / "paper_reads/A_executable_world_representation/README.md"]
        self.assertIn("[Paper 0](paper-0.md)", branch)
        self.assertIn("../task_frontiers.md#", branch)
        page = indexes[self.root / "paper_reads/task_frontiers.md"]
        self.assertIn("### 并列备选", page)
        self.assertIn("### 未审查成员", page)
        self.assertIn("尚未分配到任务：1 篇（未审查）", page)
        self.assertIn("当前主推荐 2；并列备选 1；历史基线 2；未审查 1", page)

    def test_all_168_papers_have_complete_indexes_without_implicit_current(self) -> None:
        self.registry = registry_fixture(168)
        self.frontiers["tasks"] = []
        self.write_fixture()
        indexes = build_indexes(self.registry, self.frontiers, self.root)
        self.assertEqual(len(indexes), 7)
        main = indexes[self.root / "paper_reads/README.md"]
        self.assertIn("Maintained deep dives: 168", main)
        self.assertEqual(main.count("任务更迭：未审查"), 168)
        for branch in self.registry["branches"]:
            branch_index = indexes[self.root / "paper_reads" / BRANCH_DIRECTORIES[branch["id"]] / "README.md"]
            self.assertIn(f"Maintained deep dives: {len(branch['papers'])}", branch_index)
            for paper in branch["papers"]:
                self.assertIn(paper["deep_dive_path"].removeprefix("paper_reads/"), main)
                self.assertIn(Path(paper["deep_dive_path"]).name, branch_index)
        page = indexes[self.root / "paper_reads/task_frontiers.md"]
        self.assertIn("已有比较审核的任务：0", page)
        self.assertIn("当前主推荐 0；并列备选 0；历史基线 0；未审查 0", page)
        self.assertIn("尚未分配到任务：168 篇（未审查）", page)

    def test_unreviewed_task_families_do_not_count_as_reviewed(self) -> None:
        self.frontiers["tasks"] = [task("pending-family", [member(0), member(1)])]
        page = build_indexes(self.registry, self.frontiers, self.root)[self.root / "paper_reads/task_frontiers.md"]
        self.assertIn("已有比较审核的任务：0", page)
        self.assertIn("当前主推荐 0；并列备选 0；历史基线 0；未审查 2", page)
        self.assertIn("尚无经过比较审核的当前主推荐", page)
        self.assertNotIn("<summary>历史基线：", page)

    def test_unclassified_papers_are_folded_with_all_links_preserved(self) -> None:
        self.registry = registry_fixture(168)
        self.frontiers["tasks"] = [task("pending-family", [member(number) for number in range(4)])]
        self.write_fixture()
        indexes = build_indexes(self.registry, self.frontiers, self.root)
        page = indexes[self.root / "paper_reads/task_frontiers.md"]
        section = page.index("## 尚未进入任务比较的存量论文")
        opening = page.index("<details>", section)
        summary = page.index("<summary>展开未审查存量论文（共 164 篇）</summary>", opening)
        closing = page.index("</details>", summary)
        self.assertNotIn("<details open", page[section:])
        folded = page[summary:closing]
        for branch in self.registry["branches"]:
            for paper in branch["papers"]:
                destination = paper["deep_dive_path"].removeprefix("paper_reads/")
                self.assertIn(destination, page)
                self.assertIn(destination, indexes[self.root / "paper_reads/README.md"])
                if paper["url"] not in {f"https://example.edu/papers/{number}" for number in range(4)}:
                    self.assertIn(destination, folded)

    def test_check_detects_missing_and_stale_outputs_without_writing(self) -> None:
        missing = self.run_cli("--check")
        self.assertEqual(missing.returncode, 1)
        self.assertFalse((self.root / "paper_reads/README.md").exists())
        generated = self.run_cli()
        self.assertEqual(generated.returncode, 0, generated.stderr)
        snapshot = {path: path.read_bytes() for path in (self.root / "paper_reads").rglob("*.md")}
        self.assertEqual(self.run_cli("--check").returncode, 0)
        self.assertEqual(self.run_cli().returncode, 0)
        self.assertEqual(snapshot, {path: path.read_bytes() for path in snapshot})
        main = self.root / "paper_reads/README.md"
        main.write_text("stale index\n")
        stale = self.run_cli("--check")
        self.assertEqual(stale.returncode, 1)
        self.assertIn("paper_reads/README.md", stale.stderr)
        self.assertEqual(main.read_text(), "stale index\n")

    def test_invalid_history_fails_before_any_output_is_written(self) -> None:
        self.frontiers["tasks"][0]["members"][0]["superseded_by"] = "https://example.edu/papers/4"
        self.write_fixture()
        sentinel = self.root / "paper_reads/README.md"
        sentinel.write_text("existing index\n")
        result = self.run_cli()
        self.assertEqual(result.returncode, 1)
        self.assertIn("successor must be another member of the same task", result.stderr)
        self.assertEqual(sentinel.read_text(), "existing index\n")
        self.assertFalse((self.root / "paper_reads/task_frontiers.md").exists())

    def test_rendering_is_deterministic_after_task_and_member_reordering(self) -> None:
        first = build_indexes(self.registry, self.frontiers, self.root)
        reordered = copy.deepcopy(self.frontiers)
        reordered["tasks"].reverse()
        for item in reordered["tasks"]:
            item["members"].reverse()
        self.assertEqual(first, build_indexes(self.registry, reordered, self.root))


if __name__ == "__main__":
    unittest.main()
