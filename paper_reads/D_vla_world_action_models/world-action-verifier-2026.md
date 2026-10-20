# World Action Verifier: Self-Improving World Models via Forward-Inverse Asymmetry

<!-- curation-review:start -->
> 2026-10-20 按新版标准复审：**待视觉复核**。把验证拆为plausibility/reachability并主动收集world model失败，直接提供生成世界验证接口；主源当前摘要是>22% policy增益，旧精读的>18%需标版本。
> [本次来源、分数与任务判断](../library_review.md#paper-510dc2cd7119)。下文保留原精读；旧验收标签不代表本次重新通过，所有实验仍为作者报告。
<!-- curation-review:end -->

candidate_id: CAND-0008
branch: D
decision: accepted_for_registry

## Source Links

- Paper: https://arxiv.org/abs/2604.01985
- Project: https://world-action-verifier.github.io/
- Code: https://github.com/yuejiangliu/world-action-verifier
- Data / benchmark: https://world-action-verifier.github.io/
- Demo / video: https://world-action-verifier.github.io/
- Official figures: https://world-action-verifier.github.io/

## TL;DR

Turns forward-inverse asymmetry into a self-verification and exploration mechanism instead of estimating forward-model uncertainty directly. Direct design reference for Plausibility, Reachability, InverseAction, CycleConsistency, ActionFollowingScore, and model-error-directed collection. The main caveat is that the reported gains remain source-reported and were not independently reproduced in this collection run.

## Novelty

- What is actually new: Turns forward-inverse asymmetry into a self-verification and exploration mechanism instead of estimating forward-model uncertainty directly.
- Difference from prior work: It closes a concrete gap between isolated perception/generation components and reusable embodied execution, policy, or evaluation infrastructure.
- Why the delta matters: Direct design reference for Plausibility, Reachability, InverseAction, CycleConsistency, ActionFollowingScore, and model-error-directed collection.

## Contributions

1. Factorizes verification into state plausibility and action reachability, using a video-trained subgoal generator, sparse inverse dynamics, and forward-cycle consistency to target model failures.
2. Nine tasks across MiniGrid, RoboMimic, and ManiSkill, combining action-labeled transitions with broader action-free video-derived subgoals.
3. The paper reports 2x sample efficiency and more than 18% downstream policy improvement; official code and qualitative rollout comparisons are public.

## Task

- Input: Source-specific visual observations, language/task context, state, or action signals.
- Output: Let a world model discover under-covered failures, collect useful transitions, and improve downstream imagination-based policy learning.
- Setting: Embodied simulation and/or real-robot evaluation described by the official source.
- Success criterion: The reported task metrics, transfer performance, or infrastructure validation protocol.

## Data

- Dataset / benchmark: Nine tasks across MiniGrid, RoboMimic, and ManiSkill, combining action-labeled transitions with broader action-free video-derived subgoals.
- Scale: See the official paper and project page; central scale claims are source-traced below.
- Modalities: RGB/video plus task-specific actions, kinematics, language, geometry, or simulator state.
- Collection / annotation: Defined by the official source; synthetic and real components are kept distinct.
- Splits / evaluation protocol: Use the paper's official split and matched-baseline protocol before reproducing comparisons.

## Method

- Core pipeline: Factorizes verification into state plausibility and action reachability, using a video-trained subgoal generator, sparse inverse dynamics, and forward-cycle consistency to target model failures.
- Model / representation: Task-specific learned representations and explicit embodied state/action interfaces.
- Training or optimization: Follow the official paper; this report does not infer undisclosed settings.
- Inference / deployment: Let a world model discover under-covered failures, collect useful transitions, and improve downstream imagination-based policy learning.
- Losses or metrics: See the official paper for exact objectives and evaluation definitions.

## Key Figures / Architecture

figure_status: linked_official

- Figure / demo: Official method overview and qualitative/demo evidence.
- Source: https://world-action-verifier.github.io/
- Render: linked rather than copied to preserve provenance and avoid stale assets.
- What it shows: Official page links method diagrams, an interactive MiniGrid predictor, and side-by-side RoboMimic rollout videos.
- Why it matters: It directly supports the acceptance gate for architecture, execution, visual quality, or infrastructure completeness.

## Evidence Trail

| Claim | Source | Status | Notes |
|---|---|---|---|
| Dataset scale / benchmark size | https://arxiv.org/abs/2604.01985 | verified | Checked on the primary paper surface. |
| Main reported result or comparison | https://arxiv.org/abs/2604.01985 | verified | Reported by authors; not independently reproduced. |
| Code / checkpoint / demo availability | https://world-action-verifier.github.io/ | verified | Official project surface inspected on 2026-10-05. |

## Evidence

- Main metrics: The paper reports 2x sample efficiency and more than 18% downstream policy improvement; official code and qualitative rollout comparisons are public.
- Qualitative results: Official page links method diagrams, an interactive MiniGrid predictor, and side-by-side RoboMimic rollout videos.
- Ablations: Consult the official paper for component-level ablations.
- Baselines: Comparisons are accepted only as source-reported and protocol-dependent.
- Reproducibility signals: demo score 4/5; evidence strength 5/5; official project and code available.

## Limitations

- Method limitations: Scope and robustness remain bounded by the embodiments, environments, tasks, and action interfaces studied.
- Experimental limitations: Cross-paper metric comparisons may be invalid when success definitions or hardware differ.
- Demo / visual limitations: Official demos are curated; long-tail failures and full unedited trial distributions are not always exposed.
- Claims that remain unverified: All headline metrics are author-reported and were not independently reproduced.

## Project Relevance

- Relevance to interactive embodied generation: Direct design reference for Plausibility, Reachability, InverseAction, CycleConsistency, ActionFollowingScore, and model-error-directed collection.
- Reusable fields: derive typed fields from the nouns named above, while preserving source-specific units and coordinate frames.
- Possible baseline role: High-value reference for its primary branch and for cross-branch integration tests.
- Implications for our task / benchmark: Add source-aligned validators for the claimed transfer, controllability, consistency, or evaluation capability.

## Reproduction / Follow-up

- What to check before using: licenses, exact data splits, success criteria, hardware/action conventions, and whether all checkpoints are public.
- Code / checkpoint availability: https://github.com/yuejiangliu/world-action-verifier
- Citation or related-work caveats: Cite results as reported by the authors and avoid treating project-page summaries as independent verification.
