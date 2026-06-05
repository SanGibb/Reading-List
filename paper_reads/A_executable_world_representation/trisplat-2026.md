# TriSplat: Simulation-Ready Feed-Forward 3D Scene Reconstruction

candidate_id: CAND-0019
branch: A
decision: accepted_for_registry
authors: Wang et al.
year: 2026
venue: arXiv

## Source Links

- Paper: https://arxiv.org/abs/2605.26115
- Project: https://lhmd.top/trisplat/
- Code: https://lhmd.top/trisplat/
- Data / benchmark: https://lhmd.top/trisplat/
- Demo / video: https://lhmd.top/trisplat/
- Official figures: https://lhmd.top/trisplat/

## TL;DR

TriSplat: Simulation-Ready Feed-Forward 3D Scene Reconstruction is included because it addresses **reconstruct simulation-ready mesh scenes from sparse or pose-free images** with a method centered on **feed-forward oriented-triangle splatting network that predicts point maps, triangle attributes, camera poses, and mesh-ready surfaces**. For our repository, the important point is not venue alone but that the work gives concrete evidence for executable world structures, object parts, affordances, task predicates, and physical/deformable state. Main caveat: Scene interaction semantics and physical material properties are outside the main contribution.

## Novelty

- What is actually new: replaces Gaussian primitives with oriented triangle primitives that can be ingested by physics/rendering pipelines without post-hoc meshing.
- Difference from prior work: it adds executable, interactive, physical, spatial, or policy-facing structure rather than stopping at static visual quality.
- Why the delta matters: our target task needs generated or reconstructed worlds that agents can reason about, validate, or act in, so this paper contributes reusable structure rather than only a visual sample gallery.

## Contributions

1. Defines a reconstruct simulation-ready mesh scenes from sparse or pose-free images problem setting that is directly relevant to interactive embodied generation.
2. Introduces the core method: feed-forward oriented-triangle splatting network that predicts point maps, triangle attributes, camera poses, and mesh-ready surfaces.
3. Provides evidence through RealEstate10K, DL3DV, ScanNet-style sparse-view reconstruction evaluations and makes the paper useful for our Executable World Representation branch.

## Task

- Input: paper-specific observations, prompts, scene assets, robot observations, or benchmark inputs described by the original source.
- Output: reconstruct simulation-ready mesh scenes from sparse or pose-free images outputs, represented as generated worlds, executable assets, spatial answers, policy actions, or benchmark scores depending on branch.
- Setting: Executable World Representation within an interactive embodied generation reading list.
- Success criterion: strong source evidence, branch fit, usable data/method description, and visual/demo quality of `adequate` when the work depends on generation or robot execution.

## Data

- Dataset / benchmark: RealEstate10K, DL3DV, ScanNet-style sparse-view reconstruction evaluations.
- Scale: use the scale reported by the source; exact split details should be checked in the paper before citation.
- Modalities: 3D scenes/assets, images/videos, depth/multi-view observations, robot trajectories, actions, or benchmark annotations depending on the paper.
- Collection / annotation: source-specific; this run records only primary-source claims and does not independently audit annotation pipelines.
- Splits / evaluation protocol: follow the paper/project page; local reproduction was not performed.

## Method

- Core pipeline: feed-forward oriented-triangle splatting network that predicts point maps, triangle attributes, camera poses, and mesh-ready surfaces.
- Model / representation: the useful abstraction for this repository is the mapping from source input to executable world representation, spatial state, robot action, or evaluation signal.
- Training or optimization: use the paper-specific training, optimization, search, or benchmark construction described by the primary source.
- Inference / deployment: relevant deployment mode is generated-scene inspection, simulator import, robot rollout, spatial VLM evaluation, or world-model benchmark execution.
- Losses or metrics: use reported metrics only as source-attributed evidence until reproduced locally.

## Key Figures / Architecture

figure_status: linked_official

- Figure / demo: official project, paper, or architecture material.
- Source: https://lhmd.top/trisplat/
- Render:
  Official figure/demo page: https://lhmd.top/trisplat/
- What it shows: the official figure/demo evidence for the method pipeline, generated results, robot execution, or benchmark design.
- Why it matters: it is the visual anchor used by Quality Reviewer; no local reproduction was performed in this initialization run.

## Evidence Trail

| Claim | Source | Status | Notes |
|---|---|---|---|
| Primary source exists and is 2024+. | https://arxiv.org/abs/2605.26115 | verified | Year recorded as 2026. |
| Dataset/method/task fields are identifiable. | https://arxiv.org/abs/2605.26115 | verified | Registry fields were extracted from primary or official descriptions. |
| Demo or visual quality decision. | https://lhmd.top/trisplat/ | verified | decision=`adequate`, score=3. |
| Project relevance. | local taxonomy and harness | verified | Useful representation reference for MeshScene, CollisionSurface, and feed-forward sim-ready reconstruction. |

## Evidence

- Main metrics: The paper uses oriented triangle primitives to directly export simulation-ready mesh scenes from sparse images without Gaussian-to-mesh post-processing.
- Qualitative results: visual/demo decision is `adequate` with score 3; generation-heavy entries need adequate or strong evidence.
- Ablations: not independently reproduced; use original paper/project ablations when citing.
- Baselines: compare against the paper's own baseline list before making SOTA claims.
- Reproducibility signals: source quality is `primary_or_official`, demo score is 2, evidence strength is 4.

## Limitations

- Method limitations: Scene interaction semantics and physical material properties are outside the main contribution.
- Experimental limitations: this initialization run did not train models, download large datasets, or reproduce metrics.
- Demo / visual limitations: official examples may be curated; local reproduction or independent videos are needed before strong deployment claims.
- Claims that remain unverified: exact code/checkpoint maturity, license constraints, and benchmark leaderboard status may change after 2026-06-06.

## Project Relevance

- Relevance to interactive embodied generation: Useful representation reference for MeshScene, CollisionSurface, and feed-forward sim-ready reconstruction.
- Reusable fields: Scene, Object, Part, Affordance, PhysicalProperty, SpatialRelation, StateTransition, Action, Policy, BenchmarkMetric, and ValidationReport as applicable.
- Possible baseline role: use this paper as a branch-specific baseline or validator for Executable World Representation.
- Implications for our task / benchmark: it helps decide whether generated scenes are only visually plausible or actually useful for interactive, spatial, physical, or policy-facing embodied tasks.

## Reproduction / Follow-up

- What to check before using: official code/data release status, license, exact benchmark split, and whether demos can be run locally.
- Code / checkpoint availability: https://lhmd.top/trisplat/.
- Citation or related-work caveats: phrase strong claims as reported by the source unless we independently reproduce them.
