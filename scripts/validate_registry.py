#!/usr/bin/env python3
"""Validate the frontier research paper registry."""

from __future__ import annotations

import json
import os
import sys
from pathlib import Path
from urllib.parse import urlparse


REQUIRED = {
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

MIN_YEAR = 2024
VISUAL_DECISIONS = {"strong", "adequate", "weak", "undecided", "not_applicable"}


def valid_url(value: str) -> bool:
    parsed = urlparse(value)
    return parsed.scheme in {"http", "https"} and bool(parsed.netloc)


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    repo_root = root.parent
    registry = root / "data" / "papers.seed.json"
    data = json.loads(registry.read_text())

    errors: list[str] = []
    warnings: list[str] = []
    seen_titles: set[str] = set()
    branch_ids = set()
    require_local_pdfs = os.environ.get("REQUIRE_LOCAL_PDFS") == "1"

    if data.get("minimum_year") != MIN_YEAR:
        errors.append(f"registry minimum_year must be {MIN_YEAR}")

    for branch in data.get("branches", []):
        branch_id = branch.get("id")
        branch_name = branch.get("name")
        if not branch_id or not branch_name:
            errors.append("branch missing id or name")
            continue
        branch_ids.add(branch_id)
        for paper in branch.get("papers", []):
            label = f"{branch_id}:{paper.get('title', '<missing title>')}"
            missing = sorted(REQUIRED - set(paper))
            if missing:
                errors.append(f"{label} missing fields: {', '.join(missing)}")
            title = paper.get("title", "").strip().lower()
            if title in seen_titles:
                errors.append(f"duplicate title: {paper.get('title')}")
            if title:
                seen_titles.add(title)
            url = paper.get("url", "")
            if not valid_url(url):
                errors.append(f"{label} has invalid url: {url}")
            year = paper.get("year")
            if not isinstance(year, int) or year < MIN_YEAR:
                errors.append(f"{label} year must be >= {MIN_YEAR}")
            local_pdf = paper.get("local_pdf")
            if local_pdf:
                local_pdf_path = Path(local_pdf)
                if not local_pdf_path.is_absolute():
                    local_pdf_path = repo_root / local_pdf_path
                if not local_pdf_path.exists():
                    message = f"{label} local_pdf does not exist: {local_pdf}"
                    if require_local_pdfs:
                        errors.append(message)
                    else:
                        warnings.append(message)
            demo_score = paper.get("demo_score")
            if not isinstance(demo_score, int) or not 0 <= demo_score <= 5:
                errors.append(f"{label} demo_score must be an integer from 0 to 5")
            visual_quality_score = paper.get("visual_quality_score")
            if not isinstance(visual_quality_score, int) or not 0 <= visual_quality_score <= 5:
                errors.append(f"{label} visual_quality_score must be an integer from 0 to 5")
            visual_quality_decision = paper.get("visual_quality_decision")
            if visual_quality_decision not in VISUAL_DECISIONS:
                errors.append(f"{label} visual_quality_decision must be one of {sorted(VISUAL_DECISIONS)}")
            evidence_strength = paper.get("evidence_strength")
            if not isinstance(evidence_strength, int) or not 0 <= evidence_strength <= 5:
                errors.append(f"{label} evidence_strength must be an integer from 0 to 5")

    expected = {"A", "B", "C", "D", "E"}
    if branch_ids != expected:
        errors.append(f"branch ids should be {sorted(expected)}, got {sorted(branch_ids)}")

    if errors:
        print("Registry validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    count = sum(len(branch.get("papers", [])) for branch in data["branches"])
    if warnings:
        print("Registry validation warnings:")
        for warning in warnings:
            print(f"- {warning}")
    print(f"Registry validation passed: {count} papers across {len(data['branches'])} branches, minimum year {MIN_YEAR}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
