# TwinVLA: Data-Efficient Bimanual Manipulation with Twin Single-Arm Vision-Language-Action Models

candidate_id: CAND-0040
branch: D
decision: accepted_for_registry
authors: Im et al.
year: 2025
venue: ICLR

## Source Links

- Paper: https://arxiv.org/abs/2511.05275
- Project: https://jellyho.github.io/TwinVLA/
- Code: https://jellyho.github.io/TwinVLA/
- Data / benchmark: https://jellyho.github.io/TwinVLA/
- Demo / video: https://jellyho.github.io/TwinVLA/
- Official figures: https://jellyho.github.io/TwinVLA/

## TL;DR

TwinVLA: Data-Efficient Bimanual Manipulation with Twin Single-Arm Vision-Language-Action Models is included because it addresses **data-efficient bimanual manipulation from vision-language instructions** with a method centered on **modular composition of two pretrained single-arm VLA policies into a coordinated bimanual policy**. For our repository, the important point is not venue alone but that the work gives concrete evidence for vision-language-action models, robot foundation policies, and action-conditioned world models. Main caveat: It is bimanual-policy focused; use as baseline for dexterous/bimanual tasks rather than general world generation.

## Novelty

- What is actually new: reuses single-arm data and policies instead of requiring full bimanual pretraining.
- Difference from prior work: it adds executable, interactive, physical, spatial, or policy-facing structure rather than stopping at static visual quality.
- Why the delta matters: our target task needs generated or reconstructed worlds that agents can reason about, validate, or act in, so this paper contributes reusable structure rather than only a visual sample gallery.

## Contributions

1. Defines a data-efficient bimanual manipulation from vision-language instructions problem setting that is directly relevant to interactive embodied generation.
2. Introduces the core method: modular composition of two pretrained single-arm VLA policies into a coordinated bimanual policy.
3. Provides evidence through single-arm public robot data plus bimanual real-world and simulation task evaluations and makes the paper useful for our VLA and World-Action Models branch.

## Task

- Input: paper-specific observations, prompts, scene assets, robot observations, or benchmark inputs described by the original source.
- Output: data-efficient bimanual manipulation from vision-language instructions outputs, represented as generated worlds, executable assets, spatial answers, policy actions, or benchmark scores depending on branch.
- Setting: VLA and World-Action Models within an interactive embodied generation reading list.
- Success criterion: strong source evidence, branch fit, usable data/method description, and visual/demo quality of `strong` when the work depends on generation or robot execution.

## Data

- Dataset / benchmark: single-arm public robot data plus bimanual real-world and simulation task evaluations.
- Scale: use the scale reported by the source; exact split details should be checked in the paper before citation.
- Modalities: 3D scenes/assets, images/videos, depth/multi-view observations, robot trajectories, actions, or benchmark annotations depending on the paper.
- Collection / annotation: source-specific; this run records only primary-source claims and does not independently audit annotation pipelines.
- Splits / evaluation protocol: follow the paper/project page; local reproduction was not performed.

## Method

- Core pipeline: modular composition of two pretrained single-arm VLA policies into a coordinated bimanual policy.
- Model / representation: the useful abstraction for this repository is the mapping from source input to executable world representation, spatial state, robot action, or evaluation signal.
- Training or optimization: use the paper-specific training, optimization, search, or benchmark construction described by the primary source.
- Inference / deployment: relevant deployment mode is generated-scene inspection, simulator import, robot rollout, spatial VLM evaluation, or world-model benchmark execution.
- Losses or metrics: use reported metrics only as source-attributed evidence until reproduced locally.

## Key Figures / Architecture

figure_status: linked_official

- Figure / demo: official project, paper, or architecture material.
- Source: https://jellyho.github.io/TwinVLA/
- Render:
  Official figure/demo page: https://jellyho.github.io/TwinVLA/
- What it shows: the official figure/demo evidence for the method pipeline, generated results, robot execution, or benchmark design.
- Why it matters: it is the visual anchor used by Quality Reviewer; no local reproduction was performed in this initialization run.

## Evidence Trail

| Claim | Source | Status | Notes |
|---|---|---|---|
| Primary source exists and is 2024+. | https://arxiv.org/abs/2511.05275 | verified | Year recorded as 2025. |
| Dataset/method/task fields are identifiable. | https://arxiv.org/abs/2511.05275 | verified | Registry fields were extracted from primary or official descriptions. |
| Demo or visual quality decision. | https://jellyho.github.io/TwinVLA/ | verified | decision=`strong`, score=4. |
| Project relevance. | local taxonomy and harness | verified | Good baseline for bimanual task generation and policy-evaluation suites. |

## Evidence

- Main metrics: Official ICLR 2026 page reports composing two single-arm VLAs for bimanual tasks without bimanual pretraining.
- Qualitative results: visual/demo decision is `strong` with score 4; generation-heavy entries need adequate or strong evidence.
- Ablations: not independently reproduced; use original paper/project ablations when citing.
- Baselines: compare against the paper's own baseline list before making SOTA claims.
- Reproducibility signals: source quality is `primary_or_official`, demo score is 4, evidence strength is 5.

## Limitations

- Method limitations: It is bimanual-policy focused; use as baseline for dexterous/bimanual tasks rather than general world generation.
- Experimental limitations: this initialization run did not train models, download large datasets, or reproduce metrics.
- Demo / visual limitations: official examples may be curated; local reproduction or independent videos are needed before strong deployment claims.
- Claims that remain unverified: exact code/checkpoint maturity, license constraints, and benchmark leaderboard status may change after 2026-06-06.

## Project Relevance

- Relevance to interactive embodied generation: Good baseline for bimanual task generation and policy-evaluation suites.
- Reusable fields: Scene, Object, Part, Affordance, PhysicalProperty, SpatialRelation, StateTransition, Action, Policy, BenchmarkMetric, and ValidationReport as applicable.
- Possible baseline role: use this paper as a branch-specific baseline or validator for VLA and World-Action Models.
- Implications for our task / benchmark: it helps decide whether generated scenes are only visually plausible or actually useful for interactive, spatial, physical, or policy-facing embodied tasks.

## Reproduction / Follow-up

- What to check before using: official code/data release status, license, exact benchmark split, and whether demos can be run locally.
- Code / checkpoint availability: https://jellyho.github.io/TwinVLA/.
- Citation or related-work caveats: phrase strong claims as reported by the source unless we independently reproduce them.
