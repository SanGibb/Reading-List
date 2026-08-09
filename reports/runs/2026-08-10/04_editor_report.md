# Frontier Knowledge Expansion Run

Date: 2026-08-10

## Accepted

- C: Point-It-Out — precise localization, affordance pointing, and action-trace evaluation.
- D: VLA-JEPA — leakage-free latent world supervision for VLA learning.
- D: Geometry-aware 4D Video Generation — multi-view RGB-D futures to 6-DoF actions.
- D: GEM-4D — correspondence-distilled video planning and adaptive inverse dynamics.
- D: ORV — occupancy/action-conditioned multi-view robot video generation.
- E: MolmoSpaces — open cross-simulator scenes, assets, grasps, tasks, and benchmark infrastructure.

Every reviewer-passed candidate was included; no top-k sampling was applied.

## Watchlist / Rejected

- LeRobot v0.6 is an important official infrastructure release and influence signal, but it is not a standalone research-paper registry unit. Its VLA-JEPA integration is recorded in that paper's evidence trail.
- No social-media-only claim was accepted.

## Undecided

None. Official visual/demo surfaces were sufficient for all generation-heavy and embodied-demo candidates.

## Top Demos

1. Geometry-aware 4D Video Generation: paired RGB/depth futures and successful manipulation under unseen views.
2. ORV: broad prediction/GT, three-view, and sim-to-real augmentation galleries.
3. MolmoSpaces: interactive scene browser plus executable benchmark and leaderboard.

## Most Project-Relevant

1. MolmoSpaces for portable executable-world assets, grasps, tasks, and evaluation.
2. Geometry-aware 4D Video Generation for cross-view geometry-to-action validation.
3. VLA-JEPA for a compact training-only world-model interface.

## Collection Notes

- Related work: the accepted D-branch set traces a progression from dense occupancy/geometry supervision to executable action extraction.
- Baselines: PIO is a lightweight spatial diagnostic; MolmoSpaces is an infrastructure baseline; VLA-JEPA is a latent world-action baseline.
- Evidence gaps: GEM-4D code is missing, VLA-JEPA training code is partial, and all numerical gains remain source-reported.

## Validation

`REQUIRE_UNDECIDED_DOSSIERS=1 python3 scripts/validate_all.py` passed. Only pre-existing missing-local-PDF warnings remain.
