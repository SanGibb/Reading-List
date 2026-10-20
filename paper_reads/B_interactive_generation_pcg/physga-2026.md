# PhySGA: A Physics-Space Grounded Agentic Framework for Generalizable and Interactive 3D Composition

<!-- curation-review:start -->
> 2026-10-20 按新版标准复审：**待视觉复核**。Contact diagnosis and executable assembly primitives address a real composition gap across material types. Hanging/settling/containment success must be visually checked over actual simulator sequences.
> [本次来源、分数与任务判断](../library_review.md#paper-6b1b54d1cd59)。下文保留原精读；旧验收标签不代表本次重新通过，所有实验仍为作者报告。
<!-- curation-review:end -->

candidate_id: CAND-0003
branch: B
decision: accepted_for_registry

## Source Links

- Paper: https://arxiv.org/abs/2610.20560
- Project: https://agenticei.github.io/PhySGA-page/
- Code: https://github.com/AgenticEI/PhySGA
- Data / benchmark: https://agenticei.github.io/PhySGA-page/
- Demo / video: https://agenticei.github.io/PhySGA-page/

## TL;DR

Grounds agentic 3D composition in closed-loop contact dynamics and executable simulator actions rather than static coordinate prediction. Direct reference for AssemblyPlan, ContactDiagnosis, ActionPrimitive, SkillLibrary, PhysicalRelation, and scene validators. Main caveat: the release is new and its reported results have not been independently reproduced.

## Novelty

- What is actually new: Grounds agentic 3D composition in closed-loop contact dynamics and executable simulator actions rather than static coordinate prediction.
- Difference from prior work: Assembly and critic agents plan and diagnose simulator states; action routers execute physical primitives and a self-evolving skill library reuses successful corrections.
- Why the delta matters: Direct reference for AssemblyPlan, ContactDiagnosis, ActionPrimitive, SkillLibrary, PhysicalRelation, and scene validators.

## Contributions

1. Assembly and critic agents plan and diagnose simulator states; action routers execute physical primitives and a self-evolving skill library reuses successful corrections.
2. Isaac Sim composition tasks spanning rigid, articulated, and deformable objects with hanging, settling, alignment, and containment relations.
3. Official project page provides code and a supplementary video with rigid, articulated, and deformable assembly results.

## Task

- Input: observations, instructions, actions, or simulator state as specified by the paper.
- Output: Interactively assemble physically plausible 3D object compositions in simulation.
- Setting: embodied or interactive-world evaluation described in the primary paper.
- Success criterion: the paper's task metrics plus the reported qualitative/physical checks.

## Data

- Dataset / benchmark: Isaac Sim composition tasks spanning rigid, articulated, and deformable objects with hanging, settling, alignment, and containment relations.
- Scale: see the primary source for the exact split-level counts.
- Modalities: visual/world state and the action, geometry, force, tactile, or language channels required by the task.
- Collection / annotation: author-described pipeline; not independently audited.
- Splits / evaluation protocol: official paper protocol.

## Method

- Core pipeline: Assembly and critic agents plan and diagnose simulator states; action routers execute physical primitives and a self-evolving skill library reuses successful corrections.
- Model / representation: paper-specific representation summarized above.
- Training or optimization: see the official method and ablation sections.
- Inference / deployment: evaluated in the released simulation, benchmark, or robot setting.
- Losses or metrics: official paper metrics; cross-paper values are not directly comparable.

## Key Figures / Architecture

figure_status: linked_official

- Figure / demo: official project overview/video when available; otherwise primary-paper architecture and qualitative figures.
- Source: https://agenticei.github.io/PhySGA-page/
- What it shows: the system pipeline and representative task outputs or evaluation protocol.
- Why it matters: it verifies the collection-relevant representation, execution, or benchmark interface.

## Evidence Trail

| Claim | Source | Status | Notes |
|---|---|---|---|
| Data / benchmark scope | https://arxiv.org/abs/2610.20560 | verified | Author-reported in the primary paper. |
| Main reported result | https://arxiv.org/abs/2610.20560 | verified | Official project page provides code and a supplementary video with rigid, articulated, and deformable assembly results. |
| Code / checkpoint / demo availability | https://agenticei.github.io/PhySGA-page/ | verified | Official project/code surface inspected. |

## Evidence

- Main metrics: Official project page provides code and a supplementary video with rigid, articulated, and deformable assembly results.
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

- Relevance to interactive embodied generation: Direct reference for AssemblyPlan, ContactDiagnosis, ActionPrimitive, SkillLibrary, PhysicalRelation, and scene validators.
- Reusable fields: extract the named interfaces above into structured registry/benchmark schemas.
- Possible baseline role: direct method, data, or evaluation baseline for its branch.
- Implications for our task / benchmark: motivates explicit executable state and source-traced evaluation rather than image-only plausibility.

## Reproduction / Follow-up

- What to check before using: exact splits, licenses, preprocessing, embodiment assumptions, and metric implementations.
- Code / checkpoint availability: https://github.com/AgenticEI/PhySGA.
- Citation or related-work caveats: cite results as author-reported and avoid direct numeric comparison across incompatible protocols.
