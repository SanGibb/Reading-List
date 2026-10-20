# ForceBench: Benchmarking Force Integration for Robotic Manipulation

<!-- curation-review:start -->
> 2026-10-20 按新版标准复审：**观察名单**。固定pi0.5比较腕力融合是有用窄域设计研究，八任务/五实机任务与未确认code尚不足支持长期核心；不能以最佳均值替代所有任务。
> [本次来源、分数与任务判断](../library_review.md#paper-9c5c2fc42b1f)。下文保留原精读；旧验收标签不代表本次重新通过，所有实验仍为作者报告。
<!-- curation-review:end -->

candidate_id: CAND-0014
branch: E
decision: accepted_for_registry

## Source Links

- Paper: https://arxiv.org/abs/2610.19604
- Project: https://forcebench-platform.github.io/
- Code: not published / not located
- Data / benchmark: https://forcebench-platform.github.io/
- Demo / video: https://forcebench-platform.github.io/

## TL;DR

Provides a unified protocol that separates force-fusion architecture effects from task and control differences. Adds ForceObservation, FusionDesign, Resistance, ContactAssembly, and sim/real force-integration evaluation fields. Main caveat: the release is new and its reported results have not been independently reproduced.

## Novelty

- What is actually new: Provides a unified protocol that separates force-fusion architecture effects from task and control differences.
- Difference from prior work: Controls backbone, demonstrations, task criteria, and evaluation protocol to isolate visual-force fusion design choices.
- Why the delta matters: Adds ForceObservation, FusionDesign, Resistance, ContactAssembly, and sim/real force-integration evaluation fields.

## Contributions

1. Controls backbone, demonstrations, task criteria, and evaluation protocol to isolate visual-force fusion design choices.
2. Eight tasks, 1,600 synchronized demonstrations, six-axis wrist force, seven integration designs, and five real-world tasks.
3. Official page provides an overview video; paper reports 35.31% vs 23.25% simulation success and 63% vs 40% real-world success for the strongest designs.

## Task

- Input: observations, instructions, actions, or simulator state as specified by the paper.
- Output: Benchmark how force observations should be integrated into VLA policies for physical-property, resistance, and assembly tasks.
- Setting: embodied or interactive-world evaluation described in the primary paper.
- Success criterion: the paper's task metrics plus the reported qualitative/physical checks.

## Data

- Dataset / benchmark: Eight tasks, 1,600 synchronized demonstrations, six-axis wrist force, seven integration designs, and five real-world tasks.
- Scale: see the primary source for the exact split-level counts.
- Modalities: visual/world state and the action, geometry, force, tactile, or language channels required by the task.
- Collection / annotation: author-described pipeline; not independently audited.
- Splits / evaluation protocol: official paper protocol.

## Method

- Core pipeline: Controls backbone, demonstrations, task criteria, and evaluation protocol to isolate visual-force fusion design choices.
- Model / representation: paper-specific representation summarized above.
- Training or optimization: see the official method and ablation sections.
- Inference / deployment: evaluated in the released simulation, benchmark, or robot setting.
- Losses or metrics: official paper metrics; cross-paper values are not directly comparable.

## Key Figures / Architecture

figure_status: not_applicable

- Figure / demo: official project overview/video when available; otherwise primary-paper architecture and qualitative figures.
- Source: https://forcebench-platform.github.io/
- What it shows: the system pipeline and representative task outputs or evaluation protocol.
- Why it matters: it verifies the collection-relevant representation, execution, or benchmark interface.

## Evidence Trail

| Claim | Source | Status | Notes |
|---|---|---|---|
| Data / benchmark scope | https://arxiv.org/abs/2610.19604 | verified | Author-reported in the primary paper. |
| Main reported result | https://arxiv.org/abs/2610.19604 | verified | Official page provides an overview video; paper reports 35.31% vs 23.25% simulation success and 63% vs 40% real-world success for the strongest designs. |
| Code / checkpoint / demo availability | https://forcebench-platform.github.io/ | verified | Official project/code surface inspected. |

## Evidence

- Main metrics: Official page provides an overview video; paper reports 35.31% vs 23.25% simulation success and 63% vs 40% real-world success for the strongest designs.
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

- Relevance to interactive embodied generation: Adds ForceObservation, FusionDesign, Resistance, ContactAssembly, and sim/real force-integration evaluation fields.
- Reusable fields: extract the named interfaces above into structured registry/benchmark schemas.
- Possible baseline role: direct method, data, or evaluation baseline for its branch.
- Implications for our task / benchmark: motivates explicit executable state and source-traced evaluation rather than image-only plausibility.

## Reproduction / Follow-up

- What to check before using: exact splits, licenses, preprocessing, embodiment assumptions, and metric implementations.
- Code / checkpoint availability: not confirmed in this run.
- Citation or related-work caveats: cite results as author-reported and avoid direct numeric comparison across incompatible protocols.
