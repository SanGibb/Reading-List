# CLAP: Cross-Embodiment Video World Models are Zero-Shot Physical Simulators

candidate_id: CAND-0002
branch: D
decision: accepted_for_registry

## Source Links

- Paper: https://arxiv.org/abs/2608.27406
- Project: https://omni-clap.github.io/
- Code / checkpoints: https://github.com/omni-CLAP/clap

## TL;DR

CLAP trains one action-conditioned video world model across human and heterogeneous robot video, using latent actions to learn shared physics before grounding in end-effector space. Open code, checkpoints, and policy-in-the-loop deployment make it a strong world-action reference, although generated physical hallucinations and full-scale training cost remain important caveats.

## Novelty

- Reconciles heterogeneous actions with end-effector poses, language, and learned latent actions.
- Uses curriculum transfer from unlabeled cross-embodiment video to explicit robot controls.
- Treats a video world model as a deployable zero/few-shot physical simulator.

## Contributions

1. Cross-embodiment action-conditioning scheme.
2. Two-stage latent-to-explicit action curriculum.
3. Open lifecycle covering training, adaptation, evaluation, checkpoints and policy deployment.

## Task

- Input: robot/human video plus end-effector, language, or latent action condition.
- Output: predicted future video used for planning, evaluation, or learning.
- Setting: DROID, Bridge, bimanual YAM, G1 humanoid and OXE mixtures.
- Success criterion: action fidelity, visual/dynamic quality and downstream policy improvement.

## Data

- Dataset: heterogeneous OXE sources, DROID, Bridge, YAM, G1 and egocentric human video.
- Modalities: video, robot controls, language and inferred latent actions.
- Caveat: upstream data must be acquired separately.

## Method

- Stage 1: learn physical priors from unlabeled video with latent actions.
- Stage 2: ground the dynamics in end-effector or robot-specific action spaces.
- Adaptation: few-shot post-training for target embodiments.
- Deployment: rollout interface with openpi or MolmoAct2 policy backends.

## Key Figures / Architecture

figure_status: linked_official

- Figure / demo: curriculum, cross-embodiment rollouts and real-robot planning gallery.
- Source: https://omni-clap.github.io/
- What it shows: one model conditioned through several action interfaces across distinct morphologies.
- Why it matters: demonstrates the shared-physics abstraction and downstream policy loop.

## Evidence Trail

| Claim | Source | Status | Notes |
|---|---|---|---|
| Code and checkpoints are public | Official GitHub | verified | Commands and model registry are documented. |
| DROID/Bridge/YAM/G1 support | Official GitHub | verified | Dataset and embodiment registry. |
| Matches or exceeds specialists | Paper | verified | Author-reported; not reproduced here. |

## Evidence

- Qualitative results: official cross-embodiment predictions and physical deployments are strong and varied.
- Reproducibility: pinned environment, checkpoints and evaluation/deployment commands.
- Resource signal: inference fits on a single modern GPU, while full training is multi-GPU and data-heavy.

## Limitations

- Video rollouts can hallucinate contacts or dynamics.
- Full OXE-scale data and training are costly.
- Learned latent actions do not directly expose named physical state.

## Project Relevance

- Reusable fields: Embodiment, ActionInterface, EndEffectorPose, LatentAction, PredictedFuture, PolicyRollout.
- Baseline role: open cross-embodiment world-action baseline.
- Implication: universal physical priors can be separated from embodiment-specific action grounding.

## Reproduction / Follow-up

- Start with released checkpoints and replay/evaluation commands.
- Audit licenses and preprocessing for every upstream OXE dataset.
- Measure hallucination frequency before safety-critical use.

