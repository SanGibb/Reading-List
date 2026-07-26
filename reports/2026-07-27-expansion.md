# Frontier Knowledge Expansion — 2026-07-27

This run checked every fixed core source group before broad primary-source discovery and accepted every discovered candidate that cleared the harness. Four papers were added; no visual case remained undecided.

## Accepted

### B. Interactive Generation and PCG

- [Image2Sim](../paper_reads/B_interactive_generation_pcg/image2sim-2026.md) — converts posed RGB-D imagery into nearly 20K interactive neural scenes and 10M+ navigation samples.

### D. VLA and World-Action Models

- [Mask2Real-WM](../paper_reads/D_vla_world_action_models/mask2real-wm-2026.md) — separates simulated mask dynamics from real-video rendering for controllable 23-DoF rollouts.
- [Lift3D-VLA](../paper_reads/D_vla_world_action_models/lift3d-vla-2026.md) — adds explicit current/future 3D geometry and temporally structured action chunks to a VLA.
- [LingBot-VA 2.0](../paper_reads/D_vla_world_action_models/lingbot-va-2-2026.md) — native causal video-action pretraining with sparse MoE and asynchronous closed-loop inference.

Branches A, C, and E had no new candidate clear the acceptance threshold in this run.

## Followed Sources Checked

- All 15 `priority: core` groups were checked against their official lab, project, code, or benchmark surfaces.
- Four `priority: watch` groups were spot-checked where relevant.
- The detailed status and URLs are recorded in [01_discovery.json](runs/2026-07-27/01_discovery.json).

## Rejected / Watchlist

- VLAFlow: useful controlled training-objective study, but impact prior remained below the repository threshold and no strong official demo/release surface was found.
- KAM-WM: promising kinematic-affordance mechanism, but currently narrow with insufficient project-scale evidence.
- Camera-Centric VLA: practical calibration-free view robustness, but influence/release evidence remains below threshold.
- No social-media-only claim was accepted.

## Top Demos

1. Mask2Real-WM — clearest side-by-side evidence for fine-grained action controllability and long-horizon rollout.
2. Lift3D-VLA — strongest diversity across pouring, stacking, picking, and OOD real-robot trials.
3. LingBot-VA 2.0 — broadest native video-action foundation-model demo surface.

## Undecided Visual Cases

None. All generation-heavy / physical / VLA candidates accepted this run had inspectable official visual material and received `strong` decisions. No local-only dossier was required.

## Collection Notes

- Image2Sim is the most useful new baseline for image-to-executable navigation worlds and action-aligned data generation.
- Mask2Real-WM is a strong related-work anchor for separating dynamics fidelity from rendering quality.
- Lift3D-VLA is a practical spatial-action baseline; cite its improvements as author-reported until reproduced.
- LingBot-VA 2.0 should be distinguished from the January 2026 predecessor; exact 2.0 checkpoint completeness needs rechecking before reproduction.

## Validation

- Run harness: passed for all runs, including `2026-07-27` (7 discovered, 4 analyzed and accepted, 4 registry additions).
- Registry validation: passed with 75 papers across five branches; only pre-existing missing-local-PDF warnings remain.
- Accepted primary URLs, branch fit, and deep-dive paths are populated.
- `REQUIRE_UNDECIDED_DOSSIERS=1 python3 scripts/validate_all.py`: passed.
