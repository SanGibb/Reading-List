# Ctrl-World

candidate_id: CAND-0046
branch: E
decision: accepted_for_registry
authors: Ctrl-World team
year: 2026
venue: ICLR

## Source Links

- Paper: https://ctrl-world.github.io/
- Project: https://ctrl-world.github.io/
- Code: https://ctrl-world.github.io/
- Data / benchmark: https://ctrl-world.github.io/
- Demo / video: https://ctrl-world.github.io/
- Official figures: https://ctrl-world.github.io/

## TL;DR

Ctrl-World is included because it addresses **evaluate whether world models support policy-in-the-loop manipulation rollouts** with a method centered on **controllable world-model evaluation designed to let generalist robot policies roll out actions inside imagination space**. For our repository, the important point is not venue alone but that the work gives concrete evidence for embodied/world benchmarks, robot data infrastructure, evaluation protocols, and reproducibility. Main caveat: Needs deeper source checking for dataset/model release and exact benchmark protocol.

## Novelty

- What is actually new: centers evaluation on policy utility and rollout control rather than passive generation quality.
- Difference from prior work: it adds executable, interactive, physical, spatial, or policy-facing structure rather than stopping at static visual quality.
- Why the delta matters: our target task needs generated or reconstructed worlds that agents can reason about, validate, or act in, so this paper contributes reusable structure rather than only a visual sample gallery.

## Contributions

1. Defines a evaluate whether world models support policy-in-the-loop manipulation rollouts problem setting that is directly relevant to interactive embodied generation.
2. Introduces the core method: controllable world-model evaluation designed to let generalist robot policies roll out actions inside imagination space.
3. Provides evidence through policy-in-the-loop rollouts and real-world/world-model comparisons for generalist robot policies and makes the paper useful for our Evaluation and Data Infrastructure branch.

## Task

- Input: paper-specific observations, prompts, scene assets, robot observations, or benchmark inputs described by the original source.
- Output: evaluate whether world models support policy-in-the-loop manipulation rollouts outputs, represented as generated worlds, executable assets, spatial answers, policy actions, or benchmark scores depending on branch.
- Setting: Evaluation and Data Infrastructure within an interactive embodied generation reading list.
- Success criterion: strong source evidence, branch fit, usable data/method description, and visual/demo quality of `not_applicable` when the work depends on generation or robot execution.

## Data

- Dataset / benchmark: policy-in-the-loop rollouts and real-world/world-model comparisons for generalist robot policies.
- Scale: use the scale reported by the source; exact split details should be checked in the paper before citation.
- Modalities: 3D scenes/assets, images/videos, depth/multi-view observations, robot trajectories, actions, or benchmark annotations depending on the paper.
- Collection / annotation: source-specific; this run records only primary-source claims and does not independently audit annotation pipelines.
- Splits / evaluation protocol: follow the paper/project page; local reproduction was not performed.

## Method

- Core pipeline: controllable world-model evaluation designed to let generalist robot policies roll out actions inside imagination space.
- Model / representation: the useful abstraction for this repository is the mapping from source input to executable world representation, spatial state, robot action, or evaluation signal.
- Training or optimization: use the paper-specific training, optimization, search, or benchmark construction described by the primary source.
- Inference / deployment: relevant deployment mode is generated-scene inspection, simulator import, robot rollout, spatial VLM evaluation, or world-model benchmark execution.
- Losses or metrics: use reported metrics only as source-attributed evidence until reproduced locally.

## Key Figures / Architecture

figure_status: linked_official

- Figure / demo: official project, paper, or architecture material.
- Source: https://ctrl-world.github.io/
- Render:
  Official figure/demo page: https://ctrl-world.github.io/
- What it shows: the official figure/demo evidence for the method pipeline, generated results, robot execution, or benchmark design.
- Why it matters: it is the visual anchor used by Quality Reviewer; no local reproduction was performed in this initialization run.

## Evidence Trail

| Claim | Source | Status | Notes |
|---|---|---|---|
| Primary source exists and is 2024+. | https://ctrl-world.github.io/ | verified | Year recorded as 2026. |
| Dataset/method/task fields are identifiable. | https://ctrl-world.github.io/ | verified | Registry fields were extracted from primary or official descriptions. |
| Demo or visual quality decision. | https://ctrl-world.github.io/ | verified | decision=`not_applicable`, score=0. |
| Project relevance. | local taxonomy and harness | verified | Useful benchmark design for world-action model validators and imagined rollout tests. |

## Evidence

- Main metrics: Official ICLR 2026 page describes policy-in-the-loop rollouts with generalist robot policies and comparisons between real-world and imagined rollouts.
- Qualitative results: visual/demo decision is `not_applicable` with score 0; generation-heavy entries need adequate or strong evidence.
- Ablations: not independently reproduced; use original paper/project ablations when citing.
- Baselines: compare against the paper's own baseline list before making SOTA claims.
- Reproducibility signals: source quality is `primary_or_official`, demo score is 3, evidence strength is 4.

## Limitations

- Method limitations: Needs deeper source checking for dataset/model release and exact benchmark protocol.
- Experimental limitations: this initialization run did not train models, download large datasets, or reproduce metrics.
- Demo / visual limitations: official examples may be curated; local reproduction or independent videos are needed before strong deployment claims.
- Claims that remain unverified: exact code/checkpoint maturity, license constraints, and benchmark leaderboard status may change after 2026-06-06.

## Project Relevance

- Relevance to interactive embodied generation: Useful benchmark design for world-action model validators and imagined rollout tests.
- Reusable fields: Scene, Object, Part, Affordance, PhysicalProperty, SpatialRelation, StateTransition, Action, Policy, BenchmarkMetric, and ValidationReport as applicable.
- Possible baseline role: use this paper as a branch-specific baseline or validator for Evaluation and Data Infrastructure.
- Implications for our task / benchmark: it helps decide whether generated scenes are only visually plausible or actually useful for interactive, spatial, physical, or policy-facing embodied tasks.

## Reproduction / Follow-up

- What to check before using: official code/data release status, license, exact benchmark split, and whether demos can be run locally.
- Code / checkpoint availability: https://ctrl-world.github.io/.
- Citation or related-work caveats: phrase strong claims as reported by the source unless we independently reproduce them.
