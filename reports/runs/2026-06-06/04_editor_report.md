# Frontier Knowledge Expansion Run

Date: 2026-06-06

## Summary

Initialization and full-coverage expansion run. The run accepted 46 papers for detailed knowledge-base coverage: 21 registry additions and 25 existing seed entries upgraded or refreshed with verified deep dives. The policy is full inclusion after filtering: every discovered candidate that passes the harness is included, not sampled as a top-k list.

## Followed Sources Checked

| Source | Status | Notes |
|---|---|---|
| stanford-svl-behavior | checked | Used for BEHAVIOR-1K, SceneFun3D, PhysDreamer, WorldScore-adjacent Stanford lines. |
| princeton-pvl-infinigen | checked | Used for Infinigen Indoors and procedural generation branch. |
| ai2-embodied-prior | checked | Used for Holodeck embodied environment generation. |
| nvidia-cosmos-isaac | checked | Used for SAGE, GR00T N1, SpaceTools, and physical AI follow-up search. |
| cmu-genesis-robogen | checked | Used for RoboGen agentic PCG. |
| stanford-iris-openvla | checked | Used for OpenVLA line. |
| berkeley-rail-levine | checked | Used for Octo/OpenVLA robot policy baselines. |
| physical-intelligence | checked | Used for pi0 high-quality robot demo evidence. |
| ut-austin-rpl-yuke | spot_checked | Used for RoboVerse infrastructure evidence. |
| mit-csail-drake-scene-generation | checked | Used for SceneSmith simulation-ready indoor scene generation. |
| tencent-hunyuan-world | checked | Used for HY-World 2.0 open world generation line. |
| world-model-benchmarks | checked | Used for embodied/world-model evaluation infrastructure. |

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
| PhysX-Anything: Simulation-Ready Physical 3D Assets from Single Image | A | https://arxiv.org/abs/2511.13648 | ../../../paper_reads/A_executable_world_representation/physx-anything-2025.md | strong | addition |
| SimuScene: Simulation-Ready Compositional 3D Scene Reconstruction from a Single Image | A | https://arxiv.org/abs/2606.03994 | ../../../paper_reads/A_executable_world_representation/simuscene-2026.md | adequate | addition |
| REST3D: Reconstructing Physically Stable 3D Scenes from a Single Image | A | https://arxiv.org/abs/2605.30338 | ../../../paper_reads/A_executable_world_representation/rest3d-2026.md | strong | addition |
| TriSplat: Simulation-Ready Feed-Forward 3D Scene Reconstruction | A | https://arxiv.org/abs/2605.26115 | ../../../paper_reads/A_executable_world_representation/trisplat-2026.md | adequate | addition |
| Steerable Scene Generation | B | https://arxiv.org/abs/2505.04831 | ../../../paper_reads/B_interactive_generation_pcg/steerable-scene-generation-2025.md | adequate | update |
| SAGE: Scalable Agentic 3D Scene Generation for Embodied AI | B | https://arxiv.org/abs/2602.10116 | ../../../paper_reads/B_interactive_generation_pcg/sage-2026.md | strong | update |
| EmbodiedGen: Towards a Generative 3D World Engine for Embodied Intelligence | B | https://arxiv.org/abs/2506.10600 | ../../../paper_reads/B_interactive_generation_pcg/embodiedgen-2025.md | adequate | update |
| SceneSmith: Agentic Generation of Simulation-Ready Indoor Scenes | B | https://arxiv.org/abs/2602.09153 | ../../../paper_reads/B_interactive_generation_pcg/scenesmith-2026.md | strong | addition |
| SceneFoundry: Generating Interactive Infinite 3D Worlds | B | https://arxiv.org/abs/2601.05810 | ../../../paper_reads/B_interactive_generation_pcg/scenefoundry-2026.md | adequate | addition |
| HY-World 2.0: A Multi-Modal World Model for Reconstructing, Generating, and Simulating 3D Worlds | B | https://arxiv.org/abs/2604.14268 | ../../../paper_reads/B_interactive_generation_pcg/hy-world-2-2026.md | strong | addition |
| SpatialBot: Precise Spatial Understanding with Vision Language Models | C | https://arxiv.org/abs/2406.13642 | ../../../paper_reads/C_spatial_intelligence/spatialbot-2024.md | not_applicable | update |
| HiSpatial: Taming Hierarchical 3D Spatial Understanding in Vision-Language Models | C | https://microsoft.github.io/HiSpatial/ | ../../../paper_reads/C_spatial_intelligence/hispatial-2026.md | not_applicable | update |
| SpaceTools: Tool-Augmented Spatial Reasoning via Double Interactive RL | C | https://spacetools.github.io/ | ../../../paper_reads/C_spatial_intelligence/spacetools-2026.md | not_applicable | update |
| Spatial Reasoning with Vision-Language Models in Ego-Centric Multi-View Scenes | C | https://arxiv.org/abs/2509.06266 | ../../../paper_reads/C_spatial_intelligence/ego3d-bench-2025.md | not_applicable | update |
| Seeing Across Views / MV-RoboBench | C | https://openreview.net/pdf?id=jXDZJAfRZB | ../../../paper_reads/C_spatial_intelligence/mv-robobench-2026.md | not_applicable | update |
| DepthVLA: Enhancing Vision-Language-Action Models with Depth-Aware Spatial Reasoning | C | https://arxiv.org/abs/2510.13375 | ../../../paper_reads/C_spatial_intelligence/depthvla-2025.md | adequate | update |
| ST-VLA: Enabling 4D-Aware Spatiotemporal Understanding for General Robot Manipulation | C | https://arxiv.org/abs/2603.13788 | ../../../paper_reads/C_spatial_intelligence/st-vla-2026.md | adequate | update |
| SpatialStack: Layered Geometry-Language Fusion for 3D VLM Spatial Reasoning | C | https://arxiv.org/abs/2603.27437 | ../../../paper_reads/C_spatial_intelligence/spatialstack-2026.md | not_applicable | addition |
| VLA-R1: Enhancing Reasoning in Vision-Language-Action Models | D | https://arxiv.org/abs/2510.01623 | ../../../paper_reads/D_vla_world_action_models/vla-r1-2025.md | adequate | update |
| World Action Models: The Next Frontier in Embodied AI | D | https://arxiv.org/abs/2605.12090 | ../../../paper_reads/D_vla_world_action_models/world-action-models-2026.md | not_applicable | update |
| Physically Viable World Models | D | https://arxiv.org/abs/2605.30542 | ../../../paper_reads/D_vla_world_action_models/physically-viable-world-models-2026.md | not_applicable | update |
| GR00T N1: An Open Foundation Model for Generalist Humanoid Robots | D | https://arxiv.org/abs/2503.14734 | ../../../paper_reads/D_vla_world_action_models/gr00t-n1-2025.md | strong | addition |
| Green-VLA: Staged Vision-Language-Action Model for Generalist Robots | D | https://arxiv.org/abs/2602.00919 | ../../../paper_reads/D_vla_world_action_models/green-vla-2026.md | adequate | addition |
| XR-1: Towards Versatile Vision-Language-Action Models via Learning Unified Vision-Motion Representations | D | https://arxiv.org/abs/2511.02776 | ../../../paper_reads/D_vla_world_action_models/xr-1-2025.md | strong | addition |
| TwinVLA: Data-Efficient Bimanual Manipulation with Twin Single-Arm Vision-Language-Action Models | D | https://arxiv.org/abs/2511.05275 | ../../../paper_reads/D_vla_world_action_models/twinvla-2025.md | strong | addition |
| MMaDA-VLA: Large Diffusion Vision-Language-Action Model with Unified Multi-Modal Instruction and Generation | D | https://arxiv.org/abs/2603.25406 | ../../../paper_reads/D_vla_world_action_models/mmada-vla-2026.md | adequate | addition |
| EWMBench: Evaluating Embodied World Models | E | https://arxiv.org/abs/2505.09694 | ../../../paper_reads/E_evaluation_data_infrastructure/ewmbench-2025.md | not_applicable | update |
| WorldScore: A Unified Evaluation Benchmark for World Generation | E | https://arxiv.org/abs/2504.00983 | ../../../paper_reads/E_evaluation_data_infrastructure/worldscore-2025.md | not_applicable | update |
| WorldArena: A Unified Benchmark for Evaluating Perception and Functional Utility of Embodied World Models | E | https://arxiv.org/abs/2602.08971 | ../../../paper_reads/E_evaluation_data_infrastructure/worldarena-2026.md | not_applicable | addition |
| World-in-World: World Models in a Closed-Loop World | E | https://arxiv.org/abs/2510.18135 | ../../../paper_reads/E_evaluation_data_infrastructure/world-in-world-2025.md | not_applicable | addition |
| Ctrl-World | E | https://ctrl-world.github.io/ | ../../../paper_reads/E_evaluation_data_infrastructure/ctrl-world-2026.md | not_applicable | addition |

## Collection Notes

- This run intentionally expands coverage breadth after filtering; it does not select only one or two papers per branch.
- SceneSmith, SAGE, HY-World 2.0, PhysX-Anything, PhysX-Omni, pi0, XR-1, and WorldArena are the strongest demo/evidence anchors.
- Benchmarks and spatial reasoning models are retained because they define validators and evaluation targets for generated interactive worlds.

## Validation

- Run validation passed via `python3 scripts/validate_run.py 2026-06-06`.
- Registry validation passed via `python3 scripts/validate_registry.py`.
- Full validation passed via `REQUIRE_UNDECIDED_DOSSIERS=1 python3 scripts/validate_all.py`.
- Undecided candidates: none accepted; local-only undecided dossiers remain excluded from publish by script.
