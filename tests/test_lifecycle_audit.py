"""Lifecycle audit traces cannot bypass admission or rewrite historical meaning."""

from __future__ import annotations

import copy
import json
from pathlib import Path
import tempfile
import unittest

from scripts.acceptance_policy import validate_policy_run
from tests.test_acceptance_policy import EXISTING_URL, RUN_ID, complete_run


TASK_ID = "articulated-object-generation"


class LifecycleAuditTests(unittest.TestCase):
    def setUp(self) -> None:
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.root = Path(temp.name)
        (self.root / "data").mkdir()
        (self.root / "data/follow_sources.seed.json").write_text(json.dumps({
            "source_groups": [{
                "id": "core-lab",
                "priority": "core",
                "urls": {"publications": "https://example.edu/publications"},
            }],
            "meta_sources": [],
        }))
        (self.root / "data/papers.seed.json").write_text(json.dumps({
            "branches": [{
                "id": "A",
                "papers": [{"title": "Fictional baseline", "url": EXISTING_URL}],
            }],
        }))
        self.frontiers_path = self.root / "data/task_frontiers.seed.json"
        self.frontiers = {
            "lifecycle_schema_version": 1,
            "updated": RUN_ID,
            "tasks": [{
                "task_id": TASK_ID,
                "title": "Articulated object generation",
                "branch": "A",
                "scope": {
                    "input": "Object description",
                    "output": "An articulated executable object",
                    "setting": "A fixed simulator and held-out object split",
                    "protocol": "Matched simulation success and resource budget",
                },
                "members": [{
                    "paper_url": EXISTING_URL,
                    "role": "current",
                    "reason": "A fictional evidence-backed task recommendation.",
                    "reviewed_on": RUN_ID,
                    "evidence": [{
                        "source_url": "https://example.edu/paper.pdf",
                        "locator": "Table 2, same-protocol comparison",
                        "claim": "This fictional baseline meets the stated task protocol.",
                        "source_quality": "primary",
                        "status": "verified",
                    }],
                }],
            }],
        }
        self.write_frontiers()
        self.artifacts = complete_run()
        self.change = {
            "task_id": TASK_ID,
            "paper_url": EXISTING_URL,
            "action": "keep",
            "reason": "The current recommendation retains its task-specific advantage.",
        }
        self.patch["lifecycle_changes"] = [self.change]

    @property
    def patch(self) -> dict:
        return self.artifacts["05_registry_patch.json"]

    def write_frontiers(self) -> None:
        self.frontiers_path.write_text(json.dumps(self.frontiers))

    def errors(self) -> list[str]:
        errors: list[str] = []
        validate_policy_run(RUN_ID, self.artifacts, self.root, errors)
        return errors

    def test_valid_audit_actions_preserve_complete_accepted_run(self) -> None:
        for action in ("keep", "promote", "supersede", "retain_alternative", "reopen"):
            with self.subTest(action=action):
                self.change["action"] = action
                self.assertEqual(self.errors(), [])

    def test_audit_must_reference_canonical_task_and_actual_member(self) -> None:
        for field, invalid in (("task_id", "unknown-task"), ("paper_url", "https://example.edu/unknown-paper")):
            with self.subTest(field=field):
                change = copy.deepcopy(self.change)
                change[field] = invalid
                self.patch["lifecycle_changes"] = [change]
                self.assertTrue(any("existing task membership" in error for error in self.errors()))

    def test_duplicate_task_member_audit_is_rejected_even_with_different_action(self) -> None:
        duplicate = dict(self.change, action="promote")
        self.patch["lifecycle_changes"].append(duplicate)
        self.assertTrue(any("duplicate lifecycle change" in error for error in self.errors()))

    def test_audit_requires_allowed_action_and_nonempty_reason(self) -> None:
        for field, invalid in (("action", None), ("action", "archive"), ("reason", None), ("reason", ""), ("reason", "   ")):
            with self.subTest(field=field, invalid=invalid):
                change = copy.deepcopy(self.change)
                change[field] = invalid
                self.patch["lifecycle_changes"] = [change]
                self.assertTrue(self.errors())

    def test_audit_requires_inspectable_canonical_task_file(self) -> None:
        self.frontiers_path.unlink()
        self.assertTrue(any("inspectable task-frontier file" in error for error in self.errors()))

    def test_lifecycle_audit_cannot_replace_accepted_candidate_disposition(self) -> None:
        self.patch["registry_additions"] = []
        self.change["candidate_id"] = "CAND-0001"
        self.assertTrue(any("missing editor disposition" in error for error in self.errors()))

    def test_later_role_change_does_not_invalidate_historical_audit(self) -> None:
        self.change["action"] = "promote"
        self.assertEqual(self.errors(), [])
        member = self.frontiers["tasks"][0]["members"][0]
        member["role"] = "unreviewed"
        member["reason"] = "A later protocol change reopened this fictional assessment."
        member.pop("evidence")
        member.pop("reviewed_on")
        self.write_frontiers()
        self.assertEqual(self.errors(), [])

    def test_plan_cannot_redirect_task_file_to_noncanonical_path(self) -> None:
        alternate = self.root / "data/alternate_task_frontiers.json"
        alternate.write_text(json.dumps(self.frontiers))
        self.artifacts["00_run_plan.json"]["task_frontiers_path"] = "data/alternate_task_frontiers.json"
        self.assertTrue(any("task_frontiers_path must be data/task_frontiers.seed.json" in error for error in self.errors()))


if __name__ == "__main__":
    unittest.main()
