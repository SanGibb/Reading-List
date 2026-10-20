# From Failures to Learnable Worlds: Policy-Conditioned Environment Generation for Navigation Agents

<!-- curation-review:start -->
> 2026-10-20 按新版标准复审：**待视觉复核**。Validated policy-specific weakness features and matched random/hard controls are a substantive targeted-generation capability. Actual generated worlds, navigation behaviors and failure coverage remain uninspected.
> [本次来源、分数与任务判断](../library_review.md#paper-f1b5ff16a834)。下文保留原精读；旧验收标签不代表本次重新通过，所有实验仍为作者报告。
<!-- curation-review:end -->

candidate_id: CAND-0004
branch: B
decision: accepted_for_registry

## Source Links

- Paper: https://arxiv.org/abs/2610.19420
- Project: https://zhangyuejoslin.github.io/WEDGE/
- Code: https://github.com/zhangyuejoslin/WEDGE
- Data / benchmark: https://zhangyuejoslin.github.io/WEDGE/
- Demo / video: https://zhangyuejoslin.github.io/WEDGE/

## TL;DR

Uses an agent's measured weaknesses—not generic realism or difficulty—to drive environment generation and iterative adaptation. Useful for FailureFeature, EnvironmentFactor, GeneratorControl, DiagnosticSplit, and targeted curriculum generation. Main caveat: the release is new and its reported results have not been independently reproduced.

## Novelty

- What is actually new: Uses an agent's measured weaknesses—not generic realism or difficulty—to drive environment generation and iterative adaptation.
- Difference from prior work: WEDGE contrasts successful and failed rollouts, validates executable weakness features, maps them to controllable environment factors, and regenerates targeted training worlds.
- Why the delta matters: Useful for FailureFeature, EnvironmentFactor, GeneratorControl, DiagnosticSplit, and targeted curriculum generation.

## Contributions

1. WEDGE contrasts successful and failed rollouts, validates executable weakness features, maps them to controllable environment factors, and regenerates targeted training worlds.
2. ProcTHOR diagnostic rollouts and generated navigation environments, evaluated with three agents and transfer to HM3D.
3. Official page contains extensive generated-environment videos, code, and cross-agent ProcTHOR/HM3D results.

## Task

- Input: observations, instructions, actions, or simulator state as specified by the paper.
- Output: Generate policy-specific navigation environments that target verified failure modes.
- Setting: embodied or interactive-world evaluation described in the primary paper.
- Success criterion: the paper's task metrics plus the reported qualitative/physical checks.

## Data

- Dataset / benchmark: ProcTHOR diagnostic rollouts and generated navigation environments, evaluated with three agents and transfer to HM3D.
- Scale: see the primary source for the exact split-level counts.
- Modalities: visual/world state and the action, geometry, force, tactile, or language channels required by the task.
- Collection / annotation: author-described pipeline; not independently audited.
- Splits / evaluation protocol: official paper protocol.

## Method

- Core pipeline: WEDGE contrasts successful and failed rollouts, validates executable weakness features, maps them to controllable environment factors, and regenerates targeted training worlds.
- Model / representation: paper-specific representation summarized above.
- Training or optimization: see the official method and ablation sections.
- Inference / deployment: evaluated in the released simulation, benchmark, or robot setting.
- Losses or metrics: official paper metrics; cross-paper values are not directly comparable.

## Key Figures / Architecture

figure_status: linked_official

- Figure / demo: official project overview/video when available; otherwise primary-paper architecture and qualitative figures.
- Source: https://zhangyuejoslin.github.io/WEDGE/
- What it shows: the system pipeline and representative task outputs or evaluation protocol.
- Why it matters: it verifies the collection-relevant representation, execution, or benchmark interface.

## Evidence Trail

| Claim | Source | Status | Notes |
|---|---|---|---|
| Data / benchmark scope | https://arxiv.org/abs/2610.19420 | verified | Author-reported in the primary paper. |
| Main reported result | https://arxiv.org/abs/2610.19420 | verified | Official page contains extensive generated-environment videos, code, and cross-agent ProcTHOR/HM3D results. |
| Code / checkpoint / demo availability | https://zhangyuejoslin.github.io/WEDGE/ | verified | Official project/code surface inspected. |

## Evidence

- Main metrics: Official page contains extensive generated-environment videos, code, and cross-agent ProcTHOR/HM3D results.
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

- Relevance to interactive embodied generation: Useful for FailureFeature, EnvironmentFactor, GeneratorControl, DiagnosticSplit, and targeted curriculum generation.
- Reusable fields: extract the named interfaces above into structured registry/benchmark schemas.
- Possible baseline role: direct method, data, or evaluation baseline for its branch.
- Implications for our task / benchmark: motivates explicit executable state and source-traced evaluation rather than image-only plausibility.

## Reproduction / Follow-up

- What to check before using: exact splits, licenses, preprocessing, embodiment assumptions, and metric implementations.
- Code / checkpoint availability: https://github.com/zhangyuejoslin/WEDGE.
- Citation or related-work caveats: cite results as author-reported and avoid direct numeric comparison across incompatible protocols.
