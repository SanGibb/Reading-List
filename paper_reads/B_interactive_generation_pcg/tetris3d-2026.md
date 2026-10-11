# Tetris3D: 3D Scene Generation With Objects That Fit Together

candidate_id: CAND-0003
branch: B
decision: accepted_for_registry

## Source Links

- Paper: https://arxiv.org/abs/2610.10539
- Project / figures / demos: https://cvlab-kaist.github.io/Tetris3D/

## TL;DR

Makes local inter-object fit an explicit generation condition rather than generating scene objects independently. Direct reference for ContactRelation, Support, FitConstraint, OccludedGeometry, PhysicalStability, and scene-assembly validators. Central results are author-reported and were not independently reproduced in this collection run.

## Novelty

- What is new: Makes local inter-object fit an explicit generation condition rather than generating scene objects independently.
- Why it matters: Direct reference for ContactRelation, Support, FitConstraint, OccludedGeometry, PhysicalStability, and scene-assembly validators.
- Branch fit: the work directly contributes to branch B rather than serving only as background.

## Contributions

1. Generates each scene object conditioned on surrounding geometry and physical relations so shape and pose remain compatible at occluded interaction regions.
2. ComOb, a physics-simulation dataset of 1.2M scenes with per-object meshes and pairwise physical-relation annotations.
3. The authors report state-of-the-art generation quality and physical stability on synthetic and real-world scene evaluations.

## Task

- Input / setting: official source-specific observations, task context, state, geometry, and/or actions.
- Output: Reconstruct physically and geometrically coherent object-level 3D scenes from a single image.
- Success criterion: the paper's official task metrics and matched evaluation protocol.

## Data

- Dataset / benchmark: ComOb, a physics-simulation dataset of 1.2M scenes with per-object meshes and pairwise physical-relation annotations.
- Modalities and splits: use the official paper's definitions; synthetic, simulated, and real components should not be conflated.
- Provenance: scale and collection claims are traced to the primary paper/project below.

## Method

- Core pipeline: Generates each scene object conditioned on surrounding geometry and physical relations so shape and pose remain compatible at occluded interaction regions.
- Representation and optimization: retain the source's units, coordinate frames, action conventions, and success definitions when reproducing.
- Deployment target: Reconstruct physically and geometrically coherent object-level 3D scenes from a single image.

## Key Figures / Architecture

figure_status: linked_official

- Official source: https://cvlab-kaist.github.io/Tetris3D/
- What was inspected: method overview, qualitative panels, benchmark/task examples, and available demo media.
- Visual decision: strong (4/5). Official project/paper qualitative panels and demo media were inspected; results were coherent and task-relevant.

## Evidence Trail

| Claim | Source | Status | Notes |
|---|---|---|---|
| Method and data | https://arxiv.org/abs/2610.10539 | verified | Primary paper surface checked. |
| Main reported result | https://arxiv.org/abs/2610.10539 | verified | Author-reported; not independently reproduced. |
| Project/code/demo availability | https://cvlab-kaist.github.io/Tetris3D/ | verified | Official surface checked on 2026-10-12. |

## Evidence

- Main result: The authors report state-of-the-art generation quality and physical stability on synthetic and real-world scene evaluations.
- Demo score: 3/5; evidence strength: 4/5.
- Qualitative evidence: Official project/paper qualitative panels and demo media were inspected; results were coherent and task-relevant.
- Comparisons remain protocol-dependent and should be cited as reported by the authors.

## Limitations

- Scope is bounded by the reported tasks, environments, embodiments, sensors, and action conventions.
- Curated demos do not expose the full long-tail failure distribution.
- Headline results were not independently reproduced during this literature-maintenance run.

## Project Relevance

- Direct reference for ContactRelation, Support, FitConstraint, OccludedGeometry, PhysicalStability, and scene-assembly validators.
- Reusable fields should preserve source-specific units, coordinate frames, time bases, and simulator/hardware assumptions.
- Suitable as a related-work anchor and a candidate baseline or validator for branch B.

## Reproduction / Follow-up

- Verify licenses, exact data splits, hardware requirements, metric definitions, and checkpoint completeness before reproduction.
- Code/checkpoints: See the official paper/project; no separate fully verified repository was recorded in this run.
- Cite all metrics as source-reported until independently reproduced.
