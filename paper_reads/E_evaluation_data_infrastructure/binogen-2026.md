# BinoGen: Scaling egocentric binocular data for embodied visual perception and learning

candidate_id: CAND-0007
branch: E
decision: accepted_for_registry

## Source Links

- Paper: https://arxiv.org/abs/2609.19881

## TL;DR

BinoGen procedurally generates more than 20 million embodiment-aware binocular images with dense geometry and motion labels. Paired observer configurations make morphology a controlled variable, though the project/code release was not yet exposed.

## Novelty

- Joint control of environment and observer embodiment.
- Paired views support causal-style comparison of perceptual morphology.

## Contributions

1. Large binocular egocentric generator and dataset.
2. Depth, flow, normals, semantics, object coordinates, and poses.
3. Real-world transfer plus cross-embodiment studies.

## Task

- Input: procedural world, trajectory, binocular rig configuration.
- Output: synchronized images and dense multimodal labels.
- Success: downstream depth, detection, tracking, and embodiment adaptation.

## Data

More than 20 million annotated images with paired human- and mouse-inspired observations.

## Method

Scene synthesis, probabilistic object placement, appearance randomization, stochastic trajectories, and configurable binocular geometry.

## Key Figures / Architecture

figure_status: linked_official

- Paper figures and dataset examples: https://arxiv.org/html/2609.19881

## Evidence Trail

| Claim | Source | Status | Notes |
|---|---|---|---|
| More than 20M annotated images | https://arxiv.org/abs/2609.19881 | verified | Primary abstract. |
| Real-world perception gains | https://arxiv.org/abs/2609.19881 | verified | Author-reported. |
| Public generator/data |  | unverified | No official project/code surface found. |

## Evidence

- Reported improvements cover depth, detection, and video tracking.
- Same-world paired rigs isolate embodiment-specific effects.

## Limitations

- Availability and licenses need verification.
- Synthetic transfer may be sensitive to simulator/domain choices.

## Project Relevance

Provides `ObserverEmbodiment`, `BinocularRig`, `SensorTrajectory`, and dense geometry/motion supervision schemas.

## Reproduction / Follow-up

- Recheck for data/code release.
- Audit how scene/object distributions differ from target environments.
