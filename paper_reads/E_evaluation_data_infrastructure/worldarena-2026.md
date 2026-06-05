# WorldArena: A Unified Benchmark for Evaluating Perception and Functional Utility of Embodied World Models

candidate_id: CAND-0044
branch: E
decision: accepted_for_registry
authors: Shang et al.
year: 2026
venue: arXiv / benchmark

## Source Links

- Paper: https://arxiv.org/abs/2602.08971
- Project: https://world-arena.ai/
- Code: https://world-arena.ai/
- Data / benchmark: https://world-arena.ai/
- Demo / video: https://world-arena.ai/
- Official figures: https://world-arena.ai/

## TL;DR

WorldArena: A Unified Benchmark for Evaluating Perception and Functional Utility of Embodied World Models is included because it addresses **evaluate embodied world models as perceptual predictors, synthetic data engines, policy evaluators, and action planners** with a method centered on **perception and functional-utility benchmark with 16 numerical video metrics, task-functionality evaluation, human judgment, and EWMScore**. For our repository, the important point is not venue alone but that the work gives concrete evidence for embodied/world benchmarks, robot data infrastructure, evaluation protocols, and reproducibility. Main caveat: Leaderboard and challenge are active; exact baselines and datasets may evolve quickly.

## Novelty

- What is actually new: ties world-model evaluation to functional embodied utility rather than video quality alone.
- Difference from prior work: it adds executable, interactive, physical, spatial, or policy-facing structure rather than stopping at static visual quality.
- Why the delta matters: our target task needs generated or reconstructed worlds that agents can reason about, validate, or act in, so this paper contributes reusable structure rather than only a visual sample gallery.

## Contributions

1. Defines a evaluate embodied world models as perceptual predictors, synthetic data engines, policy evaluators, and action planners problem setting that is directly relevant to interactive embodied generation.
2. Introduces the core method: perception and functional-utility benchmark with 16 numerical video metrics, task-functionality evaluation, human judgment, and EWMScore.
3. Provides evidence through public benchmark, leaderboard, dataset, and challenge for embodied world models and makes the paper useful for our Evaluation and Data Infrastructure branch.

## Task

- Input: paper-specific observations, prompts, scene assets, robot observations, or benchmark inputs described by the original source.
- Output: evaluate embodied world models as perceptual predictors, synthetic data engines, policy evaluators, and action planners outputs, represented as generated worlds, executable assets, spatial answers, policy actions, or benchmark scores depending on branch.
- Setting: Evaluation and Data Infrastructure within an interactive embodied generation reading list.
- Success criterion: strong source evidence, branch fit, usable data/method description, and visual/demo quality of `not_applicable` when the work depends on generation or robot execution.

## Data

- Dataset / benchmark: public benchmark, leaderboard, dataset, and challenge for embodied world models.
- Scale: use the scale reported by the source; exact split details should be checked in the paper before citation.
- Modalities: 3D scenes/assets, images/videos, depth/multi-view observations, robot trajectories, actions, or benchmark annotations depending on the paper.
- Collection / annotation: source-specific; this run records only primary-source claims and does not independently audit annotation pipelines.
- Splits / evaluation protocol: follow the paper/project page; local reproduction was not performed.

## Method

- Core pipeline: perception and functional-utility benchmark with 16 numerical video metrics, task-functionality evaluation, human judgment, and EWMScore.
- Model / representation: the useful abstraction for this repository is the mapping from source input to executable world representation, spatial state, robot action, or evaluation signal.
- Training or optimization: use the paper-specific training, optimization, search, or benchmark construction described by the primary source.
- Inference / deployment: relevant deployment mode is generated-scene inspection, simulator import, robot rollout, spatial VLM evaluation, or world-model benchmark execution.
- Losses or metrics: use reported metrics only as source-attributed evidence until reproduced locally.

## Key Figures / Architecture

figure_status: linked_official

- Figure / demo: official project, paper, or architecture material.
- Source: https://world-arena.ai/
- Render:
  Official figure/demo page: https://world-arena.ai/
- What it shows: the official figure/demo evidence for the method pipeline, generated results, robot execution, or benchmark design.
- Why it matters: it is the visual anchor used by Quality Reviewer; no local reproduction was performed in this initialization run.

## Evidence Trail

| Claim | Source | Status | Notes |
|---|---|---|---|
| Primary source exists and is 2024+. | https://arxiv.org/abs/2602.08971 | verified | Year recorded as 2026. |
| Dataset/method/task fields are identifiable. | https://arxiv.org/abs/2602.08971 | verified | Registry fields were extracted from primary or official descriptions. |
| Demo or visual quality decision. | https://world-arena.ai/ | verified | decision=`not_applicable`, score=0. |
| Project relevance. | local taxonomy and harness | verified | Important evaluation target for our interactive embodied world generator and world-model branches. |

## Evidence

- Main metrics: Official benchmark and arXiv describe perception metrics, embodied task functionality, EWMScore, public leaderboard, dataset, and challenge links.
- Qualitative results: visual/demo decision is `not_applicable` with score 0; generation-heavy entries need adequate or strong evidence.
- Ablations: not independently reproduced; use original paper/project ablations when citing.
- Baselines: compare against the paper's own baseline list before making SOTA claims.
- Reproducibility signals: source quality is `primary_or_official`, demo score is 4, evidence strength is 5.

## Limitations

- Method limitations: Leaderboard and challenge are active; exact baselines and datasets may evolve quickly.
- Experimental limitations: this initialization run did not train models, download large datasets, or reproduce metrics.
- Demo / visual limitations: official examples may be curated; local reproduction or independent videos are needed before strong deployment claims.
- Claims that remain unverified: exact code/checkpoint maturity, license constraints, and benchmark leaderboard status may change after 2026-06-06.

## Project Relevance

- Relevance to interactive embodied generation: Important evaluation target for our interactive embodied world generator and world-model branches.
- Reusable fields: Scene, Object, Part, Affordance, PhysicalProperty, SpatialRelation, StateTransition, Action, Policy, BenchmarkMetric, and ValidationReport as applicable.
- Possible baseline role: use this paper as a branch-specific baseline or validator for Evaluation and Data Infrastructure.
- Implications for our task / benchmark: it helps decide whether generated scenes are only visually plausible or actually useful for interactive, spatial, physical, or policy-facing embodied tasks.

## Reproduction / Follow-up

- What to check before using: official code/data release status, license, exact benchmark split, and whether demos can be run locally.
- Code / checkpoint availability: https://world-arena.ai/.
- Citation or related-work caveats: phrase strong claims as reported by the source unless we independently reproduce them.
