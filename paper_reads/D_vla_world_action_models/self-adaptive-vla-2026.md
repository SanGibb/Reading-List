# Self-Adaptive VLA for Robust Robot Deployment

candidate_id: CAND-0004
branch: D
decision: accepted_for_registry

## Source Links

- Paper: https://arxiv.org/abs/2609.30092
- Project / videos: https://icefoxzhx.github.io/self-adaptive-vla

## TL;DR

Self-Adaptive VLA conditions a frozen-style deployed policy on a compact history of its own shifted rollouts, enabling iterative correction for calibration and actuation drift. The real-robot videos and over-80% recovery result are convincing, but the tested shift family is engineered and limited.

## Novelty

- Converts rollout context into a latent descriptor of deployment-time hardware shift.
- Pre-compensates demonstrations to train shift-conditioned behavior.
- Ensembles context tokens across attempts for progressive self-correction.

## Contributions

1. A plug-in observation/proprioception/action context encoder.
2. AdaLN-based policy modulation without full onsite recalibration.
3. Four precision-critical bimanual and dexterous evaluations.

## Task

- Input: instruction, current observation/state, and prior shifted rollout context.
- Output: adapted continuous robot action chunks.
- Setting: actuation bias, encoder offsets, and new workstation deployment.
- Success criterion: recovered success relative to an unshifted base policy.

## Data

- Base demonstrations plus rollouts collected under deliberately injected hardware shifts.

## Method

- Pre-compensate expert actions for known training shifts.
- Compress rollout context into tokens and modulate policy layers through AdaLN.
- Ensemble tokens from successive attempts to refine compensation.

## Key Figures / Architecture

figure_status: linked_official

- Figure / demo: adaptation architecture and real robot recovery videos.
- Source: https://icefoxzhx.github.io/self-adaptive-vla
- What it shows: failures under shift and iterative restoration of precision.

## Evidence Trail

| Claim | Source | Status | Notes |
|---|---|---|---|
| Recovers over 80% of base performance | https://arxiv.org/abs/2609.30092 | verified | Across reported injected shifts. |
| Four real manipulation tasks | https://icefoxzhx.github.io/self-adaptive-vla | verified | Official videos inspected. |
| Public code/checkpoint | https://icefoxzhx.github.io/self-adaptive-vla | unverified | No confirmed release in this run. |

## Evidence

- Gains cover actuation bias, joint-encoder offsets, and workstation transfer.
- Context ensembling supports stepwise recovery rather than one-shot calibration.

## Limitations

- Shift distributions are constructed and may not span wear, backlash, or sensor failure.
- Evaluation breadth is four precision tasks; safety under failed adaptation is unclear.

## Project Relevance

Defines practical `DeploymentShift`, `RolloutContext`, `AdaptationIteration`, and `RecoveredPerformance` fields for embodied policy evaluation.

## Reproduction / Follow-up

- Verify shift injection ranges and context length.
- Add guardrails for detecting when adaptation worsens behavior.

