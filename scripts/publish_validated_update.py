#!/usr/bin/env python3
"""Validate, commit, and push publishable reading-list updates.

Undecided dossiers are intentionally local-only. This script validates that
they exist locally when referenced, but does not stage `undecided/**` except
for `undecided/README.md`.
"""

from __future__ import annotations

import argparse
import os
import subprocess
import sys
from pathlib import Path


EXCLUDED_PREFIXES = ("undecided/",)
INCLUDED_EXCEPTIONS = {"undecided/README.md"}


def run(cmd: list[str], cwd: Path, env: dict[str, str] | None = None) -> subprocess.CompletedProcess[str]:
    print("+ " + " ".join(cmd))
    return subprocess.run(cmd, cwd=cwd, env=env, text=True, check=False)


def changed_paths(root: Path) -> list[tuple[str, str]]:
    result = subprocess.run(
        ["git", "status", "--porcelain"],
        cwd=root,
        text=True,
        check=True,
        stdout=subprocess.PIPE,
    )
    paths: list[tuple[str, str]] = []
    for line in result.stdout.splitlines():
        if not line:
            continue
        status = line[:2]
        path = line[3:]
        if " -> " in path:
            path = path.split(" -> ", 1)[1]
        paths.append((status, path))
    return paths


def publishable(status: str, path: str) -> bool:
    if path in INCLUDED_EXCEPTIONS:
        return True
    if path.startswith(EXCLUDED_PREFIXES) and status[0] == "D":
        # Allow one-time cleanup commits that remove previously tracked
        # undecided dossiers from the remote repository.
        return True
    return not path.startswith(EXCLUDED_PREFIXES)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--message", default="Update frontier reading list")
    parser.add_argument("--remote", default="origin")
    parser.add_argument("--branch", default="")
    parser.add_argument("--no-push", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    root = Path(__file__).resolve().parents[1]
    env = os.environ.copy()
    env["REQUIRE_UNDECIDED_DOSSIERS"] = "1"

    if run([sys.executable, "scripts/validate_all.py"], root, env=env).returncode != 0:
        return 1

    paths = changed_paths(root)
    publishable_pairs = [(status, path) for status, path in paths if publishable(status, path)]
    publishable_paths = [path for _, path in publishable_pairs]
    paths_to_add = [
        path
        for status, path in publishable_pairs
        if not (path.startswith(EXCLUDED_PREFIXES) and status[0] == "D")
    ]
    local_only_paths = [path for status, path in paths if not publishable(status, path)]

    if local_only_paths:
        print("Local-only paths left unstaged:")
        for path in local_only_paths:
            print(f"- {path}")

    if not publishable_paths:
        print("No publishable changes to commit.")
        return 0

    if args.dry_run:
        print("Publishable paths:")
        for path in publishable_paths:
            print(f"- {path}")
        return 0

    if paths_to_add:
        if run(["git", "add", "--", *paths_to_add], root).returncode != 0:
            return 1

    diff_result = run(["git", "diff", "--cached", "--quiet"], root)
    if diff_result.returncode == 0:
        print("No staged changes after applying publish filters.")
        return 0
    if diff_result.returncode not in {0, 1}:
        return diff_result.returncode

    if run(["git", "commit", "-m", args.message], root).returncode != 0:
        return 1

    if args.no_push:
        print("Committed locally; push skipped by --no-push.")
        return 0

    branch = args.branch
    if not branch:
        branch_result = subprocess.run(
            ["git", "branch", "--show-current"],
            cwd=root,
            text=True,
            check=True,
            stdout=subprocess.PIPE,
        )
        branch = branch_result.stdout.strip() or "main"

    return run(["git", "push", args.remote, branch], root).returncode


if __name__ == "__main__":
    sys.exit(main())
