# PAIWorld: A 3D-Consistent World Foundation Model for Robotic Manipulation

candidate_id: CAND-0005
branch: D
decision: accepted_for_registry

## Source Links

- Paper: https://arxiv.org/abs/2606.18375
- Project / demos: https://guhuangai.github.io/PAIWorld-Proj/
- Leaderboard: https://world-arena.ai/

## TL;DR

PAIWorld adds explicit cross-view communication and geometric supervision to a video DiT so multi-camera robot futures agree in 3D. The official multi-view and depth demos are convincing and the model is directly useful for planning and policy post-training, but geometry consistency alone does not solve contact physics.

## Novelty

- Geometry-Aware Cross-View Attention provides an explicit inter-view pathway.
- Geo-RoPE encodes pixel rays and camera poses in a shared 3D frame.
- Latent 3D-REPA distills spatial/temporal feature relations from a frozen 3D model.

## Contributions

1. Diagnoses object drift, depth contradiction and texture mismatch in flat multi-view tokenization.
2. Combines architectural communication with a geometric learning signal.
3. Demonstrates prediction, planning, world-action modeling and policy post-training uses.

## Task

- Input: synchronized camera views, text and robot actions.
- Output: geometrically consistent multi-view future videos.
- Setting: robotic manipulation across multiple data sources/embodiments.
- Success criterion: consistent geometry, controllability and downstream utility.

## Data

- Scale: 2.5M clips.
- Sources: Robocoin 15%, RobotWin 15%, RoboMind 20% and Galaxea 35%, with the remainder represented in the paper/project mixture.
- Modalities: synchronized RGB views, camera calibration/depth features, actions and language.
- Evaluation: WorldArena, AgiBot Challenge 2026 and multi-view generation metrics.

## Method

- Start from a flow-matching video DiT.
- Inject camera geometry through Geo-RoPE and gated cross-view attention.
- Align latent token relations with frozen 3D-aware features via sampled 3D-REPA.
- Condition on actions for future prediction and downstream rollout use.

## Key Figures / Architecture

figure_status: linked_official

- Figure / demo: overview, depth-aware multi-view rollouts and pipeline.
- Source: https://guhuangai.github.io/PAIWorld-Proj/static/images/paiworld/teaser.png
- What it shows: training mixture and prediction/planning/policy applications.
- Why it matters: cleanly separates multi-view geometry from policy consumers.

## Evidence Trail

| Claim | Source | Status | Notes |
|---|---|---|---|
| 2.5M clips | official project/paper | verified | Shown in overview. |
| WorldArena first / AgiBot second | official project | verified | Author-reported with leaderboard links. |
| Public code/checkpoint | official project | unverified | Not confirmed during this run. |

## Evidence

- Main metrics: reported top WorldArena score and strong AgiBot scene consistency.
- Qualitative results: cross-view videos and depth maps preserve placement/layout.
- Ablations: cross-view pathway and geometric prior are both necessary.
- Reproducibility signals: primary paper/project, but code/checkpoint status remains unclear.

## Limitations

- 3D consistency is not contact, deformation or fluid physics.
- Dataset composition and compute complicate independent reproduction.
- Release completeness must be verified.

## Project Relevance

- Direct baseline for multi-camera embodied world prediction.
- Reusable fields: CameraRay, CameraPose, CrossViewRelation, DepthConsistency and ActionCondition.
- Useful geometry validation before consuming imagined rollouts in a policy.

## Reproduction / Follow-up

- Check code/checkpoint publication and exact licenses.
- Reproduce geometry metrics and add contact-aware evaluations.

