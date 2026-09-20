# Agile-WAM: An Agile Tactile World Action Model for Contact-Rich Robot Control

candidate_id: CAND-0003
branch: D
decision: accepted_for_registry

## Source Links

- Paper: https://arxiv.org/abs/2609.20761
- Project / videos: https://hanchuzhou.github.io/TARO_project_page/

## TL;DR

Agile-WAM jointly predicts actions plus future vision/touch latents in a compact flow model. Modality-specific horizons preserve abrupt contact dynamics while keeping inference at a reported 11.9 ms; breadth is limited by small real-task suites and custom sensors.

## Novelty

- Direct latent WAM avoids a large video-generation backbone.
- Predicts slower visual futures and next-step tactile state on different horizons.

## Contributions

1. Efficient tactile world-action architecture.
2. Nine simulated and five real contact-rich tasks.
3. Official execution and corrective-recovery videos.

## Task

- Input: current camera, tactile field, and robot state.
- Output: action chunk plus future vision/tactile latents.
- Success: contact-task success and low control latency.

## Data

Synchronized vision/tactile/action trajectories for insertion, assembly, cable, and related tasks.

## Method

Vision and TacFF encoders form a shared latent feeding flow matching for action/future latents; an action autoencoder and multi-horizon losses regularize control.

## Key Figures / Architecture

figure_status: linked_official

- Architecture, real-task table, and demos: https://hanchuzhou.github.io/TARO_project_page/

## Evidence Trail

| Claim | Source | Status | Notes |
|---|---|---|---|
| 11.9 ms latency | https://arxiv.org/abs/2609.20761 | verified | Author-reported. |
| 29.4% relative real-task gain | https://arxiv.org/abs/2609.20761 | verified | Across five real tasks. |
| Contact/recovery execution quality | https://hanchuzhou.github.io/TARO_project_page/ | verified | Official videos inspected. |

## Evidence

- Project table shows 20 trials per real task and strong aggregate gains.
- Videos demonstrate insertion, assembly, unplugging, and recovery behavior.

## Limitations

- Custom tactile hardware and limited tasks.
- No public code/checkpoint found during this run.

## Project Relevance

Concrete design for `TactileState`, modality-specific `PredictionHorizon`, contact-event dynamics, recovery evaluation, and high-frequency WAM control.

## Reproduction / Follow-up

- Recheck release status.
- Evaluate under sensor shift and longer contact sequences.
