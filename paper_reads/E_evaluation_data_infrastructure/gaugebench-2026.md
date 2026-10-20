# The Robot Is Not Its Description: GaugeBench for Representation Robustness in Morphology-Aware Policies

<!-- curation-review:start -->
> 2026-10-20 按新版标准复审：**优先阅读**。物理/接口认证后再测同机制描述变化，能直接验证URDF/关节坐标compiler或policy adapter的隐含表征假设；控制与权衡具体。
> [本次来源、分数与任务判断](../library_review.md#paper-3b6bd81a6a29)。下文保留原精读；旧验收标签不代表本次重新通过，所有实验仍为作者报告。
>
> **本轮准入依据**（技术贡献 / 直接相关性 / 证据：4 / 4 / 4）：比RoboTwin物理参数变动更严格固定物理机制，只动描述约定；不能拿普通跨形态成功率代替。
> - [Sec.III-A/B; Sec.IV; TableI; Sec.V-E/TableIII](https://arxiv.org/html/2610.07597v1)：1e-7逐项100step物理认证；3 policies×80robots×10rewrites×32episodes；轴随机化保留率3.6→80.6%，原描述回报约降10%，不得宣称无退化。（verified）。
>
> 引用指标、发布规模和比较结果时，以以上已定位来源和本次复审限制为准，不沿用下文旧概括。
<!-- curation-review:end -->

candidate_id: CAND-0015
branch: E
decision: accepted_for_registry

## Source Links

- Paper: https://arxiv.org/abs/2610.07597
- Project / figures / demos: https://arxiv.org/abs/2610.07597

## TL;DR

Separates embodiment generalization from arbitrary representation-gauge robustness. Direct validator for EmbodimentDescription, JointAxis, CoordinateConvention, LinkOrder, ActionTransport, and invariance tests. Central results are author-reported and were not independently reproduced in this collection run.

## Novelty

- What is new: Separates embodiment generalization from arbitrary representation-gauge robustness.
- Why it matters: Direct validator for EmbodimentDescription, JointAxis, CoordinateConvention, LinkOrder, ActionTransport, and invariance tests.
- Branch fit: the work directly contributes to branch E rather than serving only as background.

## Contributions

1. Rewrites axis direction, angle zero, link/joint ordering, and coordinates while verifying the physical mechanism and policy interface remain equivalent.
2. Physically equivalent rewrites of 80 familiar and 98 held-out robot mechanisms across MetaMorph, ModuMorph, and PyBullet.
3. MetaMorph return falls from 4030.6 to 51.6 under equivalent descriptions; axis-convention training raises retained return from 3.6% to 80.6%.

## Task

- Input / setting: official source-specific observations, task context, state, geometry, and/or actions.
- Output: Test whether morphology-aware policies preserve behavior under equivalent robot-description conventions.
- Success criterion: the paper's official task metrics and matched evaluation protocol.

## Data

- Dataset / benchmark: Physically equivalent rewrites of 80 familiar and 98 held-out robot mechanisms across MetaMorph, ModuMorph, and PyBullet.
- Modalities and splits: use the official paper's definitions; synthetic, simulated, and real components should not be conflated.
- Provenance: scale and collection claims are traced to the primary paper/project below.

## Method

- Core pipeline: Rewrites axis direction, angle zero, link/joint ordering, and coordinates while verifying the physical mechanism and policy interface remain equivalent.
- Representation and optimization: retain the source's units, coordinate frames, action conventions, and success definitions when reproducing.
- Deployment target: Test whether morphology-aware policies preserve behavior under equivalent robot-description conventions.

## Key Figures / Architecture

figure_status: linked_official

- Official source: https://arxiv.org/abs/2610.07597
- What was inspected: method overview, qualitative panels, benchmark/task examples, and available demo media.
- Visual decision: not_applicable (0/5). This is primarily an evaluation/data contribution; visual generation quality is not an acceptance gate.

## Evidence Trail

| Claim | Source | Status | Notes |
|---|---|---|---|
| Method and data | https://arxiv.org/abs/2610.07597 | verified | Primary paper surface checked. |
| Main reported result | https://arxiv.org/abs/2610.07597 | verified | Author-reported; not independently reproduced. |
| Project/code/demo availability | https://arxiv.org/abs/2610.07597 | verified | Official surface checked on 2026-10-12. |

## Evidence

- Main result: MetaMorph return falls from 4030.6 to 51.6 under equivalent descriptions; axis-convention training raises retained return from 3.6% to 80.6%.
- Demo score: 2/5; evidence strength: 4/5.
- Qualitative evidence: This is primarily an evaluation/data contribution; visual generation quality is not an acceptance gate.
- Comparisons remain protocol-dependent and should be cited as reported by the authors.

## Limitations

- Scope is bounded by the reported tasks, environments, embodiments, sensors, and action conventions.
- Curated demos do not expose the full long-tail failure distribution.
- Headline results were not independently reproduced during this literature-maintenance run.

## Project Relevance

- Direct validator for EmbodimentDescription, JointAxis, CoordinateConvention, LinkOrder, ActionTransport, and invariance tests.
- Reusable fields should preserve source-specific units, coordinate frames, time bases, and simulator/hardware assumptions.
- Suitable as a related-work anchor and a candidate baseline or validator for branch E.

## Reproduction / Follow-up

- Verify licenses, exact data splits, hardware requirements, metric definitions, and checkpoint completeness before reproduction.
- Code/checkpoints: See the official paper/project; no separate fully verified repository was recorded in this run.
- Cite all metrics as source-reported until independently reproduced.
