# Frontier Knowledge Expansion Run

Date: 2026-06-06

## Summary

Initialization expansion run. The goal was to seed the knowledge base with enough high-quality, source-checked work across executable world representation, interactive generation/PCG, spatial/VLA, and evaluation infrastructure. This run accepted 15 papers for detailed knowledge-base coverage: 5 new registry additions and 10 existing seed entries upgraded with verified deep dives.

## Followed Sources Checked

| Source | Status | Notes |
|---|---|---|
| stanford-svl-behavior | checked | Used for BEHAVIOR-1K, SceneFun3D, PhysDreamer lines. |
| princeton-pvl-infinigen | checked | Used for Infinigen Indoors and procedural generation branch. |
| ai2-embodied-prior | checked | Used for Holodeck embodied environment generation. |
| cmu-genesis-robogen | checked | Used for RoboGen agentic PCG. |
| stanford-iris-openvla | checked | Used for OpenVLA line. |
| berkeley-rail-levine | checked | Used for Octo/OpenVLA robot policy baselines. |
| physical-intelligence | checked | Used for pi0 high-quality robot demo evidence. |
| ut-austin-rpl-yuke | spot_checked | Used for RoboVerse infrastructure evidence. |

## Accepted / Updated Papers

| Paper | Branch | Source | Deep dive | Visual | Registry action |
|---|---|---|---|---|---|
| SceneFun3D: Fine-Grained Functionality and Affordance Understanding in 3D Scenes | A | https://scenefun3d.github.io/ | ../../../paper_reads/A_executable_world_representation/scenefun3d-2024.md | not_applicable | update |
| BEHAVIOR-1K: A Human-Centered, Embodied AI Benchmark with 1,000 Everyday Activities and Realistic Simulation | A | https://arxiv.org/abs/2403.09227 | ../../../paper_reads/A_executable_world_representation/behavior-1k-2024.md | not_applicable | update |
| PhysX-Omni: Unified Simulation-Ready Physical 3D Generation for Rigid, Deformable, and Articulated Objects | A | https://arxiv.org/abs/2605.21572 | ../../../paper_reads/A_executable_world_representation/physx-omni-2026.md | strong | update |
| PhysDreamer: Physics-Based Interaction with 3D Objects via Video Generation | A | https://arxiv.org/abs/2404.13026 | ../../../paper_reads/A_executable_world_representation/physdreamer-2024.md | strong | addition |
| Feature Splatting: Language-Driven Physics-Based Scene Synthesis and Editing | A | https://arxiv.org/abs/2404.01223 | ../../../paper_reads/A_executable_world_representation/feature-splatting-2024.md | strong | addition |
| PhyScene: Physically Interactable 3D Scene Synthesis for Embodied AI | B | https://arxiv.org/abs/2404.09465 | ../../../paper_reads/B_interactive_generation_pcg/physcene-2024.md | strong | update |
| Holodeck: Language Guided Generation of 3D Embodied AI Environments | B | https://arxiv.org/abs/2312.09067 | ../../../paper_reads/B_interactive_generation_pcg/holodeck-2024.md | strong | addition |
| Infinigen Indoors: Photorealistic Indoor Scenes using Procedural Generation | B | https://arxiv.org/abs/2406.11824 | ../../../paper_reads/B_interactive_generation_pcg/infinigen-indoors-2024.md | strong | addition |
| RoboGen: Towards Unleashing Infinite Data for Automated Robot Learning via Generative Simulation | B | https://arxiv.org/abs/2311.01455 | ../../../paper_reads/B_interactive_generation_pcg/robogen-2024.md | strong | update |
| SpatialVLA: Exploring Spatial Representations for Visual-Language-Action Models | C | https://arxiv.org/abs/2501.15830 | ../../../paper_reads/C_spatial_intelligence/spatialvla-2025.md | strong | update |
| Octo: An Open-Source Generalist Robot Policy | D | https://arxiv.org/abs/2405.12213 | ../../../paper_reads/D_vla_world_action_models/octo-2024.md | strong | update |
| OpenVLA: An Open-Source Vision-Language-Action Model | D | https://arxiv.org/abs/2406.09246 | ../../../paper_reads/D_vla_world_action_models/openvla-2024.md | strong | update |
| pi0: A Vision-Language-Action Flow Model for General Robot Control | D | https://arxiv.org/abs/2410.24164 | ../../../paper_reads/D_vla_world_action_models/pi0-2024.md | strong | update |
| RoboVerse: Towards a Unified Platform, Dataset and Benchmark for Scalable and Generalizable Robot Learning | E | https://arxiv.org/abs/2504.18904 | ../../../paper_reads/E_evaluation_data_infrastructure/roboverse-2025.md | not_applicable | update |
| OpenEQA: Embodied Question Answering in the Era of Foundation Models | E | https://openaccess.thecvf.com/content/CVPR2024/html/Majumdar_OpenEQA_Embodied_Question_Answering_in_the_Era_of_Foundation_Models_CVPR_2024_paper.html | ../../../paper_reads/E_evaluation_data_infrastructure/openeqa-2024.md | not_applicable | addition |

## New Registry Additions

- PhysDreamer
- Feature Splatting
- Holodeck
- Infinigen Indoors
- OpenEQA

## Existing Seed Entries Upgraded With Deep Dives

- SceneFun3D
- BEHAVIOR-1K
- PhysX-Omni
- PhyScene
- RoboGen
- SpatialVLA
- Octo
- OpenVLA
- pi0
- RoboVerse

## Top Demos / Visual Evidence

1. pi0: strong real-robot dexterity demos, including laundry folding and long-horizon table tasks.
2. PhyScene: generated interactable scenes with articulated objects and robot interaction evidence.
3. Infinigen Indoors: high-fidelity procedural indoor scene generation with dense annotation potential.
4. PhysDreamer / Feature Splatting: physical and deformable-style object/scene dynamics.
5. OpenVLA / SpatialVLA: real robot policy rollouts and spatial instruction demos.

## Collection Notes

- The initial knowledge base should not treat all entries equally: PhyScene, Holodeck, Infinigen, RoboGen, PhysDreamer, Feature Splatting, OpenVLA, Octo, pi0, and SpatialVLA are the strongest method/demo anchors.
- BEHAVIOR-1K, SceneFun3D, OpenEQA, and RoboVerse are infrastructure anchors: they define fields, tasks, or evaluation targets rather than generation quality.
- PhysX-Omni is highly aligned with physical/deformable simulation-ready assets, but it is very recent and should be rechecked after code/dataset maturity improves.

## Validation

- Run validation: passed via `python3 scripts/validate_run.py 2026-06-06`.
- Registry validation: passed via `python3 scripts/validate_registry.py`.
- Undecided candidates: none in this initialization batch.
