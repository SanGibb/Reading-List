"""Policy-level regressions for the stricter, versioned acceptance gates.

The fixtures describe a complete small run rather than production audit files.
Each rejection test starts from a valid run and changes one policy requirement.
"""

from __future__ import annotations

import copy
from datetime import date, timedelta
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

from scripts.acceptance_policy import validate_policy_paper, validate_policy_run


RUN_ID = "2026-10-20"
CID = "CAND-0001"
EXISTING_URL = "https://example.edu/infinigen"


def inspected_video() -> dict:
    return {
        "url": "https://example.edu/articulated-assets/results.mp4",
        "modality": "video",
        "locator": "00:12–00:25, cabinet opening and closing",
        "observation": "The cabinet joints move through their range without visible interpenetration.",
        "limitations": "Author-selected sequence; runtime and failure frequency cannot be inferred.",
    }


def accepted_paper() -> dict:
    return {
        "acceptance_policy_version": 2,
        "title": "Executable Articulated Assets for Robot Simulation",
        "year": 2026,
        "venue": "arXiv",
        "url": "https://arxiv.org/abs/2610.12345",
        "data": "A released collection of articulated cabinets and held-out manipulation scenes.",
        "method": "Generate joints and physical parameters, then repair assets using simulation feedback.",
        "task": "Generate articulated assets that support robot interaction in simulation.",
        "novelty": "Validates articulation and downstream task execution rather than appearance alone.",
        "project_relevance": "Provides executable joint, collision, and simulation validation contracts.",
        "source_quality": "primary_or_official",
        "impact_score": 4,
        "project_relevance_score": 5,
        "evidence_strength": 4,
        "demo_score": 4,
        "visual_quality_score": 4,
        "visual_quality_decision": "strong",
        "requires_visual_review": True,
        "requires_temporal_demo": True,
        "deep_dive_path": "paper_reads/A_executable_world_representation/test-assets-2026.md",
    }


def complete_run() -> dict[str, dict]:
    paper = accepted_paper()
    branch_queries = {}
    query_log = []
    for branch, terms in {
        "A": "articulated URDF sim-ready physical assets",
        "B": "interactive world generation procedural environments",
        "C": "spatial intelligence 3D reasoning embodied",
        "D": "vision language action world action robot models",
        "E": "embodied evaluation benchmark robot datasets",
    }.items():
        branch_queries[branch] = []
        for basis in ("submitted", "updated", "release"):
            query_id = f"Q-{branch}-{basis}"
            query = f"{terms} 2026 {basis}"
            lookback = 45 if basis == "release" else 14
            date_from = (date.fromisoformat(RUN_ID) - timedelta(days=lookback - 1)).isoformat()
            branch_queries[branch].append(query)
            query_log.append({
                "query_id": query_id,
                "branch": branch,
                "query": query,
                "source_url": "https://arxiv.org/search/advanced",
                "executed_at": "2026-10-20T09:00:00+08:00",
                "date_basis": basis,
                "date_from": date_from,
                "date_to": RUN_ID,
                "results_reviewed": 12,
                "pages_checked": 2,
                "stop_reason": "All results within the overlapping date window were inspected.",
                "candidate_ids": [CID] if query_id == "Q-A-submitted" else [],
            })

    card = {
        key: copy.deepcopy(value)
        for key, value in paper.items()
        if key not in {"deep_dive_path", "inspection_evidence"}
    }
    card.update({
        "candidate_id": CID,
        "primary_branch": "A",
        "secondary_branches": ["B", "E"],
        "evidence": "The primary paper reports held-out physical validation and a task-level comparison.",
        "limitations": "The released videos are selected by the authors and do not establish failure frequency.",
        "claim_checks": [{
            "claim": "The released assets are evaluated for joint execution and held-out manipulation tasks.",
            "source": paper["url"],
            "status": "verified",
            "notes": "Checked the primary paper's simulation validation and task evaluation tables.",
        }],
    })
    review = {
        "candidate_id": CID,
        "review_decision": "pass",
        "accepted_for_registry": True,
        "issues": [],
        "required_fixes": [],
        "selection_basis": "new_capability",
        "acceptance_rationale": "Adds executable articulation with held-out simulation and task evidence.",
        "comparison_to_registry": {
            "closest_paper": "Infinigen Articulated",
            "material_difference": "Adds simulator-driven repair and task-level verification of generated joints.",
            "why_new_entry": "The repair loop changes the executable asset contract and supplies a reusable evaluation.",
        },
    }
    for key in (
        "impact_score", "project_relevance_score", "evidence_strength", "source_quality",
    ):
        review[key] = copy.deepcopy(paper[key])
    visual = {
        "candidate_id": CID,
        "visual_materials": [paper["url"], inspected_video()["url"]],
        "inspected_modalities": ["paper_figures", "video"],
        "visual_quality_score": 4,
        "visual_quality_decision": "strong",
        "visual_notes": "Inspected the joint motion and collision behavior in the recorded sequence.",
        "failure_modes": ["Unseen objects may still require manual repair."],
        "needs_human_decision": False,
        "undecided_reason": "",
        "inspection_evidence": [inspected_video()],
    }
    return {
        "00_run_plan.json": {
            "run_id": RUN_ID,
            "acceptance_policy_version": 2,
            "branches": list("ABCDE"),
            "minimum_year": 2024,
            "follow_sources_path": "data/follow_sources.seed.json",
            "known_registry_path": "data/papers.seed.json",
            "branch_queries": branch_queries,
        },
        "01_discovery.json": {
            "run_id": RUN_ID,
            "acceptance_policy_version": 2,
            "query_log": query_log,
            "followed_sources_checked": [{
                "source_id": "core-lab",
                "status": "checked",
                "notes": "Inspected the official publications and project release pages before broad searches.",
                "checked_at": "2026-10-20T08:30:00+08:00",
                "urls_checked": ["https://example.edu/publications"],
                "evidence_url": "https://example.edu/publications",
            }],
            "candidates": [{
                "candidate_id": CID,
                "title": paper["title"],
                "source_url": paper["url"],
                "source_type": "primary_paper",
                "why_candidate": "Executable articulation and downstream simulation evaluation fit branch A.",
                "branch_hint": "A",
                "query_id": "Q-A-submitted",
            }],
            "triage": [{
                "candidate_id": CID,
                "decision": "analyze",
                "reason": "Potential new executable capability with primary evidence.",
                "impact_prior": 4,
                "project_relevance_prior": 5,
                "primary_branch": "A",
                "source_quality": "primary_or_official",
            }],
        },
        "02_evidence.json": {
            "run_id": RUN_ID,
            "acceptance_policy_version": 2,
            "paper_cards": [card],
            "demo_cards": [],
        },
        "03_review.json": {
            "run_id": RUN_ID,
            "acceptance_policy_version": 2,
            "quality_review": [review],
            "visual_cards": [visual],
        },
        "05_registry_patch.json": {
            "run_id": RUN_ID,
            "acceptance_policy_version": 2,
            "branch_assignments": [],
            "taxonomy_change_proposals": [],
            "registry_additions": [{
                "candidate_id": CID,
                "branch": "A",
                "deep_dive_path": paper["deep_dive_path"],
                "paper": paper,
            }],
            "registry_updates": [],
            "registry_noops": [],
        },
    }


class AcceptancePolicyTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tempdir = tempfile.TemporaryDirectory()
        self.addCleanup(self.tempdir.cleanup)
        self.root = Path(self.tempdir.name)
        (self.root / "data").mkdir()
        (self.root / "data" / "follow_sources.seed.json").write_text(json.dumps({
            "source_groups": [{
                "id": "core-lab", "priority": "core",
                "urls": {"publications": "https://example.edu/publications"},
            }],
            "meta_sources": [],
        }))
        (self.root / "data" / "papers.seed.json").write_text(json.dumps({
            "branches": [{
                "id": "A",
                "papers": [{"title": "Infinigen Articulated", "url": EXISTING_URL}],
            }],
        }))
        self.artifacts = complete_run()

    def run_errors(self, artifacts: dict | None = None, run_id: str = RUN_ID) -> list[str]:
        errors: list[str] = []
        validate_policy_run(run_id, self.artifacts if artifacts is None else artifacts, self.root, errors)
        return errors

    def assert_run_rejected(self) -> None:
        self.assertTrue(self.run_errors(), "An invalid policy-v2 run was accepted.")

    def paper_errors(self, paper: dict) -> list[str]:
        errors: list[str] = []
        validate_policy_paper(paper, "test paper", errors)
        return errors

    def test_complete_accepted_run_passes(self) -> None:
        self.assertEqual([], self.run_errors())
        self.assertEqual([], self.paper_errors(accepted_paper()))

    def test_zero_addition_week_passes_without_filling_a_quota(self) -> None:
        self.artifacts["01_discovery.json"]["candidates"] = []
        self.artifacts["01_discovery.json"]["triage"] = []
        for query in self.artifacts["01_discovery.json"]["query_log"]:
            query["candidate_ids"] = []
        self.artifacts["02_evidence.json"]["paper_cards"] = []
        self.artifacts["03_review.json"]["quality_review"] = []
        self.artifacts["03_review.json"]["visual_cards"] = []
        self.artifacts["05_registry_patch.json"]["registry_additions"] = []
        self.assertEqual([], self.run_errors())

    def test_validation_cli_enforces_policy_version_on_a_zero_addition_week(self) -> None:
        """Exercise the real entry point so a disconnected helper cannot pass CI."""
        discovery = self.artifacts["01_discovery.json"]
        discovery["candidates"] = []
        discovery["triage"] = []
        for query in discovery["query_log"]:
            query["candidate_ids"] = []
        self.artifacts["02_evidence.json"]["paper_cards"] = []
        self.artifacts["03_review.json"]["quality_review"] = []
        self.artifacts["03_review.json"]["visual_cards"] = []
        self.artifacts["05_registry_patch.json"]["registry_additions"] = []

        scripts_dir = self.root / "scripts"
        scripts_dir.mkdir()
        repository = Path(__file__).resolve().parents[1]
        for name in ("validate_run.py", "acceptance_policy.py"):
            shutil.copyfile(repository / "scripts" / name, scripts_dir / name)
        run_dir = self.root / "reports" / "runs" / RUN_ID
        run_dir.mkdir(parents=True)
        for name, artifact in self.artifacts.items():
            (run_dir / name).write_text(json.dumps(artifact))
        (run_dir / "run_manifest.json").write_text(json.dumps({"run_id": RUN_ID}))
        (run_dir / "04_editor_report.md").write_text(
            "All planned searches completed; no candidate met the selective acceptance gates.\n"
        )

        command = [sys.executable, str(scripts_dir / "validate_run.py"), RUN_ID]
        result = subprocess.run(command, cwd=self.root, capture_output=True, text=True, check=False)
        self.assertEqual(0, result.returncode, result.stdout + result.stderr)
        self.assertIn("Run validation passed", result.stdout)

        plan = self.artifacts["00_run_plan.json"]
        plan.pop("acceptance_policy_version")
        (run_dir / "00_run_plan.json").write_text(json.dumps(plan))
        result = subprocess.run(command, cwd=self.root, capture_output=True, text=True, check=False)
        self.assertNotEqual(0, result.returncode, result.stdout + result.stderr)
        self.assertIn("acceptance_policy_version", result.stdout + result.stderr)

    def test_legacy_run_and_unversioned_registry_paper_remain_compatible(self) -> None:
        self.assertEqual([], self.run_errors({}, "2026-10-18"))
        self.assertEqual([], self.paper_errors({"title": "Legacy registry entry"}))

    def test_new_run_cannot_disable_policy_by_removing_versions(self) -> None:
        for artifact in self.artifacts.values():
            artifact.pop("acceptance_policy_version", None)
        self.artifacts["05_registry_patch.json"]["registry_additions"][0]["paper"].pop("acceptance_policy_version")
        self.assert_run_rejected()

    def test_addition_requires_policy_version(self) -> None:
        self.artifacts["05_registry_patch.json"]["registry_additions"][0]["paper"].pop("acceptance_policy_version")
        self.assert_run_rejected()

    def test_final_quality_scores_are_hard_gates(self) -> None:
        for field in ("impact_score", "project_relevance_score", "evidence_strength"):
            with self.subTest(field=field):
                self.artifacts = complete_run()
                self.artifacts["03_review.json"]["quality_review"][0][field] = 3
                self.assert_run_rejected()

    def test_paper_quality_scores_are_hard_gates(self) -> None:
        for field in ("impact_score", "project_relevance_score", "evidence_strength"):
            with self.subTest(field=field):
                paper = accepted_paper()
                paper[field] = 3
                self.assertTrue(self.paper_errors(paper))

    def test_social_only_source_cannot_be_accepted(self) -> None:
        self.artifacts["01_discovery.json"]["triage"][0]["source_quality"] = "social_only"
        self.assert_run_rejected()
        paper = accepted_paper()
        paper["source_quality"] = "social_only"
        self.assertTrue(self.paper_errors(paper))

    def test_accepted_source_fields_cannot_be_empty(self) -> None:
        for location, field in (("candidate", "source_url"), ("triage", "source_quality")):
            with self.subTest(location=location):
                self.artifacts = complete_run()
                target = (self.artifacts["01_discovery.json"]["candidates"][0] if location == "candidate"
                          else self.artifacts["01_discovery.json"]["triage"][0])
                target[field] = ""
                self.assert_run_rejected()

    def test_weak_or_undecided_visuals_cannot_be_accepted(self) -> None:
        for decision in ("weak", "undecided"):
            with self.subTest(decision=decision):
                self.artifacts = complete_run()
                self.artifacts["03_review.json"]["visual_cards"][0]["visual_quality_decision"] = decision
                self.assert_run_rejected()

    def test_undecided_requires_human_decision_even_when_not_accepted(self) -> None:
        self.artifacts["03_review.json"]["visual_cards"][0]["visual_quality_decision"] = "undecided"
        self.artifacts["03_review.json"]["quality_review"][0]["accepted_for_registry"] = False
        self.artifacts["03_review.json"]["quality_review"][0]["review_decision"] = "block"
        self.artifacts["05_registry_patch.json"]["registry_additions"] = []
        self.assert_run_rejected()

    def test_undecided_requires_an_analyzed_paper_card(self) -> None:
        visual = self.artifacts["03_review.json"]["visual_cards"][0]
        visual.update({"visual_quality_decision": "undecided", "needs_human_decision": True})
        self.artifacts["03_review.json"]["quality_review"][0].update({
            "accepted_for_registry": False, "review_decision": "block",
        })
        self.artifacts["05_registry_patch.json"]["registry_additions"] = []
        self.artifacts["02_evidence.json"]["paper_cards"] = []
        self.assert_run_rejected()

    def test_human_decision_flag_blocks_acceptance(self) -> None:
        self.artifacts["03_review.json"]["visual_cards"][0]["needs_human_decision"] = True
        self.assert_run_rejected()

    def test_inspection_requires_observable_media_evidence(self) -> None:
        self.artifacts["03_review.json"]["visual_cards"][0]["inspection_evidence"] = []
        self.assert_run_rejected()

    def test_inspection_evidence_requires_a_locator_and_observation(self) -> None:
        for field in ("url", "locator", "observation", "limitations"):
            with self.subTest(field=field):
                self.artifacts = complete_run()
                self.artifacts["03_review.json"]["visual_cards"][0]["inspection_evidence"][0][field] = ""
                self.assert_run_rejected()

    def test_temporal_claim_cannot_be_verified_from_still_figures_only(self) -> None:
        visual = self.artifacts["03_review.json"]["visual_cards"][0]
        visual["inspection_evidence"][0]["modality"] = "paper_figure"
        self.assert_run_rejected()

    def test_explicit_nonvisual_paper_passes_with_reason(self) -> None:
        fields = {
            "requires_visual_review": False,
            "requires_temporal_demo": False,
            "visual_quality_decision": "not_applicable",
            "visual_quality_score": 0,
            "not_applicable_reason": "A metric audit with no generation, physical behavior, or embodied demo claim.",
            "inspection_evidence": [],
        }
        paper = self.artifacts["05_registry_patch.json"]["registry_additions"][0]["paper"]
        paper.update(fields)
        self.artifacts["02_evidence.json"]["paper_cards"][0].update(fields)
        visual = self.artifacts["03_review.json"]["visual_cards"][0]
        visual.update(fields)
        self.assertEqual([], self.paper_errors(paper))
        self.assertEqual([], self.run_errors())
        visual.pop("not_applicable_reason")
        self.assert_run_rejected()

    def test_visual_review_requirement_cannot_be_omitted(self) -> None:
        self.artifacts["02_evidence.json"]["paper_cards"][0].pop("requires_visual_review")
        self.assert_run_rejected()

    def test_acceptance_claims_must_be_verified_and_source_backed(self) -> None:
        for change in ("partial", "source", "no_claims"):
            with self.subTest(change=change):
                self.artifacts = complete_run()
                card = self.artifacts["02_evidence.json"]["paper_cards"][0]
                if change == "partial":
                    card["claim_checks"][0]["status"] = "partial"
                elif change == "source":
                    card["claim_checks"][0]["source"] = ""
                else:
                    card["claim_checks"] = []
                self.assert_run_rejected()

    def test_open_nonacceptance_claim_does_not_hide_verified_evidence(self) -> None:
        card = self.artifacts["02_evidence.json"]["paper_cards"][0]
        card["claim_checks"].append({
            "claim": "The method generalizes to arbitrary object categories.",
            "source": card["url"],
            "status": "partial",
            "notes": "This broader claim is unresolved and is not used to justify collection.",
            "used_for_acceptance": False,
        })
        self.assertEqual([], self.run_errors())

    def test_selection_and_comparison_are_substantive_requirements(self) -> None:
        for field, value in (
            ("selection_basis", "incremental_result"),
            ("acceptance_rationale", ""),
            ("comparison_to_registry", {"closest_paper": "Known baseline", "material_difference": "", "why_new_entry": ""}),
        ):
            with self.subTest(field=field):
                self.artifacts = complete_run()
                self.artifacts["03_review.json"]["quality_review"][0][field] = value
                self.assert_run_rejected()

    def test_final_scores_must_match_registry_addition(self) -> None:
        self.artifacts["03_review.json"]["quality_review"][0]["impact_score"] = 5
        self.assert_run_rejected()

    def test_accepted_candidate_cannot_disappear_from_patch(self) -> None:
        self.artifacts["05_registry_patch.json"]["registry_additions"] = []
        self.assert_run_rejected()

    def test_duplicate_patch_disposition_is_rejected(self) -> None:
        patch = self.artifacts["05_registry_patch.json"]
        patch["registry_noops"] = [{
            "candidate_id": CID,
            "reason": "Already present with equivalent evidence.",
            "existing_paper_url": EXISTING_URL,
        }]
        self.assert_run_rejected()

    def test_nonaccepted_candidate_cannot_receive_patch_disposition(self) -> None:
        self.artifacts["03_review.json"]["quality_review"][0]["accepted_for_registry"] = False
        self.assert_run_rejected()

    def test_accepted_update_or_noop_accounts_for_candidate_once(self) -> None:
        for field in ("registry_updates", "registry_noops"):
            with self.subTest(field=field):
                self.artifacts = complete_run()
                patch = self.artifacts["05_registry_patch.json"]
                patch["registry_additions"] = []
                patch[field] = [{
                    "candidate_id": CID,
                    "reason": "The existing registry entry already covers this work.",
                    "existing_paper_url": EXISTING_URL,
                }]
                self.assertEqual([], self.run_errors())
                patch[field][0].pop("reason")
                self.assert_run_rejected()

    def test_update_and_noop_require_an_existing_registry_target(self) -> None:
        for field in ("registry_updates", "registry_noops"):
            for target in (None, "https://example.edu/nonexistent-paper"):
                with self.subTest(field=field, target=target):
                    self.artifacts = complete_run()
                    patch = self.artifacts["05_registry_patch.json"]
                    patch["registry_additions"] = []
                    disposition = {"candidate_id": CID, "reason": "Update the existing project's released evidence."}
                    if target is not None:
                        disposition["existing_paper_url"] = target
                    patch[field] = [disposition]
                    self.assert_run_rejected()

    def test_embedded_update_has_the_same_acceptance_gates_as_an_addition(self) -> None:
        patch = self.artifacts["05_registry_patch.json"]
        paper = patch["registry_additions"][0]["paper"]
        paper["url"] = EXISTING_URL
        patch["registry_additions"] = []
        patch["registry_updates"] = [{
            "candidate_id": CID,
            "reason": "Replace the existing entry with the now verified executable release.",
            "existing_paper_url": EXISTING_URL,
            "paper": paper,
        }]
        self.assertEqual([], self.run_errors())
        valid = copy.deepcopy(self.artifacts)
        for field, value in (
            ("impact_score", 3),
            ("source_quality", "social_only"),
            ("acceptance_policy_version", None),
            ("impact_score", 5),
            ("visual_quality_decision", "adequate"),
        ):
            with self.subTest(field=field, value=value):
                self.artifacts = copy.deepcopy(valid)
                self.artifacts["05_registry_patch.json"]["registry_updates"][0]["paper"][field] = value
                self.assert_run_rejected()

    def test_core_follow_source_requires_a_record(self) -> None:
        self.artifacts["01_discovery.json"]["followed_sources_checked"] = []
        self.assert_run_rejected()

    def test_follow_sources_cannot_be_redirected_to_a_weaker_existing_file(self) -> None:
        replacement = self.root / "data" / "alternate_follow_sources.json"
        replacement.write_text(json.dumps({"source_groups": [], "meta_sources": []}))
        self.artifacts["00_run_plan.json"]["follow_sources_path"] = "data/alternate_follow_sources.json"
        self.assert_run_rejected()

    def test_registry_path_cannot_be_redirected_to_an_existing_file(self) -> None:
        shutil.copyfile(self.root / "data" / "papers.seed.json", self.root / "data" / "alternate_papers.json")
        self.artifacts["00_run_plan.json"]["known_registry_path"] = "data/alternate_papers.json"
        self.assert_run_rejected()

    def test_checked_source_requires_inspection_details(self) -> None:
        for field in ("checked_at", "urls_checked", "evidence_url"):
            with self.subTest(field=field):
                self.artifacts = complete_run()
                self.artifacts["01_discovery.json"]["followed_sources_checked"][0].pop(field)
                self.assert_run_rejected()

    def test_unreachable_source_is_allowed_with_reason_and_retry_trigger(self) -> None:
        check = self.artifacts["01_discovery.json"]["followed_sources_checked"][0]
        check.update({
            "status": "unreachable",
            "notes": "The official site timed out on both requests; no publication content was inspected.",
            "retry_trigger": "Retry the official publication page at the next run or when service recovers.",
        })
        self.assertEqual([], self.run_errors())
        check.pop("retry_trigger")
        self.assert_run_rejected()

    def test_placeholder_query_cannot_claim_search_coverage(self) -> None:
        plan = self.artifacts["00_run_plan.json"]
        discovery = self.artifacts["01_discovery.json"]
        plan["branch_queries"]["A"][0] = "fixed follow sources"
        discovery["query_log"][0]["query"] = "fixed follow sources"
        self.assert_run_rejected()

    def test_every_planned_query_requires_execution_record(self) -> None:
        self.artifacts["00_run_plan.json"]["branch_queries"]["A"].append("articulated asset URDF physics repair 2026")
        self.assert_run_rejected()

    def test_each_branch_requires_submitted_updated_and_release_searches(self) -> None:
        for basis in ("submitted", "updated", "release"):
            with self.subTest(basis=basis):
                self.artifacts = complete_run()
                query = next(query for query in self.artifacts["01_discovery.json"]["query_log"]
                             if query["branch"] == "E" and query["date_basis"] == basis)
                query["date_basis"] = "citation"
                self.assert_run_rejected()

    def test_overlapping_search_window_cannot_shrink_to_one_week(self) -> None:
        self.artifacts["01_discovery.json"]["query_log"][0]["date_from"] = "2026-10-14"
        self.assert_run_rejected()

    def test_release_search_covers_at_least_forty_five_calendar_days(self) -> None:
        query = next(query for query in self.artifacts["01_discovery.json"]["query_log"]
                     if query["date_basis"] == "release")
        query["date_from"] = (date.fromisoformat(RUN_ID) - timedelta(days=43)).isoformat()
        self.assert_run_rejected()

    def test_stale_execution_timestamps_cannot_claim_a_current_search(self) -> None:
        for delta in (-2, 2, -730):
            with self.subTest(days_from_run=delta):
                self.artifacts = complete_run()
                old_date = (date.fromisoformat(RUN_ID) + timedelta(days=delta)).isoformat()
                self.artifacts["01_discovery.json"]["query_log"][0]["executed_at"] = f"{old_date}T09:00:00+08:00"
                self.assert_run_rejected()

    def test_adjacent_execution_date_allows_timezone_and_midnight_boundaries(self) -> None:
        for delta in (-1, 1):
            with self.subTest(days_from_run=delta):
                self.artifacts = complete_run()
                adjacent_date = (date.fromisoformat(RUN_ID) + timedelta(days=delta)).isoformat()
                self.artifacts["01_discovery.json"]["query_log"][0]["executed_at"] = f"{adjacent_date}T00:01:00+08:00"
                self.assertEqual([], self.run_errors())

    def test_live_search_windows_end_on_the_run_date_or_previous_day(self) -> None:
        for basis in ("submitted", "updated", "release"):
            with self.subTest(basis=basis):
                self.artifacts = complete_run()
                query = next(query for query in self.artifacts["01_discovery.json"]["query_log"]
                             if query["date_basis"] == basis)
                query.update({"date_from": "2024-01-01", "date_to": "2024-12-31"})
                self.assert_run_rejected()

    def test_previous_day_search_windows_are_current_and_preserve_overlap(self) -> None:
        for query in self.artifacts["01_discovery.json"]["query_log"]:
            for field in ("date_from", "date_to"):
                query[field] = (date.fromisoformat(query[field]) - timedelta(days=1)).isoformat()
        self.assertEqual([], self.run_errors())

    def test_candidate_and_query_log_require_bidirectional_links(self) -> None:
        for change in ("candidate_to_query", "query_to_candidate"):
            with self.subTest(change=change):
                self.artifacts = complete_run()
                discovery = self.artifacts["01_discovery.json"]
                if change == "candidate_to_query":
                    discovery["candidates"][0]["query_id"] = "Q-unknown"
                else:
                    discovery["query_log"][0]["candidate_ids"] = []
                self.assert_run_rejected()

    def test_watchlist_requires_an_actionable_revisit_trigger(self) -> None:
        discovery = self.artifacts["01_discovery.json"]
        discovery["triage"][0].update({
            "decision": "watchlist",
            "reason": "The potential contribution is relevant, but official code has not yet been released.",
            "revisit_trigger": "Reassess when the official repository publishes reproducible simulation assets.",
        })
        self.artifacts["02_evidence.json"]["paper_cards"] = []
        self.artifacts["03_review.json"]["quality_review"] = []
        self.artifacts["03_review.json"]["visual_cards"] = []
        self.artifacts["05_registry_patch.json"]["registry_additions"] = []
        self.assertEqual([], self.run_errors())
        discovery["triage"][0].pop("revisit_trigger")
        self.assert_run_rejected()


if __name__ == "__main__":
    unittest.main()
