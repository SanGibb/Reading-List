# VLA-JEPA: Enhancing Vision-Language-Action Model with Latent World Model

candidate_id: CAND-0002
branch: D
decision: accepted_for_registry

## Source Links

- Paper: https://arxiv.org/abs/2602.10098
- Project: https://ginwind.github.io/VLA-JEPA/
- Code: https://github.com/ginwind/VLA-JEPA
- Data / benchmark: LIBERO, LIBERO-Plus, SimplerEnv, DROID, BridgeV2
- Demo / official figures: https://ginwind.github.io/VLA-JEPA/

## TL;DR

VLA-JEPA pretrains a compact VLA by predicting action-relevant future states in latent space while preventing future-frame leakage into the student path. The training-time world model disappears at inference. Its July 2026 LeRobot integration makes it practically accessible, although the public repository still labels parts of training code as partial.

## Novelty

- Introduces leakage-free JEPA future-state prediction for VLA pretraining.
- Predicts latent dynamics instead of pixels or future-contaminated latent actions.
- Adds action-relevant world supervision with no deployment-time world-model cost.

## Contributions

1. Defines a future-target encoder/current-only student split.
2. Uses JEPA pretraining followed by action-head fine-tuning.
3. Evaluates on three simulation suites and real manipulation with public integrations.

## Task

- Input: current image and language instruction.
- Output: robot action sequence.
- Setting: simulated and real manipulation under appearance/dynamics shifts.
- Success criterion: benchmark or physical task success.

## Data

- Dataset / benchmark: SSV2, DROID, BridgeV2, LIBERO, LIBERO-Plus, SimplerEnv.
- Scale: multiple video/robot corpora; aggregate scale varies by stage.
- Modalities: RGB video, language, actions.
- Collection / annotation: reused public video and demonstrations.
- Splits / evaluation protocol: standard suites plus real rollouts.

## Method

- Core pipeline: future target encoder, current-only student latent prediction, action fine-tuning.
- Model / representation: Qwen3-VL-2B VLA with V-JEPA2-style supervision.
- Training or optimization: two-stage JEPA then action learning.
- Inference / deployment: policy predicts actions directly; target branch is removed.
- Losses or metrics: latent prediction and task success.

## Key Figures / Architecture

figure_status: linked_official

- Figure / demo: official leakage-free architecture and manipulation rollouts.
- Source: https://ginwind.github.io/VLA-JEPA/
- What it shows: future targets supervise a current-only student and action head.
- Why it matters: clarifies the leakage guard and zero inference overhead.

## Evidence Trail

| Claim | Source | Status | Notes |
|---|---|---|---|
| Leakage-free latent future prediction | https://arxiv.org/abs/2602.10098 | verified | Central method. |
| Three suites plus real manipulation | https://arxiv.org/abs/2602.10098 | verified | Source-reported evaluation. |
| Public code and LeRobot integration | https://github.com/ginwind/VLA-JEPA | verified | Repository and official release. |

## Evidence

- Main metrics: consistent success gains are reported across all evaluation families.
- Qualitative results: official page supplies task rollouts.
- Ablations: leakage prevention and latent prediction choices are isolated.
- Baselines: contemporary VLA and latent-action methods.
- Reproducibility signals: repository, data recipes, evaluation instructions, checkpoints.

## Limitations

- Depends on target embeddings capturing action-relevant dynamics.
- Manipulation-centric evaluation may not transfer to navigation.
- Rollouts are selected examples, benchmark gains were not reproduced, and code is partial.

## Project Relevance

- Latent world representation directly supervises action learning.
- Reusable fields: FutureLatentTarget, LeakageGuard, ActionHead, TrainingOnlyWorldModel.
- Baseline role: compact world-action pretraining.
- Separately evaluate predictive supervision quality and deployment cost.

## Reproduction / Follow-up

- Verify released checkpoints, missing training pieces, and compute/data controls.
- Partial code and LeRobot checkpoints are public.
- Do not confuse VLA-JEPA with the separate VL-JEPA model.
