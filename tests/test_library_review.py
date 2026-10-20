"""Retrospective decisions cannot silently re-endorse unsupported legacy records."""

import copy
import json
import os
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from scripts.library_review import validate_library_review


class LibraryReviewTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.ref = "https://example.edu/paper"
        self.artifact = "reports/reorganization/2026-10-20/branch-X.json"
        self.row = {
            "paper_url": self.ref, "decision": "priority", "impact_score": 4,
            "project_relevance_score": 4, "evidence_strength": 4,
            "reason": "Provides a released protocol with controlled task comparisons.",
            "revisit_trigger": "Recheck on a protocol or release change.",
            "task_ids": ["task"], "review_artifact": self.artifact,
        }
        self.audit = dict(self.row, requires_visual_review=False, requires_temporal_demo=False,
                          visual_status="not_applicable", not_applicable_reason="Metric/protocol evaluation, no generation or execution claim used.",
                          sources=[{"source_url": self.ref, "locator": "Table 2", "claim": "Controlled protocol is defined.", "source_quality": "primary", "status": "verified"}])
        self.review = {"review_schema_version": 1, "policy_version": 2, "review_date": "2026-10-20", "reviews": [self.row]}
        self.registry = {"branches": [{"papers": [{"url": self.ref, "curation_status": "priority", "task_ids": ["task"], "source_quality": "primary", "impact_score": 4, "project_relevance_score": 4, "evidence_strength": 4, "visual_quality_score": 0, "visual_quality_decision": "not_applicable"}]}]}
        self.frontiers = {"tasks": [{"task_id": "task", "members": [{"paper_url": self.ref, "role": "current"}]}]}
        self.write_audit()

    def write_audit(self):
        path = self.root / self.artifact
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps({"reviews": [self.audit]}))

    def errors(self):
        return validate_library_review(self.review, self.registry, self.frontiers, self.root)

    def test_complete_source_backed_priority_passes(self):
        self.assertEqual([], self.errors())

    def test_every_preserved_paper_requires_one_review(self):
        self.review["reviews"] = []
        self.assertTrue(self.errors())
        self.review["reviews"] = [self.row, copy.deepcopy(self.row)]
        self.assertTrue(self.errors())

    def test_priority_cannot_use_low_or_unknown_scores(self):
        for value in (3, None, True):
            with self.subTest(value=value):
                self.row["impact_score"] = value
                self.audit["impact_score"] = value
                self.write_audit()
                self.assertTrue(self.errors())

    def test_registry_status_and_task_membership_must_agree(self):
        self.registry["branches"][0]["papers"][0]["curation_status"] = "source_issue"
        self.assertTrue(self.errors())
        self.registry["branches"][0]["papers"][0]["curation_status"] = "priority"
        self.row["task_ids"] = ["missing"]
        self.assertTrue(self.errors())

    def test_current_cannot_include_a_watchlist_record(self):
        self.row["decision"] = self.audit["decision"] = "watchlist"
        self.registry["branches"][0]["papers"][0]["curation_status"] = "watchlist"
        self.write_audit()
        self.assertTrue(self.errors())
        self.frontiers["tasks"][0]["members"][0]["role"] = "unreviewed"
        self.assertEqual([], self.errors())

    def test_audit_labels_cannot_be_changed_only_in_summary(self):
        self.audit["decision"] = "reference"
        self.write_audit()
        self.assertTrue(self.errors())

    def test_priority_needs_verified_primary_evidence(self):
        self.audit["sources"][0]["status"] = "partial"
        self.write_audit()
        self.assertTrue(self.errors())

    def test_live_priority_scores_cannot_drift_below_the_review(self):
        self.registry["branches"][0]["papers"][0]["impact_score"] = 0
        self.assertTrue(self.errors())

    def test_verified_label_needs_a_real_claim_and_locator(self):
        for field in ("locator", "claim"):
            with self.subTest(field=field):
                previous = self.audit["sources"][0][field]
                self.audit["sources"][0][field] = ""
                self.write_audit()
                self.assertTrue(self.errors())
                self.audit["sources"][0][field] = previous

    def test_watching_a_weak_result_does_not_make_it_adequate(self):
        self.audit.update(requires_visual_review=True, requires_temporal_demo=True,
                          visual_status="verified", visual_quality_score=2, visual_quality_decision="weak",
                          inspection_evidence=[{"url": self.ref, "modality": "video", "locator": "00:10-00:20",
                                                "observation": "Persistent contact errors.", "limitations": "Selected clip."}])
        self.registry["branches"][0]["papers"][0].update(visual_quality_score=2, visual_quality_decision="weak")
        self.write_audit()
        self.assertTrue(self.errors())

    def test_video_link_is_not_a_temporal_inspection(self):
        self.audit.update(requires_visual_review=True, requires_temporal_demo=True, visual_status="not_inspected", inspection_evidence=[])
        self.write_audit()
        self.assertTrue(self.errors())
        self.audit.update(visual_status="verified", inspection_evidence=[{"modality": "paper_figure"}])
        self.write_audit()
        self.assertTrue(self.errors())

    def test_unknown_scores_are_allowed_for_nonpriority(self):
        self.row.update(decision="source_issue", impact_score=None, project_relevance_score=None, evidence_strength=1)
        self.audit.update({k: self.row[k] for k in ("decision", "impact_score", "project_relevance_score", "evidence_strength")})
        self.registry["branches"][0]["papers"][0]["curation_status"] = "source_issue"
        self.frontiers["tasks"][0]["members"][0]["role"] = "unreviewed"
        self.write_audit()
        self.assertEqual([], self.errors())

    def test_required_dossier_remains_a_local_validation_gate(self):
        self.row.update(decision="undecided", dossier_path="undecided/2026-10-20/LIB-test.md")
        self.audit["decision"] = "undecided"
        self.registry["branches"][0]["papers"][0]["curation_status"] = "undecided"
        self.frontiers["tasks"][0]["members"][0]["role"] = "unreviewed"
        self.write_audit()
        with patch.dict(os.environ, {"REQUIRE_UNDECIDED_DOSSIERS": "1"}):
            self.assertTrue(self.errors())
            path = self.root / self.row["dossier_path"]
            path.parent.mkdir(parents=True)
            path.write_text("Detailed local-only dossier")
            self.assertEqual([], self.errors())


if __name__ == "__main__":
    unittest.main()
