# Frontier Knowledge Expansion Run — 2026-11-02

Policy v2 accepted three branch-E infrastructures after all fixed core sources, the VLA leaderboard, watch sources and five-branch submitted/updated/release searches were checked.

## Accepted

- **RobotAgentBench** — released open-world household autonomy runtime, assets and scoring across discovery, reasoning, manipulation, recovery, robustness and open-ended assistance (5/5/5).
- **EmbodiedLab** — executable act-to-know scientific experiments requiring physical intervention and measurement (4/4/4).
- **Embodied Playground** — 410 long-horizon physical/strategic environments with goal, rule and physical-validity checks (4/4/4).

Each received a new narrow task scope; no existing paper was superseded because protocols are complementary.

## Watchlist

- **PhysLadder** — revisit after evaluator/data release and broader repeated-trial evidence.
- **RobotWorld** — revisit after licensed stable release with repeated trials or uncertainty intervals.
- **RoboWorM** — revisit after official metric implementation and benchmark media/data release.

## Visual review

Official temporal media was inspected for every accepted paper. RobotAgentBench showed household execution, context-driven cleanup and recovery; EmbodiedLab coupled apparatus manipulation with instrument/goal state; Embodied Playground showed Rubik and Kongming reference executions. The latter are explicitly reference-controller evidence, not agent scores.

## Undecided

None. Visual uncertainty did not determine any otherwise-passing candidate.

## Validation

`REQUIRE_UNDECIDED_DOSSIERS=1 python3 scripts/validate_all.py` passed; only pre-existing missing-local-PDF warnings remain.
