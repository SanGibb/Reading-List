# SimuScene: Simulation-Ready Compositional 3D Scene Reconstruction from a Single Image

candidate_id: CAND-0017
branch: A
decision: accepted_for_registry
authors: Lee et al.
year: 2026
venue: arXiv

## Source Links

- Paper: https://arxiv.org/abs/2606.03994
- Project: https://arxiv.org/abs/2606.03994
- Code: not confirmed
- Data / benchmark: https://arxiv.org/abs/2606.03994
- Demo / video: https://arxiv.org/abs/2606.03994
- Official figures: https://arxiv.org/abs/2606.03994

## TL;DR

SimuScene: Simulation-Ready Compositional 3D Scene Reconstruction from a Single Image is included because it addresses **reconstruct stable simulation-ready 3D scenes from one image** with a method centered on **physics-in-the-loop compositional reconstruction that converts simulation failures into shape/layout correction signals**. For our repository, the important point is not venue alone but that the work gives concrete evidence for executable world structures, object parts, affordances, task predicates, and physical/deformable state. Main caveat: Published only days before this run; project/code maturity and visual demos need rechecking.

## Novelty

- What is actually new: uses physics simulation as a diagnostic measurement tool during generation rather than only post-hoc cleanup.
- Difference from prior work: it adds executable, interactive, physical, spatial, or policy-facing structure rather than stopping at static visual quality.
- Why the delta matters: our target task needs generated or reconstructed worlds that agents can reason about, validate, or act in, so this paper contributes reusable structure rather than only a visual sample gallery.

## Contributions

1. Defines a reconstruct stable simulation-ready 3D scenes from one image problem setting that is directly relevant to interactive embodied generation.
2. Introduces the core method: physics-in-the-loop compositional reconstruction that converts simulation failures into shape/layout correction signals.
3. Provides evidence through single-image compositional 3D scene reconstruction benchmarks plus humanoid and robot-arm downstream deployments and makes the paper useful for our Executable World Representation branch.

## Task

- Input: paper-specific observations, prompts, scene assets, robot observations, or benchmark inputs described by the original source.
- Output: reconstruct stable simulation-ready 3D scenes from one image outputs, represented as generated worlds, executable assets, spatial answers, policy actions, or benchmark scores depending on branch.
- Setting: Executable World Representation within an interactive embodied generation reading list.
- Success criterion: strong source evidence, branch fit, usable data/method description, and visual/demo quality of `adequate` when the work depends on generation or robot execution.

## Data

- Dataset / benchmark: single-image compositional 3D scene reconstruction benchmarks plus humanoid and robot-arm downstream deployments.
- Scale: use the scale reported by the source; exact split details should be checked in the paper before citation.
- Modalities: 3D scenes/assets, images/videos, depth/multi-view observations, robot trajectories, actions, or benchmark annotations depending on the paper.
- Collection / annotation: source-specific; this run records only primary-source claims and does not independently audit annotation pipelines.
- Splits / evaluation protocol: follow the paper/project page; local reproduction was not performed.

## Method

- Core pipeline: physics-in-the-loop compositional reconstruction that converts simulation failures into shape/layout correction signals.
- Model / representation: the useful abstraction for this repository is the mapping from source input to executable world representation, spatial state, robot action, or evaluation signal.
- Training or optimization: use the paper-specific training, optimization, search, or benchmark construction described by the primary source.
- Inference / deployment: relevant deployment mode is generated-scene inspection, simulator import, robot rollout, spatial VLM evaluation, or world-model benchmark execution.
- Losses or metrics: use reported metrics only as source-attributed evidence until reproduced locally.

## Key Figures / Architecture

figure_status: linked_official

- Figure / demo: official project, paper, or architecture material.
- Source: https://arxiv.org/abs/2606.03994
- Render:
  Official figure/demo page: https://arxiv.org/abs/2606.03994
- What it shows: the official figure/demo evidence for the method pipeline, generated results, robot execution, or benchmark design.
- Why it matters: it is the visual anchor used by Quality Reviewer; no local reproduction was performed in this initialization run.

## Evidence Trail

| Claim | Source | Status | Notes |
|---|---|---|---|
| Primary source exists and is 2024+. | https://arxiv.org/abs/2606.03994 | verified | Year recorded as 2026. |
| Dataset/method/task fields are identifiable. | https://arxiv.org/abs/2606.03994 | verified | Registry fields were extracted from primary or official descriptions. |
| Demo or visual quality decision. | https://arxiv.org/abs/2606.03994 | verified | decision=`adequate`, score=3. |
| Project relevance. | local taxonomy and harness | verified | Relevant to SceneTree, SupportRelation, PhysicalViolation, and simulator-ready reconstruction validators. |

## Evidence

- Main metrics: The paper puts physics in the loop of shape and layout estimation, using gravity simulation signals to correct penetration/support failures and showing humanoid and robot-arm deployment examples.
- Qualitative results: visual/demo decision is `adequate` with score 3; generation-heavy entries need adequate or strong evidence.
- Ablations: not independently reproduced; use original paper/project ablations when citing.
- Baselines: compare against the paper's own baseline list before making SOTA claims.
- Reproducibility signals: source quality is `primary_or_official`, demo score is 2, evidence strength is 4.

## Limitations

- Method limitations: Published only days before this run; project/code maturity and visual demos need rechecking.
- Experimental limitations: this initialization run did not train models, download large datasets, or reproduce metrics.
- Demo / visual limitations: official examples may be curated; local reproduction or independent videos are needed before strong deployment claims.
- Claims that remain unverified: exact code/checkpoint maturity, license constraints, and benchmark leaderboard status may change after 2026-06-06.

## Project Relevance

- Relevance to interactive embodied generation: Relevant to SceneTree, SupportRelation, PhysicalViolation, and simulator-ready reconstruction validators.
- Reusable fields: Scene, Object, Part, Affordance, PhysicalProperty, SpatialRelation, StateTransition, Action, Policy, BenchmarkMetric, and ValidationReport as applicable.
- Possible baseline role: use this paper as a branch-specific baseline or validator for Executable World Representation.
- Implications for our task / benchmark: it helps decide whether generated scenes are only visually plausible or actually useful for interactive, spatial, physical, or policy-facing embodied tasks.

## Reproduction / Follow-up

- What to check before using: official code/data release status, license, exact benchmark split, and whether demos can be run locally.
- Code / checkpoint availability: not confirmed.
- Citation or related-work caveats: phrase strong claims as reported by the source unless we independently reproduce them.
