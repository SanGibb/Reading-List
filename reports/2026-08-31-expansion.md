# Weekly Frontier Knowledge Expansion — 2026-08-31

This run checked every core follow-source group before a broad primary-source scan covering the missing late-August window. Five candidates passed the full acceptance gates; three generation/physical-demo candidates remain local-only for human visual review.

## Accepted by branch

### B. Interactive Generation and PCG

- [SpatialCrafter](../paper_reads/B_interactive_generation_pcg/spatialcrafter-2026.md) — global generative 3D proxy for persistent, controllable single-image world exploration.

### D. VLA and World-Action Models

- [Gemini Robotics 2](../paper_reads/D_vla_world_action_models/gemini-robotics-2-2026.md) — official whole-body, cross-embodiment and multi-robot VLA family.
- [CLAP](../paper_reads/D_vla_world_action_models/clap-cross-embodiment-world-models-2026.md) — open cross-embodiment action-conditioned video world model and deployment stack.

### E. Evaluation and Data Infrastructure

- [PAWBench](../paper_reads/E_evaluation_data_infrastructure/pawbench-2026.md) — support and probability-mass evaluation across possible physical futures.
- [R2M-Bench](../paper_reads/E_evaluation_data_infrastructure/r2m-bench-2026.md) — shortcut-resistant revisit-memory evaluation.

No candidates passed Branch A or C gates this week.

## Follow-source coverage

- Checked: all 15 core source groups plus the core VLA leaderboard.
- Spot-checked: all four watch groups and the VLA survey index.
- Unreachable/skipped: none.
- Late-July fixed-source hit: Gemini Robotics 2 was accepted because the repository had no durable run after August 3.

## Top demos

1. CLAP — open models, code, cross-embodiment rollouts and policy-in-the-loop deployment.
2. Gemini Robotics 2 — whole-body humanoid, dexterous and multi-robot official videos.
3. SpatialCrafter — diverse indoor/outdoor exploration with strong long-horizon consistency.

## Undecided (local-only)

- `CAND-0006` 4DSynth — needs official visual/simulator inspection.
- `CAND-0007` Riemann-1.0 — needs official real-robot demos and release verification.
- `CAND-0008` WorldEcho/WorldSync — needs side-by-side generated and physical rollout review.

These dossiers are under `undecided/2026-08-31/` and are intentionally excluded from publication.

## Watchlist / rejected

- From Generation to Simulation is retained as a related-work evidence map; it does not itself clear the impact gate for registry infrastructure.
- MolmoSpaces, pi0.7, and Hy-Embodied are older missed-release signals for a separate backfill audit.
- No social-media-only claim was accepted.

## Most relevant to this repository

1. CLAP — open learned simulator and cross-embodiment action interface.
2. PAWBench — explicit stochastic-future schema and calibration protocol.
3. SpatialCrafter — persistent global 3D proxy for interactive generation.

## Collection notes

- Related work: cite PAWBench for probabilistic alignment and R2M-Bench for revisit-specific memory.
- Baselines: CLAP is reproducible; Gemini Robotics 2 is a closed frontier comparison.
- Evidence gaps: recheck SpatialCrafter code, R2M-Bench release artifacts, and all three undecided demo surfaces.

## Validation

`REQUIRE_UNDECIDED_DOSSIERS=1 python3 scripts/validate_all.py` passed. Only pre-existing missing-local-PDF warnings remain; publication status is recorded in the run manifest.
