# RoboJEPA: Scaling Robotic Latent World Models

<!-- curation-review:start -->
> 2026-10-20 按新版标准复审：**待视觉复核**。把imagination error与算力/真实规划性能联系并释放训练部署代码有实质方法价值；本轮只读摘要，未核查scalingfit/extrapolation或真实goal-image规划。
> [本次来源、分数与任务判断](../library_review.md#paper-b66fa1e99299)。下文保留原精读；旧验收标签不代表本次重新通过，所有实验仍为作者报告。
<!-- curation-review:end -->

candidate_id: CAND-0008
branch: D
decision: accepted_for_registry

## Source Links

- Paper: https://arxiv.org/abs/2610.10515
- Project / figures / demos: https://arxiv.org/abs/2610.10515

## TL;DR

Establishes empirical scaling laws for multi-embodiment latent robot world models and validates imagination error as a real-robot proxy. Useful for LatentRollout, ImaginationError, ComputeBudget, Embodiment, GoalImage, and scaling-law evaluation. Central results are author-reported and were not independently reproduced in this collection run.

## Novelty

- What is new: Establishes empirical scaling laws for multi-embodiment latent robot world models and validates imagination error as a real-robot proxy.
- Why it matters: Useful for LatentRollout, ImaginationError, ComputeBudget, Embodiment, GoalImage, and scaling-law evaluation.
- Branch fit: the work directly contributes to branch D rather than serving only as background.

## Contributions

1. An 8B-parameter JEPA predictor learns latent rollouts; second-order compute scaling laws link imagination error to downstream planning performance.
2. Large-scale real robot data spanning 12 embodiments, with released checkpoints and robot-deployment code.
3. The paper reports predictable power-law improvement with compute and zero-shot real-hardware planning; checkpoints and deployment code are released.

## Task

- Input / setting: official source-specific observations, task context, state, geometry, and/or actions.
- Output: Predict latent robot futures and plan zero-shot toward goal images on real hardware.
- Success criterion: the paper's official task metrics and matched evaluation protocol.

## Data

- Dataset / benchmark: Large-scale real robot data spanning 12 embodiments, with released checkpoints and robot-deployment code.
- Modalities and splits: use the official paper's definitions; synthetic, simulated, and real components should not be conflated.
- Provenance: scale and collection claims are traced to the primary paper/project below.

## Method

- Core pipeline: An 8B-parameter JEPA predictor learns latent rollouts; second-order compute scaling laws link imagination error to downstream planning performance.
- Representation and optimization: retain the source's units, coordinate frames, action conventions, and success definitions when reproducing.
- Deployment target: Predict latent robot futures and plan zero-shot toward goal images on real hardware.

## Key Figures / Architecture

figure_status: linked_official

- Official source: https://arxiv.org/abs/2610.10515
- What was inspected: method overview, qualitative panels, benchmark/task examples, and available demo media.
- Visual decision: strong (4/5). Official project/paper qualitative panels and demo media were inspected; results were coherent and task-relevant.

## Evidence Trail

| Claim | Source | Status | Notes |
|---|---|---|---|
| Method and data | https://arxiv.org/abs/2610.10515 | verified | Primary paper surface checked. |
| Main reported result | https://arxiv.org/abs/2610.10515 | verified | Author-reported; not independently reproduced. |
| Project/code/demo availability | https://arxiv.org/abs/2610.10515 | verified | Official surface checked on 2026-10-12. |

## Evidence

- Main result: The paper reports predictable power-law improvement with compute and zero-shot real-hardware planning; checkpoints and deployment code are released.
- Demo score: 5/5; evidence strength: 4/5.
- Qualitative evidence: Official project/paper qualitative panels and demo media were inspected; results were coherent and task-relevant.
- Comparisons remain protocol-dependent and should be cited as reported by the authors.

## Limitations

- Scope is bounded by the reported tasks, environments, embodiments, sensors, and action conventions.
- Curated demos do not expose the full long-tail failure distribution.
- Headline results were not independently reproduced during this literature-maintenance run.

## Project Relevance

- Useful for LatentRollout, ImaginationError, ComputeBudget, Embodiment, GoalImage, and scaling-law evaluation.
- Reusable fields should preserve source-specific units, coordinate frames, time bases, and simulator/hardware assumptions.
- Suitable as a related-work anchor and a candidate baseline or validator for branch D.

## Reproduction / Follow-up

- Verify licenses, exact data splits, hardware requirements, metric definitions, and checkpoint completeness before reproduction.
- Code/checkpoints: See the official paper/project; no separate fully verified repository was recorded in this run.
- Cite all metrics as source-reported until independently reproduced.
