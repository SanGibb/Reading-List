# WonderWorld: Interactive 3D Scene Generation from a Single Image

candidate_id: CAND-0002
branch: B
decision: accepted_for_registry

## Source Links

- Paper: https://arxiv.org/abs/2406.09394
- Proceedings: https://openaccess.thecvf.com/content/CVPR2025/html/Yu_WonderWorld_Interactive_3D_Scene_Generation_from_a_Single_Image_CVPR_2025_paper.html
- Project / demo: https://kovenyu.com/wonderworld/
- Code: https://github.com/KovenYu/WonderWorld

## TL;DR

WonderWorld turns a single image into a user-steered, connected 3D world by combining fast layered Gaussian surfels, outpainting and guided depth diffusion. Official galleries are visually strong and latency is interactive, though the representation is not a full physics-ready simulator.

## Novelty

- First low-latency workflow for incrementally expanding connected 3D scenes under online camera/content control.
- FLAGS avoids dense multi-view optimization; guided depth aligns new and existing scene boundaries.

## Contributions

1. Fast Layered Gaussian Surfels for single-view scene construction.
2. Guided depth diffusion for coherent scene extension.
3. Public software, code and diverse interactive demonstrations.

## Task

- Input: one image plus user camera movement and text content controls.
- Output: connected renderable 3D scenes.
- Setting: iterative interactive world prototyping.
- Success criterion: coherent expansion in less than ten seconds per scene.

## Data

- Evaluation: nature, city and campus scenes from generated and real images.
- Modalities: RGB, estimated depth, text prompts and camera controls.
- Protocol: speed, perceptual/geometry comparisons and user-facing examples.

## Method

- Decompose a view into depth layers and generate layer imagery.
- Optimize FLAGS from a geometry-based initialization.
- Outpaint a user-selected direction, estimate partially conditioned depth and attach the new scene.

## Key Figures / Architecture

figure_status: linked_official

- Figure / demo: pipeline and interactive galleries.
- Source: https://kovenyu.com/wonderworld/approach.jpg
- What it shows: initialization and iterative user-controlled expansion.
- Why it matters: exposes the representation/compiler boundary for interactive PCG.

## Evidence Trail

| Claim | Source | Status | Notes |
|---|---|---|---|
| Under ten seconds per scene | CVPR paper | verified | Reported on one A6000. |
| Connected interactive generation | project videos | verified | Multiple official examples inspected. |
| Code/software released | official project | verified | Links resolve. |

## Evidence

- Qualitative results: convincing city, campus and natural-world expansions.
- Baselines: offline single-image 3D world-generation methods.
- Reproducibility signals: proceedings, code, project videos and software.

## Limitations

- Depth seams, geometry distortion and drift may accumulate.
- Visual 3D does not encode articulated objects or physical interaction semantics.
- Some examples are stylized and do not test collision-ready geometry.

## Project Relevance

- Direct interactive-generation baseline for camera/content steering.
- Reusable fields: ScenePatch, CameraControl, ContentPrompt, DepthBoundary and GenerationLatency.
- Useful front end for worlds that later require semantic/physical compilation.

## Reproduction / Follow-up

- Measure boundary drift across long expansion chains.
- Test export quality and collision geometry before simulator use.

