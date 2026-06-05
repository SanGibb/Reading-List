# Steerable Scene Generation

candidate_id: CAND-0020
branch: B
decision: accepted_for_registry
authors: Steerable Scene Generation team
year: 2025
venue: CoRL

## Source Links

- Paper: https://arxiv.org/abs/2505.04831
- Project: not confirmed
- Code: not confirmed
- Data / benchmark: https://arxiv.org/abs/2505.04831
- Demo / video: https://arxiv.org/abs/2505.04831
- Official figures: https://arxiv.org/abs/2505.04831

## TL;DR

Steerable Scene Generation is included because it addresses **generate scenes satisfying task and physical objectives** with a method centered on **diffusion scene prior steered by RL, conditioning and MCTS**. For our repository, the important point is not venue alone but that the work gives concrete evidence for interactive assets, scenes, tasks, worlds, and PCG-style simulation data. Main caveat: Project/demo evidence is weaker than SAGE or SceneSmith; treat it as a method baseline rather than a visual-quality anchor.

## Novelty

- What is actually new: combines PCG-scale data with inference-time search and downstream steering.
- Difference from prior work: it adds executable, interactive, physical, spatial, or policy-facing structure rather than stopping at static visual quality.
- Why the delta matters: our target task needs generated or reconstructed worlds that agents can reason about, validate, or act in, so this paper contributes reusable structure rather than only a visual sample gallery.

## Contributions

1. Defines a generate scenes satisfying task and physical objectives problem setting that is directly relevant to interactive embodied generation.
2. Introduces the core method: diffusion scene prior steered by RL, conditioning and MCTS.
3. Provides evidence through over 44M procedurally generated SE(3) scene placements and makes the paper useful for our Interactive Generation and PCG branch.

## Task

- Input: paper-specific observations, prompts, scene assets, robot observations, or benchmark inputs described by the original source.
- Output: generate scenes satisfying task and physical objectives outputs, represented as generated worlds, executable assets, spatial answers, policy actions, or benchmark scores depending on branch.
- Setting: Interactive Generation and PCG within an interactive embodied generation reading list.
- Success criterion: strong source evidence, branch fit, usable data/method description, and visual/demo quality of `adequate` when the work depends on generation or robot execution.

## Data

- Dataset / benchmark: over 44M procedurally generated SE(3) scene placements.
- Scale: use the scale reported by the source; exact split details should be checked in the paper before citation.
- Modalities: 3D scenes/assets, images/videos, depth/multi-view observations, robot trajectories, actions, or benchmark annotations depending on the paper.
- Collection / annotation: source-specific; this run records only primary-source claims and does not independently audit annotation pipelines.
- Splits / evaluation protocol: follow the paper/project page; local reproduction was not performed.

## Method

- Core pipeline: diffusion scene prior steered by RL, conditioning and MCTS.
- Model / representation: the useful abstraction for this repository is the mapping from source input to executable world representation, spatial state, robot action, or evaluation signal.
- Training or optimization: use the paper-specific training, optimization, search, or benchmark construction described by the primary source.
- Inference / deployment: relevant deployment mode is generated-scene inspection, simulator import, robot rollout, spatial VLM evaluation, or world-model benchmark execution.
- Losses or metrics: use reported metrics only as source-attributed evidence until reproduced locally.

## Key Figures / Architecture

figure_status: linked_official

- Figure / demo: official project, paper, or architecture material.
- Source: https://arxiv.org/abs/2505.04831
- Render:
  Official figure/demo page: https://arxiv.org/abs/2505.04831
- What it shows: the official figure/demo evidence for the method pipeline, generated results, robot execution, or benchmark design.
- Why it matters: it is the visual anchor used by Quality Reviewer; no local reproduction was performed in this initialization run.

## Evidence Trail

| Claim | Source | Status | Notes |
|---|---|---|---|
| Primary source exists and is 2024+. | https://arxiv.org/abs/2505.04831 | verified | Year recorded as 2025. |
| Dataset/method/task fields are identifiable. | https://arxiv.org/abs/2505.04831 | verified | Registry fields were extracted from primary or official descriptions. |
| Demo or visual quality decision. | https://arxiv.org/abs/2505.04831 | verified | decision=`adequate`, score=3. |
| Project relevance. | local taxonomy and harness | verified | strong baseline for task-constrained scene generation |

## Evidence

- Main metrics: The paper reports a scene prior trained from more than 44M procedurally generated SE(3) placements, then steered by RL and search objectives.
- Qualitative results: visual/demo decision is `adequate` with score 3; generation-heavy entries need adequate or strong evidence.
- Ablations: not independently reproduced; use original paper/project ablations when citing.
- Baselines: compare against the paper's own baseline list before making SOTA claims.
- Reproducibility signals: source quality is `primary_or_official`, demo score is 2, evidence strength is 3.

## Limitations

- Method limitations: Project/demo evidence is weaker than SAGE or SceneSmith; treat it as a method baseline rather than a visual-quality anchor.
- Experimental limitations: this initialization run did not train models, download large datasets, or reproduce metrics.
- Demo / visual limitations: official examples may be curated; local reproduction or independent videos are needed before strong deployment claims.
- Claims that remain unverified: exact code/checkpoint maturity, license constraints, and benchmark leaderboard status may change after 2026-06-06.

## Project Relevance

- Relevance to interactive embodied generation: strong baseline for task-constrained scene generation
- Reusable fields: Scene, Object, Part, Affordance, PhysicalProperty, SpatialRelation, StateTransition, Action, Policy, BenchmarkMetric, and ValidationReport as applicable.
- Possible baseline role: use this paper as a branch-specific baseline or validator for Interactive Generation and PCG.
- Implications for our task / benchmark: it helps decide whether generated scenes are only visually plausible or actually useful for interactive, spatial, physical, or policy-facing embodied tasks.

## Reproduction / Follow-up

- What to check before using: official code/data release status, license, exact benchmark split, and whether demos can be run locally.
- Code / checkpoint availability: not confirmed.
- Citation or related-work caveats: phrase strong claims as reported by the source unless we independently reproduce them.
