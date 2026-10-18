# OneWM: Can World and Action Modeling Benefit Each Other under Unified Causal Training?

candidate_id: CAND-0010
branch: D
decision: accepted_for_registry

## Source Links

- Paper: https://arxiv.org/abs/2610.21095
- Project: https://selen-suyue.github.io/OneWMNet/
- Code: https://github.com/Interactive-Active-AI/OneWM
- Data / benchmark: https://selen-suyue.github.io/OneWMNet/
- Demo / video: https://selen-suyue.github.io/OneWMNet/

## TL;DR

Provides controlled evidence that forward modeling improves policies and action learning improves multi-view world prediction in the same architecture. Direct baseline for UnifiedCausalTraining, ActionCondition, WorldTarget, PolicyTarget, and reciprocal-benefit ablations. Main caveat: the release is new and its reported results have not been independently reproduced.

## Novelty

- What is actually new: Provides controlled evidence that forward modeling improves policies and action learning improves multi-view world prediction in the same architecture.
- Difference from prior work: A shared causal video-action architecture treats actions as both world-prediction conditions and policy targets.
- Why the delta matters: Direct baseline for UnifiedCausalTraining, ActionCondition, WorldTarget, PolicyTarget, and reciprocal-benefit ablations.

## Contributions

1. A shared causal video-action architecture treats actions as both world-prediction conditions and policy targets.
2. LIBERO, LIBERO-Plus, RoboCasa365, and real-world manipulation rollouts.
3. Official page exposes code and multiple real-robot videos alongside benchmark and world-prediction comparisons.

## Task

- Input: observations, instructions, actions, or simulator state as specified by the paper.
- Output: Jointly learn action-conditioned world prediction and robot action generation.
- Setting: embodied or interactive-world evaluation described in the primary paper.
- Success criterion: the paper's task metrics plus the reported qualitative/physical checks.

## Data

- Dataset / benchmark: LIBERO, LIBERO-Plus, RoboCasa365, and real-world manipulation rollouts.
- Scale: see the primary source for the exact split-level counts.
- Modalities: visual/world state and the action, geometry, force, tactile, or language channels required by the task.
- Collection / annotation: author-described pipeline; not independently audited.
- Splits / evaluation protocol: official paper protocol.

## Method

- Core pipeline: A shared causal video-action architecture treats actions as both world-prediction conditions and policy targets.
- Model / representation: paper-specific representation summarized above.
- Training or optimization: see the official method and ablation sections.
- Inference / deployment: evaluated in the released simulation, benchmark, or robot setting.
- Losses or metrics: official paper metrics; cross-paper values are not directly comparable.

## Key Figures / Architecture

figure_status: linked_official

- Figure / demo: official project overview/video when available; otherwise primary-paper architecture and qualitative figures.
- Source: https://selen-suyue.github.io/OneWMNet/
- What it shows: the system pipeline and representative task outputs or evaluation protocol.
- Why it matters: it verifies the collection-relevant representation, execution, or benchmark interface.

## Evidence Trail

| Claim | Source | Status | Notes |
|---|---|---|---|
| Data / benchmark scope | https://arxiv.org/abs/2610.21095 | verified | Author-reported in the primary paper. |
| Main reported result | https://arxiv.org/abs/2610.21095 | verified | Official page exposes code and multiple real-robot videos alongside benchmark and world-prediction comparisons. |
| Code / checkpoint / demo availability | https://selen-suyue.github.io/OneWMNet/ | verified | Official project/code surface inspected. |

## Evidence

- Main metrics: Official page exposes code and multiple real-robot videos alongside benchmark and world-prediction comparisons.
- Qualitative results: inspected on the official project page/video or primary-paper figures as recorded above.
- Ablations: see primary paper; acceptance does not depend on an unverified SOTA claim.
- Baselines: paper-defined comparisons only.
- Reproducibility signals: official code/project assets are available.

## Limitations

- Method limitations: scoped to the paper's environments, embodiments, or benchmark protocol.
- Experimental limitations: author-reported fresh-release evidence; no independent reproduction.
- Demo / visual limitations: official materials may be selected examples.
- Claims that remain unverified: external generalization beyond reported settings and compute/data cost details not exposed in the abstract/project page.

## Project Relevance

- Relevance to interactive embodied generation: Direct baseline for UnifiedCausalTraining, ActionCondition, WorldTarget, PolicyTarget, and reciprocal-benefit ablations.
- Reusable fields: extract the named interfaces above into structured registry/benchmark schemas.
- Possible baseline role: direct method, data, or evaluation baseline for its branch.
- Implications for our task / benchmark: motivates explicit executable state and source-traced evaluation rather than image-only plausibility.

## Reproduction / Follow-up

- What to check before using: exact splits, licenses, preprocessing, embodiment assumptions, and metric implementations.
- Code / checkpoint availability: https://github.com/Interactive-Active-AI/OneWM.
- Citation or related-work caveats: cite results as author-reported and avoid direct numeric comparison across incompatible protocols.
