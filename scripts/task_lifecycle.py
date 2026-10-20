"""Validate task-scoped reading recommendations and evidence-backed succession."""

from __future__ import annotations

from datetime import date
from pathlib import Path
import re
from urllib.parse import urlparse


ROLES = {"current", "alternative", "historical", "unreviewed"}
TASK_ID = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
OFFICIAL_SOURCES = {"primary", "official", "primary_or_official"}


def text(value: object) -> bool:
    return isinstance(value, str) and bool(value.strip())


def url(value: object) -> bool:
    if not isinstance(value, str):
        return False
    parsed = urlparse(value)
    return parsed.scheme in {"http", "https"} and bool(parsed.netloc)


def iso_date(value: object) -> bool:
    if not isinstance(value, str):
        return False
    try:
        return date.fromisoformat(value).isoformat() == value
    except ValueError:
        return False


def validate_task_frontiers(frontiers: dict, registry: dict, root: Path | None = None) -> list[str]:
    """No global paper archival is inferred from a role in one particular task."""
    errors: list[str] = []
    if not isinstance(frontiers, dict) or not isinstance(registry, dict):
        return ["task frontiers and registry must be JSON objects"]
    if type(frontiers.get("lifecycle_schema_version")) is not int or frontiers["lifecycle_schema_version"] != 1:
        errors.append("task frontiers lifecycle_schema_version must be 1")
    if not iso_date(frontiers.get("updated")):
        errors.append("task frontiers updated must be an ISO date")

    papers: dict[str, dict] = {}
    branches = registry.get("branches", [])
    if not isinstance(branches, list):
        return errors + ["registry branches must be an array"]
    for branch in branches:
        if not isinstance(branch, dict) or not isinstance(branch.get("papers"), list):
            errors.append("registry branches need a papers array")
            continue
        for paper in branch["papers"]:
            if not isinstance(paper, dict):
                errors.append("registry papers must be objects")
                continue
            ref = paper.get("url")
            if not url(ref):
                errors.append("task registry paper needs a valid URL")
                continue
            if ref in papers:
                errors.append(f"duplicate canonical paper URL: {ref}")
            papers[ref] = paper
            path = paper.get("deep_dive_path")
            if not isinstance(path, str) or not path.startswith("paper_reads/") or Path(path).is_absolute() or ".." in Path(path).parts:
                errors.append(f"paper {ref} needs a safe paper_reads/ deep_dive_path")
            elif root is not None:
                target = (root / path).resolve()
                if not target.is_relative_to(root.resolve()):
                    errors.append(f"paper {ref} deep dive escapes the repository root: {path}")
                elif not target.is_file():
                    errors.append(f"paper {ref} deep dive does not exist: {path}")

    tasks = frontiers.get("tasks")
    if not isinstance(tasks, list):
        return errors + ["task frontiers tasks must be an array"]
    task_ids: set[str] = set()
    memberships: dict[str, set[str]] = {ref: set() for ref in papers}
    for task in tasks:
        if not isinstance(task, dict):
            errors.append("task entries must be objects")
            continue
        tid = task.get("task_id")
        if not isinstance(tid, str) or not TASK_ID.fullmatch(tid):
            errors.append("task_id must be a stable lowercase-hyphen identifier")
            continue
        if tid in task_ids:
            errors.append(f"duplicate task_id: {tid}")
        task_ids.add(tid)
        label = f"task {tid}"
        if not text(task.get("title")) or task.get("branch") not in set("ABCDE"):
            errors.append(f"{label} needs title and primary branch A-E")
        scope = task.get("scope")
        if not isinstance(scope, dict) or any(not text(scope.get(key)) for key in ("input", "output", "setting", "protocol")):
            errors.append(f"{label} needs explicit input/output/setting/protocol scope")
        members = task.get("members")
        if not isinstance(members, list) or not members:
            errors.append(f"{label} needs at least one member")
            continue
        member_map: dict[str, dict] = {}
        for member in members:
            if not isinstance(member, dict):
                errors.append(f"{label} members must be objects")
                continue
            ref = member.get("paper_url")
            if not isinstance(ref, str) or ref not in papers:
                errors.append(f"{label} references an unknown registry paper: {ref}")
                continue
            if ref in member_map:
                errors.append(f"{label} has a duplicate member: {ref}")
            member_map[ref] = member
            memberships[ref].add(tid)
            role = member.get("role")
            if role not in ROLES:
                errors.append(f"{label} {ref} has an invalid role")
            if not text(member.get("reason")):
                errors.append(f"{label} {ref} needs a specific reason")
            if role == "unreviewed":
                if "superseded_by" in member:
                    errors.append(f"{label} unreviewed member cannot have superseded_by")
                continue
            if not iso_date(member.get("reviewed_on")):
                errors.append(f"{label} {ref} needs reviewed_on")
            elif iso_date(frontiers.get("updated")) and member["reviewed_on"] > frontiers["updated"]:
                errors.append(f"{label} reviewed_on cannot be later than updated")
            evidence = member.get("evidence")
            if not isinstance(evidence, list) or not evidence:
                errors.append(f"{label} {ref} needs official evidence for its reviewed role")
            else:
                for item in evidence:
                    if not isinstance(item, dict):
                        errors.append(f"{label} evidence entries must be objects")
                        continue
                    if not url(item.get("source_url")) or not text(item.get("locator")) or not text(item.get("claim")):
                        errors.append(f"{label} evidence needs source_url, locator, and claim")
                    if item.get("source_quality") not in OFFICIAL_SOURCES or item.get("status") != "verified":
                        errors.append(f"{label} lifecycle evidence must be verified primary/official evidence")
            if role != "historical":
                if "superseded_by" in member:
                    errors.append(f"{label} only historical members can have superseded_by")
                continue
            successor = member.get("superseded_by")
            if not url(successor) or successor == ref:
                errors.append(f"{label} historical {ref} needs a distinct successor")
            comparison = member.get("comparison")
            if not isinstance(comparison, dict):
                errors.append(f"{label} historical {ref} needs a comparison")
            else:
                for key in ("same_task", "comparable_protocol", "no_material_regression"):
                    if comparison.get(key) is not True:
                        errors.append(f"{label} cannot archive without {key}: true")
                for key in ("improvements", "tradeoffs", "retained_value"):
                    if not text(comparison.get(key)):
                        errors.append(f"{label} comparison needs {key}")

        # Each historical record points to one successor. Rendering reverses these
        # edges so predecessors fold underneath the latest recommendation.
        for ref, member in member_map.items():
            if member.get("role") != "historical":
                continue
            seen: set[str] = set()
            cursor = ref
            while cursor in member_map and member_map[cursor].get("role") == "historical":
                if cursor in seen:
                    errors.append(f"{label} contains a supersession cycle involving {cursor}")
                    break
                seen.add(cursor)
                successor = member_map[cursor].get("superseded_by")
                if not isinstance(successor, str) or successor not in member_map:
                    errors.append(f"{label} successor must be another member of the same task")
                    break
                cursor = successor
            else:
                if cursor not in member_map or member_map[cursor].get("role") != "current":
                    errors.append(f"{label} historical chain must terminate at a current recommendation")

    # Newly admitted papers must be classified for a task; existing unclassified
    # literature remains available and is never implicitly labeled current/obsolete.
    for ref, paper in papers.items():
        ids = paper.get("task_ids")
        if ids is None and paper.get("acceptance_policy_version") != 2:
            continue
        if not isinstance(ids, list) or not ids or any(not isinstance(tid, str) for tid in ids):
            errors.append(f"paper {ref} needs non-empty task_ids")
            continue
        if len(ids) != len(set(ids)) or not set(ids) <= task_ids:
            errors.append(f"paper {ref} has duplicate or unknown task_ids")
        if set(ids) != memberships[ref]:
            errors.append(f"paper {ref} task_ids must match task memberships in both directions")
    return errors
