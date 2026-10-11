# 2026-10-12 Frontier Knowledge Expansion

## Accepted

- **PhysLDM: Latent Diffusion for High-Fidelity Deformable Simulation** (branch A) — [`physldm-2026.md`](../../paper_reads/A_executable_world_representation/physldm-2026.md)
- **WorldCast: Distributed Multiplayer World Models** (branch B) — [`worldcast-2026.md`](../../paper_reads/B_interactive_generation_pcg/worldcast-2026.md)
- **Tetris3D: 3D Scene Generation With Objects That Fit Together** (branch B) — [`tetris3d-2026.md`](../../paper_reads/B_interactive_generation_pcg/tetris3d-2026.md)
- **Never Look Back: Understanding Persistence in 3D Object Memory from Egocentric Videos** (branch C) — [`ledger-3d-2026.md`](../../paper_reads/C_spatial_intelligence/ledger-3d-2026.md)
- **DreamTrue: Action-Faithful Robot World Model with Counterfactual Post-Training** (branch D) — [`dreamtrue-2026.md`](../../paper_reads/D_vla_world_action_models/dreamtrue-2026.md)
- **PLaW-VLA: Predictive Latent World Modeling for Vision-Language-Action Policies** (branch D) — [`plaw-vla-2026.md`](../../paper_reads/D_vla_world_action_models/plaw-vla-2026.md)
- **UNITAS: A 3D-Native World Action Model for Embodied Manipulation** (branch D) — [`unitas-2026.md`](../../paper_reads/D_vla_world_action_models/unitas-2026.md)
- **RoboJEPA: Scaling Robotic Latent World Models** (branch D) — [`robojepa-2026.md`](../../paper_reads/D_vla_world_action_models/robojepa-2026.md)
- **Long-WAM: Scaling the Context of World-Action Models** (branch D) — [`long-wam-2026.md`](../../paper_reads/D_vla_world_action_models/long-wam-2026.md)
- **DepthWorld: 3D World Model for Robot Manipulation** (branch D) — [`depthworld-2026.md`](../../paper_reads/D_vla_world_action_models/depthworld-2026.md)
- **LIVIN: Benchmarking Spatial and Embodied Intelligence in Digital Twins of Lived-In Homes** (branch E) — [`livin-2026.md`](../../paper_reads/E_evaluation_data_infrastructure/livin-2026.md)
- **MultiWorldBench: Do Independently Controlled Views Describe One Shared World?** (branch E) — [`multiworldbench-2026.md`](../../paper_reads/E_evaluation_data_infrastructure/multiworldbench-2026.md)
- **OpenViTac: Learning and Benchmarking Visuo-Tactile Policies in a Unified Sim-and-Real Framework** (branch E) — [`openvitac-2026.md`](../../paper_reads/E_evaluation_data_infrastructure/openvitac-2026.md)
- **RT-Safe: Benchmarking Agent Safety in Real-Time Embodied Environment** (branch E) — [`rt-safe-2026.md`](../../paper_reads/E_evaluation_data_infrastructure/rt-safe-2026.md)
- **The Robot Is Not Its Description: GaugeBench for Representation Robustness in Morphology-Aware Policies** (branch E) — [`gaugebench-2026.md`](../../paper_reads/E_evaluation_data_infrastructure/gaugebench-2026.md)
- **BiGym 2.0: Benchmarking Learned and Agent-Developed Policies for Humanoid Household Manipulation** (branch E) — [`bigym-2-2026.md`](../../paper_reads/E_evaluation_data_infrastructure/bigym-2-2026.md)

## Followed sources checked

All 15 core source groups plus the core VLA leaderboard were checked; all four watch groups and the VLA survey were spot-checked. Physical Intelligence returned HTTP 403 and was query-checked through indexed official sources.

## Rejected / Watchlist

- **RealtimeWAM: How Fast Can I Run My World Action Model?** — watchlist: Promising 8.90x-10.67x latency result, but the linked project is still an anonymous staging surface and the current run could not confidently inspect representative unedited hardware demos.
- **SpaceFlow: Locally Controllable 3D Generation** — reject: Strong local 3D control, but current evidence is object generation rather than interactive scene/world generation; project relevance is below the branch threshold.
- **A Balanced Data Diet: Addressing the Exploration Bottleneck in Mega-Scale RL for Robot Control** — reject: Impressive simulation-scale RL, but it is a policy optimization contribution rather than VLA/world-action modeling or shared evaluation infrastructure for this repository.

## Top demos

1. DreamTrue — counterfactual action-conditioned multi-view robot futures and interaction-defect post-training.
2. WorldCast — distributed, independently controlled multiplayer views with shared state.
3. BiGym 2.0 — open humanoid tasks, demonstrations, agent traces, and browser 3D replay.

## Undecided visual cases

None. RealtimeWAM remains watchlist-only rather than accepted because its staged demo surface did not support confident review.

## Collection notes

- Most relevant: UNITAS, DreamTrue, and MultiWorldBench.
- Best baseline additions: RoboJEPA and Long-WAM for latent/long-context world models; OpenViTac and BiGym 2.0 for infrastructure.
- Cite metrics as author-reported until reproduction; do not compare success rates across different embodiments or protocols directly.
- No social-media-only claim was accepted.

## Validation

`REQUIRE_UNDECIDED_DOSSIERS=1 python3 scripts/validate_all.py` passed for 152 registry papers and every completed run. Only the pre-existing missing-local-PDF warnings remain.
