# Qwen-VLA: Unifying Vision-Language-Action Modeling across Tasks, Environments, and Robot Embodiments

<!-- curation-review:start -->
> 2026-10-20 按新版标准复审：**待视觉复核**。统一manipulation/navigation/trajectory与embodiment文字控制规范是具体跨任务候选；本轮主源可核查，未检代码完整性和不同动作任务时序。
> [本次来源、分数与任务判断](../library_review.md#paper-1578d582cfab)。下文保留原精读；旧验收标签不代表本次重新通过，所有实验仍为作者报告。
<!-- curation-review:end -->

candidate_id: CAND-0006
branch: D
decision: accepted_for_registry

## Source Links

- Paper: https://arxiv.org/abs/2605.30280
- Project: https://github.com/QwenLM/Qwen-VLA
- Code: https://github.com/QwenLM/Qwen-VLA
- Data / benchmark: https://github.com/QwenLM/Qwen-VLA
- Demo / video: https://github.com/QwenLM/Qwen-VLA
- Official figures: https://github.com/QwenLM/Qwen-VLA

## TL;DR

Treats manipulation, navigation, and trajectory prediction as one transferable action-generation problem instead of separate specialist policies. Strong multi-task VLA baseline for EmbodimentDescription, ControlConvention, ContinuousAction, NavigationWaypoint, and trajectory-transfer schemas. The main caveat is that the reported gains remain source-reported and were not independently reproduced in this collection run.

## Novelty

- What is actually new: Treats manipulation, navigation, and trajectory prediction as one transferable action-generation problem instead of separate specialist policies.
- Difference from prior work: It closes a concrete gap between isolated perception/generation components and reusable embodied execution, policy, or evaluation infrastructure.
- Why the delta matters: Strong multi-task VLA baseline for EmbodimentDescription, ControlConvention, ContinuousAction, NavigationWaypoint, and trajectory-transfer schemas.

## Contributions

1. A Qwen vision-language backbone with a DiT continuous-action decoder and embodiment-aware textual conditioning that unifies manipulation, navigation, and trajectory prediction.
2. Joint pretraining over robot manipulation trajectories, egocentric human demonstrations, simulation, vision-language navigation, trajectory supervision, and auxiliary vision-language data.
3. The paper reports 97.9% LIBERO, 73.7% Simpler-WidowX, 86.1/87.2% RoboTwin Easy/Hard, 76.9% average real ALOHA OOD success, and 26.6% zero-shot DOMINO success.

## Task

- Input: Source-specific visual observations, language/task context, state, or action signals.
- Output: Generate continuous actions and trajectories across tasks, environments, and heterogeneous robot embodiments.
- Setting: Embodied simulation and/or real-robot evaluation described by the official source.
- Success criterion: The reported task metrics, transfer performance, or infrastructure validation protocol.

## Data

- Dataset / benchmark: Joint pretraining over robot manipulation trajectories, egocentric human demonstrations, simulation, vision-language navigation, trajectory supervision, and auxiliary vision-language data.
- Scale: See the official paper and project page; central scale claims are source-traced below.
- Modalities: RGB/video plus task-specific actions, kinematics, language, geometry, or simulator state.
- Collection / annotation: Defined by the official source; synthetic and real components are kept distinct.
- Splits / evaluation protocol: Use the paper's official split and matched-baseline protocol before reproducing comparisons.

## Method

- Core pipeline: A Qwen vision-language backbone with a DiT continuous-action decoder and embodiment-aware textual conditioning that unifies manipulation, navigation, and trajectory prediction.
- Model / representation: Task-specific learned representations and explicit embodied state/action interfaces.
- Training or optimization: Follow the official paper; this report does not infer undisclosed settings.
- Inference / deployment: Generate continuous actions and trajectories across tasks, environments, and heterogeneous robot embodiments.
- Losses or metrics: See the official paper for exact objectives and evaluation definitions.

## Key Figures / Architecture

figure_status: linked_official

- Figure / demo: Official method overview and qualitative/demo evidence.
- Source: https://github.com/QwenLM/Qwen-VLA
- Render: linked rather than copied to preserve provenance and avoid stale assets.
- What it shows: The official repository exposes architecture, benchmark tables, and continuous robot demo videos.
- Why it matters: It directly supports the acceptance gate for architecture, execution, visual quality, or infrastructure completeness.

## Evidence Trail

| Claim | Source | Status | Notes |
|---|---|---|---|
| Dataset scale / benchmark size | https://arxiv.org/abs/2605.30280 | verified | Checked on the primary paper surface. |
| Main reported result or comparison | https://arxiv.org/abs/2605.30280 | verified | Reported by authors; not independently reproduced. |
| Code / checkpoint / demo availability | https://github.com/QwenLM/Qwen-VLA | verified | Official project surface inspected on 2026-10-05. |

## Evidence

- Main metrics: The paper reports 97.9% LIBERO, 73.7% Simpler-WidowX, 86.1/87.2% RoboTwin Easy/Hard, 76.9% average real ALOHA OOD success, and 26.6% zero-shot DOMINO success.
- Qualitative results: The official repository exposes architecture, benchmark tables, and continuous robot demo videos.
- Ablations: Consult the official paper for component-level ablations.
- Baselines: Comparisons are accepted only as source-reported and protocol-dependent.
- Reproducibility signals: demo score 4/5; evidence strength 5/5; official project and code available.

## Limitations

- Method limitations: Scope and robustness remain bounded by the embodiments, environments, tasks, and action interfaces studied.
- Experimental limitations: Cross-paper metric comparisons may be invalid when success definitions or hardware differ.
- Demo / visual limitations: Official demos are curated; long-tail failures and full unedited trial distributions are not always exposed.
- Claims that remain unverified: All headline metrics are author-reported and were not independently reproduced.

## Project Relevance

- Relevance to interactive embodied generation: Strong multi-task VLA baseline for EmbodimentDescription, ControlConvention, ContinuousAction, NavigationWaypoint, and trajectory-transfer schemas.
- Reusable fields: derive typed fields from the nouns named above, while preserving source-specific units and coordinate frames.
- Possible baseline role: High-value reference for its primary branch and for cross-branch integration tests.
- Implications for our task / benchmark: Add source-aligned validators for the claimed transfer, controllability, consistency, or evaluation capability.

## Reproduction / Follow-up

- What to check before using: licenses, exact data splits, success criteria, hardware/action conventions, and whether all checkpoints are public.
- Code / checkpoint availability: https://github.com/QwenLM/Qwen-VLA
- Citation or related-work caveats: Cite results as reported by the authors and avoid treating project-page summaries as independent verification.
