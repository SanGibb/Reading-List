# GeoState: Learning View-Decoupled Geometry States for 3D World Modeling

<!-- curation-review:start -->
> 2026-10-20 按新版标准复审：**观察名单**。主源证实drivinggeometryforecasting及cross-viewquery，但未展示机器人action-intervention接口。作为3D状态表示背景，与本repo具体操控任务仅单层支撑。
> [本次来源、分数与任务判断](../library_review.md#paper-44a91b7395e1)。下文保留原精读；旧验收标签不代表本次重新通过，所有实验仍为作者报告。
<!-- curation-review:end -->

candidate_id: CAND-0009
branch: D
decision: accepted_for_registry

## Source Links

- Paper: https://arxiv.org/abs/2610.22343
- Project: https://hongchang-liu.github.io/GeoState-project-page/
- Code: https://github.com/Hongchang-Liu/GeoState
- Data / benchmark: https://hongchang-liu.github.io/GeoState-project-page/
- Demo / video: https://hongchang-liu.github.io/GeoState-project-page/

## TL;DR

Decouples predictive geometry state from viewpoint while preserving one context-derived scale over rollout. Provides ViewDecoupledState, CameraMotion, MetricScale, RayQuery, and cross-view rollout interfaces. Main caveat: the release is new and its reported results have not been independently reproduced.

## Novelty

- What is actually new: Decouples predictive geometry state from viewpoint while preserving one context-derived scale over rollout.
- Difference from prior work: A scene tokenizer aggregates geometry-foundation-model features into view-decoupled state; a ray-query decoder and autoregressive model separate scene dynamics from camera motion.
- Why the delta matters: Provides ViewDecoupledState, CameraMotion, MetricScale, RayQuery, and cross-view rollout interfaces.

## Contributions

1. A scene tokenizer aggregates geometry-foundation-model features into view-decoupled state; a ray-query decoder and autoregressive model separate scene dynamics from camera motion.
2. Waymo training/evaluation with zero-shot transfer to KITTI and nuScenes.
3. Official page supplies code and a promotional results video; the paper reports Waymo gains and zero-shot KITTI/nuScenes transfer.

## Task

- Input: observations, instructions, actions, or simulator state as specified by the paper.
- Output: Predict metric 3D scene-state evolution and query it from arbitrary cameras.
- Setting: embodied or interactive-world evaluation described in the primary paper.
- Success criterion: the paper's task metrics plus the reported qualitative/physical checks.

## Data

- Dataset / benchmark: Waymo training/evaluation with zero-shot transfer to KITTI and nuScenes.
- Scale: see the primary source for the exact split-level counts.
- Modalities: visual/world state and the action, geometry, force, tactile, or language channels required by the task.
- Collection / annotation: author-described pipeline; not independently audited.
- Splits / evaluation protocol: official paper protocol.

## Method

- Core pipeline: A scene tokenizer aggregates geometry-foundation-model features into view-decoupled state; a ray-query decoder and autoregressive model separate scene dynamics from camera motion.
- Model / representation: paper-specific representation summarized above.
- Training or optimization: see the official method and ablation sections.
- Inference / deployment: evaluated in the released simulation, benchmark, or robot setting.
- Losses or metrics: official paper metrics; cross-paper values are not directly comparable.

## Key Figures / Architecture

figure_status: linked_official

- Figure / demo: official project overview/video when available; otherwise primary-paper architecture and qualitative figures.
- Source: https://hongchang-liu.github.io/GeoState-project-page/
- What it shows: the system pipeline and representative task outputs or evaluation protocol.
- Why it matters: it verifies the collection-relevant representation, execution, or benchmark interface.

## Evidence Trail

| Claim | Source | Status | Notes |
|---|---|---|---|
| Data / benchmark scope | https://arxiv.org/abs/2610.22343 | verified | Author-reported in the primary paper. |
| Main reported result | https://arxiv.org/abs/2610.22343 | verified | Official page supplies code and a promotional results video; the paper reports Waymo gains and zero-shot KITTI/nuScenes transfer. |
| Code / checkpoint / demo availability | https://hongchang-liu.github.io/GeoState-project-page/ | verified | Official project/code surface inspected. |

## Evidence

- Main metrics: Official page supplies code and a promotional results video; the paper reports Waymo gains and zero-shot KITTI/nuScenes transfer.
- Qualitative results: inspected on the official project page/video or primary-paper figures as recorded above.
- Ablations: see primary paper; acceptance does not depend on an unverified SOTA claim.
- Baselines: paper-defined comparisons only.
- Reproducibility signals: official code/project assets are available.

## Limitations

- Method limitations: scoped to the paper's environments, embodiments, or benchmark protocol.
- Experimental limitations: author-reported fresh-release evidence; no independent reproduction.
- Demo / visual limitations: official materials may be selected examples.
- Claims that remain unverified: external generalization beyond reported settings and compute/data cost details not exposed in the abstract/project page.

## Project Relevance

- Relevance to interactive embodied generation: Provides ViewDecoupledState, CameraMotion, MetricScale, RayQuery, and cross-view rollout interfaces.
- Reusable fields: extract the named interfaces above into structured registry/benchmark schemas.
- Possible baseline role: direct method, data, or evaluation baseline for its branch.
- Implications for our task / benchmark: motivates explicit executable state and source-traced evaluation rather than image-only plausibility.

## Reproduction / Follow-up

- What to check before using: exact splits, licenses, preprocessing, embodiment assumptions, and metric implementations.
- Code / checkpoint availability: https://github.com/Hongchang-Liu/GeoState.
- Citation or related-work caveats: cite results as author-reported and avoid direct numeric comparison across incompatible protocols.
