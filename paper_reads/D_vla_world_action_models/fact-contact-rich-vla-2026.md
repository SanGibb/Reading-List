# Demystifying When and Why VLAs Fail in Contact-Rich Tasks and How to Fix Them

<!-- curation-review:start -->
> 2026-10-20 按新版标准复审：**优先阅读**。已核查官方matched训练与每任务结果，并实际查看Plug/FACT的成功及失败双视角时序。它把接触失败拆为精度/受力并提供无新增数据的噪声调度和force conditioning，直接用于接触任务验证。
> [本次来源、分数与任务判断](../library_review.md#paper-e5b78755d707)。下文保留原精读；旧验收标签不代表本次重新通过，所有实验仍为作者报告。
>
> **本轮准入依据**（技术贡献 / 直接相关性 / 证据：4 / 4 / 4）：相对Agile-WAM的tactile未来latent，此法重在低噪动作学习与force时序调制诊断；本轮没有相同传感器的二者直接比较。平均66%不意味着每任务无退化：Board基线100%对FACT90%。
> - [Title; Abstract (method and evaluation paragraphs); submission history / Comments when present](https://arxiv.org/abs/2608.01402)：Abstract identifies precision and force failure modes; FACT increases low-noise sampling and adds structured force conditioning, reporting 66% versus 41% average success across five tasks and almost 2,500 real-world rollouts.（verified）。
> - [Approach: Precision / Force; Results per-task table and caption; Rollout Gallery](https://stanford-iprl-lab.github.io/fact/)：All methods use pi0.5 LoRA,100 demonstrations/task,20K steps and40 trials/method/task. FACT's average is66.0 versus40.5 ForceVLA; Board regresses100→90 relative to pi0.5. Thus the paper does not establish no-material-regression succession.（verified）。
>
> 引用指标、发布规模和比较结果时，以以上已定位来源和本次复审限制为准，不沿用下文旧概括。
<!-- curation-review:end -->

## Source Links

- Paper: https://arxiv.org/abs/2608.01402
- Project, code, figures, and videos: https://stanford-iprl-lab.github.io/fact/

## TL;DR

FACT diagnoses two distinct VLA breakdowns in contact-rich manipulation: precision failure from under-training the low-noise flow-matching regime and force failure from sparse, temporally structured force signals. A targeted noise schedule plus time-aware force modulation raises source-reported average success from 41% to 66% across five tasks and nearly 2,500 real rollouts.

## Novelty

The paper replaces a generic “VLAs need force” diagnosis with two causal mechanisms and two narrowly targeted fixes that preserve the base policy and require no extra demonstrations.

## Contributions

1. Separates precision and force failure modes with controlled diagnostics.
2. Reallocates flow-matching supervision toward low-noise, sub-millimeter corrections.
3. Encodes force history and modulates its influence according to denoising/contact state.
4. Evaluates the combined method at unusually large real-rollout scale.

## Task Definition

Execute precision- and force-sensitive contact tasks such as plug insertion and board erasing using vision, proprioception, and wrist force/torque sensing.

## Data / Dataset / Benchmark

Five real-world contact-rich tasks and almost 2,500 rollouts, with pi0.5 as the main backbone and pi0 checks for generality. The source reports plug insertion and board erasing as representative precision/force cases.

## Method / Pipeline

FACT replaces the common Beta noise schedule with a logit-normal schedule that emphasizes low-noise action correction. A causal temporal encoder represents instantaneous and recent force, while timestep-conditioned modulation changes force sensitivity through the action denoising process.

## Key Figures / Architecture

figure_status: linked_official

The official page provides success/failure rollouts, force profiles, root-cause plots, the FACT architecture, and per-task comparisons: https://stanford-iprl-lab.github.io/fact/

## Evidence Trail

| Claim | Primary source | Status |
|---|---|---|
| Two distinct contact failure modes | https://arxiv.org/abs/2608.01402 | verified as paper analysis |
| 66% versus 41% average success | https://stanford-iprl-lab.github.io/fact/ | verified, source-reported |
| Nearly 2,500 real rollouts across five tasks | https://arxiv.org/abs/2608.01402 | verified |
| Code release | https://stanford-iprl-lab.github.io/fact/ | linked by official page |

## Evidence / Metrics / Qualitative Results

The official results report a 25-point average improvement, with targeted components contributing up to 20 points on precision tasks and 22.5 points on force tasks. Videos visibly distinguish rim-stall precision errors from incomplete-seating force errors.

## Limitations

The causal claims depend on the paper's schedule and force-ablation setup; external baseline reproduction is not yet established. Evaluation covers five lab tasks, wrist sensing, and primarily pi-family flow policies, so broader embodiment and sensor generality remains open.

## Project Relevance

FACT supplies a useful failure taxonomy and measurable validators for generated-world contact physics, action precision, force history, and VLA training schedules.

## Reproduction / Follow-up Notes

- Reproduce with published ForceVLA/TA-VLA baselines under the same rollout protocol.
- Log low-delta contact segments separately from free-space motion.
- Carry force-history and contact-state fields into action-evaluation schemas.
