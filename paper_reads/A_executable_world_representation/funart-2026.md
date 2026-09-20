# FunArt: Decoding Functional Structure and Articulation from Generative 3D Latents

candidate_id: CAND-0004
branch: A
decision: accepted_for_registry

## Source Links

- Paper: https://arxiv.org/abs/2609.20673

## TL;DR

FunArt converts static posed RGB-D observations into functional, articulation-aware 3D scene graphs by decoding frozen TRELLIS.2 geometry latents. It unifies movable parts, interaction elements, and joint parameters, though code and downstream manipulation validation are absent.

## Novelty

- Uses a frozen generative 3D latent as an actionable structural prior.
- Jointly predicts functional elements and articulation rather than decoupling them.

## Contributions

1. End-to-end functional 3D graph construction.
2. Joint part/function/kinematic decoder.
3. State-of-the-art Articulate3D results reported across all three outputs.

## Task

- Input: posed RGB-D views of a static scene.
- Output: objects, movable parts, functional elements, motion type, axis, origin, and range.
- Success: detection/segmentation and joint-constrained AP.

## Data

Articulate3D, with ground-truth-object and end-to-end protocols.

## Method

Fused object geometry is converted into TRELLIS.2 O-Voxel features; a lightweight query decoder combines compact object latents with dense surface-aligned features.

## Key Figures / Architecture

figure_status: linked_official

- Paper HTML figures: https://arxiv.org/html/2609.20673
- The pipeline figure shows RGB-D fusion, frozen generative encoding, and the joint functional/articulation heads.

## Evidence Trail

| Claim | Source | Status | Notes |
|---|---|---|---|
| Joint functional/articulation output | https://arxiv.org/abs/2609.20673 | verified | Primary abstract/method. |
| +1.5/+2.8/+6.7 AP50 gains | https://arxiv.org/abs/2609.20673 | verified | Author-reported end-to-end comparisons. |

## Evidence

- Reported gains cover movable parts, constrained joint estimation, and functional elements.
- Both ground-truth-object and end-to-end settings are evaluated.

## Limitations

- No official project, code, or checkpoint found.
- No closed-loop manipulation evaluation.

## Project Relevance

Strong schema reference for functional elements and executable kinematics before interaction.

## Reproduction / Follow-up

- Recheck code availability.
- Validate graph outputs in a simulator or planner before using operationally.
