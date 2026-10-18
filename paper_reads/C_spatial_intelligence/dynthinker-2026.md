# DynThinker: Unifying Static 3D and Dynamic 4D Spatial Reasoning

candidate_id: CAND-0007
branch: C
decision: accepted_for_registry

## Source Links

- Paper: https://arxiv.org/abs/2610.20598
- Project: not published / not located
- Code: not published / not located
- Data / benchmark: see primary paper
- Demo / video: paper figures and experiment section

## TL;DR

Targets non-uniform spatial-dynamic interference at parameter-group level instead of training separate static and dynamic models. Useful for Static3D, Dynamic4D, TemporalGeometry, InterferenceAudit, and unified spatial-evaluation design. Main caveat: the release is new and its reported results have not been independently reproduced.

## Novelty

- What is actually new: Targets non-uniform spatial-dynamic interference at parameter-group level instead of training separate static and dynamic models.
- Difference from prior work: Decoupled EMA constrains interference-sensitive parameter groups while Spatial-Dynamic Fusion injects geometry-encoder priors under semantic guidance.
- Why the delta matters: Useful for Static3D, Dynamic4D, TemporalGeometry, InterferenceAudit, and unified spatial-evaluation design.

## Contributions

1. Decoupled EMA constrains interference-sensitive parameter groups while Spatial-Dynamic Fusion injects geometry-encoder priors under semantic guidance.
2. Nine static-3D and dynamic-4D benchmarks summarized by ten metrics, including ReVSI, DSR-Bench, and DSI-Bench.
3. Primary paper reports the highest mean across ten metrics and open-model SOTA on four named evaluations.

## Task

- Input: observations, instructions, actions, or simulator state as specified by the paper.
- Output: Jointly improve static 3D and dynamic 4D spatial reasoning in one model.
- Setting: embodied or interactive-world evaluation described in the primary paper.
- Success criterion: the paper's task metrics plus the reported qualitative/physical checks.

## Data

- Dataset / benchmark: Nine static-3D and dynamic-4D benchmarks summarized by ten metrics, including ReVSI, DSR-Bench, and DSI-Bench.
- Scale: see the primary source for the exact split-level counts.
- Modalities: visual/world state and the action, geometry, force, tactile, or language channels required by the task.
- Collection / annotation: author-described pipeline; not independently audited.
- Splits / evaluation protocol: official paper protocol.

## Method

- Core pipeline: Decoupled EMA constrains interference-sensitive parameter groups while Spatial-Dynamic Fusion injects geometry-encoder priors under semantic guidance.
- Model / representation: paper-specific representation summarized above.
- Training or optimization: see the official method and ablation sections.
- Inference / deployment: evaluated in the released simulation, benchmark, or robot setting.
- Losses or metrics: official paper metrics; cross-paper values are not directly comparable.

## Key Figures / Architecture

figure_status: not_applicable

- Figure / demo: official project overview/video when available; otherwise primary-paper architecture and qualitative figures.
- Source: https://arxiv.org/pdf/2610.20598
- What it shows: the system pipeline and representative task outputs or evaluation protocol.
- Why it matters: it verifies the collection-relevant representation, execution, or benchmark interface.

## Evidence Trail

| Claim | Source | Status | Notes |
|---|---|---|---|
| Data / benchmark scope | https://arxiv.org/abs/2610.20598 | verified | Author-reported in the primary paper. |
| Main reported result | https://arxiv.org/abs/2610.20598 | verified | Primary paper reports the highest mean across ten metrics and open-model SOTA on four named evaluations. |
| Code / checkpoint / demo availability | https://arxiv.org/abs/2610.20598 | partial | No separate official project or code release located. |

## Evidence

- Main metrics: Primary paper reports the highest mean across ten metrics and open-model SOTA on four named evaluations.
- Qualitative results: inspected on the official project page/video or primary-paper figures as recorded above.
- Ablations: see primary paper; acceptance does not depend on an unverified SOTA claim.
- Baselines: paper-defined comparisons only.
- Reproducibility signals: paper and official materials are available; code/checkpoints were not confirmed.

## Limitations

- Method limitations: scoped to the paper's environments, embodiments, or benchmark protocol.
- Experimental limitations: author-reported fresh-release evidence; no independent reproduction.
- Demo / visual limitations: official materials may be selected examples.
- Claims that remain unverified: external generalization beyond reported settings and compute/data cost details not exposed in the abstract/project page.

## Project Relevance

- Relevance to interactive embodied generation: Useful for Static3D, Dynamic4D, TemporalGeometry, InterferenceAudit, and unified spatial-evaluation design.
- Reusable fields: extract the named interfaces above into structured registry/benchmark schemas.
- Possible baseline role: direct method, data, or evaluation baseline for its branch.
- Implications for our task / benchmark: motivates explicit executable state and source-traced evaluation rather than image-only plausibility.

## Reproduction / Follow-up

- What to check before using: exact splits, licenses, preprocessing, embodiment assumptions, and metric implementations.
- Code / checkpoint availability: not confirmed in this run.
- Citation or related-work caveats: cite results as author-reported and avoid direct numeric comparison across incompatible protocols.
