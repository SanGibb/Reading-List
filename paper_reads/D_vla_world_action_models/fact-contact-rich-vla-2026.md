# Demystifying When and Why VLAs Fail in Contact-Rich Tasks and How to Fix Them

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
