# Orbia: Do Generated Videos Form a Consistent 3D World?

candidate_id: CAND-0013
branch: E
decision: accepted_for_registry

## Source Links

- Paper: https://arxiv.org/abs/2610.20693
- Project: https://orbia-bench.github.io/
- Code: https://github.com/worldbench/Orbia
- Data / benchmark: https://orbia-bench.github.io/
- Demo / video: https://orbia-bench.github.io/

## TL;DR

Systematically tests newly generated regions for persistence as well as cross-view geometric agreement and minute-long return consistency. Direct validator for Persistence, Revisit, InputPreservation, CrossViewDepth, RegionalScale, and held-out reconstruction. Main caveat: the release is new and its reported results have not been independently reproduced.

## Novelty

- What is actually new: Systematically tests newly generated regions for persistence as well as cross-view geometric agreement and minute-long return consistency.
- Difference from prior work: Measures input preservation, generated-content persistence, and 3D self-consistency using registered RGB-D anchors, revisit comparisons, cross-view geometry, scale, and held-out rendering.
- Why the delta matters: Direct validator for Persistence, Revisit, InputPreservation, CrossViewDepth, RegionalScale, and held-out reconstruction.

## Contributions

1. Measures input preservation, generated-content persistence, and 3D self-consistency using registered RGB-D anchors, revisit comparisons, cross-view geometry, scale, and held-out rendering.
2. 720 indoor/outdoor exploration cases, six exploration-and-revisit protocols, and evaluations of 27 text-, action-, and camera-conditioned models.
3. Official benchmark page provides code, dataset, leaderboard, animated protocols, galleries, and results for 27 models.

## Task

- Input: observations, instructions, actions, or simulator state as specified by the paper.
- Output: Benchmark whether interactive video generators preserve one consistent 3D world across exploration and revisits.
- Setting: embodied or interactive-world evaluation described in the primary paper.
- Success criterion: the paper's task metrics plus the reported qualitative/physical checks.

## Data

- Dataset / benchmark: 720 indoor/outdoor exploration cases, six exploration-and-revisit protocols, and evaluations of 27 text-, action-, and camera-conditioned models.
- Scale: see the primary source for the exact split-level counts.
- Modalities: visual/world state and the action, geometry, force, tactile, or language channels required by the task.
- Collection / annotation: author-described pipeline; not independently audited.
- Splits / evaluation protocol: official paper protocol.

## Method

- Core pipeline: Measures input preservation, generated-content persistence, and 3D self-consistency using registered RGB-D anchors, revisit comparisons, cross-view geometry, scale, and held-out rendering.
- Model / representation: paper-specific representation summarized above.
- Training or optimization: see the official method and ablation sections.
- Inference / deployment: evaluated in the released simulation, benchmark, or robot setting.
- Losses or metrics: official paper metrics; cross-paper values are not directly comparable.

## Key Figures / Architecture

figure_status: not_applicable

- Figure / demo: official project overview/video when available; otherwise primary-paper architecture and qualitative figures.
- Source: https://orbia-bench.github.io/
- What it shows: the system pipeline and representative task outputs or evaluation protocol.
- Why it matters: it verifies the collection-relevant representation, execution, or benchmark interface.

## Evidence Trail

| Claim | Source | Status | Notes |
|---|---|---|---|
| Data / benchmark scope | https://arxiv.org/abs/2610.20693 | verified | Author-reported in the primary paper. |
| Main reported result | https://arxiv.org/abs/2610.20693 | verified | Official benchmark page provides code, dataset, leaderboard, animated protocols, galleries, and results for 27 models. |
| Code / checkpoint / demo availability | https://orbia-bench.github.io/ | verified | Official project/code surface inspected. |

## Evidence

- Main metrics: Official benchmark page provides code, dataset, leaderboard, animated protocols, galleries, and results for 27 models.
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

- Relevance to interactive embodied generation: Direct validator for Persistence, Revisit, InputPreservation, CrossViewDepth, RegionalScale, and held-out reconstruction.
- Reusable fields: extract the named interfaces above into structured registry/benchmark schemas.
- Possible baseline role: direct method, data, or evaluation baseline for its branch.
- Implications for our task / benchmark: motivates explicit executable state and source-traced evaluation rather than image-only plausibility.

## Reproduction / Follow-up

- What to check before using: exact splits, licenses, preprocessing, embodiment assumptions, and metric implementations.
- Code / checkpoint availability: https://github.com/worldbench/Orbia.
- Citation or related-work caveats: cite results as author-reported and avoid direct numeric comparison across incompatible protocols.
