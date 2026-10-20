# LIBERO-PeRM: Benchmarking Personalized Robotic Manipulation

<!-- curation-review:start -->
> 2026-10-20 按新版标准复审：**观察名单**。偏好完成与任务成功分开有用，但当前主要是LIBERO上专门taxonomy和成对数据构建，缺对核心物理/交互生成能力的决定性贡献证据。
> [本次来源、分数与任务判断](../library_review.md#paper-4381aca01c32)。下文保留原精读；旧验收标签不代表本次重新通过，所有实验仍为作者报告。
<!-- curation-review:end -->

candidate_id: CAND-0012
branch: E
decision: accepted_for_registry

## Source Links

- Paper: https://arxiv.org/abs/2610.22372
- Project: https://libero-perm.github.io/
- Code: linked from the official project page; stable repository URL was not exposed to the inspection client
- Data / benchmark: https://libero-perm.github.io/
- Demo / video: https://libero-perm.github.io/

## TL;DR

Separates robotic task success from how a user wants the task performed with reusable, automatically scored preference variables. Adds Preference, SatisfactionMetric, Conflict, Composition, UserProfile, and personalized manipulation evaluation fields. Main caveat: the release is new and its reported results have not been independently reproduced.

## Novelty

- What is actually new: Separates robotic task success from how a user wants the task performed with reusable, automatically scored preference variables.
- Difference from prior work: A procedural LIBERO pipeline generates preference-ready scenes, paired preferred/non-preferred demonstrations, and explicit satisfaction metrics for motion, skill, and user-profile preferences.
- Why the delta matters: Adds Preference, SatisfactionMetric, Conflict, Composition, UserProfile, and personalized manipulation evaluation fields.

## Contributions

1. A procedural LIBERO pipeline generates preference-ready scenes, paired preferred/non-preferred demonstrations, and explicit satisfaction metrics for motion, skill, and user-profile preferences.
2. 312 tasks in five suites, 37 single and 18 paired preferences, and 40.8K demonstrations with task, preference, simulator-state, and per-step metadata.
3. Official project page exposes task explorer clips, dataset/code links, five suites, and complete reproduction scripts.

## Task

- Input: observations, instructions, actions, or simulator state as specified by the paper.
- Output: Evaluate zero-shot, learned, generalized, composed, and conflicting preferences separately from task completion.
- Setting: embodied or interactive-world evaluation described in the primary paper.
- Success criterion: the paper's task metrics plus the reported qualitative/physical checks.

## Data

- Dataset / benchmark: 312 tasks in five suites, 37 single and 18 paired preferences, and 40.8K demonstrations with task, preference, simulator-state, and per-step metadata.
- Scale: see the primary source for the exact split-level counts.
- Modalities: visual/world state and the action, geometry, force, tactile, or language channels required by the task.
- Collection / annotation: author-described pipeline; not independently audited.
- Splits / evaluation protocol: official paper protocol.

## Method

- Core pipeline: A procedural LIBERO pipeline generates preference-ready scenes, paired preferred/non-preferred demonstrations, and explicit satisfaction metrics for motion, skill, and user-profile preferences.
- Model / representation: paper-specific representation summarized above.
- Training or optimization: see the official method and ablation sections.
- Inference / deployment: evaluated in the released simulation, benchmark, or robot setting.
- Losses or metrics: official paper metrics; cross-paper values are not directly comparable.

## Key Figures / Architecture

figure_status: not_applicable

- Figure / demo: official project overview/video when available; otherwise primary-paper architecture and qualitative figures.
- Source: https://libero-perm.github.io/
- What it shows: the system pipeline and representative task outputs or evaluation protocol.
- Why it matters: it verifies the collection-relevant representation, execution, or benchmark interface.

## Evidence Trail

| Claim | Source | Status | Notes |
|---|---|---|---|
| Data / benchmark scope | https://arxiv.org/abs/2610.22372 | verified | Author-reported in the primary paper. |
| Main reported result | https://arxiv.org/abs/2610.22372 | verified | Official project page exposes task explorer clips, dataset/code links, five suites, and complete reproduction scripts. |
| Code / checkpoint / demo availability | https://libero-perm.github.io/ | verified | Official page links code, dataset, and reproduction scripts; the stable repository URL was not exposed to the inspection client. |

## Evidence

- Main metrics: Official project page exposes task explorer clips, dataset/code links, five suites, and complete reproduction scripts.
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

- Relevance to interactive embodied generation: Adds Preference, SatisfactionMetric, Conflict, Composition, UserProfile, and personalized manipulation evaluation fields.
- Reusable fields: extract the named interfaces above into structured registry/benchmark schemas.
- Possible baseline role: direct method, data, or evaluation baseline for its branch.
- Implications for our task / benchmark: motivates explicit executable state and source-traced evaluation rather than image-only plausibility.

## Reproduction / Follow-up

- What to check before using: exact splits, licenses, preprocessing, embodiment assumptions, and metric implementations.
- Code / checkpoint availability: linked from the official project page; stable repository URL not confirmed in this run.
- Citation or related-work caveats: cite results as author-reported and avoid direct numeric comparison across incompatible protocols.
