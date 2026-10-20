# RoboTwin-Phys: Do WAMs and VLAs Understand the Physical World?

<!-- curation-review:start -->
> 2026-10-20 按新版标准复审：**参考备选**。连续物理条件轴对生成环境有效性有直接价值，和视觉/语言扰动有独立作用；具体参数范围、成功率曲线与公开release仍未核实。
> [本次来源、分数与任务判断](../library_review.md#paper-dac2d1f3a1bc)。下文保留原精读；旧验收标签不代表本次重新通过，所有实验仍为作者报告。
<!-- curation-review:end -->

candidate_id: CAND-0010
branch: E
decision: accepted_for_registry

## Source Links

- Paper: https://arxiv.org/abs/2609.26292
- Data / benchmark: described in the primary technical report; dedicated public project URL not found this run.

## TL;DR

RoboTwin-Phys adds continuous physical-condition variation—mass, friction, joint dynamics, and ten other attributes—to robot policy evaluation, with 5,000+ demonstrations and ground truth. It fills an important gap left by appearance/layout randomization, though the release currently lacks a dedicated project/code surface.

## Novelty

- Treats physical-condition diversity as a first-class benchmark axis.
- Uses continuous, plausible parameter ranges rather than discrete visual perturbations.
- Exposes ground-truth physics for estimation and condition-aware training.

## Contributions

1. Thirteen varied physical attributes.
2. More than 5,000 expert demonstrations with parameter ground truth.
3. Comparative WAM/VLA robustness evaluation.

## Task

- Input: robot observation/instruction under hidden or explicit physical conditions.
- Output: manipulation actions and optionally physical-attribute estimates.
- Setting: RoboTwin simulation with controlled physics sweeps.
- Success criterion: robust task success across condition ranges.

## Data

- 5,000+ expert demonstrations paired with physical parameters.
- Variations include mass, friction, and joint dynamics among 13 attributes.

## Method

- Continuously randomize attributes within plausible ranges.
- Evaluate representative WAMs and VLAs under matched tasks.
- Support physical estimation, condition-aware modeling, and physics-conditioned policy training.

## Key Figures / Architecture

figure_status: linked_official

- Figure / demo: benchmark protocol and parameter/result figures in the official paper.
- Source: https://arxiv.org/abs/2609.26292
- What it shows: performance degradation under physics shifts despite visual/layout robustness.

## Evidence Trail

| Claim | Source | Status | Notes |
|---|---|---|---|
| 13 physical attributes | https://arxiv.org/abs/2609.26292 | verified | Primary technical report. |
| 5,000+ demonstrations with ground truth | https://arxiv.org/abs/2609.26292 | verified | Primary report. |
| Public code/data download | https://arxiv.org/abs/2609.26292 | partial | Described as released; dedicated URL not found. |

## Evidence

- Representative models degrade markedly under physical changes even when robust to visual/layout randomization.
- Ground-truth parameters enable both diagnosis and condition-aware training.

## Limitations

- Simulation-centered and dependent on RoboTwin physics fidelity.
- No dedicated official project/code page was located.
- Aggregate robustness can hide attribute-specific failures.

## Project Relevance

Defines `Mass`, `Friction`, `JointDynamics`, `PhysicalCondition`, `ParameterGroundTruth`, and physics-robustness evaluation fields.

## Reproduction / Follow-up

- Locate and pin the eventual official release before reproduction.
- Report per-attribute curves, not only aggregate success.

