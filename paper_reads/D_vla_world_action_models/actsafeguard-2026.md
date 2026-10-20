# ActSafeGuard: Differentiable and Training-Aligned Constraint Enforcement for Flow-Matching Policies

<!-- curation-review:start -->
> 2026-10-20 按新版标准复审：**待视觉复核**。hard feasible-set层是明确的动作合法性接口，文本可验证ray-scaling与训练对齐；本轮未读完整定理假设/实验或检查物理执行，100% step safety不能转述为全局安全。
> [本次来源、分数与任务判断](../library_review.md#paper-523157d7fa1c)。下文保留原精读；旧验收标签不代表本次重新通过，所有实验仍为作者报告。
<!-- curation-review:end -->

candidate_id: CAND-0003
branch: D
decision: accepted_for_registry

## Source Links

- Paper: https://arxiv.org/abs/2609.11697
- HTML / figures: https://arxiv.org/html/2609.11697v1
- Project: not released
- Code: not released

## TL;DR

ActSafeGuard analytically rescales every discrete flow-matching update so an action trajectory remains inside a hard feasible set, while retaining useful boundary-aware gradients during training. It is a compact and highly relevant action-validity primitive for pi0.5/Fast-WAM-style policies; the caveat is that the current evidence is paper-only and focuses on constraints that admit the ray-intersection construction.

## Novelty

- Enforces feasibility inside both training and inference rather than adding an inference-only filter.
- Preserves the pretrained velocity direction whenever the nominal step is feasible.
- Converts outward gradients at active boundaries into boundary-sliding gradients.

## Contributions

1. A differentiable ray-scaling operator for discrete flow updates.
2. Construction-level stepwise safety and differentiability arguments.
3. Evaluation on pi0.5 and Fast-WAM backbones.

## Task

- Input: observation-conditioned flow velocity and a feasible action set.
- Output: a rescaled update that remains within the constraint boundary.
- Setting: flow-matching VLA/WAM manipulation policies.
- Success criterion: 100% step feasibility without reducing task success.

## Data

- Uses standard policy benchmarks/tasks for pi0.5 and Fast-WAM.
- The paper does not release a new dataset.
- Exact task splits should be checked in the primary tables before reproduction.

## Method

- Convert each velocity prediction into a discrete update direction.
- Ray-shoot against active linear constraint facets.
- Apply scale `min(1, alpha)` so the next state is feasible.
- Backpropagate through the closed-form local Jacobian, yielding tangential correction signals.

## Key Figures / Architecture

figure_status: linked_official

- Figure: boundary intersection and boundary-sliding gradient (Figure 2).
- Source: https://arxiv.org/html/2609.11697v1
- What it shows: unsafe nominal updates are shortened to the active facet while gradients remain tangent to it.
- Why it matters: the geometry explains both the hard guarantee and training alignment.

## Evidence Trail

| Claim | Source | Status | Notes |
|---|---|---|---|
| 100% step safety across evaluated settings | https://arxiv.org/html/2609.11697v1 | verified | Author-reported, not independently reproduced. |
| Task success preserved or improved | https://arxiv.org/abs/2609.11697 | verified | Abstract claim backed by paper tables. |
| Closed-form differentiable constraint layer | https://arxiv.org/html/2609.11697v1 | verified | Equations 5-14 and propositions. |

## Evidence

- Paper evaluates two widely relevant flow-based backbones.
- Feasibility follows stepwise if initial noise/state lies within the closed feasible set.
- Analytical ablation distinguishes training-aligned safeguard behavior from clipping.

## Limitations

- No public code, checkpoint, or project page at review time.
- Convex/polyhedral feasible sets are narrower than full contact, collision, or deformable-body safety.
- Guarantee depends on correct observation-conditioned constraints and a feasible initialization.

## Project Relevance

- Direct ActionConstraint and FeasibilityProjector primitive.
- Useful validator for generated action chunks before execution.
- Supports training-time alignment between policy outputs and executable action domains.

## Reproduction / Follow-up

- Implement the ray-scaling layer first on box constraints.
- Compare against naive clipping and inference-only projection.
- Stress-test incorrect, moving, nonconvex, and mutually inconsistent constraints.
