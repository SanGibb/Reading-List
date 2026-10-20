"""Task-scoped succession checks, using fictional papers and in-memory fixtures."""

from __future__ import annotations

import copy
from pathlib import Path
import tempfile
import unittest

from scripts.task_lifecycle import validate_task_frontiers


OLD_URL = "https://example.edu/older-articulated-assets"
NEW_URL = "https://example.edu/newer-articulated-assets"
OTHER_URL = "https://example.edu/alternative-articulated-assets"
TASK_ID = "articulated-object-generation"
OTHER_TASK_ID = "articulated-object-reconstruction"


def evidence() -> list[dict]:
    return [{
        "source_url": "https://example.edu/newer-articulated-assets/paper.pdf",
        "locator": "Table 2 and Appendix C, matched held-out simulation protocol",
        "claim": "The fictional comparison reports better success under the same protocol.",
        "source_quality": "primary",
        "status": "verified",
    }]


def member(url: str, role: str = "current") -> dict:
    result = {
        "paper_url": url,
        "role": role,
        "reason": "A task-scoped editorial assessment based on the cited comparison.",
    }
    if role != "unreviewed":
        result.update({"reviewed_on": "2026-10-20", "evidence": evidence()})
    if role == "historical":
        result.update({
            "superseded_by": NEW_URL,
            "comparison": {
                "same_task": True,
                "comparable_protocol": True,
                "no_material_regression": True,
                "improvements": "Higher success under the same fictional held-out protocol.",
                "tradeoffs": "Both methods use the same resource budget in this fixture.",
                "retained_value": "The older method remains a useful baseline and simpler implementation.",
            },
        })
    return result


def task(task_id: str = TASK_ID, members: list[dict] | None = None) -> dict:
    return {
        "task_id": task_id,
        "title": "Executable articulated object generation",
        "branch": "A",
        "scope": {
            "input": "A single object description",
            "output": "A simulator-ready object with articulated joints",
            "setting": "Held-out cabinet instances in the same simulator",
            "protocol": "Matched object split, success definition, and resource budget",
        },
        "members": members if members is not None else [
            member(NEW_URL), member(OLD_URL, "historical"), member(OTHER_URL, "alternative"),
        ],
    }


def registry() -> dict:
    return {"branches": [{
        "id": "A",
        "name": "Executable world representation",
        "papers": [{
            "title": title,
            "url": url,
            "deep_dive_path": f"paper_reads/A_executable_world_representation/{slug}.md",
        } for title, url, slug in (
            ("Fictional older method", OLD_URL, "older-articulated-assets"),
            ("Fictional newer method", NEW_URL, "newer-articulated-assets"),
            ("Fictional alternative", OTHER_URL, "alternative-articulated-assets"),
        )],
    }]}


def frontiers() -> dict:
    return {
        "lifecycle_schema_version": 1,
        "updated": "2026-10-20",
        "tasks": [task()],
    }


class TaskLifecycleTests(unittest.TestCase):
    def setUp(self) -> None:
        self.frontiers = frontiers()
        self.registry = registry()

    @property
    def members(self) -> list[dict]:
        return self.frontiers["tasks"][0]["members"]

    @property
    def papers(self) -> list[dict]:
        return self.registry["branches"][0]["papers"]

    def assert_valid(self) -> None:
        self.assertEqual(validate_task_frontiers(self.frontiers, self.registry), [])

    def assert_invalid(self) -> None:
        errors = validate_task_frontiers(self.frontiers, self.registry)
        self.assertIsInstance(errors, list)
        self.assertTrue(errors, "The invalid lifecycle fixture must be rejected.")
        self.assertTrue(all(isinstance(error, str) for error in errors))

    def test_valid_current_alternative_and_historical_members(self) -> None:
        self.assert_valid()

    def test_legacy_registry_can_remain_unmapped(self) -> None:
        self.frontiers["tasks"] = []
        self.assert_valid()

    def test_validation_does_not_rewrite_metadata_or_registry(self) -> None:
        before_frontiers = copy.deepcopy(self.frontiers)
        before_registry = copy.deepcopy(self.registry)
        self.assert_valid()
        self.assertEqual(self.frontiers, before_frontiers)
        self.assertEqual(self.registry, before_registry)

    def test_unknown_member_paper_is_rejected(self) -> None:
        self.members[0]["paper_url"] = "https://example.edu/not-in-registry"
        self.assert_invalid()

    def test_member_reference_must_match_registry_url_exactly(self) -> None:
        self.members[0]["paper_url"] = NEW_URL + "/"
        self.assert_invalid()

    def test_unknown_successor_is_rejected(self) -> None:
        self.members[1]["superseded_by"] = "https://example.edu/unknown-successor"
        self.assert_invalid()

    def test_successor_must_belong_to_same_task(self) -> None:
        self.members.pop(0)
        self.frontiers["tasks"].append(task(OTHER_TASK_ID, [member(NEW_URL)]))
        self.assert_invalid()

    def test_historical_member_cannot_replace_itself(self) -> None:
        self.members[1]["superseded_by"] = OLD_URL
        self.assert_invalid()

    def test_historical_cycle_is_rejected(self) -> None:
        newer = member(NEW_URL, "historical")
        newer["superseded_by"] = OLD_URL
        self.members[0] = newer
        self.assert_invalid()

    def test_longer_historical_cycle_is_rejected(self) -> None:
        self.members[0] = member(NEW_URL, "historical")
        self.members[0]["superseded_by"] = OTHER_URL
        self.members[2] = member(OTHER_URL, "historical")
        self.members[2]["superseded_by"] = OLD_URL
        self.assert_invalid()

    def test_valid_historical_chain_terminates_at_current(self) -> None:
        self.members[1]["superseded_by"] = OTHER_URL
        self.members[2] = member(OTHER_URL, "historical")
        self.assert_valid()

    def test_historical_chain_cannot_terminate_at_alternative(self) -> None:
        self.members[0]["role"] = "alternative"
        self.assert_invalid()

    def test_historical_chain_cannot_terminate_at_unreviewed(self) -> None:
        self.members[0] = member(NEW_URL, "unreviewed")
        self.assert_invalid()

    def test_historical_member_requires_successor(self) -> None:
        self.members[1].pop("superseded_by")
        self.assert_invalid()

    def test_nonhistorical_member_cannot_have_successor(self) -> None:
        for role in ("current", "alternative", "unreviewed"):
            with self.subTest(role=role):
                self.frontiers = frontiers()
                candidate = member(NEW_URL, role)
                candidate["superseded_by"] = OTHER_URL
                self.members[0] = candidate
                self.assert_invalid()

    def test_duplicate_task_ids_are_rejected(self) -> None:
        self.frontiers["tasks"].append(copy.deepcopy(self.frontiers["tasks"][0]))
        self.assert_invalid()

    def test_task_id_format_is_stable_lowercase_hyphenated(self) -> None:
        for invalid in ("", "Articulated-Objects", "articulated_objects", "articulated objects", "-objects", "objects-"):
            with self.subTest(task_id=invalid):
                self.frontiers = frontiers()
                self.frontiers["tasks"][0]["task_id"] = invalid
                self.assert_invalid()

    def test_duplicate_members_within_task_are_rejected(self) -> None:
        self.members.append(copy.deepcopy(self.members[0]))
        self.assert_invalid()

    def test_same_paper_can_be_historical_and_current_in_distinct_tasks(self) -> None:
        self.frontiers["tasks"].append(task(OTHER_TASK_ID, [member(OLD_URL)]))
        self.assert_valid()

    def test_all_member_roles_require_nonempty_reason(self) -> None:
        for role in ("current", "alternative", "historical", "unreviewed"):
            for bad_reason in (None, "", "   "):
                with self.subTest(role=role, reason=bad_reason):
                    self.frontiers = frontiers()
                    candidate = member(OLD_URL, role)
                    candidate["reason"] = bad_reason
                    self.members[1] = candidate
                    self.assert_invalid()

    def test_reviewed_roles_require_evidence(self) -> None:
        for role in ("current", "alternative", "historical"):
            with self.subTest(role=role):
                self.frontiers = frontiers()
                candidate = member(OLD_URL, role)
                candidate.pop("evidence")
                self.members[1] = candidate
                self.assert_invalid()

    def test_empty_evidence_is_rejected(self) -> None:
        self.members[0]["evidence"] = []
        self.assert_invalid()

    def test_evidence_requires_source_locator_and_claim(self) -> None:
        for field in ("source_url", "locator", "claim"):
            for value in (None, "", "   "):
                with self.subTest(field=field, value=value):
                    self.frontiers = frontiers()
                    self.members[0]["evidence"][0][field] = value
                    self.assert_invalid()

    def test_evidence_source_must_be_http_url(self) -> None:
        for url in ("paper.pdf", "file:///tmp/paper.pdf", "https://"):
            with self.subTest(source_url=url):
                self.frontiers = frontiers()
                self.members[0]["evidence"][0]["source_url"] = url
                self.assert_invalid()

    def test_evidence_rejects_social_only_or_unverified_claims(self) -> None:
        for field, value in (("source_quality", "social_only"), ("source_quality", "secondary"), ("status", "unverified")):
            with self.subTest(field=field, value=value):
                self.frontiers = frontiers()
                self.members[0]["evidence"][0][field] = value
                self.assert_invalid()

    def test_all_allowed_primary_and_official_evidence_types(self) -> None:
        for quality in ("primary", "official", "primary_or_official"):
            with self.subTest(source_quality=quality):
                self.frontiers = frontiers()
                self.members[0]["evidence"][0]["source_quality"] = quality
                self.assert_valid()

    def test_reviewed_roles_require_iso_review_date(self) -> None:
        for value in (None, "", "20-10-2026", "2026-02-30", "2026-10-20T12:00:00Z"):
            with self.subTest(reviewed_on=value):
                self.frontiers = frontiers()
                self.members[0]["reviewed_on"] = value
                self.assert_invalid()

    def test_unreviewed_members_need_no_evidence_or_ranking(self) -> None:
        self.frontiers["tasks"][0]["members"] = [member(OLD_URL, "unreviewed")]
        self.assert_valid()

    def test_all_four_scope_fields_are_required(self) -> None:
        for field in ("input", "output", "setting", "protocol"):
            with self.subTest(field=field):
                self.frontiers = frontiers()
                self.frontiers["tasks"][0]["scope"].pop(field)
                self.assert_invalid()

    def test_historical_comparison_requires_all_boolean_gates(self) -> None:
        for gate in ("same_task", "comparable_protocol", "no_material_regression"):
            for value in (None, False, "true", 1):
                with self.subTest(gate=gate, value=value):
                    self.frontiers = frontiers()
                    self.members[1]["comparison"][gate] = value
                    self.assert_invalid()

    def test_historical_comparison_requires_improvements_tradeoffs_and_retained_value(self) -> None:
        for field in ("improvements", "tradeoffs", "retained_value"):
            with self.subTest(field=field):
                self.frontiers = frontiers()
                self.members[1]["comparison"].pop(field)
                self.assert_invalid()

    def test_historical_member_requires_comparison(self) -> None:
        self.members[1].pop("comparison")
        self.assert_invalid()

    def test_metadata_schema_version_and_updated_date_are_required(self) -> None:
        for field, value in (("lifecycle_schema_version", None), ("lifecycle_schema_version", True), ("lifecycle_schema_version", 2), ("updated", None), ("updated", "2026-02-30")):
            with self.subTest(field=field, value=value):
                self.frontiers = frontiers()
                self.frontiers[field] = value
                self.assert_invalid()

    def test_unknown_roles_and_branches_are_rejected(self) -> None:
        self.members[0]["role"] = "sota"
        self.assert_invalid()
        self.frontiers = frontiers()
        self.frontiers["tasks"][0]["branch"] = "F"
        self.assert_invalid()

    def test_policy_v2_papers_require_nonempty_task_ids(self) -> None:
        for value in (None, [], "articulated-object-generation"):
            with self.subTest(task_ids=value):
                self.registry = registry()
                self.papers[0]["acceptance_policy_version"] = 2
                self.papers[0]["task_ids"] = value
                self.assert_invalid()

    def test_policy_v2_bidirectional_task_mapping_is_valid(self) -> None:
        for paper in self.papers:
            paper["acceptance_policy_version"] = 2
            paper["task_ids"] = [TASK_ID]
        self.assert_valid()

    def test_paper_task_ids_cannot_reference_unknown_task(self) -> None:
        self.papers[0]["task_ids"] = ["unknown-task"]
        self.assert_invalid()

    def test_paper_task_ids_cannot_contain_duplicates(self) -> None:
        self.papers[0]["task_ids"] = [TASK_ID, TASK_ID]
        self.assert_invalid()

    def test_paper_task_ids_require_membership_in_each_task(self) -> None:
        self.frontiers["tasks"].append(task(OTHER_TASK_ID, [member(OTHER_URL)]))
        self.papers[0]["task_ids"] = [TASK_ID, OTHER_TASK_ID]
        self.assert_invalid()

    def test_declared_task_ids_cannot_omit_existing_membership(self) -> None:
        self.frontiers["tasks"].append(task(OTHER_TASK_ID, [member(OLD_URL)]))
        self.papers[0]["task_ids"] = [TASK_ID]
        self.assert_invalid()

    def test_legacy_papers_without_task_ids_can_have_curated_memberships(self) -> None:
        self.assertNotIn("task_ids", self.papers[0])
        self.assert_valid()

    def test_policy_v2_paper_cannot_claim_mapping_while_absent_from_members(self) -> None:
        self.papers[2]["acceptance_policy_version"] = 2
        self.papers[2]["task_ids"] = [TASK_ID]
        self.members.pop(2)
        self.assert_invalid()

    def test_deep_dive_paths_are_verified_when_root_is_given(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            for paper in self.papers:
                target = root / paper["deep_dive_path"]
                target.parent.mkdir(parents=True, exist_ok=True)
                target.touch()
            self.assertEqual(validate_task_frontiers(self.frontiers, self.registry, root), [])
            (root / self.papers[0]["deep_dive_path"]).unlink()
            self.assertTrue(validate_task_frontiers(self.frontiers, self.registry, root))

    def test_deep_dive_paths_must_be_safe_and_under_paper_reads(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            for paper in self.papers:
                target = root / paper["deep_dive_path"]
                target.parent.mkdir(parents=True, exist_ok=True)
                target.touch()
            for path in ("../outside.md", "paper_reads/../../outside.md", "/tmp/absolute.md", "reports/older.md"):
                with self.subTest(deep_dive_path=path):
                    self.papers[0]["deep_dive_path"] = path
                    self.assertTrue(validate_task_frontiers(self.frontiers, self.registry, root))

    def test_deep_dive_symlinks_cannot_escape_repository_root(self) -> None:
        with tempfile.TemporaryDirectory() as temp, tempfile.TemporaryDirectory() as external:
            root = Path(temp)
            for paper in self.papers:
                target = root / paper["deep_dive_path"]
                target.parent.mkdir(parents=True, exist_ok=True)
                target.touch()
            outside = Path(external) / "outside.md"
            outside.touch()
            link = root / self.papers[0]["deep_dive_path"]
            link.unlink()
            link.symlink_to(outside)
            self.assertTrue(validate_task_frontiers(self.frontiers, self.registry, root))


if __name__ == "__main__":
    unittest.main()
