# WorldCast: Distributed Multiplayer World Models

<!-- curation-review:start -->
> 2026-10-20 按新版标准复审：**待视觉复核**。Distributed local video/state clients and compact shared state are a substantial scaling alternative. Player identities, shared events and hour-long consistency require actual paired-rollout inspection.
> [本次来源、分数与任务判断](../library_review.md#paper-0e0b8dce565d)。下文保留原精读；旧验收标签不代表本次重新通过，所有实验仍为作者报告。
<!-- curation-review:end -->

candidate_id: CAND-0002
branch: B
decision: accepted_for_registry

## Source Links

- Paper: https://arxiv.org/abs/2610.12412
- Project / figures / demos: https://ziyang-ye.github.io/WorldCast-Page

## TL;DR

Replaces costly joint multi-view generation with distributed local world-model clients coordinated through compact shared state. Useful for SharedWorldState, PlayerState, CrossViewConsistency, ConcurrentAction, and distributed interactive-world runtime contracts. Central results are author-reported and were not independently reproduced in this collection run.

## Novelty

- What is new: Replaces costly joint multi-view generation with distributed local world-model clients coordinated through compact shared state.
- Why it matters: Useful for SharedWorldState, PlayerState, CrossViewConsistency, ConcurrentAction, and distributed interactive-world runtime contracts.
- Branch fit: the work directly contributes to branch B rather than serving only as background.

## Contributions

1. Each player runs a local video-generator/state-model client; clients exchange compact player and scene states projected into camera-aligned fields.
2. Counter-Strike 2 multi-player trajectories with player positions, map geometry, controls, and synchronized views.
3. The paper reports over an order-of-magnitude gain in player rendering rate over joint generation and real-time scaling to four-player generation.

## Task

- Input / setting: official source-specific observations, task context, state, geometry, and/or actions.
- Output: Generate independently controlled, mutually consistent multiplayer views in real time.
- Success criterion: the paper's official task metrics and matched evaluation protocol.

## Data

- Dataset / benchmark: Counter-Strike 2 multi-player trajectories with player positions, map geometry, controls, and synchronized views.
- Modalities and splits: use the official paper's definitions; synthetic, simulated, and real components should not be conflated.
- Provenance: scale and collection claims are traced to the primary paper/project below.

## Method

- Core pipeline: Each player runs a local video-generator/state-model client; clients exchange compact player and scene states projected into camera-aligned fields.
- Representation and optimization: retain the source's units, coordinate frames, action conventions, and success definitions when reproducing.
- Deployment target: Generate independently controlled, mutually consistent multiplayer views in real time.

## Key Figures / Architecture

figure_status: linked_official

- Official source: https://ziyang-ye.github.io/WorldCast-Page
- What was inspected: method overview, qualitative panels, benchmark/task examples, and available demo media.
- Visual decision: strong (4/5). Official project/paper qualitative panels and demo media were inspected; results were coherent and task-relevant.

## Evidence Trail

| Claim | Source | Status | Notes |
|---|---|---|---|
| Method and data | https://arxiv.org/abs/2610.12412 | verified | Primary paper surface checked. |
| Main reported result | https://arxiv.org/abs/2610.12412 | verified | Author-reported; not independently reproduced. |
| Project/code/demo availability | https://ziyang-ye.github.io/WorldCast-Page | verified | Official surface checked on 2026-10-12. |

## Evidence

- Main result: The paper reports over an order-of-magnitude gain in player rendering rate over joint generation and real-time scaling to four-player generation.
- Demo score: 3/5; evidence strength: 4/5.
- Qualitative evidence: Official project/paper qualitative panels and demo media were inspected; results were coherent and task-relevant.
- Comparisons remain protocol-dependent and should be cited as reported by the authors.

## Limitations

- Scope is bounded by the reported tasks, environments, embodiments, sensors, and action conventions.
- Curated demos do not expose the full long-tail failure distribution.
- Headline results were not independently reproduced during this literature-maintenance run.

## Project Relevance

- Useful for SharedWorldState, PlayerState, CrossViewConsistency, ConcurrentAction, and distributed interactive-world runtime contracts.
- Reusable fields should preserve source-specific units, coordinate frames, time bases, and simulator/hardware assumptions.
- Suitable as a related-work anchor and a candidate baseline or validator for branch B.

## Reproduction / Follow-up

- Verify licenses, exact data splits, hardware requirements, metric definitions, and checkpoint completeness before reproduction.
- Code/checkpoints: See the official paper/project; no separate fully verified repository was recorded in this run.
- Cite all metrics as source-reported until independently reproduced.
