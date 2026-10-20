#!/usr/bin/env python3
"""Validate task frontiers without changing paper records or archived deep dives."""

import argparse
import json
from pathlib import Path

from task_lifecycle import validate_task_frontiers


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    try:
        registry = json.loads((args.root / "data/papers.seed.json").read_text())
        frontiers = json.loads((args.root / "data/task_frontiers.seed.json").read_text())
    except (OSError, ValueError) as exc:
        print(f"Task-frontier validation failed: {exc}")
        return 1
    errors = validate_task_frontiers(frontiers, registry, args.root)
    if errors:
        print("Task-frontier validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"Task-frontier validation passed: {len(frontiers['tasks'])} task scopes; no global paper archival inferred.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
