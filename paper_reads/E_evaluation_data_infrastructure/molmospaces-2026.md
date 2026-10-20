# MolmoSpaces: A Large-Scale Open Ecosystem for Robot Navigation and Manipulation

<!-- curation-review:start -->
> 2026-10-20 按新版标准复审：**优先阅读**。规模、物理标注、模块化配置和跨模拟器八类任务形成可复用基础，主要推荐其数据/测试接口，不依据未看demo宣称场景/策略质量。
> [本次来源、分数与任务判断](../library_review.md#paper-cf1da4010d62)。下文保留原精读；旧验收标签不代表本次重新通过，所有实验仍为作者报告。
>
> **本轮准入依据**（技术贡献 / 直接相关性 / 证据：5 / 5 / 4）：相较RoboVerse平台统一，MolmoSpaces提供大规模场景/物体/抓取、显式划分和质量测试，保留平台备选。
> - [Sec.3.1 Tables2-4; Sec.3 ecosystem list; Sec.4 Benchmark](https://arxiv.org/html/2602.11337v1)：230k+场景、130k物体/42M grasps；八零样本任务；质量表按稳定/抬升/交互/关节分开，MSMultiType关节仅65.2%，不能概括为所有测试95%+。（verified）。
>
> 引用指标、发布规模和比较结果时，以以上已定位来源和本次复审限制为准，不沿用下文旧概括。
<!-- curation-review:end -->

candidate_id: CAND-0004
branch: E
decision: accepted_for_registry

## Source Links

- Paper: https://arxiv.org/abs/2602.11337
- Project: https://molmospaces.allen.ai/
- Code: https://github.com/allenai/MolmoSpaces
- Data / benchmark: https://molmospaces.allen.ai/
- Demo / video: https://molmospaces.allen.ai/
- Official figures: https://allenai.org/blog/molmospaces

## TL;DR

Unifies unusually large scene, asset, grasp, simulator-portability, and factor-controlled evaluation layers in one open embodied ecosystem. Direct source for Scene, Asset, Collider, Joint, Grasp, PhysicalParameter, DistributionShiftAxis, and cross-simulator evaluation schemas. The main caveat is that the reported gains remain source-reported and were not independently reproduced in this collection run.

## Novelty

- What is actually new: Unifies unusually large scene, asset, grasp, simulator-portability, and factor-controlled evaluation layers in one open embodied ecosystem.
- Difference from prior work: It closes a concrete gap between isolated perception/generation components and reusable embodied execution, policy, or evaluation infrastructure.
- Why the delta matters: Direct source for Scene, Asset, Collider, Joint, Grasp, PhysicalParameter, DistributionShiftAxis, and cross-simulator evaluation schemas.

## Contributions

1. An open asset, scene, grasp, validation, conversion, trajectory-generation, and benchmark stack with explicit physical parameters and systematic variation axes.
2. 230K+ indoor scenes, 130K+ curated object assets, and 42M+ physics-grounded 6-DoF grasps, with cross-simulator conversion and controlled splits.
3. The official release documents 95%+ scene validation pass rates, 42M grasps over 48K+ objects, and compatibility with MuJoCo, ManiSkill, Isaac Lab, and Isaac Sim.

## Task

- Input: Source-specific visual observations, language/task context, state, or action signals.
- Output: Provide scalable physics-grounded infrastructure for training and diagnosing navigation and manipulation policies.
- Setting: Embodied simulation and/or real-robot evaluation described by the official source.
- Success criterion: The reported task metrics, transfer performance, or infrastructure validation protocol.

## Data

- Dataset / benchmark: 230K+ indoor scenes, 130K+ curated object assets, and 42M+ physics-grounded 6-DoF grasps, with cross-simulator conversion and controlled splits.
- Scale: See the official paper and project page; central scale claims are source-traced below.
- Modalities: RGB/video plus task-specific actions, kinematics, language, geometry, or simulator state.
- Collection / annotation: Defined by the official source; synthetic and real components are kept distinct.
- Splits / evaluation protocol: Use the paper's official split and matched-baseline protocol before reproducing comparisons.

## Method

- Core pipeline: An open asset, scene, grasp, validation, conversion, trajectory-generation, and benchmark stack with explicit physical parameters and systematic variation axes.
- Model / representation: Task-specific learned representations and explicit embodied state/action interfaces.
- Training or optimization: Follow the official paper; this report does not infer undisclosed settings.
- Inference / deployment: Provide scalable physics-grounded infrastructure for training and diagnosing navigation and manipulation policies.
- Losses or metrics: See the official paper for exact objectives and evaluation definitions.

## Key Figures / Architecture

figure_status: linked_official

- Figure / demo: Official method overview and qualitative/demo evidence.
- Source: https://allenai.org/blog/molmospaces
- Render: linked rather than copied to preserve provenance and avoid stale assets.
- What it shows: Official diagrams, interactive MuJoCo demo, asset browser, and benchmark surfaces expose the full infrastructure stack.
- Why it matters: It directly supports the acceptance gate for architecture, execution, visual quality, or infrastructure completeness.

## Evidence Trail

| Claim | Source | Status | Notes |
|---|---|---|---|
| Dataset scale / benchmark size | https://arxiv.org/abs/2602.11337 | verified | Checked on the primary paper surface. |
| Main reported result or comparison | https://arxiv.org/abs/2602.11337 | verified | Reported by authors; not independently reproduced. |
| Code / checkpoint / demo availability | https://molmospaces.allen.ai/ | verified | Official project surface inspected on 2026-10-05. |

## Evidence

- Main metrics: The official release documents 95%+ scene validation pass rates, 42M grasps over 48K+ objects, and compatibility with MuJoCo, ManiSkill, Isaac Lab, and Isaac Sim.
- Qualitative results: Official diagrams, interactive MuJoCo demo, asset browser, and benchmark surfaces expose the full infrastructure stack.
- Ablations: Consult the official paper for component-level ablations.
- Baselines: Comparisons are accepted only as source-reported and protocol-dependent.
- Reproducibility signals: demo score 5/5; evidence strength 5/5; official project and code available.

## Limitations

- Method limitations: Scope and robustness remain bounded by the embodiments, environments, tasks, and action interfaces studied.
- Experimental limitations: Cross-paper metric comparisons may be invalid when success definitions or hardware differ.
- Demo / visual limitations: Official demos are curated; long-tail failures and full unedited trial distributions are not always exposed.
- Claims that remain unverified: All headline metrics are author-reported and were not independently reproduced.

## Project Relevance

- Relevance to interactive embodied generation: Direct source for Scene, Asset, Collider, Joint, Grasp, PhysicalParameter, DistributionShiftAxis, and cross-simulator evaluation schemas.
- Reusable fields: derive typed fields from the nouns named above, while preserving source-specific units and coordinate frames.
- Possible baseline role: High-value reference for its primary branch and for cross-branch integration tests.
- Implications for our task / benchmark: Add source-aligned validators for the claimed transfer, controllability, consistency, or evaluation capability.

## Reproduction / Follow-up

- What to check before using: licenses, exact data splits, success criteria, hardware/action conventions, and whether all checkpoints are public.
- Code / checkpoint availability: https://github.com/allenai/MolmoSpaces
- Citation or related-work caveats: Cite results as reported by the authors and avoid treating project-page summaries as independent verification.
