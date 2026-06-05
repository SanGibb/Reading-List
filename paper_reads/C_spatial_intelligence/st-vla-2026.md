# ST-VLA: Enabling 4D-Aware Spatiotemporal Understanding for General Robot Manipulation

candidate_id: CAND-0032
branch: C
decision: accepted_for_registry
authors: Wu et al.
year: 2026
venue: arXiv

## Source Links

- Paper: https://arxiv.org/abs/2603.13788
- Project: https://oucx117.github.io/ST-VLA/
- Code: https://oucx117.github.io/ST-VLA/
- Data / benchmark: https://oucx117.github.io/ST-VLA/
- Demo / video: https://oucx117.github.io/ST-VLA/
- Official figures: https://oucx117.github.io/ST-VLA/

## TL;DR

ST-VLA: Enabling 4D-Aware Spatiotemporal Understanding for General Robot Manipulation is included because it addresses **open-world long-horizon robot manipulation** with a method centered on **3D-4D representation, spatial masks and spatiotemporal VLM**. For our repository, the important point is not venue alone but that the work gives concrete evidence for 3D reasoning, multi-view understanding, spatial VLMs, and spatial representations for action. Main caveat: Dataset release and cross-embodiment reproduction need follow-up.

## Novelty

- What is actually new: bridges semantic reasoning and continuous control through 4D spatial context.
- Difference from prior work: it adds executable, interactive, physical, spatial, or policy-facing structure rather than stopping at static visual quality.
- Why the delta matters: our target task needs generated or reconstructed worlds that agents can reason about, validate, or act in, so this paper contributes reusable structure rather than only a visual sample gallery.

## Contributions

1. Defines a open-world long-horizon robot manipulation problem setting that is directly relevant to interactive embodied generation.
2. Introduces the core method: 3D-4D representation, spatial masks and spatiotemporal VLM.
3. Provides evidence through ST-Human with 14 tasks and 300k episodes plus RLBench and real-world tasks and makes the paper useful for our Spatial Intelligence branch.

## Task

- Input: paper-specific observations, prompts, scene assets, robot observations, or benchmark inputs described by the original source.
- Output: open-world long-horizon robot manipulation outputs, represented as generated worlds, executable assets, spatial answers, policy actions, or benchmark scores depending on branch.
- Setting: Spatial Intelligence within an interactive embodied generation reading list.
- Success criterion: strong source evidence, branch fit, usable data/method description, and visual/demo quality of `adequate` when the work depends on generation or robot execution.

## Data

- Dataset / benchmark: ST-Human with 14 tasks and 300k episodes plus RLBench and real-world tasks.
- Scale: use the scale reported by the source; exact split details should be checked in the paper before citation.
- Modalities: 3D scenes/assets, images/videos, depth/multi-view observations, robot trajectories, actions, or benchmark annotations depending on the paper.
- Collection / annotation: source-specific; this run records only primary-source claims and does not independently audit annotation pipelines.
- Splits / evaluation protocol: follow the paper/project page; local reproduction was not performed.

## Method

- Core pipeline: 3D-4D representation, spatial masks and spatiotemporal VLM.
- Model / representation: the useful abstraction for this repository is the mapping from source input to executable world representation, spatial state, robot action, or evaluation signal.
- Training or optimization: use the paper-specific training, optimization, search, or benchmark construction described by the primary source.
- Inference / deployment: relevant deployment mode is generated-scene inspection, simulator import, robot rollout, spatial VLM evaluation, or world-model benchmark execution.
- Losses or metrics: use reported metrics only as source-attributed evidence until reproduced locally.

## Key Figures / Architecture

figure_status: linked_official

- Figure / demo: official project, paper, or architecture material.
- Source: https://oucx117.github.io/ST-VLA/
- Render:
  Official figure/demo page: https://oucx117.github.io/ST-VLA/
- What it shows: the official figure/demo evidence for the method pipeline, generated results, robot execution, or benchmark design.
- Why it matters: it is the visual anchor used by Quality Reviewer; no local reproduction was performed in this initialization run.

## Evidence Trail

| Claim | Source | Status | Notes |
|---|---|---|---|
| Primary source exists and is 2024+. | https://arxiv.org/abs/2603.13788 | verified | Year recorded as 2026. |
| Dataset/method/task fields are identifiable. | https://arxiv.org/abs/2603.13788 | verified | Registry fields were extracted from primary or official descriptions. |
| Demo or visual quality decision. | https://oucx117.github.io/ST-VLA/ | verified | decision=`adequate`, score=3. |
| Project relevance. | local taxonomy and harness | verified | points to temporal/deformable state and trajectory grounding |

## Evidence

- Main metrics: The paper introduces ST-Human with 14 tasks and 300k episodes plus 3D-4D spatial masks for long-horizon manipulation.
- Qualitative results: visual/demo decision is `adequate` with score 3; generation-heavy entries need adequate or strong evidence.
- Ablations: not independently reproduced; use original paper/project ablations when citing.
- Baselines: compare against the paper's own baseline list before making SOTA claims.
- Reproducibility signals: source quality is `primary_or_official`, demo score is 3, evidence strength is 3.

## Limitations

- Method limitations: Dataset release and cross-embodiment reproduction need follow-up.
- Experimental limitations: this initialization run did not train models, download large datasets, or reproduce metrics.
- Demo / visual limitations: official examples may be curated; local reproduction or independent videos are needed before strong deployment claims.
- Claims that remain unverified: exact code/checkpoint maturity, license constraints, and benchmark leaderboard status may change after 2026-06-06.

## Project Relevance

- Relevance to interactive embodied generation: points to temporal/deformable state and trajectory grounding
- Reusable fields: Scene, Object, Part, Affordance, PhysicalProperty, SpatialRelation, StateTransition, Action, Policy, BenchmarkMetric, and ValidationReport as applicable.
- Possible baseline role: use this paper as a branch-specific baseline or validator for Spatial Intelligence.
- Implications for our task / benchmark: it helps decide whether generated scenes are only visually plausible or actually useful for interactive, spatial, physical, or policy-facing embodied tasks.

## Reproduction / Follow-up

- What to check before using: official code/data release status, license, exact benchmark split, and whether demos can be run locally.
- Code / checkpoint availability: https://oucx117.github.io/ST-VLA/.
- Citation or related-work caveats: phrase strong claims as reported by the source unless we independently reproduce them.
