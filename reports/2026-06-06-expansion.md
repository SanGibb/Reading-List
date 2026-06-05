# Frontier Knowledge Expansion Summary - 2026-06-06

This run initializes and expands the maintained reading-list knowledge base with **46 accepted papers**. The acceptance policy is: discover broadly, filter by the harness, then include **all** qualifying candidates with a deep-dive report. It is not a weekly report and not a top-k paper sampler.

## Accepted Papers by Branch

### A. Executable World Representation (9)

| Paper | Year | Why it matters | Deep dive |
|---|---:|---|---|
| SceneFun3D: Fine-Grained Functionality and Affordance Understanding in 3D Scenes | 2024 | Defines reusable fields Object, Part, Affordance, FunctionalElement, TaskLanguage, MotionParameter for our typed interactive-world representation. | [scenefun3d-2024.md](../paper_reads/A_executable_world_representation/scenefun3d-2024.md) |
| BEHAVIOR-1K: A Human-Centered, Embodied AI Benchmark with 1,000 Everyday Activities and Realistic Simulation | 2024 | Directly informs Task, StatePredicate, GoalCondition, SceneObject, PhysicalProperty, and validation protocol design. | [behavior-1k-2024.md](../paper_reads/A_executable_world_representation/behavior-1k-2024.md) |
| PhysX-Omni: Unified Simulation-Ready Physical 3D Generation for Rigid, Deformable, and Articulated Objects | 2026 | Strong candidate for PhysicalProperty, Material, DeformableState, KinematicJoint, and simulator export fields. | [physx-omni-2026.md](../paper_reads/A_executable_world_representation/physx-omni-2026.md) |
| PhysDreamer: Physics-Based Interaction with 3D Objects via Video Generation | 2024 | Provides concrete fields for MaterialField, ExternalForce, DynamicResponse, and DeformableState validators. | [physdreamer-2024.md](../paper_reads/A_executable_world_representation/physdreamer-2024.md) |
| Feature Splatting: Language-Driven Physics-Based Scene Synthesis and Editing | 2024 | Useful for SceneRepresentation, MaterialProperty, SegmentByText, PhysicsEdit, and simulator-backed validation. | [feature-splatting-2024.md](../paper_reads/A_executable_world_representation/feature-splatting-2024.md) |
| PhysX-Anything: Simulation-Ready Physical 3D Assets from Single Image | 2025 | Strong object-level source for PhysicalProperty, KinematicJoint, AssetToSimulator, and contact-rich policy-learning validation. | [physx-anything-2025.md](../paper_reads/A_executable_world_representation/physx-anything-2025.md) |
| SimuScene: Simulation-Ready Compositional 3D Scene Reconstruction from a Single Image | 2026 | Relevant to SceneTree, SupportRelation, PhysicalViolation, and simulator-ready reconstruction validators. | [simuscene-2026.md](../paper_reads/A_executable_world_representation/simuscene-2026.md) |
| REST3D: Reconstructing Physically Stable 3D Scenes from a Single Image | 2026 | Provides a useful template for SceneTree, SupportGraph, StabilityCheck, and PhysicsRefinement stages. | [rest3d-2026.md](../paper_reads/A_executable_world_representation/rest3d-2026.md) |
| TriSplat: Simulation-Ready Feed-Forward 3D Scene Reconstruction | 2026 | Useful representation reference for MeshScene, CollisionSurface, and feed-forward sim-ready reconstruction. | [trisplat-2026.md](../paper_reads/A_executable_world_representation/trisplat-2026.md) |

### B. Interactive Generation and PCG (10)

| Paper | Year | Why it matters | Deep dive |
|---|---:|---|---|
| PhyScene: Physically Interactable 3D Scene Synthesis for Embodied AI | 2024 | Baseline for InteractionConstraint, Reachability, Collision, Articulation, and GeneratedScene validity metrics. | [physcene-2024.md](../paper_reads/B_interactive_generation_pcg/physcene-2024.md) |
| RoboGen: Towards Unleashing Infinite Data for Automated Robot Learning via Generative Simulation | 2024 | Directly motivates TaskGenerator, SceneGenerator, SupervisionGenerator, PolicyLearner, and validation-loop abstractions. | [robogen-2024.md](../paper_reads/B_interactive_generation_pcg/robogen-2024.md) |
| Steerable Scene Generation | 2025 | strong baseline for task-constrained scene generation | [steerable-scene-generation-2025.md](../paper_reads/B_interactive_generation_pcg/steerable-scene-generation-2025.md) |
| SAGE: Scalable Agentic 3D Scene Generation for Embodied AI | 2026 | closest PCG baseline; it can use a typed interaction representation as I/O and evaluator | [sage-2026.md](../paper_reads/B_interactive_generation_pcg/sage-2026.md) |
| EmbodiedGen: Towards a Generative 3D World Engine for Embodied Intelligence | 2025 | generation engine that can consume or be evaluated by a typed interactive-world representation | [embodiedgen-2025.md](../paper_reads/B_interactive_generation_pcg/embodiedgen-2025.md) |
| Holodeck: Language Guided Generation of 3D Embodied AI Environments | 2024 | Important baseline for Prompt, SceneSpec, SpatialConstraint, AssetRetrieval, LayoutOptimization, and downstream embodied evaluation. | [holodeck-2024.md](../paper_reads/B_interactive_generation_pcg/holodeck-2024.md) |
| Infinigen Indoors: Photorealistic Indoor Scenes using Procedural Generation | 2024 | Strong generator for Scene, Asset, Annotation, LayoutConstraint, and synthetic data pipelines. | [infinigen-indoors-2024.md](../paper_reads/B_interactive_generation_pcg/infinigen-indoors-2024.md) |
| SceneSmith: Agentic Generation of Simulation-Ready Indoor Scenes | 2026 | Top PCG baseline for PromptToScene, CriticLoop, ObjectPopulation, PhysicalProperty, and policy evaluation. | [scenesmith-2026.md](../paper_reads/B_interactive_generation_pcg/scenesmith-2026.md) |
| SceneFoundry: Generating Interactive Infinite 3D Worlds | 2026 | Relevant PCG line for LayoutConstraint, ArticulationConstraint, WalkableSpace, and infinite-world expansion. | [scenefoundry-2026.md](../paper_reads/B_interactive_generation_pcg/scenefoundry-2026.md) |
| HY-World 2.0: A Multi-Modal World Model for Reconstructing, Generating, and Simulating 3D Worlds | 2026 | Strong open-source world-generation baseline for WorldRepresentation, TrajectoryPlan, 3DGSScene, MeshExport, and engine integration. | [hy-world-2-2026.md](../paper_reads/B_interactive_generation_pcg/hy-world-2-2026.md) |

### C. Spatial Intelligence (9)

| Paper | Year | Why it matters | Deep dive |
|---|---:|---|---|
| SpatialBot: Precise Spatial Understanding with Vision Language Models | 2024 | supports grounding spatial relations from observations | [spatialbot-2024.md](../paper_reads/C_spatial_intelligence/spatialbot-2024.md) |
| HiSpatial: Taming Hierarchical 3D Spatial Understanding in Vision-Language Models | 2026 | useful for spatial relation completion and validation | [hispatial-2026.md](../paper_reads/C_spatial_intelligence/hispatial-2026.md) |
| SpaceTools: Tool-Augmented Spatial Reasoning via Double Interactive RL | 2026 | prototype for target-task validators that invoke measurement/simulation tools | [spacetools-2026.md](../paper_reads/C_spatial_intelligence/spacetools-2026.md) |
| Spatial Reasoning with Vision-Language Models in Ego-Centric Multi-View Scenes | 2025 | supports Scene coordinate-frame and relation grounding | [ego3d-bench-2025.md](../paper_reads/C_spatial_intelligence/ego3d-bench-2025.md) |
| Seeing Across Views / MV-RoboBench | 2026 | important benchmark for observation-to-scene-graph parsing | [mv-robobench-2026.md](../paper_reads/C_spatial_intelligence/mv-robobench-2026.md) |
| SpatialVLA: Exploring Spatial Representations for Visual-Language-Action Models | 2025 | Useful for Scene.spatial_graph, Ego3DEncoding, SpatialActionToken, and spatial instruction validation. | [spatialvla-2025.md](../paper_reads/C_spatial_intelligence/spatialvla-2025.md) |
| DepthVLA: Enhancing Vision-Language-Action Models with Depth-Aware Spatial Reasoning | 2025 | supports depth-based scene grounding and precise spatial action | [depthvla-2025.md](../paper_reads/C_spatial_intelligence/depthvla-2025.md) |
| ST-VLA: Enabling 4D-Aware Spatiotemporal Understanding for General Robot Manipulation | 2026 | points to temporal/deformable state and trajectory grounding | [st-vla-2026.md](../paper_reads/C_spatial_intelligence/st-vla-2026.md) |
| SpatialStack: Layered Geometry-Language Fusion for 3D VLM Spatial Reasoning | 2026 | Good spatial encoder/validator reference for local geometry, global context, and relation checking in generated worlds. | [spatialstack-2026.md](../paper_reads/C_spatial_intelligence/spatialstack-2026.md) |

### D. VLA and World-Action Models (11)

| Paper | Year | Why it matters | Deep dive |
|---|---:|---|---|
| Octo: An Open-Source Generalist Robot Policy | 2024 | Baseline for Policy, Observation, ActionDistribution, GoalImageCondition, and embodiment adaptation. | [octo-2024.md](../paper_reads/D_vla_world_action_models/octo-2024.md) |
| OpenVLA: An Open-Source Vision-Language-Action Model | 2024 | Baseline for VLA policy execution, generated-task transfer, action-token interface, and finetuning experiments. | [openvla-2024.md](../paper_reads/D_vla_world_action_models/openvla-2024.md) |
| pi0: A Vision-Language-Action Flow Model for General Robot Control | 2024 | Sets a high demo-quality target for robot execution, deformable manipulation, long-horizon interaction, and continuous action generation. | [pi0-2024.md](../paper_reads/D_vla_world_action_models/pi0-2024.md) |
| VLA-R1: Enhancing Reasoning in Vision-Language-Action Models | 2025 | bridges target-task predicates and action selection | [vla-r1-2025.md](../paper_reads/D_vla_world_action_models/vla-r1-2025.md) |
| World Action Models: The Next Frontier in Embodied AI | 2026 | aligns directly with target-task StateTransition and ValidationReport | [world-action-models-2026.md](../paper_reads/D_vla_world_action_models/world-action-models-2026.md) |
| Physically Viable World Models | 2026 | supports the target representation as a query-conditioned physical interface | [physically-viable-world-models-2026.md](../paper_reads/D_vla_world_action_models/physically-viable-world-models-2026.md) |
| GR00T N1: An Open Foundation Model for Generalist Humanoid Robots | 2025 | Important VLA baseline for humanoid embodiments and synthetic-data-to-policy evaluation. | [gr00t-n1-2025.md](../paper_reads/D_vla_world_action_models/gr00t-n1-2025.md) |
| Green-VLA: Staged Vision-Language-Action Model for Generalist Robots | 2026 | Useful systems reference for staged VLA training and safety-aware execution. | [green-vla-2026.md](../paper_reads/D_vla_world_action_models/green-vla-2026.md) |
| XR-1: Towards Versatile Vision-Language-Action Models via Learning Unified Vision-Motion Representations | 2025 | Strong VLA reference for cross-embodiment action representation and real rollout quality. | [xr-1-2025.md](../paper_reads/D_vla_world_action_models/xr-1-2025.md) |
| TwinVLA: Data-Efficient Bimanual Manipulation with Twin Single-Arm Vision-Language-Action Models | 2025 | Good baseline for bimanual task generation and policy-evaluation suites. | [twinvla-2025.md](../paper_reads/D_vla_world_action_models/twinvla-2025.md) |
| MMaDA-VLA: Large Diffusion Vision-Language-Action Model with Unified Multi-Modal Instruction and Generation | 2026 | Relevant to world-action interfaces because it predicts future visual outcomes and actions jointly. | [mmada-vla-2026.md](../paper_reads/D_vla_world_action_models/mmada-vla-2026.md) |

### E. Evaluation and Data Infrastructure (7)

| Paper | Year | Why it matters | Deep dive |
|---|---:|---|---|
| EWMBench: Evaluating Embodied World Models | 2025 | evaluation philosophy for interactive embodied generation benchmark | [ewmbench-2025.md](../paper_reads/E_evaluation_data_infrastructure/ewmbench-2025.md) |
| WorldScore: A Unified Evaluation Benchmark for World Generation | 2025 | baseline for interactive embodied generation benchmark metrics | [worldscore-2025.md](../paper_reads/E_evaluation_data_infrastructure/worldscore-2025.md) |
| RoboVerse: Towards a Unified Platform, Dataset and Benchmark for Scalable and Generalizable Robot Learning | 2025 | Useful for benchmark packaging, generated-task evaluation, policy baselines, and trajectory/data schema design. | [roboverse-2025.md](../paper_reads/E_evaluation_data_infrastructure/roboverse-2025.md) |
| OpenEQA: Embodied Question Answering in the Era of Foundation Models | 2024 | downstream benchmark for testing whether generated interactive environments preserve object identity, spatial relations, and semantic affordances | [openeqa-2024.md](../paper_reads/E_evaluation_data_infrastructure/openeqa-2024.md) |
| WorldArena: A Unified Benchmark for Evaluating Perception and Functional Utility of Embodied World Models | 2026 | Important evaluation target for our interactive embodied world generator and world-model branches. | [worldarena-2026.md](../paper_reads/E_evaluation_data_infrastructure/worldarena-2026.md) |
| World-in-World: World Models in a Closed-Loop World | 2025 | Provides a harness template for action-conditioned rollout evaluation and closed-loop generated-world testing. | [world-in-world-2025.md](../paper_reads/E_evaluation_data_infrastructure/world-in-world-2025.md) |
| Ctrl-World | 2026 | Useful benchmark design for world-action model validators and imagined rollout tests. | [ctrl-world-2026.md](../paper_reads/E_evaluation_data_infrastructure/ctrl-world-2026.md) |

## Strongest Demo / Evidence Anchors

1. SceneSmith, SAGE, PhyScene, Infinigen Indoors, HY-World 2.0: interactive/PCG world generation.
2. PhysX-Omni, PhysX-Anything, REST3D, SimuScene: simulation-ready physical assets/scenes and stability constraints.
3. pi0, OpenVLA, Octo, GR00T N1, XR-1, TwinVLA: robot policy and VLA execution baselines.
4. WorldArena, World-in-World, Ctrl-World, WorldScore: world-model and world-generation evaluation harnesses.

## Validation

- Run validation passed via `python3 scripts/validate_run.py 2026-06-06`.
- Registry validation passed via `python3 scripts/validate_registry.py`.
- Full validation passed via `REQUIRE_UNDECIDED_DOSSIERS=1 python3 scripts/validate_all.py`.
- `undecided/**` remains local-only and is not part of automatic publish.
