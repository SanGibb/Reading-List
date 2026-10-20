# RoboSimStudio: An Interactive Toolkit for Human and Agent Rapid Real2Sim of Robot Manipulation Tasks

<!-- curation-review:start -->
> 2026-10-20 按新版标准复审：**待视觉复核**。Editable solver/contact choices and force-feedback calibration expose a specific reusable real-to-sim interface. Actual contact fidelity, calibration failures and agentic Real2Sim2Real sequences were not inspected.
> [本次来源、分数与任务判断](../library_review.md#paper-2fbe111cb39f)。下文保留原精读；旧验收标签不代表本次重新通过，所有实验仍为作者报告。
<!-- curation-review:end -->

candidate_id: CAND-0001
branch: A
decision: accepted_for_registry

## Source Links

- Paper: https://arxiv.org/abs/2610.18835
- Project: https://robosimstudio.github.io/
- Code: https://github.com/robosimstudio/robosimstudio
- Data / benchmark: https://robosimstudio.github.io/
- Demo / video: https://robosimstudio.github.io/

## TL;DR

Makes contact modeling and physical parameter revision explicit, editable, and agent-operable rather than hiding them in a one-shot real-to-sim pipeline. Directly informs editable PhysicsConfig, ContactModel, ForceTrace, SimCalibration, and Real2Sim2Real validation fields. Main caveat: the release is new and its reported results have not been independently reproduced.

## Novelty

- What is actually new: Makes contact modeling and physical parameter revision explicit, editable, and agent-operable rather than hiding them in a one-shot real-to-sim pipeline.
- Difference from prior work: An interactive toolkit exposes solver, contact-model, and physical-parameter choices to humans and coding agents for iterative simulation refinement.
- Why the delta matters: Directly informs editable PhysicsConfig, ContactModel, ForceTrace, SimCalibration, and Real2Sim2Real validation fields.

## Contributions

1. An interactive toolkit exposes solver, contact-model, and physical-parameter choices to humans and coding agents for iterative simulation refinement.
2. Observed real robot interactions, editable Newton simulations, visual and force-feedback traces, and agentic Real2Sim2Real case studies.
3. Official project page exposes source code and multiple real/generated/output/deployment videos.

## Task

- Input: observations, instructions, actions, or simulator state as specified by the paper.
- Output: Rapidly build and calibrate manipulation simulations from observed physical behavior.
- Setting: embodied or interactive-world evaluation described in the primary paper.
- Success criterion: the paper's task metrics plus the reported qualitative/physical checks.

## Data

- Dataset / benchmark: Observed real robot interactions, editable Newton simulations, visual and force-feedback traces, and agentic Real2Sim2Real case studies.
- Scale: see the primary source for the exact split-level counts.
- Modalities: visual/world state and the action, geometry, force, tactile, or language channels required by the task.
- Collection / annotation: author-described pipeline; not independently audited.
- Splits / evaluation protocol: official paper protocol.

## Method

- Core pipeline: An interactive toolkit exposes solver, contact-model, and physical-parameter choices to humans and coding agents for iterative simulation refinement.
- Model / representation: paper-specific representation summarized above.
- Training or optimization: see the official method and ablation sections.
- Inference / deployment: evaluated in the released simulation, benchmark, or robot setting.
- Losses or metrics: official paper metrics; cross-paper values are not directly comparable.

## Key Figures / Architecture

figure_status: linked_official

- Figure / demo: official project overview/video when available; otherwise primary-paper architecture and qualitative figures.
- Source: https://robosimstudio.github.io/
- What it shows: the system pipeline and representative task outputs or evaluation protocol.
- Why it matters: it verifies the collection-relevant representation, execution, or benchmark interface.

## Evidence Trail

| Claim | Source | Status | Notes |
|---|---|---|---|
| Data / benchmark scope | https://arxiv.org/abs/2610.18835 | verified | Author-reported in the primary paper. |
| Main reported result | https://arxiv.org/abs/2610.18835 | verified | Official project page exposes source code and multiple real/generated/output/deployment videos. |
| Code / checkpoint / demo availability | https://robosimstudio.github.io/ | verified | Official project/code surface inspected. |

## Evidence

- Main metrics: Official project page exposes source code and multiple real/generated/output/deployment videos.
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

- Relevance to interactive embodied generation: Directly informs editable PhysicsConfig, ContactModel, ForceTrace, SimCalibration, and Real2Sim2Real validation fields.
- Reusable fields: extract the named interfaces above into structured registry/benchmark schemas.
- Possible baseline role: direct method, data, or evaluation baseline for its branch.
- Implications for our task / benchmark: motivates explicit executable state and source-traced evaluation rather than image-only plausibility.

## Reproduction / Follow-up

- What to check before using: exact splits, licenses, preprocessing, embodiment assumptions, and metric implementations.
- Code / checkpoint availability: https://github.com/robosimstudio/robosimstudio.
- Citation or related-work caveats: cite results as author-reported and avoid direct numeric comparison across incompatible protocols.
