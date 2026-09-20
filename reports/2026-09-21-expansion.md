# Frontier Knowledge Expansion — 2026-09-21

This run checked the September 15-21 release window, all fixed core sources, watch groups, the VLA leaderboard, and broader primary-source searches. Eight candidates passed every gate; one remains local-only undecided.

## Accepted by Branch

### A. Executable World Representation

- [FAMOS](../paper_reads/A_executable_world_representation/famos-2026.md) — feed-forward multi-state movable-part and joint recovery.
- [FunArt](../paper_reads/A_executable_world_representation/funart-2026.md) — functional elements and executable articulation from generative 3D latents.

### B. Interactive Generation and PCG

- [Astronex-World 1.0](../paper_reads/B_interactive_generation_pcg/astronex-world-2026.md) — open real-time video worlds with camera, action, embodiment, and event control.

### D. VLA and World-Action Models

- [Agile-WAM](../paper_reads/D_vla_world_action_models/agile-wam-2026.md) — low-latency tactile future modeling for contact-rich control.

### E. Evaluation and Data Infrastructure

- [PersistBench](../paper_reads/E_evaluation_data_infrastructure/persistbench-2026.md) — reference-backed off-screen memory evaluation.
- [Universal Navigation Interface](../paper_reads/E_evaluation_data_infrastructure/universal-navigation-interface-2026.md) — 37.2 km of physically constrained robot-free navigation data.
- [BinoGen](../paper_reads/E_evaluation_data_infrastructure/binogen-2026.md) — 20M+ embodiment-aware binocular images with dense supervision.
- [SlugTrails](../paper_reads/E_evaluation_data_infrastructure/slugtrails-2026.md) — large-building egocentric floor-plan localization.

No candidate passed in C this week.

## Followed-source Coverage

- Checked all 15 core groups plus the core VLA leaderboard.
- Spot-checked all four watch groups and the VLA survey.
- Berkeley RAIL remains unreachable/redirected; primary author and arXiv searches compensated.

## Top Demos

1. Astronex-World — diverse real-time camera/action/event-controlled worlds with code and weights.
2. Agile-WAM — contact-rich assembly/insertion and corrective-recovery executions.
3. FAMOS — moving multi-state comparisons that visibly disambiguate joints.

## Undecided — Local Only

- Workspace Models clears source, impact, and relevance gates, but no official continuous hardware execution surface was found. The dossier at `undecided/2026-09-21/CAND-0009.md` remains local-only.

## Watchlist / Rejected

- HIL-UMI and DexTouch-WM remain watchlist-only pending stronger official demos/releases.
- GeoAAC, MoWAM, and StageGuard were below the impact threshold.
- The world-model survey remains discovery context only. No social-only claim was accepted.

## Top Project-Relevant Papers

1. PersistBench — strongest new persistent-world evaluator.
2. FAMOS — strongest new executable articulation representation.
3. Astronex-World — strongest reproducible real-time interactive generation baseline.

## Collection Notes

- Pair PersistBench with R2M-Bench to distinguish reference-backed object memory from same-rollout revisit gains.
- Treat Astronex video coherence as a generation result, not proof of simulator-valid physics.
- Recheck BinoGen release availability before attempting reproduction.

## Validation

- `REQUIRE_UNDECIDED_DOSSIERS=1 python3 scripts/validate_all.py` passed for 118 papers and all completed runs. Only pre-existing missing-local-PDF warnings remain.
