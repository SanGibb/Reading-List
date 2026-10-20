# Streaming-WAM: Action-Conditioned World-Action Model for Asynchronous Robot Manipulation

<!-- curation-review:start -->
> 2026-10-20 按新版标准复审：**观察名单**。committed action前缀明确改善异步预测对齐，但本轮仅摘要98.35%、2.93x时间和单Stamp例子，尚不足distinguish为主阅读新能力。
> [本次来源、分数与任务判断](../library_review.md#paper-28a63f20d0fb)。下文保留原精读；旧验收标签不代表本次重新通过，所有实验仍为作者报告。
<!-- curation-review:end -->

candidate_id: CAND-0006
branch: D
decision: accepted_for_registry

## Source Links

- Paper: https://arxiv.org/abs/2609.28927
- Project / demos / models: https://sjtu-deng-lab.github.io/Streaming-WAM/
- Code: https://github.com/SJTU-DENG-Lab/Streaming-WAM

## TL;DR

Streaming-WAM overlaps prediction with execution while conditioning the next visual future on actions already committed during inference. The open implementation and real-robot timing gains make this a strong systems reference for continuous WAM control; task breadth is still limited.

## Novelty

- Treats committed actions as a fixed prefix of the next action chunk.
- Routes that prefix into future visual prediction so asynchronous inference remains aligned.
- Produces the remaining actions and future video in one streaming update.

## Contributions

1. Action-conditioned cross-chunk attention for streaming WAMs.
2. Open code, models, tests, and example configurations.
3. Simulation and real-robot speed/success evaluation.

## Task

- Input: latest observation, instruction/state, and actions scheduled during inference.
- Output: aligned next visual/action chunks.
- Setting: uninterrupted asynchronous robot manipulation.
- Success criterion: high task success with lower total and chunk time.

## Data

- LIBERO, RoboTwin 2.0, and real stamp/block manipulation.

## Method

- Cold start matches a standard joint WAM.
- During execution, committed actions populate known condition slots.
- The next stream update predicts scene consequences and remaining actions concurrently.

## Key Figures / Architecture

figure_status: linked_official

- Figure / demo: synchronous-vs-streaming timeline, attention mask, and robot rollouts.
- Source: https://sjtu-deng-lab.github.io/Streaming-WAM/
- What it shows: continuous execution without observation/action misalignment.

## Evidence Trail

| Claim | Source | Status | Notes |
|---|---|---|---|
| 98.35% LIBERO average | https://sjtu-deng-lab.github.io/Streaming-WAM/ | verified | Official result. |
| Stamp task 90 s to 38 s | https://arxiv.org/abs/2609.28927 | verified | Primary report. |
| Code/models released | https://github.com/SJTU-DENG-Lab/Streaming-WAM | verified | Public repository. |

## Evidence

- Reported average episode time improves 2.93x over Fast-WAM.
- RoboTwin success improves 4.74 points over FastWAM-Joint while total time drops.

## Limitations

- Limited real-task variety and short evaluation horizon.
- Incorrect committed actions can propagate into predicted futures.

## Project Relevance

Defines `CommittedActionPrefix`, `StreamUpdate`, `ConditionSlot`, `ExecutionOverlap`, and end-to-end timing fields.

## Reproduction / Follow-up

- Run repository tests and reproduce timing on matched hardware.
- Evaluate recovery when committed actions are interrupted or clipped.

