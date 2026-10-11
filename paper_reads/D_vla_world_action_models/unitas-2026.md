# UNITAS: A 3D-Native World Action Model for Embodied Manipulation

candidate_id: CAND-0007
branch: D
decision: accepted_for_registry

## Source Links

- Paper: https://arxiv.org/abs/2610.12099
- Project / figures / demos: https://unitas-wam.github.io/
- Code: https://github.com/DexForce/UNITAS

## TL;DR

Moves WAM representation from view-dependent pixels to a shared metric 3D motion interface. Direct reference for MetricFrame, ActionFlow, SceneFlow, PointTrajectory, PhysicalTime, and cross-embodiment action schemas. Central results are author-reported and were not independently reproduced in this collection run.

## Novelty

- What is new: Moves WAM representation from view-dependent pixels to a shared metric 3D motion interface.
- Why it matters: Direct reference for MetricFrame, ActionFlow, SceneFlow, PointTrajectory, PhysicalTime, and cross-embodiment action schemas.
- Branch fit: the work directly contributes to branch D rather than serving only as background.

## Contributions

1. Unifies visual observations, action flow, and scene flow in a metric 3D frame using point trajectories, scene displacements, and world-aligned embeddings.
2. RoboTwin, LIBERO, real-world tasks, and mixed human-hand/robot interaction data.
3. The paper reports up to 49% lower scene-displacement error than PointWorld, 99.8% LIBERO success, and 85% average real-world success.

## Task

- Input / setting: official source-specific observations, task context, state, geometry, and/or actions.
- Output: Jointly generate executable actions and action-conditioned 3D scene evolution across hands and robot embodiments.
- Success criterion: the paper's official task metrics and matched evaluation protocol.

## Data

- Dataset / benchmark: RoboTwin, LIBERO, real-world tasks, and mixed human-hand/robot interaction data.
- Modalities and splits: use the official paper's definitions; synthetic, simulated, and real components should not be conflated.
- Provenance: scale and collection claims are traced to the primary paper/project below.

## Method

- Core pipeline: Unifies visual observations, action flow, and scene flow in a metric 3D frame using point trajectories, scene displacements, and world-aligned embeddings.
- Representation and optimization: retain the source's units, coordinate frames, action conventions, and success definitions when reproducing.
- Deployment target: Jointly generate executable actions and action-conditioned 3D scene evolution across hands and robot embodiments.

## Key Figures / Architecture

figure_status: linked_official

- Official source: https://unitas-wam.github.io/
- What was inspected: method overview, qualitative panels, benchmark/task examples, and available demo media.
- Visual decision: strong (4/5). Official project/paper qualitative panels and demo media were inspected; results were coherent and task-relevant.

## Evidence Trail

| Claim | Source | Status | Notes |
|---|---|---|---|
| Method and data | https://arxiv.org/abs/2610.12099 | verified | Primary paper surface checked. |
| Main reported result | https://arxiv.org/abs/2610.12099 | verified | Author-reported; not independently reproduced. |
| Project/code/demo availability | https://unitas-wam.github.io/ | verified | Official surface checked on 2026-10-12. |

## Evidence

- Main result: The paper reports up to 49% lower scene-displacement error than PointWorld, 99.8% LIBERO success, and 85% average real-world success.
- Demo score: 3/5; evidence strength: 4/5.
- Qualitative evidence: Official project/paper qualitative panels and demo media were inspected; results were coherent and task-relevant.
- Comparisons remain protocol-dependent and should be cited as reported by the authors.

## Limitations

- Scope is bounded by the reported tasks, environments, embodiments, sensors, and action conventions.
- Curated demos do not expose the full long-tail failure distribution.
- Headline results were not independently reproduced during this literature-maintenance run.

## Project Relevance

- Direct reference for MetricFrame, ActionFlow, SceneFlow, PointTrajectory, PhysicalTime, and cross-embodiment action schemas.
- Reusable fields should preserve source-specific units, coordinate frames, time bases, and simulator/hardware assumptions.
- Suitable as a related-work anchor and a candidate baseline or validator for branch D.

## Reproduction / Follow-up

- Verify licenses, exact data splits, hardware requirements, metric definitions, and checkpoint completeness before reproduction.
- Code/checkpoints: https://github.com/DexForce/UNITAS
- Cite all metrics as source-reported until independently reproduced.
