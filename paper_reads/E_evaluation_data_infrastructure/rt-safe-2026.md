# RT-Safe: Benchmarking Agent Safety in Real-Time Embodied Environment

<!-- curation-review:start -->
> 2026-10-20 按新版标准复审：**优先阅读**。同初态与action API的static/real-time拆分揭示冻结模拟器隐藏的风险，具体计时/碰撞接口可直接用于运行时评价。
> [本次来源、分数与任务判断](../library_review.md#paper-2698d471c63b)。下文保留原精读；旧验收标签不代表本次重新通过，所有实验仍为作者报告。
>
> **本轮准入依据**（技术贡献 / 直接相关性 / 证据：4 / 4 / 4）：VLA-Arena静态安全轴之外显式计入推理时环境推进；独立评价轴并不替代其任务安全约束。
> - [Sec.3.3; Appendix A.2 timing prompts; Appendix B.4/Table11](https://arxiv.org/html/2610.09294v1)：288 matched model-route pairs；static91.3/19.8 vs realtime94.1/0.7任务/安全成功；碰撞3.31→40.68；两模式timing instructions不同，差异非纯延迟因果。（verified）。
>
> 引用指标、发布规模和比较结果时，以以上已定位来源和本次复审限制为准，不沿用下文旧概括。
<!-- curation-review:end -->

candidate_id: CAND-0014
branch: E
decision: accepted_for_registry

## Source Links

- Paper: https://arxiv.org/abs/2610.09294
- Project / figures / demos: https://arxiv.org/abs/2610.09294

## TL;DR

Makes inference latency itself part of the embodied safety environment instead of freezing the world at observation time. Adds ObservationTime, DecisionLatency, ExecutionTime, DynamicHazard, CollisionEvent, and SafeCompletion fields. Central results are author-reported and were not independently reproduced in this collection run.

## Novelty

- What is new: Makes inference latency itself part of the embodied safety environment instead of freezing the world at observation time.
- Why it matters: Adds ObservationTime, DecisionLatency, ExecutionTime, DynamicHazard, CollisionEvent, and SafeCompletion fields.
- Branch fit: the work directly contributes to branch E rather than serving only as background.

## Contributions

1. Matched static and real-time evaluation explicitly measures both decision safety and latency-induced risk; the benchmark also supports offline RL.
2. Simulated urban navigation tasks with moving actors, hazards, traffic rules, and worlds that evolve during inference.
3. The paper reports only 0.7% safe completion in the hardest setting and 12.3x more collisions in real-time than matched static evaluation.

## Task

- Input / setting: official source-specific observations, task context, state, geometry, and/or actions.
- Output: Evaluate embodied-agent safety when the physical world continues changing during reasoning and execution.
- Success criterion: the paper's official task metrics and matched evaluation protocol.

## Data

- Dataset / benchmark: Simulated urban navigation tasks with moving actors, hazards, traffic rules, and worlds that evolve during inference.
- Modalities and splits: use the official paper's definitions; synthetic, simulated, and real components should not be conflated.
- Provenance: scale and collection claims are traced to the primary paper/project below.

## Method

- Core pipeline: Matched static and real-time evaluation explicitly measures both decision safety and latency-induced risk; the benchmark also supports offline RL.
- Representation and optimization: retain the source's units, coordinate frames, action conventions, and success definitions when reproducing.
- Deployment target: Evaluate embodied-agent safety when the physical world continues changing during reasoning and execution.

## Key Figures / Architecture

figure_status: linked_official

- Official source: https://arxiv.org/abs/2610.09294
- What was inspected: method overview, qualitative panels, benchmark/task examples, and available demo media.
- Visual decision: not_applicable (0/5). This is primarily an evaluation/data contribution; visual generation quality is not an acceptance gate.

## Evidence Trail

| Claim | Source | Status | Notes |
|---|---|---|---|
| Method and data | https://arxiv.org/abs/2610.09294 | verified | Primary paper surface checked. |
| Main reported result | https://arxiv.org/abs/2610.09294 | verified | Author-reported; not independently reproduced. |
| Project/code/demo availability | https://arxiv.org/abs/2610.09294 | verified | Official surface checked on 2026-10-12. |

## Evidence

- Main result: The paper reports only 0.7% safe completion in the hardest setting and 12.3x more collisions in real-time than matched static evaluation.
- Demo score: 2/5; evidence strength: 4/5.
- Qualitative evidence: This is primarily an evaluation/data contribution; visual generation quality is not an acceptance gate.
- Comparisons remain protocol-dependent and should be cited as reported by the authors.

## Limitations

- Scope is bounded by the reported tasks, environments, embodiments, sensors, and action conventions.
- Curated demos do not expose the full long-tail failure distribution.
- Headline results were not independently reproduced during this literature-maintenance run.

## Project Relevance

- Adds ObservationTime, DecisionLatency, ExecutionTime, DynamicHazard, CollisionEvent, and SafeCompletion fields.
- Reusable fields should preserve source-specific units, coordinate frames, time bases, and simulator/hardware assumptions.
- Suitable as a related-work anchor and a candidate baseline or validator for branch E.

## Reproduction / Follow-up

- Verify licenses, exact data splits, hardware requirements, metric definitions, and checkpoint completeness before reproduction.
- Code/checkpoints: See the official paper/project; no separate fully verified repository was recorded in this run.
- Cite all metrics as source-reported until independently reproduced.
