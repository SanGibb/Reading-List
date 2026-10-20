# PointCast: One World Model for Rigid, Articulated, and Deformable Object Manipulation

<!-- curation-review:start -->
> 2026-10-20 按新版标准复审：**待视觉复核**。Identity-preserving point trajectories across topology regimes are a concrete dynamics/control interface. Need actual rollout/MPC inspection and full matched results before current recommendation.
> [本次来源、分数与任务判断](../library_review.md#paper-4aea6bb26c10)。下文保留原精读；旧验收标签不代表本次重新通过，所有实验仍为作者报告。
<!-- curation-review:end -->

candidate_id: CAND-0001
branch: A
decision: accepted_for_registry

## Source Links

- Paper: https://arxiv.org/abs/2609.28393
- Project / demo: https://pointcast-wm.github.io

## TL;DR

PointCast predicts identity-preserving 3D point trajectories under end-effector motion, using one mesh-free representation and training recipe across rigid objects, cabinets, cloth, and rope. Its strongest value is an executable, topology-agnostic state interface; the main caveat is that each regime still uses a separate checkpoint.

## Novelty

- One point-set state and diffusion architecture spans rigid, articulated, and deformable dynamics.
- Per-point trajectory supervision preserves correspondences instead of only matching aggregate shape.
- The learned model is inserted unchanged into sampling-based MPC.

## Contributions

1. A 19.8M diffusion transformer alternating local/global attention with end-effector cross-attention.
2. Matched evaluation on simulation, real teleoperation data, zero-shot captures, and MPC.
3. An object-state abstraction that avoids meshes and fixed topology.

## Task

- Input: recent object/end-effector point histories and commanded end-effector motion.
- Output: a short window of future point positions.
- Setting: rigid, cloth, rope, and articulated cabinet manipulation.
- Success criterion: low point-trajectory error and successful MPC completion.

## Data

- Randomized simulation for four object regimes and a real robot teleoperation dataset.
- Separate checkpoints are trained per regime; simulation checkpoints are also tested zero-shot on captures.

## Method

- Identity-tagged object and end-effector points form the state.
- A diffusion transformer denoises future point windows with local/global attention.
- End-effector motion conditions predictions; sampling-based MPC scores candidate actions.

## Key Figures / Architecture

figure_status: linked_official

- Figure / demo: architecture, predicted point motion, and MPC rollouts.
- Source: https://pointcast-wm.github.io
- What it shows: coherent trajectories and manipulation across four topology regimes.
- Why it matters: verifies that the representation is executable, not merely reconstructive.

## Evidence Trail

| Claim | Source | Status | Notes |
|---|---|---|---|
| Best on three of four simulated regimes | https://arxiv.org/abs/2609.28393 | verified | Author-reported matched comparison. |
| Lowest mean real-data error in four of six categories | https://arxiv.org/abs/2609.28393 | verified | Primary report. |
| Public qualitative rollouts | https://pointcast-wm.github.io | verified | Official media inspected. |

## Evidence

- MPC covers four simulated tasks and 64 episodes.
- The model improves on the real dataset's native model in all six reported categories.
- Zero-shot simulation checkpoints lead on two of four captured cases.

## Limitations

- Separate regime-specific checkpoints weaken the “one model” framing.
- MPC evidence is primarily simulated and object-centric.
- Public code/checkpoint availability was not confirmed.

## Project Relevance

PointCast supplies reusable `PointIdentity`, `ObjectState`, `EndEffectorMotion`, `PredictedTrajectory`, and `TopologyRegime` fields for executable worlds and planning.

## Reproduction / Follow-up

- Verify exact point sampling, normalization, and MPC cost before reuse.
- Test a shared multi-regime checkpoint and cluttered-scene transfer.

