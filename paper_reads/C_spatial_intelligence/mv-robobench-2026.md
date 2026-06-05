# Seeing Across Views / MV-RoboBench

candidate_id: CAND-0030
branch: C
decision: accepted_for_registry
authors: MV-RoboBench team
year: 2026
venue: ICLR

## Source Links

- Paper: https://openreview.net/pdf?id=jXDZJAfRZB
- Project: https://openreview.net/pdf?id=jXDZJAfRZB
- Code: not confirmed
- Data / benchmark: https://openreview.net/pdf?id=jXDZJAfRZB
- Demo / video: https://openreview.net/pdf?id=jXDZJAfRZB
- Official figures: https://openreview.net/pdf?id=jXDZJAfRZB

## TL;DR

Seeing Across Views / MV-RoboBench is included because it addresses **spatial and robotic reasoning across synchronized camera views** with a method centered on **benchmarking multi-view spatial reasoning of VLMs in robotic scenes**. For our repository, the important point is not venue alone but that the work gives concrete evidence for 3D reasoning, multi-view understanding, spatial VLMs, and spatial representations for action. Main caveat: Benchmark details should be checked from the OpenReview paper before using exact metric values.

## Novelty

- What is actually new: shows single-view spatial reasoning does not transfer reliably to robotic multi-view settings.
- Difference from prior work: it adds executable, interactive, physical, spatial, or policy-facing structure rather than stopping at static visual quality.
- Why the delta matters: our target task needs generated or reconstructed worlds that agents can reason about, validate, or act in, so this paper contributes reusable structure rather than only a visual sample gallery.

## Contributions

1. Defines a spatial and robotic reasoning across synchronized camera views problem setting that is directly relevant to interactive embodied generation.
2. Introduces the core method: benchmarking multi-view spatial reasoning of VLMs in robotic scenes.
3. Provides evidence through multi-view robotic manipulation scenes with spatial QA and makes the paper useful for our Spatial Intelligence branch.

## Task

- Input: paper-specific observations, prompts, scene assets, robot observations, or benchmark inputs described by the original source.
- Output: spatial and robotic reasoning across synchronized camera views outputs, represented as generated worlds, executable assets, spatial answers, policy actions, or benchmark scores depending on branch.
- Setting: Spatial Intelligence within an interactive embodied generation reading list.
- Success criterion: strong source evidence, branch fit, usable data/method description, and visual/demo quality of `not_applicable` when the work depends on generation or robot execution.

## Data

- Dataset / benchmark: multi-view robotic manipulation scenes with spatial QA.
- Scale: use the scale reported by the source; exact split details should be checked in the paper before citation.
- Modalities: 3D scenes/assets, images/videos, depth/multi-view observations, robot trajectories, actions, or benchmark annotations depending on the paper.
- Collection / annotation: source-specific; this run records only primary-source claims and does not independently audit annotation pipelines.
- Splits / evaluation protocol: follow the paper/project page; local reproduction was not performed.

## Method

- Core pipeline: benchmarking multi-view spatial reasoning of VLMs in robotic scenes.
- Model / representation: the useful abstraction for this repository is the mapping from source input to executable world representation, spatial state, robot action, or evaluation signal.
- Training or optimization: use the paper-specific training, optimization, search, or benchmark construction described by the primary source.
- Inference / deployment: relevant deployment mode is generated-scene inspection, simulator import, robot rollout, spatial VLM evaluation, or world-model benchmark execution.
- Losses or metrics: use reported metrics only as source-attributed evidence until reproduced locally.

## Key Figures / Architecture

figure_status: linked_official

- Figure / demo: official project, paper, or architecture material.
- Source: https://openreview.net/pdf?id=jXDZJAfRZB
- Render:
  Official figure/demo page: https://openreview.net/pdf?id=jXDZJAfRZB
- What it shows: the official figure/demo evidence for the method pipeline, generated results, robot execution, or benchmark design.
- Why it matters: it is the visual anchor used by Quality Reviewer; no local reproduction was performed in this initialization run.

## Evidence Trail

| Claim | Source | Status | Notes |
|---|---|---|---|
| Primary source exists and is 2024+. | https://openreview.net/pdf?id=jXDZJAfRZB | verified | Year recorded as 2026. |
| Dataset/method/task fields are identifiable. | https://openreview.net/pdf?id=jXDZJAfRZB | verified | Registry fields were extracted from primary or official descriptions. |
| Demo or visual quality decision. | https://openreview.net/pdf?id=jXDZJAfRZB | verified | decision=`not_applicable`, score=0. |
| Project relevance. | local taxonomy and harness | verified | important benchmark for observation-to-scene-graph parsing |

## Evidence

- Main metrics: The ICLR 2026 paper benchmarks multi-view spatial reasoning in robotic manipulation scenes and shows single-view reasoning does not reliably transfer.
- Qualitative results: visual/demo decision is `not_applicable` with score 0; generation-heavy entries need adequate or strong evidence.
- Ablations: not independently reproduced; use original paper/project ablations when citing.
- Baselines: compare against the paper's own baseline list before making SOTA claims.
- Reproducibility signals: source quality is `primary_or_official`, demo score is 3, evidence strength is 3.

## Limitations

- Method limitations: Benchmark details should be checked from the OpenReview paper before using exact metric values.
- Experimental limitations: this initialization run did not train models, download large datasets, or reproduce metrics.
- Demo / visual limitations: official examples may be curated; local reproduction or independent videos are needed before strong deployment claims.
- Claims that remain unverified: exact code/checkpoint maturity, license constraints, and benchmark leaderboard status may change after 2026-06-06.

## Project Relevance

- Relevance to interactive embodied generation: important benchmark for observation-to-scene-graph parsing
- Reusable fields: Scene, Object, Part, Affordance, PhysicalProperty, SpatialRelation, StateTransition, Action, Policy, BenchmarkMetric, and ValidationReport as applicable.
- Possible baseline role: use this paper as a branch-specific baseline or validator for Spatial Intelligence.
- Implications for our task / benchmark: it helps decide whether generated scenes are only visually plausible or actually useful for interactive, spatial, physical, or policy-facing embodied tasks.

## Reproduction / Follow-up

- What to check before using: official code/data release status, license, exact benchmark split, and whether demos can be run locally.
- Code / checkpoint availability: not confirmed.
- Citation or related-work caveats: phrase strong claims as reported by the source unless we independently reproduce them.
