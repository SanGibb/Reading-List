# HY-World 2.0: A Multi-Modal World Model for Reconstructing, Generating, and Simulating 3D Worlds

candidate_id: CAND-0025
branch: B
decision: accepted_for_registry
authors: Tencent Hunyuan / HY-World team
year: 2026
venue: arXiv

## Source Links

- Paper: https://arxiv.org/abs/2604.14268
- Project: https://hyworld.dev/
- Code: https://huggingface.co/tencent/HY-World-2.0
- Data / benchmark: https://hyworld.dev/
- Demo / video: https://hyworld.dev/
- Official figures: https://hyworld.dev/

## TL;DR

HY-World 2.0: A Multi-Modal World Model for Reconstructing, Generating, and Simulating 3D Worlds is included because it addresses **reconstruct, generate, and simulate navigable 3D worlds from multimodal inputs** with a method centered on **four-stage world pipeline with panorama generation, trajectory planning, world expansion, reconstruction, and WorldLens rendering**. For our repository, the important point is not venue alone but that the work gives concrete evidence for interactive assets, scenes, tasks, worlds, and PCG-style simulation data. Main caveat: General world generation is not robotics-specific; physical interaction fidelity must be tested before embodied-policy use.

## Novelty

- What is actually new: unifies generation and reconstruction for explorable 3D worlds with open weights/code.
- Difference from prior work: it adds executable, interactive, physical, spatial, or policy-facing structure rather than stopping at static visual quality.
- Why the delta matters: our target task needs generated or reconstructed worlds that agents can reason about, validate, or act in, so this paper contributes reusable structure rather than only a visual sample gallery.

## Contributions

1. Defines a reconstruct, generate, and simulate navigable 3D worlds from multimodal inputs problem setting that is directly relevant to interactive embodied generation.
2. Introduces the core method: four-stage world pipeline with panorama generation, trajectory planning, world expansion, reconstruction, and WorldLens rendering.
3. Provides evidence through text, single-view, multi-view, and video inputs; generated 3DGS/mesh worlds; released model weights and code and makes the paper useful for our Interactive Generation and PCG branch.

## Task

- Input: paper-specific observations, prompts, scene assets, robot observations, or benchmark inputs described by the original source.
- Output: reconstruct, generate, and simulate navigable 3D worlds from multimodal inputs outputs, represented as generated worlds, executable assets, spatial answers, policy actions, or benchmark scores depending on branch.
- Setting: Interactive Generation and PCG within an interactive embodied generation reading list.
- Success criterion: strong source evidence, branch fit, usable data/method description, and visual/demo quality of `strong` when the work depends on generation or robot execution.

## Data

- Dataset / benchmark: text, single-view, multi-view, and video inputs; generated 3DGS/mesh worlds; released model weights and code.
- Scale: use the scale reported by the source; exact split details should be checked in the paper before citation.
- Modalities: 3D scenes/assets, images/videos, depth/multi-view observations, robot trajectories, actions, or benchmark annotations depending on the paper.
- Collection / annotation: source-specific; this run records only primary-source claims and does not independently audit annotation pipelines.
- Splits / evaluation protocol: follow the paper/project page; local reproduction was not performed.

## Method

- Core pipeline: four-stage world pipeline with panorama generation, trajectory planning, world expansion, reconstruction, and WorldLens rendering.
- Model / representation: the useful abstraction for this repository is the mapping from source input to executable world representation, spatial state, robot action, or evaluation signal.
- Training or optimization: use the paper-specific training, optimization, search, or benchmark construction described by the primary source.
- Inference / deployment: relevant deployment mode is generated-scene inspection, simulator import, robot rollout, spatial VLM evaluation, or world-model benchmark execution.
- Losses or metrics: use reported metrics only as source-attributed evidence until reproduced locally.

## Key Figures / Architecture

figure_status: linked_official

- Figure / demo: official project, paper, or architecture material.
- Source: https://hyworld.dev/
- Render:
  Official figure/demo page: https://hyworld.dev/
- What it shows: the official figure/demo evidence for the method pipeline, generated results, robot execution, or benchmark design.
- Why it matters: it is the visual anchor used by Quality Reviewer; no local reproduction was performed in this initialization run.

## Evidence Trail

| Claim | Source | Status | Notes |
|---|---|---|---|
| Primary source exists and is 2024+. | https://arxiv.org/abs/2604.14268 | verified | Year recorded as 2026. |
| Dataset/method/task fields are identifiable. | https://arxiv.org/abs/2604.14268 | verified | Registry fields were extracted from primary or official descriptions. |
| Demo or visual quality decision. | https://hyworld.dev/ | verified | decision=`strong`, score=4. |
| Project relevance. | local taxonomy and harness | verified | Strong open-source world-generation baseline for WorldRepresentation, TrajectoryPlan, 3DGSScene, MeshExport, and engine integration. |

## Evidence

- Main metrics: The technical report and official model card describe text/image/multi-view/video inputs, 3DGS/mesh outputs, WorldNav/WorldStereo/WorldMirror components, WorldLens rendering, and released weights/code.
- Qualitative results: visual/demo decision is `strong` with score 4; generation-heavy entries need adequate or strong evidence.
- Ablations: not independently reproduced; use original paper/project ablations when citing.
- Baselines: compare against the paper's own baseline list before making SOTA claims.
- Reproducibility signals: source quality is `primary_or_official`, demo score is 5, evidence strength is 5.

## Limitations

- Method limitations: General world generation is not robotics-specific; physical interaction fidelity must be tested before embodied-policy use.
- Experimental limitations: this initialization run did not train models, download large datasets, or reproduce metrics.
- Demo / visual limitations: official examples may be curated; local reproduction or independent videos are needed before strong deployment claims.
- Claims that remain unverified: exact code/checkpoint maturity, license constraints, and benchmark leaderboard status may change after 2026-06-06.

## Project Relevance

- Relevance to interactive embodied generation: Strong open-source world-generation baseline for WorldRepresentation, TrajectoryPlan, 3DGSScene, MeshExport, and engine integration.
- Reusable fields: Scene, Object, Part, Affordance, PhysicalProperty, SpatialRelation, StateTransition, Action, Policy, BenchmarkMetric, and ValidationReport as applicable.
- Possible baseline role: use this paper as a branch-specific baseline or validator for Interactive Generation and PCG.
- Implications for our task / benchmark: it helps decide whether generated scenes are only visually plausible or actually useful for interactive, spatial, physical, or policy-facing embodied tasks.

## Reproduction / Follow-up

- What to check before using: official code/data release status, license, exact benchmark split, and whether demos can be run locally.
- Code / checkpoint availability: https://huggingface.co/tencent/HY-World-2.0.
- Citation or related-work caveats: phrase strong claims as reported by the source unless we independently reproduce them.
