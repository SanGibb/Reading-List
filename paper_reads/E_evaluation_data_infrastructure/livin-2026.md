# LIVIN: Benchmarking Spatial and Embodied Intelligence in Digital Twins of Lived-In Homes

<!-- curation-review:start -->
> 2026-10-20 按新版标准复审：**待视觉复核**。拥挤有人居住宅与真实对应对任务很相关；核心home twin来自物体生成和放置，旧not_applicable无观察支持，不能自动通过物理交互质量。
> [本次来源、分数与任务判断](../library_review.md#paper-2cf667f472f2)。下文保留原精读；旧验收标签不代表本次重新通过，所有实验仍为作者报告。
<!-- curation-review:end -->

candidate_id: CAND-0011
branch: E
decision: accepted_for_registry

## Source Links

- Paper: https://arxiv.org/abs/2610.12069
- Project / figures / demos: https://arxiv.org/abs/2610.12069

## TL;DR

Combines real-home correspondence, interaction readiness, and dense lived-in arrangements in one digital-twin benchmark. Direct infrastructure for HomeTwin, ObjectArrangement, FreeSpace, InteractionRegion, Reconstruction, Navigation, and LocoManipulation schemas. Central results are author-reported and were not independently reproduced in this collection run.

## Novelty

- What is new: Combines real-home correspondence, interaction readiness, and dense lived-in arrangements in one digital-twin benchmark.
- Why it matters: Direct infrastructure for HomeTwin, ObjectArrangement, FreeSpace, InteractionRegion, Reconstruction, Navigation, and LocoManipulation schemas.
- Branch fit: the work directly contributes to branch E rather than serving only as background.

## Contributions

1. Human-in-the-loop instance recognition, architectural reconstruction, object generation, and placement, with review against source observations.
2. Digital twins of 30 diverse lived-in homes preserving layouts, furniture, belongings, and constrained interaction regions.
3. The benchmark exposes large drops under dense objects, occlusion, limited free space, and constrained interaction regions across four task families.

## Task

- Input / setting: official source-specific observations, task context, state, geometry, and/or actions.
- Output: Evaluate 3D detection, reconstruction, navigation, and loco-manipulation in realistic lived-in homes.
- Success criterion: the paper's official task metrics and matched evaluation protocol.

## Data

- Dataset / benchmark: Digital twins of 30 diverse lived-in homes preserving layouts, furniture, belongings, and constrained interaction regions.
- Modalities and splits: use the official paper's definitions; synthetic, simulated, and real components should not be conflated.
- Provenance: scale and collection claims are traced to the primary paper/project below.

## Method

- Core pipeline: Human-in-the-loop instance recognition, architectural reconstruction, object generation, and placement, with review against source observations.
- Representation and optimization: retain the source's units, coordinate frames, action conventions, and success definitions when reproducing.
- Deployment target: Evaluate 3D detection, reconstruction, navigation, and loco-manipulation in realistic lived-in homes.

## Key Figures / Architecture

figure_status: linked_official

- Official source: https://arxiv.org/abs/2610.12069
- What was inspected: method overview, qualitative panels, benchmark/task examples, and available demo media.
- Visual decision: not_applicable (0/5). This is primarily an evaluation/data contribution; visual generation quality is not an acceptance gate.

## Evidence Trail

| Claim | Source | Status | Notes |
|---|---|---|---|
| Method and data | https://arxiv.org/abs/2610.12069 | verified | Primary paper surface checked. |
| Main reported result | https://arxiv.org/abs/2610.12069 | verified | Author-reported; not independently reproduced. |
| Project/code/demo availability | https://arxiv.org/abs/2610.12069 | verified | Official surface checked on 2026-10-12. |

## Evidence

- Main result: The benchmark exposes large drops under dense objects, occlusion, limited free space, and constrained interaction regions across four task families.
- Demo score: 2/5; evidence strength: 4/5.
- Qualitative evidence: This is primarily an evaluation/data contribution; visual generation quality is not an acceptance gate.
- Comparisons remain protocol-dependent and should be cited as reported by the authors.

## Limitations

- Scope is bounded by the reported tasks, environments, embodiments, sensors, and action conventions.
- Curated demos do not expose the full long-tail failure distribution.
- Headline results were not independently reproduced during this literature-maintenance run.

## Project Relevance

- Direct infrastructure for HomeTwin, ObjectArrangement, FreeSpace, InteractionRegion, Reconstruction, Navigation, and LocoManipulation schemas.
- Reusable fields should preserve source-specific units, coordinate frames, time bases, and simulator/hardware assumptions.
- Suitable as a related-work anchor and a candidate baseline or validator for branch E.

## Reproduction / Follow-up

- Verify licenses, exact data splits, hardware requirements, metric definitions, and checkpoint completeness before reproduction.
- Code/checkpoints: See the official paper/project; no separate fully verified repository was recorded in this run.
- Cite all metrics as source-reported until independently reproduced.
