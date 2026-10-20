# Long-WAM: Scaling the Context of World-Action Models

<!-- curation-review:start -->
> 2026-10-20 按新版标准复审：**待视觉复核**。longhistory收益依赖ARpretraining以及107.4ms系统实现是可区分能力；主源context ablation具体，但本轮未观看动态杯堆与长期恢复，不能据摘要判当前最佳。
> [本次来源、分数与任务判断](../library_review.md#paper-2794e21dec6b)。下文保留原精读；旧验收标签不代表本次重新通过，所有实验仍为作者报告。
<!-- curation-review:end -->

candidate_id: CAND-0009
branch: D
decision: accepted_for_registry

## Source Links

- Paper: https://arxiv.org/abs/2610.10528
- Project / figures / demos: https://arxiv.org/abs/2610.10528

## TL;DR

Shows long context benefits depend on autoregressive video foundations and packages that history into a real-time WAM system. Direct baseline for ObservationHistory, ProgressState, StreamingEncoder, AsyncExecution, ContextLength, and latency-aware control. Central results are author-reported and were not independently reproduced in this collection run.

## Novelty

- What is new: Shows long context benefits depend on autoregressive video foundations and packages that history into a real-time WAM system.
- Why it matters: Direct baseline for ObservationHistory, ProgressState, StreamingEncoder, AsyncExecution, ContextLength, and latency-aware control.
- Branch fit: the work directly contributes to branch D rather than serving only as background.

## Contributions

1. Causal autoregressive pretraining is preserved during WAM adaptation, with streaming encoding, asynchronous execution, and hardware-specific acceleration.
2. Robot and egocentric video, RoboCasa GR-1, LIBERO-Long, RoboTwin 2.0, DOMINO, Unitree G1, and YAM deployments.
3. The paper reports GR-1 success rising from 63.3% to 78.7% with 19.2 s context and 95% success on dynamic cup stacking.

## Task

- Input / setting: official source-specific observations, task context, state, geometry, and/or actions.
- Output: Use long visual histories for responsive, dynamic, long-horizon manipulation.
- Success criterion: the paper's official task metrics and matched evaluation protocol.

## Data

- Dataset / benchmark: Robot and egocentric video, RoboCasa GR-1, LIBERO-Long, RoboTwin 2.0, DOMINO, Unitree G1, and YAM deployments.
- Modalities and splits: use the official paper's definitions; synthetic, simulated, and real components should not be conflated.
- Provenance: scale and collection claims are traced to the primary paper/project below.

## Method

- Core pipeline: Causal autoregressive pretraining is preserved during WAM adaptation, with streaming encoding, asynchronous execution, and hardware-specific acceleration.
- Representation and optimization: retain the source's units, coordinate frames, action conventions, and success definitions when reproducing.
- Deployment target: Use long visual histories for responsive, dynamic, long-horizon manipulation.

## Key Figures / Architecture

figure_status: linked_official

- Official source: https://arxiv.org/abs/2610.10528
- What was inspected: method overview, qualitative panels, benchmark/task examples, and available demo media.
- Visual decision: strong (4/5). Official project/paper qualitative panels and demo media were inspected; results were coherent and task-relevant.

## Evidence Trail

| Claim | Source | Status | Notes |
|---|---|---|---|
| Method and data | https://arxiv.org/abs/2610.10528 | verified | Primary paper surface checked. |
| Main reported result | https://arxiv.org/abs/2610.10528 | verified | Author-reported; not independently reproduced. |
| Project/code/demo availability | https://arxiv.org/abs/2610.10528 | verified | Official surface checked on 2026-10-12. |

## Evidence

- Main result: The paper reports GR-1 success rising from 63.3% to 78.7% with 19.2 s context and 95% success on dynamic cup stacking.
- Demo score: 3/5; evidence strength: 4/5.
- Qualitative evidence: Official project/paper qualitative panels and demo media were inspected; results were coherent and task-relevant.
- Comparisons remain protocol-dependent and should be cited as reported by the authors.

## Limitations

- Scope is bounded by the reported tasks, environments, embodiments, sensors, and action conventions.
- Curated demos do not expose the full long-tail failure distribution.
- Headline results were not independently reproduced during this literature-maintenance run.

## Project Relevance

- Direct baseline for ObservationHistory, ProgressState, StreamingEncoder, AsyncExecution, ContextLength, and latency-aware control.
- Reusable fields should preserve source-specific units, coordinate frames, time bases, and simulator/hardware assumptions.
- Suitable as a related-work anchor and a candidate baseline or validator for branch D.

## Reproduction / Follow-up

- Verify licenses, exact data splits, hardware requirements, metric definitions, and checkpoint completeness before reproduction.
- Code/checkpoints: See the official paper/project; no separate fully verified repository was recorded in this run.
- Cite all metrics as source-reported until independently reproduced.
