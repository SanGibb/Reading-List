# TacClaw-Infinity: A Large-Scale Vision-Tactile-Language-Action Dataset for Dexterous Manipulation

<!-- curation-review:start -->
> 2026-10-20 按新版标准复审：**待视觉复核**。大规模VTLA、质量过滤及无目标机器人采集有核心潜力，但数据/许可尚未确证，且跨三机器人迁移是其核心效用，不能用static论文代替时序检查。
> [本次来源、分数与任务判断](../library_review.md#paper-8f00ff5a9d8d)。下文保留原精读；旧验收标签不代表本次重新通过，所有实验仍为作者报告。
<!-- curation-review:end -->

candidate_id: CAND-0015
branch: E
decision: accepted_for_registry

## Source Links

- Paper: https://arxiv.org/abs/2610.20320
- Project: not published / not located
- Code: not published / not located
- Data / benchmark: see primary paper
- Demo / video: paper figures and experiment section

## TL;DR

Combines unprecedented VTLA scale with contact segmentation, subtasks, spatial grounding, and collection independent of the target robot. Direct source for VisionTactileLanguageAction, ContactSegment, QualityFilter, EmbodimentMap, and large-scale manipulation data schemas. Main caveat: the release is new and its reported results have not been independently reproduced.

## Novelty

- What is actually new: Combines unprecedented VTLA scale with contact segmentation, subtasks, spatial grounding, and collection independent of the target robot.
- Difference from prior work: A tactile UMI-style handheld interface plus distributed collection, trajectory reconstruction, embodiment-aware filtering, quality control, and structured contact/spatial annotation.
- Why the delta matters: Direct source for VisionTactileLanguageAction, ContactSegment, QualityFilter, EmbodimentMap, and large-scale manipulation data schemas.

## Contributions

1. A tactile UMI-style handheld interface plus distributed collection, trajectory reconstruction, embodiment-aware filtering, quality control, and structured contact/spatial annotation.
2. Over 10,000 hours, one million episodes, and one billion frames across more than 1,000 tasks, with synchronized vision, fingertip tactile, language, and actions.
3. Primary paper reports data- and model-level validation plus transfer to three robots without robot-specific demonstrations.

## Task

- Input: observations, instructions, actions, or simulator state as specified by the paper.
- Output: Scale contact-rich VTLA demonstrations and test cross-embodiment dexterous transfer.
- Setting: embodied or interactive-world evaluation described in the primary paper.
- Success criterion: the paper's task metrics plus the reported qualitative/physical checks.

## Data

- Dataset / benchmark: Over 10,000 hours, one million episodes, and one billion frames across more than 1,000 tasks, with synchronized vision, fingertip tactile, language, and actions.
- Scale: see the primary source for the exact split-level counts.
- Modalities: visual/world state and the action, geometry, force, tactile, or language channels required by the task.
- Collection / annotation: author-described pipeline; not independently audited.
- Splits / evaluation protocol: official paper protocol.

## Method

- Core pipeline: A tactile UMI-style handheld interface plus distributed collection, trajectory reconstruction, embodiment-aware filtering, quality control, and structured contact/spatial annotation.
- Model / representation: paper-specific representation summarized above.
- Training or optimization: see the official method and ablation sections.
- Inference / deployment: evaluated in the released simulation, benchmark, or robot setting.
- Losses or metrics: official paper metrics; cross-paper values are not directly comparable.

## Key Figures / Architecture

figure_status: not_applicable

- Figure / demo: official project overview/video when available; otherwise primary-paper architecture and qualitative figures.
- Source: https://arxiv.org/pdf/2610.20320
- What it shows: the system pipeline and representative task outputs or evaluation protocol.
- Why it matters: it verifies the collection-relevant representation, execution, or benchmark interface.

## Evidence Trail

| Claim | Source | Status | Notes |
|---|---|---|---|
| Data / benchmark scope | https://arxiv.org/abs/2610.20320 | verified | Author-reported in the primary paper. |
| Main reported result | https://arxiv.org/abs/2610.20320 | verified | Primary paper reports data- and model-level validation plus transfer to three robots without robot-specific demonstrations. |
| Code / checkpoint / demo availability | https://arxiv.org/abs/2610.20320 | partial | No separate official project or code release located. |

## Evidence

- Main metrics: Primary paper reports data- and model-level validation plus transfer to three robots without robot-specific demonstrations.
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

- Relevance to interactive embodied generation: Direct source for VisionTactileLanguageAction, ContactSegment, QualityFilter, EmbodimentMap, and large-scale manipulation data schemas.
- Reusable fields: extract the named interfaces above into structured registry/benchmark schemas.
- Possible baseline role: direct method, data, or evaluation baseline for its branch.
- Implications for our task / benchmark: motivates explicit executable state and source-traced evaluation rather than image-only plausibility.

## Reproduction / Follow-up

- What to check before using: exact splits, licenses, preprocessing, embodiment assumptions, and metric implementations.
- Code / checkpoint availability: not confirmed in this run.
- Citation or related-work caveats: cite results as author-reported and avoid direct numeric comparison across incompatible protocols.
