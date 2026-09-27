# InternW0: A Foundational Physical World Model for Efficient Real-World Interactions

candidate_id: CAND-0007
branch: D
decision: accepted_for_registry

## Source Links

- Paper: https://arxiv.org/abs/2609.27656
- Project / demos: https://internrobotics.github.io/internw0/
- Code: https://github.com/InternRobotics/internw0
- Models: https://huggingface.co/InternRobotics/models

## TL;DR

InternW0 is an open asynchronous video-action world model trained on 7,233.5 hours across 25 domains, with force/tactile post-training and unusually demanding scientific-manipulation demos. Its scale and release quality make it a high-value baseline, although exact reproduction is expensive.

## Novelty

- Separates a high-capacity predictive video expert from a faster action expert.
- Reuses predictive K/V context and routes new observations instead of regenerating the future per update.
- Adds heterogeneous-embodiment interfaces plus contact-aware force/tactile control.

## Contributions

1. Open model family for asynchronous physical prediction and control.
2. A 7,233.5-hour mixture with EgoLab's 275.4 hours of lab activity.
3. Everyday, industrial, 15-stage MOF, and five-stage dexterous pipetting evaluation.

## Task

- Input: language, images, robot state, embodiment prompts, and optional force/tactile signals.
- Output: future visual context and continuous actions at different update frequencies.
- Setting: heterogeneous robots and long-horizon scientific tasks.
- Success criterion: task success/progress under efficient update latency.

## Data

- 811,969 episodes across 25 domains from six robot datasets plus EgoLab.
- Sources include simulated and real manipulation and egocentric video-only supervision.

## Method

- Mixture-of-transformers video/action experts trained with joint flow matching.
- Observation-conditioned context routing updates cached predictive features.
- Soft prompts and a unified 37D interface handle domains; contact post-training adds physical channels.

## Key Figures / Architecture

figure_status: linked_official

- Figure / demo: architecture, data mixture, latency chart, and robot/lab videos.
- Source: https://internrobotics.github.io/internw0/
- What it shows: asynchronous context reuse and real multi-stage physical execution.

## Evidence Trail

| Claim | Source | Status | Notes |
|---|---|---|---|
| 7,233.5 hours / 811,969 episodes | https://internrobotics.github.io/internw0/ | verified | Official data table. |
| 16.47 Hz, 60.73 ms update | https://internrobotics.github.io/internw0/ | verified | RTX 5090D model-side measurement. |
| Code and model weights | https://github.com/InternRobotics/internw0 | verified | Official release links. |

## Evidence

- Reports 98.6% LIBERO and 93.12% RoboTwin 2.0-Full.
- On real tasks, reports 82.7% part sorting, 88.9% tube sorting, 68.4% MOF progress, and 65.3% pipetting progress.

## Limitations

- Training scale and hardware make full reproduction costly.
- Real results are author-reported over 15 trials per task.
- Multi-source data licenses and domain balance need audit before reuse.

## Project Relevance

InternW0 connects `VisualFuture`, `ActionExpert`, `ContextCache`, `EmbodimentInterface`, `Force`, `Tactile`, and ordered task-progress fields.

## Reproduction / Follow-up

- Start with released delta checkpoints on LIBERO/RoboTwin.
- Verify data licenses and reproduce latency with the same inclusion/exclusion rules.

