# Frontier Knowledge Expansion Summary

Date: 2026-06-06

## Summary

This initialization run expands the repository from a mostly JSON seed list into a usable reading knowledge base. It adds 5 missing key papers to the registry and writes or updates 15 deep-dive reports under `paper_reads/`.

## Accepted Papers

| Paper | Branch | Deep dive | Action |
|---|---|---|---|
| SceneFun3D: Fine-Grained Functionality and Affordance Understanding in 3D Scenes | A | ../paper_reads/A_executable_world_representation/scenefun3d-2024.md | update |
| BEHAVIOR-1K: A Human-Centered, Embodied AI Benchmark with 1,000 Everyday Activities and Realistic Simulation | A | ../paper_reads/A_executable_world_representation/behavior-1k-2024.md | update |
| PhysX-Omni: Unified Simulation-Ready Physical 3D Generation for Rigid, Deformable, and Articulated Objects | A | ../paper_reads/A_executable_world_representation/physx-omni-2026.md | update |
| PhysDreamer: Physics-Based Interaction with 3D Objects via Video Generation | A | ../paper_reads/A_executable_world_representation/physdreamer-2024.md | addition |
| Feature Splatting: Language-Driven Physics-Based Scene Synthesis and Editing | A | ../paper_reads/A_executable_world_representation/feature-splatting-2024.md | addition |
| PhyScene: Physically Interactable 3D Scene Synthesis for Embodied AI | B | ../paper_reads/B_interactive_generation_pcg/physcene-2024.md | update |
| Holodeck: Language Guided Generation of 3D Embodied AI Environments | B | ../paper_reads/B_interactive_generation_pcg/holodeck-2024.md | addition |
| Infinigen Indoors: Photorealistic Indoor Scenes using Procedural Generation | B | ../paper_reads/B_interactive_generation_pcg/infinigen-indoors-2024.md | addition |
| RoboGen: Towards Unleashing Infinite Data for Automated Robot Learning via Generative Simulation | B | ../paper_reads/B_interactive_generation_pcg/robogen-2024.md | update |
| SpatialVLA: Exploring Spatial Representations for Visual-Language-Action Models | C | ../paper_reads/C_spatial_intelligence/spatialvla-2025.md | update |
| Octo: An Open-Source Generalist Robot Policy | D | ../paper_reads/D_vla_world_action_models/octo-2024.md | update |
| OpenVLA: An Open-Source Vision-Language-Action Model | D | ../paper_reads/D_vla_world_action_models/openvla-2024.md | update |
| pi0: A Vision-Language-Action Flow Model for General Robot Control | D | ../paper_reads/D_vla_world_action_models/pi0-2024.md | update |
| RoboVerse: Towards a Unified Platform, Dataset and Benchmark for Scalable and Generalizable Robot Learning | E | ../paper_reads/E_evaluation_data_infrastructure/roboverse-2025.md | update |
| OpenEQA: Embodied Question Answering in the Era of Foundation Models | E | ../paper_reads/E_evaluation_data_infrastructure/openeqa-2024.md | addition |

## New Registry Additions

- PhysDreamer: physics-based interaction with 3D objects via video-generation priors.
- Feature Splatting: language-driven physical scene synthesis/editing over 3D Gaussians.
- Holodeck: language-guided 3D embodied environment generation.
- Infinigen Indoors: photorealistic procedural indoor scene generation.
- OpenEQA: embodied question-answering benchmark for environment understanding.

## Upgraded Existing Seed Entries

SceneFun3D, BEHAVIOR-1K, PhysX-Omni, PhyScene, RoboGen, SpatialVLA, Octo, OpenVLA, pi0, and RoboVerse now have maintained deep-dive reports.

## Undecided

None for this run. The old local dry-run SmolVLA dossier remains ignored under `undecided/` and was not published.

## Validation

- Run validation: passed via `python3 scripts/validate_run.py 2026-06-06`.
- Registry validation: passed via `python3 scripts/validate_registry.py`.
