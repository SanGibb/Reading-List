# OpenViTac: Learning and Benchmarking Visuo-Tactile Policies in a Unified Sim-and-Real Framework

candidate_id: CAND-0013
branch: E
decision: accepted_for_registry

## Source Links

- Paper: https://arxiv.org/abs/2610.10384
- Project / figures / demos: https://fvl-repo.github.io/OpenViTac/

## TL;DR

Provides aligned sim-real tactile tasks and controlled comparisons of tactile representations, fusion, and co-training. Direct source for TactileHistory, PhysicalProperty, SensorType, SimRealPair, ContactTask, and cross-domain evaluation. Central results are author-reported and were not independently reproduced in this collection run.

## Novelty

- What is new: Provides aligned sim-real tactile tasks and controlled comparisons of tactile representations, fusion, and co-training.
- Why it matters: Direct source for TactileHistory, PhysicalProperty, SensorType, SimRealPair, ContactTask, and cross-domain evaluation.
- Branch fit: the work directly contributes to branch E rather than serving only as background.

## Contributions

1. A paired sim-real benchmark plus OpenVTLA, which prepends temporally encoded tactile tokens to a pretrained VLA visual sequence.
2. 11 simulation tasks, eight paired real tasks, four tactile capabilities, and three tactile-sensor types.
3. The official page reports 68.7% simulated and 54.6% real success, 0.913 sim-real correlation, and +15 points from sim co-training on two tasks.

## Task

- Input / setting: official source-specific observations, task context, state, geometry, and/or actions.
- Output: Evaluate and train VLA, WAM, and VTLA policies on contact-rich manipulation in simulation and reality.
- Success criterion: the paper's official task metrics and matched evaluation protocol.

## Data

- Dataset / benchmark: 11 simulation tasks, eight paired real tasks, four tactile capabilities, and three tactile-sensor types.
- Modalities and splits: use the official paper's definitions; synthetic, simulated, and real components should not be conflated.
- Provenance: scale and collection claims are traced to the primary paper/project below.

## Method

- Core pipeline: A paired sim-real benchmark plus OpenVTLA, which prepends temporally encoded tactile tokens to a pretrained VLA visual sequence.
- Representation and optimization: retain the source's units, coordinate frames, action conventions, and success definitions when reproducing.
- Deployment target: Evaluate and train VLA, WAM, and VTLA policies on contact-rich manipulation in simulation and reality.

## Key Figures / Architecture

figure_status: linked_official

- Official source: https://fvl-repo.github.io/OpenViTac/
- What was inspected: method overview, qualitative panels, benchmark/task examples, and available demo media.
- Visual decision: not_applicable (0/5). This is primarily an evaluation/data contribution; visual generation quality is not an acceptance gate.

## Evidence Trail

| Claim | Source | Status | Notes |
|---|---|---|---|
| Method and data | https://arxiv.org/abs/2610.10384 | verified | Primary paper surface checked. |
| Main reported result | https://arxiv.org/abs/2610.10384 | verified | Author-reported; not independently reproduced. |
| Project/code/demo availability | https://fvl-repo.github.io/OpenViTac/ | verified | Official surface checked on 2026-10-12. |

## Evidence

- Main result: The official page reports 68.7% simulated and 54.6% real success, 0.913 sim-real correlation, and +15 points from sim co-training on two tasks.
- Demo score: 3/5; evidence strength: 4/5.
- Qualitative evidence: This is primarily an evaluation/data contribution; visual generation quality is not an acceptance gate.
- Comparisons remain protocol-dependent and should be cited as reported by the authors.

## Limitations

- Scope is bounded by the reported tasks, environments, embodiments, sensors, and action conventions.
- Curated demos do not expose the full long-tail failure distribution.
- Headline results were not independently reproduced during this literature-maintenance run.

## Project Relevance

- Direct source for TactileHistory, PhysicalProperty, SensorType, SimRealPair, ContactTask, and cross-domain evaluation.
- Reusable fields should preserve source-specific units, coordinate frames, time bases, and simulator/hardware assumptions.
- Suitable as a related-work anchor and a candidate baseline or validator for branch E.

## Reproduction / Follow-up

- Verify licenses, exact data splits, hardware requirements, metric definitions, and checkpoint completeness before reproduction.
- Code/checkpoints: See the official paper/project; no separate fully verified repository was recorded in this run.
- Cite all metrics as source-reported until independently reproduced.
