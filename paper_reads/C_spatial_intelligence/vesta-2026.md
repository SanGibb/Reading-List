# Vesta: A Generalist Embodied Reasoning Model

<!-- curation-review:start -->
> 2026-10-20 按新版标准复审：**待视觉复核**。官方方法与记忆 harness 可确认，但核心还包括真实机器人长期执行；本轮未完整观察相关媒体。保留为待复核，不用 broad generalist 宣传或摘要平均提升通过新门槛。
> [本次来源、分数与任务判断](../library_review.md#paper-e67c4198395f)。下文保留原精读；旧验收标签不代表本次重新通过，所有实验仍为作者报告。
<!-- curation-review:end -->

candidate_id: CAND-0005
branch: C
decision: accepted_for_registry

## Source Links

- Paper: https://arxiv.org/abs/2606.20905
- Project: https://research.nvidia.com/labs/gear/vesta/
- Code: not publicly identified in this run
- Data / benchmark: https://research.nvidia.com/labs/gear/vesta/
- Demo / video: https://research.nvidia.com/labs/gear/vesta/
- Official figures: https://research.nvidia.com/labs/gear/vesta/

## TL;DR

Shows that one embodied reasoning checkpoint can match specialist systems while retaining explicit episodic memory and tool-calling for robot planning. Provides a concrete memory-and-planning interface for Observation, Progress, Reasoning, Action, EpisodicMemory, PixelGoal, and ToolCall fields. The main caveat is that the reported gains remain source-reported and were not independently reproduced in this collection run.

## Novelty

- What is actually new: Shows that one embodied reasoning checkpoint can match specialist systems while retaining explicit episodic memory and tool-calling for robot planning.
- Difference from prior work: It closes a concrete gap between isolated perception/generation components and reusable embodied execution, policy, or evaluation infrastructure.
- Why the delta matters: Provides a concrete memory-and-planning interface for Observation, Progress, Reasoning, Action, EpisodicMemory, PixelGoal, and ToolCall fields.

## Contributions

1. Qwen3-VL-8B fine-tuning plus a multimodal memory harness that interleaves observations, textual progress state, reasoning, and next-subtask actions for hierarchical control.
2. A curated SFT mixture spanning localization, navigation, spatial intelligence, grounding, embodied reasoning, general VLM data, and real-robot action planning.
3. The official project reports 68.7 average embodied-cognition score, 55.5 R2R-CE success, and a 38.3-point real-robot success improvement over actor-only control.

## Task

- Input: Source-specific visual observations, language/task context, state, or action signals.
- Output: Unify spatial grounding, navigation, embodied QA, memory, and long-horizon robot planning in a single model.
- Setting: Embodied simulation and/or real-robot evaluation described by the official source.
- Success criterion: The reported task metrics, transfer performance, or infrastructure validation protocol.

## Data

- Dataset / benchmark: A curated SFT mixture spanning localization, navigation, spatial intelligence, grounding, embodied reasoning, general VLM data, and real-robot action planning.
- Scale: See the official paper and project page; central scale claims are source-traced below.
- Modalities: RGB/video plus task-specific actions, kinematics, language, geometry, or simulator state.
- Collection / annotation: Defined by the official source; synthetic and real components are kept distinct.
- Splits / evaluation protocol: Use the paper's official split and matched-baseline protocol before reproducing comparisons.

## Method

- Core pipeline: Qwen3-VL-8B fine-tuning plus a multimodal memory harness that interleaves observations, textual progress state, reasoning, and next-subtask actions for hierarchical control.
- Model / representation: Task-specific learned representations and explicit embodied state/action interfaces.
- Training or optimization: Follow the official paper; this report does not infer undisclosed settings.
- Inference / deployment: Unify spatial grounding, navigation, embodied QA, memory, and long-horizon robot planning in a single model.
- Losses or metrics: See the official paper for exact objectives and evaluation definitions.

## Key Figures / Architecture

figure_status: linked_official

- Figure / demo: Official method overview and qualitative/demo evidence.
- Source: https://research.nvidia.com/labs/gear/vesta/
- Render: linked rather than copied to preserve provenance and avoid stale assets.
- What it shows: Official page includes architecture figures and continuous YAM manipulation and simulated G1 navigation videos.
- Why it matters: It directly supports the acceptance gate for architecture, execution, visual quality, or infrastructure completeness.

## Evidence Trail

| Claim | Source | Status | Notes |
|---|---|---|---|
| Dataset scale / benchmark size | https://arxiv.org/abs/2606.20905 | verified | Checked on the primary paper surface. |
| Main reported result or comparison | https://arxiv.org/abs/2606.20905 | verified | Reported by authors; not independently reproduced. |
| Code / checkpoint / demo availability | https://research.nvidia.com/labs/gear/vesta/ | verified | Official project surface inspected on 2026-10-05. |

## Evidence

- Main metrics: The official project reports 68.7 average embodied-cognition score, 55.5 R2R-CE success, and a 38.3-point real-robot success improvement over actor-only control.
- Qualitative results: Official page includes architecture figures and continuous YAM manipulation and simulated G1 navigation videos.
- Ablations: Consult the official paper for component-level ablations.
- Baselines: Comparisons are accepted only as source-reported and protocol-dependent.
- Reproducibility signals: demo score 3/5; evidence strength 5/5; official project available.

## Limitations

- Method limitations: Scope and robustness remain bounded by the embodiments, environments, tasks, and action interfaces studied.
- Experimental limitations: Cross-paper metric comparisons may be invalid when success definitions or hardware differ.
- Demo / visual limitations: Official demos are curated; long-tail failures and full unedited trial distributions are not always exposed.
- Claims that remain unverified: All headline metrics are author-reported and were not independently reproduced.

## Project Relevance

- Relevance to interactive embodied generation: Provides a concrete memory-and-planning interface for Observation, Progress, Reasoning, Action, EpisodicMemory, PixelGoal, and ToolCall fields.
- Reusable fields: derive typed fields from the nouns named above, while preserving source-specific units and coordinate frames.
- Possible baseline role: High-value reference for its primary branch and for cross-branch integration tests.
- Implications for our task / benchmark: Add source-aligned validators for the claimed transfer, controllability, consistency, or evaluation capability.

## Reproduction / Follow-up

- What to check before using: licenses, exact data splits, success criteria, hardware/action conventions, and whether all checkpoints are public.
- Code / checkpoint availability: No public code URL was confirmed in this run.
- Citation or related-work caveats: Cite results as reported by the authors and avoid treating project-page summaries as independent verification.
