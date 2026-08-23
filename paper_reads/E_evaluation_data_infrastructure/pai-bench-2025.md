# PAI-Bench: A Comprehensive Benchmark For Physical AI

candidate_id: CAND-0006
branch: E
decision: accepted_for_registry

## Source Links

- Paper: https://arxiv.org/abs/2512.01989
- Code / data / leaderboard: https://github.com/SHI-Labs/physical-ai-bench

## TL;DR

PAI-Bench provides a public, cross-domain suite for physical video generation, condition-controlled generation and video understanding. Its 2,808 real-world cases create a useful common evaluation layer, though robotics-specific diagnosis should use per-domain rather than aggregate scores.

## Novelty

- Unifies generation, conditional generation and understanding.
- Covers driving, robotics, smart-space and egocentric domains.
- Supplies separate datasets and a public leaderboard for each task family.

## Contributions

1. Releases 2,808 real-world evaluation cases.
2. Defines PAI-Bench-G, PAI-Bench-C and PAI-Bench-U.
3. Provides code, datasets, leaderboard and broad model comparisons.

## Task

- Input: physical-scene video/image context and task-specific controls/questions.
- Output: predicted video or understanding answer.
- Setting: cross-domain Physical AI.
- Success criterion: physically plausible, control-aligned predictions and correct understanding.

## Data

- Scale: 2,808 real-world cases.
- Domains: autonomous driving, robotics, smart spaces and egocentric everyday scenes.
- Modalities: video, image/control maps and text.
- Splits: separate Hugging Face datasets for G/C/U tasks with official leaderboard.

## Method

- Generation evaluates future-state prediction.
- Conditional generation adds edges, segmentation or depth controls.
- Understanding evaluates physical-scene interpretation.
- Task-aligned metrics measure plausibility and domain reasoning.

## Key Figures / Architecture

figure_status: linked_official

- Figure / demo: repository overview and dataset links.
- Source: https://github.com/SHI-Labs/physical-ai-bench
- What it shows: three-task benchmark structure.
- Why it matters: provides a compact evaluation map across model capabilities.

## Evidence Trail

| Claim | Source | Status | Notes |
|---|---|---|---|
| 2,808 cases | arXiv paper | verified | Stated in abstract. |
| CVPR 2026 Oral | official repository | verified | Dated acceptance news. |
| Three public datasets and leaderboard | official repository | verified | Links resolve. |

## Evidence

- Metrics: task-aligned generation and understanding scores.
- Baselines: proprietary and open video/VLM systems.
- Reproducibility: MIT-licensed repository, datasets and leaderboard.

## Limitations

- Aggregate breadth may hide robotics-specific weaknesses.
- Automated video metrics imperfectly capture causality and execution.
- Benchmark success does not by itself imply closed-loop competence.

## Project Relevance

- Reusable task split for world generation, controlled transformation and understanding.
- Baseline role: umbrella scorecard across physical-AI model classes.
- Pair with action/closed-loop benchmarks for embodied claims.

## Reproduction / Follow-up

- Pin dataset and leaderboard versions.
- Report robotics-domain slices and metric uncertainty separately.

