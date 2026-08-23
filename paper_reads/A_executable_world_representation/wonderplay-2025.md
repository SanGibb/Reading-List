# WonderPlay: Dynamic 3D Scene Generation from a Single Image and Actions

candidate_id: CAND-0003
branch: A
decision: accepted_for_registry

## Source Links

- Paper: https://arxiv.org/abs/2505.18151
- Proceedings: https://www.openaccess.thecvf.com/content/ICCV2025/html/Li_WonderPlay_Dynamic_3D_Scene_Generation_from_a_Single_Image_and_ICCV_2025_paper.html
- Project / demos: https://kyleleey.github.io/WonderPlay/

## TL;DR

WonderPlay reconstructs a dynamic 3D scene from one image, simulates coarse action consequences with material-specific solvers, and uses a video generator plus differentiable rendering to refine appearance and motion. It is unusually relevant for executable multi-material worlds, but generated realism must not be mistaken for physical correctness.

## Novelty

- Hybrid loop joins physics solvers and a video generator.
- Supports rigid, elastic, cloth, smoke, liquid and granular materials.
- Produces action-conditioned dynamic 3D rather than only a rendered video.

## Contributions

1. Object/background Gaussian-surfels representation with dynamic state.
2. Material inference and material-specific coarse simulation.
3. Video-conditioned update of 3D dynamics through differentiable rendering.

## Task

- Input: single RGB image and gravity, wind or point-force controls.
- Output: time-varying 3D scene and rendered action consequences.
- Setting: open-world multi-material dynamics.
- Success criterion: controllable, visually plausible dynamics across material families.

## Data

- Examples: rigid objects, cloth, hair, elastic bodies, smoke, liquid, snow/sand.
- Modalities: RGB, segmentation, geometry, material parameters, force fields and video.
- Evaluation: official qualitative comparisons and paper metrics/user studies.

## Method

- Reconstruct background and dynamic objects as connected Gaussian surfels.
- Classify material and estimate solver parameters.
- Simulate coarse 3D dynamics, condition a video generator, then fit scene state to the video.

## Key Figures / Architecture

figure_status: linked_official

- Figure / demo: action-conditioned material gallery and pipeline.
- Source: https://kyleleey.github.io/WonderPlay/
- What it shows: forces applied to varied materials and resulting dynamic scenes.
- Why it matters: maps explicit action/physics fields to a generative refinement loop.

## Evidence Trail

| Claim | Source | Status | Notes |
|---|---|---|---|
| Six material classes | ICCV paper | verified | Defined in method. |
| Hybrid physics/video loop | paper and project | verified | Architecture and videos agree. |
| Full code availability | project | partial | Confirm complete training/reconstruction release before reproducing. |

## Evidence

- Qualitative results: diverse material/action cases are visually strong.
- Ablations: paper isolates solver/video/refinement roles.
- Baselines: prior rigid/elastic dynamic-scene methods.
- Reproducibility signals: peer-reviewed paper and extensive official demos.

## Limitations

- Material/geometry estimates from one view are uncertain.
- The video prior can hallucinate plausible motion inconsistent with conservation/contact constraints.
- Full public-code coverage needs verification.

## Project Relevance

- Reusable fields: MaterialType, MaterialParameters, ForceField, SolverState and GeneratedObservation.
- Baseline role: hybrid executable/generative world representation.
- Implication: separate explicit simulated state from appearance-refinement confidence.

## Reproduction / Follow-up

- Verify code completeness and run conservation/contact diagnostics.
- Compare 3D state fidelity, not only rendered-video preference.

