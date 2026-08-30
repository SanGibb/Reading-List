# Gemini Robotics 2

candidate_id: CAND-0001
branch: D
decision: accepted_for_registry

## Source Links

- Paper / launch: https://deepmind.google/blog/gemini-robotics-2-brings-whole-body-intelligence-to-robots/
- Project: https://deepmind.google/models/gemini-robotics/
- ER 2 model card: https://deepmind.google/models/model-cards/gemini-robotics-er-2/
- Demo / video: official launch and capability pages above

## TL;DR

Gemini Robotics 2 is Google DeepMind's 2026 VLA family for whole-body humanoid control, fine dexterity, cross-embodiment transfer, on-device execution, and high-level multi-robot orchestration. The demos are unusually broad, but the closed weights, undisclosed training mixture, and curated evaluation surface limit reproducibility.

## Novelty

- Extends the Gemini Robotics line from arm-centric manipulation to whole-body humanoid control.
- Packages low-level VLA control, an on-device model, and ER 2 high-level embodied reasoning as one system family.
- Demonstrates task delegation and coordinated planning across multiple robots.

## Contributions

1. Whole-body control across locomotion and dexterous manipulation.
2. Cross-embodiment support across hands, grippers, bi-arms, and humanoids.
3. ER 2 planning that can hand off execution to a lower-level VLA.

## Task

- Input: interleaved language, images, video and audio for ER 2; robot observations and instructions for VLA control.
- Output: plans, tool/policy calls, and embodied motor behavior.
- Setting: local and cloud-assisted physical robots, including multi-robot tasks.
- Success criterion: correct, safe completion of instructed multi-stage tasks.

## Data

- Dataset / benchmark: undisclosed training mixture; official evaluations span whole-body control, dexterity, collaboration and embodied reasoning.
- Scale / collection: not disclosed.
- Evaluation protocol: official model cards and curated task demonstrations.

## Method

- Core pipeline: ER 2 reasons and orchestrates while lower-level Gemini Robotics 2 policies execute.
- Model / representation: Gemini-based multimodal reasoning plus VLA action generation.
- Deployment: cloud-scale and on-device variants.

## Key Figures / Architecture

figure_status: linked_official

- Figure / demo: whole-body, dexterity and multi-robot capability videos.
- Source: https://deepmind.google/models/gemini-robotics/
- What it shows: task decomposition, varied effectors, locomotion-plus-manipulation, and coordinated agents.
- Why it matters: makes the hierarchical reasoning/control boundary visible.

## Evidence Trail

| Claim | Source | Status | Notes |
|---|---|---|---|
| July 30, 2026 release and whole-body capability | Official launch | verified | Primary company source. |
| ER 2 inputs and 128k context | ER 2 model card | verified | Official model card. |
| Public weights/training data | Project page | unverified | No open release claimed. |

## Evidence

- Qualitative results: diverse official videos cover humanoid movement, hand/gripper dexterity, replanning and collaboration.
- Reproducibility signals: model cards and product access exist, but no public weights.
- Baselines / ablations: limited public detail relative to an academic paper.

## Limitations

- Closed weights and undisclosed training data.
- Curated demos do not expose failure distributions.
- Product/model-card evidence is less complete than a reproducible paper release.

## Project Relevance

- Reusable fields: HighLevelPlan, Embodiment, EndEffector, WholeBodyAction, PolicyHandoff, RobotTeam.
- Baseline role: frontier closed-system reference for hierarchical and collaborative robotics.
- Implication: evaluation should separate reasoning/orchestration from low-level execution.

## Reproduction / Follow-up

- Recheck trusted-tester/API availability and future technical reports.
- Do not cite training scale or open availability without a newer official source.

