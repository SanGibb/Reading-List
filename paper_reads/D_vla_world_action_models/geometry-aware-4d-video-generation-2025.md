# Geometry-aware 4D Video Generation for Robot Manipulation

candidate_id: CAND-0004
branch: D
decision: accepted_for_registry

## Source Links

- Paper: https://arxiv.org/abs/2507.01099
- Project: https://robot4dgen.github.io/
- Code: https://github.com/lzylucy/4dgen
- Data / benchmark: https://real.stanford.edu/4dgen/
- Demo / official figures: https://robot4dgen.github.io/

## TL;DR

This ICLR 2026 paper generates synchronized multi-view RGB-D futures from initial RGB-D observations, then extracts 6-DoF end-effector trajectories with an off-the-shelf tracker. Cross-view pointmap supervision makes the videos geometrically aligned enough to drive manipulation in simulation and selected real settings.

## Novelty

- Joint temporal and cross-view geometric consistency for robot video generation.
- Predicts pointmaps/RGB-D across views rather than single-view RGB.
- Enables metric 3D trajectory recovery from generated futures.

## Contributions

1. Adds cross-attention and pointmap supervision to video diffusion.
2. Publishes multi-view RGB-D data, code, and checkpoints.
3. Demonstrates execution on occlusion-heavy, narrow-object, and bimanual tasks.

## Task

- Input: initial RGB-D from two views and manipulation context.
- Output: aligned future RGB-D and recovered 6-DoF trajectory.
- Setting: simulation plus sim-finetuned physical transfer.
- Success criterion: video/depth quality, pose accuracy, task success.

## Data

- Dataset / benchmark: multi-view RGB-D manipulation sequences and real examples.
- Scale: multiple tasks/views; exact counts are in the dataset card.
- Modalities: RGB, depth, pointmaps, poses, task labels.
- Collection / annotation: simulation rollouts and physical capture.
- Splits / evaluation protocol: unseen views and downstream rollouts.

## Method

- Core pipeline: dual-view conditioning, RGB/pointmap prediction, pose tracking.
- Model / representation: diffusion U-Net with geometric pointmaps.
- Training or optimization: video plus cross-view pointmap supervision.
- Inference / deployment: generate rollout, track gripper, execute trajectory.
- Losses or metrics: RGB/depth, geometric consistency, pose, success.

## Key Figures / Architecture

figure_status: linked_official

- Figure / demo: method diagram and RGB/depth/rollout galleries for three simulation tasks and real transfer.
- Source: https://robot4dgen.github.io/
- What it shows: unseen-view futures and baseline policy outcomes.
- Why it matters: directly supports the world-to-action claim.

## Evidence Trail

| Claim | Source | Status | Notes |
|---|---|---|---|
| Multi-view RGB-D with pointmap consistency | https://arxiv.org/abs/2507.01099 | verified | Central method. |
| Public code/data/checkpoints | https://robot4dgen.github.io/ | verified | Links live. |
| Generated rollouts support manipulation | https://robot4dgen.github.io/ | verified | Demonstrated, not reproduced. |

## Evidence

- Main metrics: improved video, depth, pose, and manipulation results are reported.
- Qualitative results: paired RGB/depth galleries and physical examples.
- Ablations: removes cross-attention and compares SVD variants.
- Baselines: SVD, 3D Diffusion Policy, Multi-View Diffusion Policy.
- Reproducibility signals: ICLR paper, code, data, checkpoints, official videos.

## Limitations

- Requires synchronized calibrated RGB-D views and tracking.
- Physical task/robot diversity is limited.
- Curated compressed videos make some depth artifacts hard to judge; results were not reproduced.

## Project Relevance

- Converts generated futures into metric actions.
- Reusable fields: CameraView, DepthFrame, PointMap, Correspondence, EndEffectorPose.
- Baseline role: geometry-aware video world-action model.
- Require cross-view geometry and action recovery, not RGB fidelity alone.

## Reproduction / Follow-up

- Check calibration, tracker sensitivity, and failure frequency.
- Code, dataset, and checkpoints are public.
- Cite arXiv 2025 and ICLR 2026 consistently.
