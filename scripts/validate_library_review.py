#!/usr/bin/env python3
"""Validate current retrospective reading decisions and their original evidence."""

import argparse
import json
from pathlib import Path
import sys

if __package__:
    from .library_review import validate_library_review
else:
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
    from scripts.library_review import validate_library_review


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    try:
        docs = [json.loads((args.root / "data" / name).read_text()) for name in (
            "library_review.seed.json", "papers.seed.json", "task_frontiers.seed.json"
        )]
    except (OSError, ValueError) as exc:
        print(f"Library-review validation failed: {exc}")
        return 1
    errors = validate_library_review(*docs, root=args.root)
    if errors:
        print("Library-review validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"Library-review validation passed: {len(docs[0]['reviews'])} preserved papers, all decisions traced.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
