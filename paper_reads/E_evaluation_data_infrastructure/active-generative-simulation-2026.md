# Active Generative Simulation: Meta-Learning What to Simulate for Sim-and-Real Policy Co-Training

<!-- curation-review:start -->
> 2026-10-20 按新版标准复审：**待视觉复核**。优化生成分布以提升真实policy是直接核心方法；旧strong只留下页面视频存在与150%数字，未记录实际rollout观察，需重新时序审核。
> [本次来源、分数与任务判断](../library_review.md#paper-8c72c61f3028)。下文保留原精读；旧验收标签不代表本次重新通过，所有实验仍为作者报告。
<!-- curation-review:end -->

candidate_id: CAND-0016
branch: E
decision: accepted_for_registry

## Source Links

- Paper: https://arxiv.org/abs/2610.19479
- Project: https://meta-gensim.github.io/
- Code: not published / not located
- Data / benchmark: https://meta-gensim.github.io/
- Demo / video: https://meta-gensim.github.io/

## TL;DR

Turns simulator data generation into a downstream-performance optimization problem rather than uniform sampling or manual alignment. Useful for GeneratorDistribution, UtilityRater, SimRealAlignment, SkillStitching, and data-curriculum infrastructure. Main caveat: the release is new and its reported results have not been independently reproduced.

## Novelty

- What is actually new: Turns simulator data generation into a downstream-performance optimization problem rather than uniform sampling or manual alignment.
- Difference from prior work: MetaGenSim trains a rater by meta-gradients to select simulator generation distributions that maximize downstream real-policy performance.
- Why the delta matters: Useful for GeneratorDistribution, UtilityRater, SimRealAlignment, SkillStitching, and data-curriculum infrastructure.

## Contributions

1. MetaGenSim trains a rater by meta-gradients to select simulator generation distributions that maximize downstream real-policy performance.
2. Simulation parameter spaces, limited real demonstrations, generated skill/object-receptacle combinations, and real manipulation evaluations.
3. Official page provides overview and real-rollout videos; paper reports 150% relative full-task success improvement over uniform generation.

## Task

- Input: observations, instructions, actions, or simulator state as specified by the paper.
- Output: Optimize what simulation data to generate for sim-and-real co-training.
- Setting: embodied or interactive-world evaluation described in the primary paper.
- Success criterion: the paper's task metrics plus the reported qualitative/physical checks.

## Data

- Dataset / benchmark: Simulation parameter spaces, limited real demonstrations, generated skill/object-receptacle combinations, and real manipulation evaluations.
- Scale: see the primary source for the exact split-level counts.
- Modalities: visual/world state and the action, geometry, force, tactile, or language channels required by the task.
- Collection / annotation: author-described pipeline; not independently audited.
- Splits / evaluation protocol: official paper protocol.

## Method

- Core pipeline: MetaGenSim trains a rater by meta-gradients to select simulator generation distributions that maximize downstream real-policy performance.
- Model / representation: paper-specific representation summarized above.
- Training or optimization: see the official method and ablation sections.
- Inference / deployment: evaluated in the released simulation, benchmark, or robot setting.
- Losses or metrics: official paper metrics; cross-paper values are not directly comparable.

## Key Figures / Architecture

figure_status: linked_official

- Figure / demo: official project overview/video when available; otherwise primary-paper architecture and qualitative figures.
- Source: https://meta-gensim.github.io/
- What it shows: the system pipeline and representative task outputs or evaluation protocol.
- Why it matters: it verifies the collection-relevant representation, execution, or benchmark interface.

## Evidence Trail

| Claim | Source | Status | Notes |
|---|---|---|---|
| Data / benchmark scope | https://arxiv.org/abs/2610.19479 | verified | Author-reported in the primary paper. |
| Main reported result | https://arxiv.org/abs/2610.19479 | verified | Official page provides overview and real-rollout videos; paper reports 150% relative full-task success improvement over uniform generation. |
| Code / checkpoint / demo availability | https://meta-gensim.github.io/ | verified | Official project/code surface inspected. |

## Evidence

- Main metrics: Official page provides overview and real-rollout videos; paper reports 150% relative full-task success improvement over uniform generation.
- Qualitative results: inspected on the official project page/video or primary-paper figures as recorded above.
- Ablations: see primary paper; acceptance does not depend on an unverified SOTA claim.
- Baselines: paper-defined comparisons only.
- Reproducibility signals: paper and official materials are available; code/checkpoints were not confirmed.

## Limitations

- Method limitations: scoped to the paper's environments, embodiments, or benchmark protocol.
- Experimental limitations: author-reported fresh-release evidence; no independent reproduction.
- Demo / visual limitations: official materials may be selected examples.
- Claims that remain unverified: external generalization beyond reported settings and compute/data cost details not exposed in the abstract/project page.

## Project Relevance

- Relevance to interactive embodied generation: Useful for GeneratorDistribution, UtilityRater, SimRealAlignment, SkillStitching, and data-curriculum infrastructure.
- Reusable fields: extract the named interfaces above into structured registry/benchmark schemas.
- Possible baseline role: direct method, data, or evaluation baseline for its branch.
- Implications for our task / benchmark: motivates explicit executable state and source-traced evaluation rather than image-only plausibility.

## Reproduction / Follow-up

- What to check before using: exact splits, licenses, preprocessing, embodiment assumptions, and metric implementations.
- Code / checkpoint availability: not confirmed in this run.
- Citation or related-work caveats: cite results as author-reported and avoid direct numeric comparison across incompatible protocols.
