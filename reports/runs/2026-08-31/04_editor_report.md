# Frontier Knowledge Expansion Run — 2026-08-31

## Accepted

- B: SpatialCrafter — persistent generative 3D proxy for controllable single-image worlds.
- D: Gemini Robotics 2 — whole-body, cross-embodiment and multi-robot VLA family.
- D: CLAP — open cross-embodiment action-conditioned video world model.
- E: PAWBench — distributional possible-futures benchmark.
- E: R2M-Bench — relative revisit-memory benchmark.

## Followed-source coverage

All 15 core source groups and the core VLA leaderboard were checked. Four watch groups and the survey index were spot-checked. Fixed sources were evaluated before the broad primary-source August scan.

## Undecided (local-only)

- CAND-0006 4DSynth: official dynamic-world demo needed.
- CAND-0007 Riemann-1.0: official real-robot demos and release evidence needed.
- CAND-0008 WorldEcho/WorldSync: official generated and physical rollout comparison needed.

## Watchlist / rejected

- CAND-0009 is a useful simulator-gap survey/evidence map but does not clear the impact gate as executable infrastructure.
- Older missed signals (MolmoSpaces, pi0.7, Hy-Embodied) are reserved for a separate backfill audit so this run remains a clean August 24–31 scan.

## Top demos

1. CLAP: open cross-embodiment rollouts and policy-in-the-loop deployment.
2. Gemini Robotics 2: whole-body dexterity and multi-robot coordination.
3. SpatialCrafter: indoor/outdoor exploration and long-video consistency.

## Collection notes

- PAWBench is the strongest new citation for stochastic future distributions.
- R2M-Bench is a focused baseline for persistent state and slow-motion shortcut control.
- CLAP is the most reproducible new world-action baseline.
- Gemini Robotics 2 is a closed frontier reference, not a reproducible baseline.
- SpatialCrafter should be revisited when code/checkpoints ship.

## Validation

Passed `REQUIRE_UNDECIDED_DOSSIERS=1 python3 scripts/validate_all.py`; only pre-existing missing-local-PDF warnings remain.
