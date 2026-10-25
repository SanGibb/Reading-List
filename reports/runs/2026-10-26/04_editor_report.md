# Frontier Knowledge Expansion Run

Date: 2026-10-26
Acceptance policy: v2

## Outcome

Accepted three evaluation/infrastructure papers, all in branch E: Sensorimotor Alignment, PhysTrace, and RoboJudge. They add, respectively, an offline success proxy, temporal physical-violation localization, and human-validated judging of embodied generated videos. No paper was admitted merely for recency, venue, or a linked demo.

## Discovery coverage

All core configured source groups and the VLA leaderboard were checked; all watch groups and the VLA survey were spot-checked. The five branches each have submitted and updated searches covering 2026-10-12 through 2026-10-26, plus repository/release searches covering 2026-09-11 through 2026-10-26. Search result caps and endpoint failures are explicit in `01_discovery.json`. The full 168-paper monthly retrospective completed on 2026-10-20, so another full backfill was not due.

## Accepted

- [Sensorimotor Alignment](../../../paper_reads/E_evaluation_data_infrastructure/sensorimotor-alignment-2026.md) — released offline metric correlated with closed-loop success across embodied model families.
- [PhysTrace](../../../paper_reads/E_evaluation_data_infrastructure/phystrace-2026.md) — released temporal evaluator and IntPhys2-Timing annotations.
- [RoboJudge](../../../paper_reads/E_evaluation_data_infrastructure/robojudge-2026.md) — human-annotated judge benchmark, training set, and specialized embodied-video evaluator.

## Undecided local-only

- SceneRig (`undecided/2026-10-26/CAND-0001.md`) and PhysiCalWorld (`CAND-0005.md`) otherwise met the score gates, but temporal media playback was unavailable. Their dossiers retain exact human decisions needed; neither enters the registry.

## Watchlist

NeoWorld-3, InfiniDream, UniFlowWAM, AutoPhyX, DRILL, and PVBench remain watchlisted with concrete release, relevance, or evidence triggers.

## Task lifecycle

A new narrow task records offline embodied-policy success proxies. PhysTrace and RoboJudge join the physical-future/outcome evaluation task as complementary current diagnostics; no existing paper was superseded because protocols are not interchangeable.

## Validation

`REQUIRE_UNDECIDED_DOSSIERS=1 python3 scripts/validate_all.py` passed for 171 papers and 49 task scopes; only the pre-existing missing-local-PDF warnings remain. Mechanical validation does not independently verify scientific claims.
