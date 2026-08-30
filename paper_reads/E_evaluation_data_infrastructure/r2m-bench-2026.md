# R2M-Bench: Evaluating Revisit Memory via Relative Consistency in Interactive Video World Models

candidate_id: CAND-0005
branch: E
decision: accepted_for_registry

## Source Links

- Paper: https://arxiv.org/abs/2608.27328
- Project / code: not located at review time

## TL;DR

R2M-Bench measures whether an interactive video world model remembers a place after leaving and returning, while controlling for generic temporal stability and failed motion. Its relative metrics directly address a common shortcut, although the benchmark is modest and currently lacks a separate public project/code surface.

## Novelty

- Compares revisit pairs against gap-matched non-revisit controls from the same rollout.
- Adds a short-range control to normalize the usable consistency range.
- Reduces sensitivity to static/slow rollouts that inflate absolute similarity.

## Contributions

1. MemoryGain and Normalized Memory Ratio metrics.
2. A 300-instance leave-and-return benchmark.
3. Human-correlation and motion-shortcut analysis across seven models.

## Task

- Input: interactive generated rollout containing a departure and return.
- Output: relative consistency scores for appearance, identity, geometry and persistent state.
- Success criterion: revisit-specific consistency beyond temporal baselines.

## Data

- Scale: 100 scenes × three trajectories = 300 instances.
- Criteria: appearance fidelity, scene/object identity, local geometry and persistent state.
- Evaluation: seven action-conditioned video world models and human judgments.

## Method

- Extract revisit, gap-matched non-revisit, and short-range pairs.
- Compute MemoryGain against generic temporal stability.
- Normalize with the short-to-baseline dynamic range to obtain NMR.

## Key Figures / Architecture

figure_status: linked_official

- Figure / demo: protocol and correlation figures in the official arXiv paper.
- Source: https://arxiv.org/abs/2608.27328
- What it shows: matched controls and the slow-motion shortcut.
- Why it matters: prevents static video from masquerading as memory.

## Evidence Trail

| Claim | Source | Status | Notes |
|---|---|---|---|
| 300 instances from 100 scenes | Paper | verified | Primary source. |
| Seven models evaluated | Paper | verified | Author-reported. |
| NMR-human Spearman rho 0.547 | Paper | verified | 95% CI reported. |

## Evidence

- Overall NMR correlates with human consistency judgments at reported rho 0.547.
- Reported motion correlation magnitude is lower for NMR than raw revisit similarity.
- DreamX-World-Memo is the top evaluated model by Overall NMR.

## Limitations

- No separate code/project release located.
- Moderate scale and controlled trajectories.
- Revisit memory is only one dimension of interactive-world quality.

## Project Relevance

- Reusable fields: VisitId, RevisitPair, GapControl, ShortRangeControl, MemoryGain, NormalizedMemoryRatio.
- Baseline role: targeted persistent-state diagnostic.
- Implication: every memory metric needs an explicit motion/stability control.

## Reproduction / Follow-up

- Recheck code release and exact pair-mining implementation.
- Validate metric sensitivity to camera-path and rendering changes.

