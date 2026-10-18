# What Matters for World Modeling in Vision-Language-Action Models?

candidate_id: CAND-0011
branch: D
decision: accepted_for_registry

## Source Links

- Paper: https://arxiv.org/abs/2610.19825
- Project: https://dylanmqs.github.io/WM-in-VLAs/
- Code: not published / not located
- Data / benchmark: https://dylanmqs.github.io/WM-in-VLAs/
- Demo / video: https://dylanmqs.github.io/WM-in-VLAs/

## TL;DR

Separates representation, integration paradigm, and backbone effects that prior systems change simultaneously. A direct design/evaluation map for FutureRepresentation, IntegrationParadigm, PolicyBackbone, and long-horizon/OOD tests. Main caveat: the release is new and its reported results have not been independently reproduced.

## Novelty

- What is actually new: Separates representation, integration paradigm, and backbone effects that prior systems change simultaneously.
- Difference from prior work: Instantiates four world-model integration paradigms under a unified framework and crosses them with different future representations and policy backbones.
- Why the delta matters: A direct design/evaluation map for FutureRepresentation, IntegrationParadigm, PolicyBackbone, and long-horizon/OOD tests.

## Contributions

1. Instantiates four world-model integration paradigms under a unified framework and crosses them with different future representations and policy backbones.
2. In-domain, OOD, long-horizon, dynamic, few-shot, and real-world evaluations over multiple policy backbones.
3. Official project page and video demonstrations support a broad controlled comparison; claims remain author-reported.

## Task

- Input: observations, instructions, actions, or simulator state as specified by the paper.
- Output: Identify which world representations and integration patterns reliably improve VLA control.
- Setting: embodied or interactive-world evaluation described in the primary paper.
- Success criterion: the paper's task metrics plus the reported qualitative/physical checks.

## Data

- Dataset / benchmark: In-domain, OOD, long-horizon, dynamic, few-shot, and real-world evaluations over multiple policy backbones.
- Scale: see the primary source for the exact split-level counts.
- Modalities: visual/world state and the action, geometry, force, tactile, or language channels required by the task.
- Collection / annotation: author-described pipeline; not independently audited.
- Splits / evaluation protocol: official paper protocol.

## Method

- Core pipeline: Instantiates four world-model integration paradigms under a unified framework and crosses them with different future representations and policy backbones.
- Model / representation: paper-specific representation summarized above.
- Training or optimization: see the official method and ablation sections.
- Inference / deployment: evaluated in the released simulation, benchmark, or robot setting.
- Losses or metrics: official paper metrics; cross-paper values are not directly comparable.

## Key Figures / Architecture

figure_status: linked_official

- Figure / demo: official project overview/video when available; otherwise primary-paper architecture and qualitative figures.
- Source: https://dylanmqs.github.io/WM-in-VLAs/
- What it shows: the system pipeline and representative task outputs or evaluation protocol.
- Why it matters: it verifies the collection-relevant representation, execution, or benchmark interface.

## Evidence Trail

| Claim | Source | Status | Notes |
|---|---|---|---|
| Data / benchmark scope | https://arxiv.org/abs/2610.19825 | verified | Author-reported in the primary paper. |
| Main reported result | https://arxiv.org/abs/2610.19825 | verified | Official project page and video demonstrations support a broad controlled comparison; claims remain author-reported. |
| Code / checkpoint / demo availability | https://dylanmqs.github.io/WM-in-VLAs/ | verified | Official project/code surface inspected. |

## Evidence

- Main metrics: Official project page and video demonstrations support a broad controlled comparison; claims remain author-reported.
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

- Relevance to interactive embodied generation: A direct design/evaluation map for FutureRepresentation, IntegrationParadigm, PolicyBackbone, and long-horizon/OOD tests.
- Reusable fields: extract the named interfaces above into structured registry/benchmark schemas.
- Possible baseline role: direct method, data, or evaluation baseline for its branch.
- Implications for our task / benchmark: motivates explicit executable state and source-traced evaluation rather than image-only plausibility.

## Reproduction / Follow-up

- What to check before using: exact splits, licenses, preprocessing, embodiment assumptions, and metric implementations.
- Code / checkpoint availability: not confirmed in this run.
- Citation or related-work caveats: cite results as author-reported and avoid direct numeric comparison across incompatible protocols.
