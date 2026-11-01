# 2026-11-02 Weekly Frontier Knowledge Expansion

This policy-v2 run checked all configured core follow sources, the VLA leaderboard, all watch groups, and submitted/updated 14-day plus release 45-day searches across A–E. It admitted three distinct evaluation infrastructures; the registry now contains 174 papers.

## Accepted — E. Evaluation and Data Infrastructure

| Paper | Scores (impact / relevance / evidence) | Material increment | Deep dive |
|---|---:|---|---|
| RobotAgentBench | 5 / 5 / 5 | Released open-world household autonomy runtime spanning discovery, context, recovery and high-level needs. | [deep dive](../paper_reads/E_evaluation_data_infrastructure/robotagentbench-2026.md) |
| EmbodiedLab | 4 / 4 / 4 | New executable act-to-know protocol requiring intervention, measurement and grounded conclusions. | [deep dive](../paper_reads/E_evaluation_data_infrastructure/embodiedlab-2026.md) |
| Embodied Playground | 4 / 4 / 4 | 410 environments with explicit goal, task-rule and physical-validity checks. | [deep dive](../paper_reads/E_evaluation_data_infrastructure/embodied-playground-2026.md) |

Official temporal media was actually inspected for all three. Reference-controller clips for Embodied Playground were kept explicitly separate from external-agent scores.

## Watchlist

- **PhysLadder**: matched sim-real contact hierarchy is useful, but three trials per task and no verified reusable evaluator release keep evidence below 4. Revisit after broader trials and release.
- **RobotWorld**: broad five-domain benchmark, but one episode per model-task and unclear licensing keep evidence below 4. Revisit after stable licensed repeated-trial evaluation.
- **RoboWorM**: promising kinematic/geometric metrics, but no official reusable implementation or inspectable media release was found. Revisit on code/data/demo release.

## Task frontier

Created three narrow current scopes: open-world household autonomy, embodied act-to-know science, and long-horizon physical/strategic reasoning. No predecessor was archived or superseded.

## Undecided

None this run. Historical local-only dossiers remain required for full validation and remain untracked.

## Validation

`REQUIRE_UNDECIDED_DOSSIERS=1 python3 scripts/validate_all.py` passed for 174 papers, 52 task scopes, the retrospective, every run and all generated indexes. Only pre-existing missing-local-PDF warnings remain. Author-reported results were not independently reproduced.
