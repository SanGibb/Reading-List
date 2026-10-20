# DepthWorld: 3D World Model for Robot Manipulation

<!-- curation-review:start -->
> 2026-10-20 按新版标准复审：**待视觉复核**。DROID-3D因子图标定和metricdepth监督直接提供数据/validator；等训练预算RGB+1.48dB是具体控制证据，仍未检查跨view时序几何和释放。
> [本次来源、分数与任务判断](../library_review.md#paper-6195c0fbc272)。下文保留原精读；旧验收标签不代表本次重新通过，所有实验仍为作者报告。
<!-- curation-review:end -->

candidate_id: CAND-0010
branch: D
decision: accepted_for_registry

## Source Links

- Paper: https://arxiv.org/abs/2610.08780
- Project / figures / demos: https://www.jaibardhan.com/depthworld

## TL;DR

Adds large-scale metric 3D supervision to a pretrained robot video world model without replacing its visual VAE. Provides CameraCalibration, MetricDepth, Extrinsics, ReprojectionError, MultiViewFuture, and geometry-consistency fields. Central results are author-reported and were not independently reproduced in this collection run.

## Novelty

- What is new: Adds large-scale metric 3D supervision to a pretrained robot video world model without replacing its visual VAE.
- Why it matters: Provides CameraCalibration, MetricDepth, Extrinsics, ReprojectionError, MultiViewFuture, and geometry-consistency fields.
- Branch fit: the work directly contributes to branch D rather than serving only as background.

## Contributions

1. Joint factor-graph calibration pools episodes from each robot, then a tiled Stable Video Diffusion model predicts multi-view RGB and metric depth.
2. DROID-3D, a calibrated derivative of DROID with dense metric depth and recalibrated multi-view extrinsics.
3. DROID-3D achieves under 0.7 px reprojection error on 90% of episodes; depth supervision improves equal-budget RGB PSNR by 1.48 dB.

## Task

- Input / setting: official source-specific observations, task context, state, geometry, and/or actions.
- Output: Generate geometrically consistent action-conditioned robot futures for planning and evaluation.
- Success criterion: the paper's official task metrics and matched evaluation protocol.

## Data

- Dataset / benchmark: DROID-3D, a calibrated derivative of DROID with dense metric depth and recalibrated multi-view extrinsics.
- Modalities and splits: use the official paper's definitions; synthetic, simulated, and real components should not be conflated.
- Provenance: scale and collection claims are traced to the primary paper/project below.

## Method

- Core pipeline: Joint factor-graph calibration pools episodes from each robot, then a tiled Stable Video Diffusion model predicts multi-view RGB and metric depth.
- Representation and optimization: retain the source's units, coordinate frames, action conventions, and success definitions when reproducing.
- Deployment target: Generate geometrically consistent action-conditioned robot futures for planning and evaluation.

## Key Figures / Architecture

figure_status: linked_official

- Official source: https://www.jaibardhan.com/depthworld
- What was inspected: method overview, qualitative panels, benchmark/task examples, and available demo media.
- Visual decision: strong (4/5). Official project/paper qualitative panels and demo media were inspected; results were coherent and task-relevant.

## Evidence Trail

| Claim | Source | Status | Notes |
|---|---|---|---|
| Method and data | https://arxiv.org/abs/2610.08780 | verified | Primary paper surface checked. |
| Main reported result | https://arxiv.org/abs/2610.08780 | verified | Author-reported; not independently reproduced. |
| Project/code/demo availability | https://www.jaibardhan.com/depthworld | verified | Official surface checked on 2026-10-12. |

## Evidence

- Main result: DROID-3D achieves under 0.7 px reprojection error on 90% of episodes; depth supervision improves equal-budget RGB PSNR by 1.48 dB.
- Demo score: 3/5; evidence strength: 4/5.
- Qualitative evidence: Official project/paper qualitative panels and demo media were inspected; results were coherent and task-relevant.
- Comparisons remain protocol-dependent and should be cited as reported by the authors.

## Limitations

- Scope is bounded by the reported tasks, environments, embodiments, sensors, and action conventions.
- Curated demos do not expose the full long-tail failure distribution.
- Headline results were not independently reproduced during this literature-maintenance run.

## Project Relevance

- Provides CameraCalibration, MetricDepth, Extrinsics, ReprojectionError, MultiViewFuture, and geometry-consistency fields.
- Reusable fields should preserve source-specific units, coordinate frames, time bases, and simulator/hardware assumptions.
- Suitable as a related-work anchor and a candidate baseline or validator for branch D.

## Reproduction / Follow-up

- Verify licenses, exact data splits, hardware requirements, metric definitions, and checkpoint completeness before reproduction.
- Code/checkpoints: See the official paper/project; no separate fully verified repository was recorded in this run.
- Cite all metrics as source-reported until independently reproduced.
