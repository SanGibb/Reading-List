#!/usr/bin/env python3
"""Run all mechanical repository validations."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


def run(cmd: list[str], cwd: Path) -> int:
    print("+ " + " ".join(cmd))
    return subprocess.run(cmd, cwd=cwd, check=False).returncode


def validate_json(path: Path) -> list[str]:
    try:
        json.loads(path.read_text())
    except Exception as exc:  # noqa: BLE001
        return [f"{path.relative_to(path.parents[1])} is invalid JSON: {exc}"]
    return []


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    errors: list[str] = []

    for json_path in [
        root / "data" / "papers.seed.json",
        root / "data" / "follow_sources.seed.json",
    ]:
        errors.extend(validate_json(json_path))

    if errors:
        print("Static JSON validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    if run([sys.executable, "scripts/validate_registry.py"], root) != 0:
        return 1

    runs_root = root / "reports" / "runs"
    if runs_root.exists():
        for run_dir in sorted(path for path in runs_root.iterdir() if path.is_dir()):
            if (run_dir / "run_manifest.json").exists():
                if run([sys.executable, "scripts/validate_run.py", run_dir.name], root) != 0:
                    return 1

    print("All validations passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
