# Can 4D Foundation Models Remember? (PersistBench)

candidate_id: CAND-0001
branch: E
decision: accepted_for_registry

## Source Links

- Paper: https://arxiv.org/abs/2609.20819
- Project / benchmark / code / data: https://guangzhaohe.com/persistbench

## TL;DR

PersistBench uses 360-degree video as an omniscient reference to test whether 4D foundation models preserve objects after they leave view. It measures permanence, motion continuity, and appearance rather than rewarding local pixel consistency.

## Novelty

- Reference-backed evaluation of off-screen object memory.
- Separates three failure modes that aggregate video metrics hide.

## Contributions

1. Dataset with panoramic ground truth.
2. Object-centric metric suite.
3. Cross-family evaluation showing short-lived memory.

## Task

- Input: model rollout/reconstruction plus panoramic reference.
- Output: permanence, motion-continuity, and appearance-preservation scores.
- Success: correct state after occlusion or camera departure.

## Data

360-degree videos paired with camera views and object/reference annotations; exact counts should be cited from the released paper rather than inferred from gallery samples.

## Method

Object-centric matching and reference comparison score what happens while the object is outside the model's visible context.

## Key Figures / Architecture

figure_status: linked_official

- Teaser, panorama/input/reference construction, and comparisons: https://guangzhaohe.com/persistbench

## Evidence Trail

| Claim | Source | Status | Notes |
|---|---|---|---|
| 360-degree omniscient ground truth | https://arxiv.org/abs/2609.20819 | verified | Primary paper. |
| Three memory dimensions | https://guangzhaohe.com/persistbench | verified | Official benchmark page. |
| Code/data available | https://guangzhaohe.com/persistbench | verified | Official release links. |

## Evidence

- Official examples make off-screen disappearance, identity drift, and motion discontinuity visible.
- Evaluated model families degrade substantially once objects leave view.

## Limitations

- Depends on reliable object/reference association.
- Scenario diversity is bounded by panoramic capture.

## Project Relevance

Direct evaluator for persistent state, revisit consistency, identity retention, and off-screen world memory.

## Reproduction / Follow-up

- Compare with R2M-Bench's same-rollout calibration.
- Check whether static/slow-motion shortcuts influence reported memory.
