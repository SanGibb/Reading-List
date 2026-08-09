# Weekly Frontier Knowledge Expansion — 2026-08-10

This run checked all 16 core follow-source groups and spot-checked all five watch groups before broad primary-source search. Six newly influential 2025–2026 works passed every acceptance gate and were added; no candidate required an undecided dossier.

## Accepted

### C. Spatial Intelligence

- [Point-It-Out](../paper_reads/C_spatial_intelligence/point-it-out-2025.md) — TMLR benchmark for box, point, and action-trace embodied grounding.

### D. VLA and World-Action Models

- [VLA-JEPA](../paper_reads/D_vla_world_action_models/vla-jepa-2026.md) — leakage-free latent future supervision, now integrated into LeRobot.
- [Geometry-aware 4D Video Generation](../paper_reads/D_vla_world_action_models/geometry-aware-4d-video-generation-2025.md) — synchronized RGB-D futures and 6-DoF trajectory extraction.
- [GEM-4D](../paper_reads/D_vla_world_action_models/gem-4d-2026.md) — correspondence-distilled video generation plus adaptive inverse dynamics.
- [ORV](../paper_reads/D_vla_world_action_models/orv-2025.md) — 4D occupancy and action conditioned multi-view robot video generation.

### E. Evaluation and Data Infrastructure

- [MolmoSpaces](../paper_reads/E_evaluation_data_infrastructure/molmospaces-2026.md) — 230K+ scenes, 130K objects, 42M grasps, eight tasks, and cross-simulator tooling.

## Follow-Source Coverage

- Core: 16/16 checked.
- Watch: 5/5 spot-checked.
- Primary/official sources used for every acceptance; no social-media-only claim entered the registry.

## Visual / Demo Review

- Strong: Geometry-aware 4D Video Generation and ORV.
- Adequate: MolmoSpaces, VLA-JEPA, and GEM-4D.
- Not applicable: Point-It-Out is an evaluation/data benchmark.
- Undecided: none.

## Watchlist

- LeRobot v0.6 is recorded as an official infrastructure signal, not a standalone paper entry; its VLA-JEPA integration supports that paper's influence and reproducibility evidence.

## Top Demos

1. Geometry-aware 4D Video Generation: paired RGB/depth future videos and policy outcomes.
2. ORV: large prediction/GT, three-view, and sim-to-real galleries.
3. MolmoSpaces: interactive environment snapshot, executable benchmark, and leaderboard.

## Collection Notes

- Related work: ORV, Geometry-aware 4D, and GEM-4D form a useful progression from dense physical-state conditioning to executable action recovery.
- Baselines: PIO is a compact spatial diagnostic; MolmoSpaces is an infrastructure baseline; VLA-JEPA is a training-only latent world-model baseline.
- Evidence gaps: GEM-4D code is unavailable, VLA-JEPA training code is partial, and all numerical gains are source-reported.

## Validation

`REQUIRE_UNDECIDED_DOSSIERS=1 python3 scripts/validate_all.py` passed. The only warnings are pre-existing missing local PDF paths.
