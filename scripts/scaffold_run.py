#!/usr/bin/env python3
"""Create an empty consolidated multi-agent run directory."""

from __future__ import annotations

import json
import sys
from pathlib import Path


def write_json(path: Path, obj: dict) -> None:
    path.write_text(json.dumps(obj, indent=2, ensure_ascii=False) + "\n")


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: scaffold_run.py YYYY-MM-DD", file=sys.stderr)
        return 2

    run_id = sys.argv[1]
    root = Path(__file__).resolve().parents[1]
    run_dir = root / "reports" / "runs" / run_id
    run_dir.mkdir(parents=True, exist_ok=True)

    write_json(
        run_dir / "00_run_plan.json",
        {
            "run_id": run_id,
            "created_at": run_id,
            "branches": ["A", "B", "C", "D", "E"],
            "minimum_year": 2024,
            "search_windows": {"default_days": 14, "high_priority_days": 45},
            "branch_queries": {"A": [], "B": [], "C": [], "D": [], "E": []},
            "known_registry_path": "data/papers.seed.json",
            "follow_sources_path": "data/follow_sources.seed.json",
            "harness_paths": [
                "harness/system_harness.md",
                "harness/acceptance_harness.md",
            ],
        },
    )
    write_json(
        run_dir / "01_discovery.json",
        {"run_id": run_id, "followed_sources_checked": [], "candidates": [], "triage": []},
    )
    write_json(
        run_dir / "02_evidence.json",
        {"run_id": run_id, "paper_cards": [], "demo_cards": []},
    )
    write_json(
        run_dir / "03_review.json",
        {"run_id": run_id, "visual_cards": [], "quality_review": [], "run_level_issues": []},
    )
    (run_dir / "04_editor_report.md").write_text(
        f"# Weekly Interactive Embodied Generation Frontier Scan\n\nDate: {run_id}\n\nNo accepted updates yet.\n"
    )
    write_json(
        run_dir / "05_registry_patch.json",
        {
            "run_id": run_id,
            "branch_assignments": [],
            "taxonomy_change_proposals": [],
            "registry_additions": [],
            "registry_updates": [],
            "registry_noops": [],
        },
    )
    write_json(
        run_dir / "run_manifest.json",
        {
            "run_id": run_id,
            "status": "scaffolded",
            "created_artifacts": [
                "00_run_plan.json",
                "01_discovery.json",
                "02_evidence.json",
                "03_review.json",
                "04_editor_report.md",
                "05_registry_patch.json",
            ],
            "created_directories": [],
            "validation": "not_run",
        },
    )
    print(f"Created run scaffold: {run_dir}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
