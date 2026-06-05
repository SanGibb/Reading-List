# SceneSmith: Agentic Generation of Simulation-Ready Indoor Scenes

candidate_id: CAND-0023
branch: B
decision: accepted_for_registry
authors: Pfaff et al.
year: 2026
venue: ICML Spotlight

## Source Links

- Paper: https://arxiv.org/abs/2602.09153
- Project: https://scenesmith.github.io/
- Code: https://scenesmith.github.io/
- Data / benchmark: https://scenesmith.github.io/
- Demo / video: https://scenesmith.github.io/
- Official figures: https://scenesmith.github.io/

## TL;DR

SceneSmith: Agentic Generation of Simulation-Ready Indoor Scenes is included because it addresses **generate dense simulation-ready indoor environments from natural language prompts** with a method centered on **hierarchical agentic text-to-scene framework with designer, critic, and orchestrator VLM agents across layout, furniture, and object-population stages**. For our repository, the important point is not venue alone but that the work gives concrete evidence for interactive assets, scenes, tasks, worlds, and PCG-style simulation data. Main caveat: Pipeline complexity and dependency on multiple generators/assets may make reproduction heavy.

## Novelty

- What is actually new: combines agentic generation with physical property estimation and policy-evaluation-ready scene export.
- Difference from prior work: it adds executable, interactive, physical, spatial, or policy-facing structure rather than stopping at static visual quality.
- Why the delta matters: our target task needs generated or reconstructed worlds that agents can reason about, validate, or act in, so this paper contributes reusable structure rather than only a visual sample gallery.

## Contributions

1. Defines a generate dense simulation-ready indoor environments from natural language prompts problem setting that is directly relevant to interactive embodied generation.
2. Introduces the core method: hierarchical agentic text-to-scene framework with designer, critic, and orchestrator VLM agents across layout, furniture, and object-population stages.
3. Provides evidence through text-prompted indoor scenes, generated static assets, retrieved articulated objects, physical properties, and example scene dataset and makes the paper useful for our Interactive Generation and PCG branch.

## Task

- Input: paper-specific observations, prompts, scene assets, robot observations, or benchmark inputs described by the original source.
- Output: generate dense simulation-ready indoor environments from natural language prompts outputs, represented as generated worlds, executable assets, spatial answers, policy actions, or benchmark scores depending on branch.
- Setting: Interactive Generation and PCG within an interactive embodied generation reading list.
- Success criterion: strong source evidence, branch fit, usable data/method description, and visual/demo quality of `strong` when the work depends on generation or robot execution.

## Data

- Dataset / benchmark: text-prompted indoor scenes, generated static assets, retrieved articulated objects, physical properties, and example scene dataset.
- Scale: use the scale reported by the source; exact split details should be checked in the paper before citation.
- Modalities: 3D scenes/assets, images/videos, depth/multi-view observations, robot trajectories, actions, or benchmark annotations depending on the paper.
- Collection / annotation: source-specific; this run records only primary-source claims and does not independently audit annotation pipelines.
- Splits / evaluation protocol: follow the paper/project page; local reproduction was not performed.

## Method

- Core pipeline: hierarchical agentic text-to-scene framework with designer, critic, and orchestrator VLM agents across layout, furniture, and object-population stages.
- Model / representation: the useful abstraction for this repository is the mapping from source input to executable world representation, spatial state, robot action, or evaluation signal.
- Training or optimization: use the paper-specific training, optimization, search, or benchmark construction described by the primary source.
- Inference / deployment: relevant deployment mode is generated-scene inspection, simulator import, robot rollout, spatial VLM evaluation, or world-model benchmark execution.
- Losses or metrics: use reported metrics only as source-attributed evidence until reproduced locally.

## Key Figures / Architecture

figure_status: linked_official

- Figure / demo: official project, paper, or architecture material.
- Source: https://scenesmith.github.io/
- Render:
  Official figure/demo page: https://scenesmith.github.io/
- What it shows: the official figure/demo evidence for the method pipeline, generated results, robot execution, or benchmark design.
- Why it matters: it is the visual anchor used by Quality Reviewer; no local reproduction was performed in this initialization run.

## Evidence Trail

| Claim | Source | Status | Notes |
|---|---|---|---|
| Primary source exists and is 2024+. | https://arxiv.org/abs/2602.09153 | verified | Year recorded as 2026. |
| Dataset/method/task fields are identifiable. | https://arxiv.org/abs/2602.09153 | verified | Registry fields were extracted from primary or official descriptions. |
| Demo or visual quality decision. | https://scenesmith.github.io/ | verified | decision=`strong`, score=5. |
| Project relevance. | local taxonomy and harness | verified | Top PCG baseline for PromptToScene, CriticLoop, ObjectPopulation, PhysicalProperty, and policy evaluation. |

## Evidence

- Main metrics: Official ICML 2026 Spotlight page reports hierarchical VLM agents, dense object population, articulated-object retrieval, physical property estimation, under 2 percent inter-object collisions, and policy-evaluation use.
- Qualitative results: visual/demo decision is `strong` with score 5; generation-heavy entries need adequate or strong evidence.
- Ablations: not independently reproduced; use original paper/project ablations when citing.
- Baselines: compare against the paper's own baseline list before making SOTA claims.
- Reproducibility signals: source quality is `primary_or_official`, demo score is 4, evidence strength is 5.

## Limitations

- Method limitations: Pipeline complexity and dependency on multiple generators/assets may make reproduction heavy.
- Experimental limitations: this initialization run did not train models, download large datasets, or reproduce metrics.
- Demo / visual limitations: official examples may be curated; local reproduction or independent videos are needed before strong deployment claims.
- Claims that remain unverified: exact code/checkpoint maturity, license constraints, and benchmark leaderboard status may change after 2026-06-06.

## Project Relevance

- Relevance to interactive embodied generation: Top PCG baseline for PromptToScene, CriticLoop, ObjectPopulation, PhysicalProperty, and policy evaluation.
- Reusable fields: Scene, Object, Part, Affordance, PhysicalProperty, SpatialRelation, StateTransition, Action, Policy, BenchmarkMetric, and ValidationReport as applicable.
- Possible baseline role: use this paper as a branch-specific baseline or validator for Interactive Generation and PCG.
- Implications for our task / benchmark: it helps decide whether generated scenes are only visually plausible or actually useful for interactive, spatial, physical, or policy-facing embodied tasks.

## Reproduction / Follow-up

- What to check before using: official code/data release status, license, exact benchmark split, and whether demos can be run locally.
- Code / checkpoint availability: https://scenesmith.github.io/.
- Citation or related-work caveats: phrase strong claims as reported by the source unless we independently reproduce them.
