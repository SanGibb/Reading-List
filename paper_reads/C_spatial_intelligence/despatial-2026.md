# DeSpatial: The devil of Agentic Spatial Reasoning Lies in 3D Itself

<!-- curation-review:start -->
> 2026-10-20 按新版标准复审：**观察名单**。主源确认感知 oracle 与实例融合设计，但当前核心增量主要是既有工具的几何修整与融合；没有足够可复用发布/统一对照来支撑独立优先入口。保留具体失败模式研究，待协议与工具落地。
> [本次来源、分数与任务判断](../library_review.md#paper-3a5eb576324a)。下文保留原精读；旧验收标签不代表本次重新通过，所有实验仍为作者报告。
<!-- curation-review:end -->

candidate_id: CAND-0006
branch: C
decision: accepted_for_registry

## Source Links

- Paper: https://arxiv.org/abs/2610.20990
- Project: not published / not located
- Code: not published / not located
- Data / benchmark: see primary paper
- Demo / video: paper figures and experiment section

## TL;DR

Diagnoses perception as the dominant bottleneck and separates scene reconciliation from downstream reasoning tools. Provides UnifiedScene, GravityFrame, InstanceFusion, ProjectionArtifact, and perception-oracle diagnostic fields. Main caveat: the release is new and its reported results have not been independently reproduced.

## Novelty

- What is actually new: Diagnoses perception as the dominant bottleneck and separates scene reconciliation from downstream reasoning tools.
- Difference from prior work: A shared metric gravity-aligned 3D perception tool co-refines segmentation/depth and fuses instances across views before tool-based reasoning.
- Why the delta matters: Provides UnifiedScene, GravityFrame, InstanceFusion, ProjectionArtifact, and perception-oracle diagnostic fields.

## Contributions

1. A shared metric gravity-aligned 3D perception tool co-refines segmentation/depth and fuses instances across views before tool-based reasoning.
2. VSI-Bench, MindCube-Tiny, ViewSpatial, and VSI-SUPER object-centric spatial reasoning tasks.
3. Primary paper reports an oracle study and leading results across four spatial benchmarks.

## Task

- Input: observations, instructions, actions, or simulator state as specified by the paper.
- Output: Build reliable unified 3D scenes for agentic spatial question answering.
- Setting: embodied or interactive-world evaluation described in the primary paper.
- Success criterion: the paper's task metrics plus the reported qualitative/physical checks.

## Data

- Dataset / benchmark: VSI-Bench, MindCube-Tiny, ViewSpatial, and VSI-SUPER object-centric spatial reasoning tasks.
- Scale: see the primary source for the exact split-level counts.
- Modalities: visual/world state and the action, geometry, force, tactile, or language channels required by the task.
- Collection / annotation: author-described pipeline; not independently audited.
- Splits / evaluation protocol: official paper protocol.

## Method

- Core pipeline: A shared metric gravity-aligned 3D perception tool co-refines segmentation/depth and fuses instances across views before tool-based reasoning.
- Model / representation: paper-specific representation summarized above.
- Training or optimization: see the official method and ablation sections.
- Inference / deployment: evaluated in the released simulation, benchmark, or robot setting.
- Losses or metrics: official paper metrics; cross-paper values are not directly comparable.

## Key Figures / Architecture

figure_status: not_applicable

- Figure / demo: official project overview/video when available; otherwise primary-paper architecture and qualitative figures.
- Source: https://arxiv.org/pdf/2610.20990
- What it shows: the system pipeline and representative task outputs or evaluation protocol.
- Why it matters: it verifies the collection-relevant representation, execution, or benchmark interface.

## Evidence Trail

| Claim | Source | Status | Notes |
|---|---|---|---|
| Data / benchmark scope | https://arxiv.org/abs/2610.20990 | verified | Author-reported in the primary paper. |
| Main reported result | https://arxiv.org/abs/2610.20990 | verified | Primary paper reports an oracle study and leading results across four spatial benchmarks. |
| Code / checkpoint / demo availability | https://arxiv.org/abs/2610.20990 | partial | No separate official project or code release located. |

## Evidence

- Main metrics: Primary paper reports an oracle study and leading results across four spatial benchmarks.
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

- Relevance to interactive embodied generation: Provides UnifiedScene, GravityFrame, InstanceFusion, ProjectionArtifact, and perception-oracle diagnostic fields.
- Reusable fields: extract the named interfaces above into structured registry/benchmark schemas.
- Possible baseline role: direct method, data, or evaluation baseline for its branch.
- Implications for our task / benchmark: motivates explicit executable state and source-traced evaluation rather than image-only plausibility.

## Reproduction / Follow-up

- What to check before using: exact splits, licenses, preprocessing, embodiment assumptions, and metric implementations.
- Code / checkpoint availability: not confirmed in this run.
- Citation or related-work caveats: cite results as author-reported and avoid direct numeric comparison across incompatible protocols.
