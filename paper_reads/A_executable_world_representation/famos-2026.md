# FAMOS: Feed-Forward 3D Articulation Modeling from Sparse Observations

<!-- curation-review:start -->
> 2026-10-20 按新版标准复审：**待视觉复核**。Variable-state articulation recovery and procedural motion supervision directly supply executable joints. Joint-motion reconstruction was not re-inspected; generation/recovery quality cannot inherit the old unlocated video assertion.
> [本次来源、分数与任务判断](../library_review.md#paper-69916d9d7c46)。下文保留原精读；旧验收标签不代表本次重新通过，所有实验仍为作者报告。
<!-- curation-review:end -->

candidate_id: CAND-0002
branch: A
decision: accepted_for_registry

## Source Links

- Paper: https://arxiv.org/abs/2609.20817
- Project / demos: https://kevinqu7.github.io/famos

## TL;DR

FAMOS predicts movable parts and joint parameters from one or more sparse unordered observations. Its multi-state transformer and procedural supervision make articulation recoverable without per-object optimization; the main caveat is object-centric rather than full-scene evaluation.

## Novelty

- Jointly aggregates articulation evidence across a variable number of observed states.
- Supervises observed motion span so the model uses the whole observation set.
- Adds procedural self-annotated assets to compensate for limited articulation data.

## Contributions

1. Feed-forward multi-state articulation recovery.
2. Explicit part, joint-axis, origin, and range predictions.
3. Strong official moving comparisons on three benchmark families.

## Task

- Input: sparse unordered partial point clouds from one or more object states.
- Output: movable-part masks and executable joint parameters.
- Success: accurate part segmentation and kinematics on held-out articulated objects.

## Data

PartNet-Mobility, ACD, ArtiCraft-10K, plus procedurally generated self-annotated assets.

## Method

A Multi-state Articulation Transformer alternates state-wise and global attention. An observed-span objective encourages correct use of cross-state motion evidence.

## Key Figures / Architecture

figure_status: linked_official

- Official comparison videos and result panel: https://kevinqu7.github.io/famos
- They show how one-state estimates improve when a second observed state disambiguates the joint.

## Evidence Trail

| Claim | Source | Status | Notes |
|---|---|---|---|
| Variable-view feed-forward articulation | https://arxiv.org/abs/2609.20817 | verified | Primary paper. |
| Benchmark improvements | https://arxiv.org/abs/2609.20817 | verified | Author-reported. |
| Qualitative motion recovery | https://kevinqu7.github.io/famos | verified | Official videos inspected. |

## Evidence

- Consistent gains over feed-forward and optimization-based baselines.
- Qualitative outputs expose predicted masks, axes, and motion spans.

## Limitations

- Object-centric benchmarks; no downstream manipulation success study.
- No public code link found during this run.

## Project Relevance

Direct source for `MovablePart`, `JointType`, `JointAxis`, `JointOrigin`, `MotionRange`, and multi-state observation fields.

## Reproduction / Follow-up

- Verify code/checkpoint release before adopting as a baseline.
- Test robustness in cluttered scenes and partial multi-object observations.
