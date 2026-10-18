# 2026-10-18 Frontier Expansion Editor Report

## Accepted

- **RoboSimStudio: An Interactive Toolkit for Human and Agent Rapid Real2Sim of Robot Manipulation Tasks** (branch A) — [`robosimstudio-2026.md`](../../paper_reads/A_executable_world_representation/robosimstudio-2026.md)
- **AutoRSR: Automated Real-to-Sim-to-Real Data Generation for Scalable Robot Learning** (branch A) — [`autorsr-2026.md`](../../paper_reads/A_executable_world_representation/autorsr-2026.md)
- **PhySGA: A Physics-Space Grounded Agentic Framework for Generalizable and Interactive 3D Composition** (branch B) — [`physga-2026.md`](../../paper_reads/B_interactive_generation_pcg/physga-2026.md)
- **From Failures to Learnable Worlds: Policy-Conditioned Environment Generation for Navigation Agents** (branch B) — [`wedge-2026.md`](../../paper_reads/B_interactive_generation_pcg/wedge-2026.md)
- **PAWA: Panoramic Action-conditioned World Modeling for Multiple Agents** (branch B) — [`pawa-2026.md`](../../paper_reads/B_interactive_generation_pcg/pawa-2026.md)
- **DeSpatial: The devil of Agentic Spatial Reasoning Lies in 3D Itself** (branch C) — [`despatial-2026.md`](../../paper_reads/C_spatial_intelligence/despatial-2026.md)
- **DynThinker: Unifying Static 3D and Dynamic 4D Spatial Reasoning** (branch C) — [`dynthinker-2026.md`](../../paper_reads/C_spatial_intelligence/dynthinker-2026.md)
- **T2-z: Test-Time Optimization of Environment Latents for Robotic World Models** (branch D) — [`t2-z-2026.md`](../../paper_reads/D_vla_world_action_models/t2-z-2026.md)
- **GeoState: Learning View-Decoupled Geometry States for 3D World Modeling** (branch D) — [`geostate-2026.md`](../../paper_reads/D_vla_world_action_models/geostate-2026.md)
- **OneWM: Can World and Action Modeling Benefit Each Other under Unified Causal Training?** (branch D) — [`onewm-2026.md`](../../paper_reads/D_vla_world_action_models/onewm-2026.md)
- **What Matters for World Modeling in Vision-Language-Action Models?** (branch D) — [`what-matters-world-modeling-vla-2026.md`](../../paper_reads/D_vla_world_action_models/what-matters-world-modeling-vla-2026.md)
- **LIBERO-PeRM: Benchmarking Personalized Robotic Manipulation** (branch E) — [`libero-perm-2026.md`](../../paper_reads/E_evaluation_data_infrastructure/libero-perm-2026.md)
- **Orbia: Do Generated Videos Form a Consistent 3D World?** (branch E) — [`orbia-2026.md`](../../paper_reads/E_evaluation_data_infrastructure/orbia-2026.md)
- **ForceBench: Benchmarking Force Integration for Robotic Manipulation** (branch E) — [`forcebench-2026.md`](../../paper_reads/E_evaluation_data_infrastructure/forcebench-2026.md)
- **TacClaw-Infinity: A Large-Scale Vision-Tactile-Language-Action Dataset for Dexterous Manipulation** (branch E) — [`tacclaw-infinity-2026.md`](../../paper_reads/E_evaluation_data_infrastructure/tacclaw-infinity-2026.md)
- **Active Generative Simulation: Meta-Learning What to Simulate for Sim-and-Real Policy Co-Training** (branch E) — [`active-generative-simulation-2026.md`](../../paper_reads/E_evaluation_data_infrastructure/active-generative-simulation-2026.md)

## Followed sources checked

All core source groups plus the core VLA leaderboard were checked; watch groups and the VLA survey were spot-checked. Physical Intelligence remained access-controlled, and the configured Berkeley RAIL surface remained unsuitable, so indexed official/primary searches were used.

## Rejected / Watchlist

- P3-WAM — watchlist: official demo surface returned access controls, so visual execution quality was not confidently reviewable.
- Mallea and GRASE — watchlist pending official inspectable demo/code surfaces.
- VLA-Delta and VeriVLA — rejected below the impact boundary for this collection.

## Top demos

1. RoboSimStudio — editable contact physics with real/generated/output/deployment videos.
2. OneWM — unified causal world/action learning with public code and real-robot rollouts.
3. Orbia — interactive 3D-consistency protocols, gallery, open data/code, and a 27-model leaderboard.

## Undecided visual cases

P3-WAM, Mallea, and GRASE have detailed local-only dossiers because their acceptance depends on official moving/interactive evidence that could not be inspected confidently. They remain outside the registry pending human review.

## Collection notes

- Most relevant: RoboSimStudio, GeoState, OneWM, and Orbia.
- Strong infrastructure: LIBERO-PeRM, ForceBench, TacClaw-Infinity, and MetaGenSim.
- Cite all fresh-release metrics as author-reported; do not compare success rates across incompatible protocols.
- No social-media-only claim was accepted.

## Validation

`REQUIRE_UNDECIDED_DOSSIERS=1 python3 scripts/validate_all.py` passed for 168 papers and every completed run. Only the pre-existing missing-local-PDF warnings remain.
