# Universal Navigation Interface: Robot-Free Data for Wheeled Robot Navigation

<!-- curation-review:start -->
> 2026-10-20 按新版标准复审：**观察名单**。目标机器人之外的rollator采集设计有启发，但规模和跨域收益有限，当前对项目主要是导航数据支撑层，不满足核心技术/相关性门槛。
> [本次来源、分数与任务判断](../library_review.md#paper-5fd7cf511013)。下文保留原精读；旧验收标签不代表本次重新通过，所有实验仍为作者报告。
<!-- curation-review:end -->

candidate_id: CAND-0006
branch: E
decision: accepted_for_registry

## Source Links

- Paper: https://arxiv.org/abs/2609.20114
- Project / data / videos: https://universal-nav.github.io/

## TL;DR

UNI collects navigation demonstrations with a smartphone-equipped rollator whose mechanics naturally enforce wheeled feasibility. The resulting 37.2 km corpus improves trajectory prediction and transfers to a powered wheelchair.

## Novelty

- Encodes target-embodiment constraints in a cheap human-operated proxy.
- Avoids target-robot teleoperation while producing metric goal-conditioned trajectories.

## Contributions

1. Reproducible physical collection interface.
2. 37.2 km real-world corpus.
3. Closed-loop wheelchair transfer evidence.

## Task

- Input: egocentric smartphone observations and goal.
- Output: metric wheeled trajectory.
- Success: prediction accuracy and safe closed-loop navigation around curbs/stairs.

## Data

37.2 km of rollator trajectories with recovered metric paths and held-out evaluation splits.

## Method

Physical constraints of the rollator bias human demonstrations toward routes a wheeled robot can execute; models are fine-tuned on the aligned trajectories.

## Key Figures / Architecture

figure_status: linked_official

- Assembly, collection, replay, and powered-wheelchair videos: https://universal-nav.github.io/

## Evidence Trail

| Claim | Source | Status | Notes |
|---|---|---|---|
| 37.2 km collected | https://arxiv.org/abs/2609.20114 | verified | Primary abstract. |
| 17.4-24.8% trajectory-error reduction | https://arxiv.org/abs/2609.20114 | verified | Author-reported. |
| Closed-loop wheelchair transfer | https://universal-nav.github.io/ | verified | Official videos inspected. |

## Evidence

- Curb, staircase, and curb-cut scenarios expose the feasibility prior.
- Cross-dataset gains vary, which appropriately bounds the claim.

## Limitations

- Specific to wheeled navigation.
- Proxy constraints do not encode every powered platform's dynamics.

## Project Relevance

Useful design for `CollectionEmbodiment`, `FeasibilityConstraint`, `MetricTrajectory`, and low-cost data provenance.

## Reproduction / Follow-up

- Audit trajectory calibration and licensing.
- Test on additional wheelchair/AMR morphologies.
