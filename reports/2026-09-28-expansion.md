# Frontier Knowledge Expansion — 2026-09-28

This run checked all 15 core follow groups plus the VLA leaderboard, spot-checked all four watch groups and the VLA survey, and searched primary sources for September 22–28 releases. Ten candidates passed every acceptance gate; two remain local-only for human visual judgment.

## Accepted

### A — Executable World Representation

- [PointCast](../paper_reads/A_executable_world_representation/pointcast-2026.md) — identity-preserving point dynamics across rigid, articulated, and deformable objects.

### B — Interactive Generation and PCG

- [AgriGen](../paper_reads/B_interactive_generation_pcg/agrigen-2026.md) — ROS/Isaac-Sim procedural agricultural environments with physics and domain randomization.

### D — VLA and World-Action Models

- [AD-WM](../paper_reads/D_vla_world_action_models/ad-wm-2026.md) — counterfactual action discrimination for MPC.
- [Self-Adaptive VLA](../paper_reads/D_vla_world_action_models/self-adaptive-vla-2026.md) — rollout-conditioned recovery from hardware shifts.
- [Rolling-WAM](../paper_reads/D_vla_world_action_models/rolling-wam-2026.md) — staggered rolling imagination with a 4.5x reported replanning speedup.
- [Streaming-WAM](../paper_reads/D_vla_world_action_models/streaming-wam-2026.md) — committed-action-conditioned asynchronous control with open code/models.
- [InternW0](../paper_reads/D_vla_world_action_models/internw0-2026.md) — open physical world model trained on 7,233.5 hours with tactile/force and scientific-task demos.

### E — Evaluation and Data Infrastructure

- [EmbodiedMemory-Bench](../paper_reads/E_evaluation_data_infrastructure/embodiedmemory-bench-2026.md) — 2,554 executable long-horizon memory episodes.
- [Training Object Permanence in World Models](../paper_reads/E_evaluation_data_infrastructure/wrop-object-permanence-2026.md) — 150 generators, 1.5M samples, fixed exam, weights, and training code.
- [RoboTwin-Phys](../paper_reads/E_evaluation_data_infrastructure/robotwin-phys-2026.md) — 13 physical-condition axes and 5,000+ parameter-labeled demonstrations.

No Branch C candidate cleared all gates this week.

## Top demos

1. InternW0: long-horizon MOF synthesis and force-aware dexterous pipetting.
2. Streaming-WAM: continuous execution with explicit timing and released implementation.
3. WROP: complete cognitive-task browser with data, outputs, model, code, and leaderboard.

## Undecided (local-only)

- CAND-0011 Fysiverse-3D-Vision: official moving/interactive evidence is needed to judge executable generation and collision behavior.
- CAND-0012 World Action Agent: official continuous robot execution evidence is needed to judge rehearsal/correction quality.

Both dossiers exist under ignored `undecided/2026-09-28/` and are excluded from publication.

## Rejected / watchlist

- Ego-Exo4D Human Meshes was rejected for this repository because project relevance is below the acceptance threshold.
- No social-media-only claim was accepted.

## Follow-source coverage

- All configured core groups were checked where reachable.
- Physical Intelligence returned HTTP 429; Berkeley RAIL remains an unusable configured surface.
- Four watch groups and the VLA survey were spot-checked.

## Collection notes

- InternW0 is the strongest new general baseline for open asynchronous physical world-action modeling.
- PointCast offers a clean executable-state abstraction for cross-topology dynamics.
- EMem-Bench and RoboTwin-Phys supply orthogonal memory and physical robustness axes for evaluation.
- AgriGen is accepted with adequate visuals, but code/data reproducibility remains pending.

## Validation

`REQUIRE_UNDECIDED_DOSSIERS=1 python3 scripts/validate_all.py` is recorded as passed in the run manifest after final validation.

