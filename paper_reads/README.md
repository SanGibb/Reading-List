# Paper Reading Reports

This directory is the maintained deep-dive library for accepted papers.

Each report is updated across runs and linked from `data/papers.seed.json` through `deep_dive_path`. Run folders under `reports/runs/` keep audit artifacts only; final paper analyses live here.

## Branches

| Branch | Directory | Focus | Count |
|---|---|---|---|
| A | `A_executable_world_representation/` | executable world structures, object parts, affordances, task predicates, and physical/deformable state | 9 |
| B | `B_interactive_generation_pcg/` | interactive assets, scenes, tasks, worlds, and PCG-style simulation data | 10 |
| C | `C_spatial_intelligence/` | 3D reasoning, multi-view understanding, spatial VLMs, and spatial representations for action | 11 |
| D | `D_vla_world_action_models/` | vision-language-action models, robot foundation policies, and action-conditioned world models | 12 |
| E | `E_evaluation_data_infrastructure/` | embodied/world benchmarks, robot data infrastructure, evaluation protocols, and reproducibility | 8 |

## Current Reports

| Paper | Branch | Report |
|---|---|---|
| SceneFun3D: Fine-Grained Functionality and Affordance Understanding in 3D Scenes | A | [scenefun3d-2024.md](A_executable_world_representation/scenefun3d-2024.md) |
| BEHAVIOR-1K: A Human-Centered, Embodied AI Benchmark with 1,000 Everyday Activities and Realistic Simulation | A | [behavior-1k-2024.md](A_executable_world_representation/behavior-1k-2024.md) |
| PhysX-Omni: Unified Simulation-Ready Physical 3D Generation for Rigid, Deformable, and Articulated Objects | A | [physx-omni-2026.md](A_executable_world_representation/physx-omni-2026.md) |
| PhysDreamer: Physics-Based Interaction with 3D Objects via Video Generation | A | [physdreamer-2024.md](A_executable_world_representation/physdreamer-2024.md) |
| Feature Splatting: Language-Driven Physics-Based Scene Synthesis and Editing | A | [feature-splatting-2024.md](A_executable_world_representation/feature-splatting-2024.md) |
| PhysX-Anything: Simulation-Ready Physical 3D Assets from Single Image | A | [physx-anything-2025.md](A_executable_world_representation/physx-anything-2025.md) |
| SimuScene: Simulation-Ready Compositional 3D Scene Reconstruction from a Single Image | A | [simuscene-2026.md](A_executable_world_representation/simuscene-2026.md) |
| REST3D: Reconstructing Physically Stable 3D Scenes from a Single Image | A | [rest3d-2026.md](A_executable_world_representation/rest3d-2026.md) |
| TriSplat: Simulation-Ready Feed-Forward 3D Scene Reconstruction | A | [trisplat-2026.md](A_executable_world_representation/trisplat-2026.md) |
| PhyScene: Physically Interactable 3D Scene Synthesis for Embodied AI | B | [physcene-2024.md](B_interactive_generation_pcg/physcene-2024.md) |
| RoboGen: Towards Unleashing Infinite Data for Automated Robot Learning via Generative Simulation | B | [robogen-2024.md](B_interactive_generation_pcg/robogen-2024.md) |
| Steerable Scene Generation | B | [steerable-scene-generation-2025.md](B_interactive_generation_pcg/steerable-scene-generation-2025.md) |
| SAGE: Scalable Agentic 3D Scene Generation for Embodied AI | B | [sage-2026.md](B_interactive_generation_pcg/sage-2026.md) |
| EmbodiedGen: Towards a Generative 3D World Engine for Embodied Intelligence | B | [embodiedgen-2025.md](B_interactive_generation_pcg/embodiedgen-2025.md) |
| Holodeck: Language Guided Generation of 3D Embodied AI Environments | B | [holodeck-2024.md](B_interactive_generation_pcg/holodeck-2024.md) |
| Infinigen Indoors: Photorealistic Indoor Scenes using Procedural Generation | B | [infinigen-indoors-2024.md](B_interactive_generation_pcg/infinigen-indoors-2024.md) |
| SceneSmith: Agentic Generation of Simulation-Ready Indoor Scenes | B | [scenesmith-2026.md](B_interactive_generation_pcg/scenesmith-2026.md) |
| SceneFoundry: Generating Interactive Infinite 3D Worlds | B | [scenefoundry-2026.md](B_interactive_generation_pcg/scenefoundry-2026.md) |
| HY-World 2.0: A Multi-Modal World Model for Reconstructing, Generating, and Simulating 3D Worlds | B | [hy-world-2-2026.md](B_interactive_generation_pcg/hy-world-2-2026.md) |
| SpatialBot: Precise Spatial Understanding with Vision Language Models | C | [spatialbot-2024.md](C_spatial_intelligence/spatialbot-2024.md) |
| HiSpatial: Taming Hierarchical 3D Spatial Understanding in Vision-Language Models | C | [hispatial-2026.md](C_spatial_intelligence/hispatial-2026.md) |
| SpaceTools: Tool-Augmented Spatial Reasoning via Double Interactive RL | C | [spacetools-2026.md](C_spatial_intelligence/spacetools-2026.md) |
| Spatial Reasoning with Vision-Language Models in Ego-Centric Multi-View Scenes | C | [ego3d-bench-2025.md](C_spatial_intelligence/ego3d-bench-2025.md) |
| Seeing Across Views / MV-RoboBench | C | [mv-robobench-2026.md](C_spatial_intelligence/mv-robobench-2026.md) |
| SpatialVLA: Exploring Spatial Representations for Visual-Language-Action Models | C | [spatialvla-2025.md](C_spatial_intelligence/spatialvla-2025.md) |
| DepthVLA: Enhancing Vision-Language-Action Models with Depth-Aware Spatial Reasoning | C | [depthvla-2025.md](C_spatial_intelligence/depthvla-2025.md) |
| ST-VLA: Enabling 4D-Aware Spatiotemporal Understanding for General Robot Manipulation | C | [st-vla-2026.md](C_spatial_intelligence/st-vla-2026.md) |
| SpatialStack: Layered Geometry-Language Fusion for 3D VLM Spatial Reasoning | C | [spatialstack-2026.md](C_spatial_intelligence/spatialstack-2026.md) |
| Embodied3DBench: Benchmarking Low-Level Embodied Spatial Intelligence of Vision Language Models | C | [embodied3dbench-2026.md](C_spatial_intelligence/embodied3dbench-2026.md) |
| ESPIRE: A Diagnostic Benchmark for Embodied Spatial Reasoning of Vision-Language Models | C | [espire-2026.md](C_spatial_intelligence/espire-2026.md) |
| Octo: An Open-Source Generalist Robot Policy | D | [octo-2024.md](D_vla_world_action_models/octo-2024.md) |
| OpenVLA: An Open-Source Vision-Language-Action Model | D | [openvla-2024.md](D_vla_world_action_models/openvla-2024.md) |
| pi0: A Vision-Language-Action Flow Model for General Robot Control | D | [pi0-2024.md](D_vla_world_action_models/pi0-2024.md) |
| VLA-R1: Enhancing Reasoning in Vision-Language-Action Models | D | [vla-r1-2025.md](D_vla_world_action_models/vla-r1-2025.md) |
| World Action Models: The Next Frontier in Embodied AI | D | [world-action-models-2026.md](D_vla_world_action_models/world-action-models-2026.md) |
| Physically Viable World Models | D | [physically-viable-world-models-2026.md](D_vla_world_action_models/physically-viable-world-models-2026.md) |
| GR00T N1: An Open Foundation Model for Generalist Humanoid Robots | D | [gr00t-n1-2025.md](D_vla_world_action_models/gr00t-n1-2025.md) |
| Green-VLA: Staged Vision-Language-Action Model for Generalist Robots | D | [green-vla-2026.md](D_vla_world_action_models/green-vla-2026.md) |
| XR-1: Towards Versatile Vision-Language-Action Models via Learning Unified Vision-Motion Representations | D | [xr-1-2025.md](D_vla_world_action_models/xr-1-2025.md) |
| TwinVLA: Data-Efficient Bimanual Manipulation with Twin Single-Arm Vision-Language-Action Models | D | [twinvla-2025.md](D_vla_world_action_models/twinvla-2025.md) |
| MMaDA-VLA: Large Diffusion Vision-Language-Action Model with Unified Multi-Modal Instruction and Generation | D | [mmada-vla-2026.md](D_vla_world_action_models/mmada-vla-2026.md) |
| MolmoAct2: Action Reasoning Models for Real-world Deployment | D | [molmoact2-2026.md](D_vla_world_action_models/molmoact2-2026.md) |
| EWMBench: Evaluating Embodied World Models | E | [ewmbench-2025.md](E_evaluation_data_infrastructure/ewmbench-2025.md) |
| WorldScore: A Unified Evaluation Benchmark for World Generation | E | [worldscore-2025.md](E_evaluation_data_infrastructure/worldscore-2025.md) |
| RoboVerse: Towards a Unified Platform, Dataset and Benchmark for Scalable and Generalizable Robot Learning | E | [roboverse-2025.md](E_evaluation_data_infrastructure/roboverse-2025.md) |
| OpenEQA: Embodied Question Answering in the Era of Foundation Models | E | [openeqa-2024.md](E_evaluation_data_infrastructure/openeqa-2024.md) |
| WorldArena: A Unified Benchmark for Evaluating Perception and Functional Utility of Embodied World Models | E | [worldarena-2026.md](E_evaluation_data_infrastructure/worldarena-2026.md) |
| World-in-World: World Models in a Closed-Loop World | E | [world-in-world-2025.md](E_evaluation_data_infrastructure/world-in-world-2025.md) |
| Ctrl-World | E | [ctrl-world-2026.md](E_evaluation_data_infrastructure/ctrl-world-2026.md) |
| WorldArena 2.0: Extending Embodied World Model Benchmarking on Modality, Functionality and Platform | E | [worldarena-2-2026.md](E_evaluation_data_infrastructure/worldarena-2-2026.md) |
