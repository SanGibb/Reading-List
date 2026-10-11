# Never Look Back: Understanding Persistence in 3D Object Memory from Egocentric Videos

candidate_id: CAND-0004
branch: C
decision: accepted_for_registry

## Source Links

- Paper: https://arxiv.org/abs/2610.10538
- Project / figures / demos: https://ledger-3d.github.io/
- Code: https://github.com/LEDGER-3D/LEDGER

## TL;DR

Combines persistent 3D localization, object histories, and contextual descriptions while retaining untouched and out-of-view objects. Provides concrete PersistentObject, RestingLocation, MoveEvent, ContainerState, ObservationHistory, and retrieval fields. Central results are author-reported and were not independently reproduced in this collection run.

## Novelty

- What is new: Combines persistent 3D localization, object histories, and contextual descriptions while retaining untouched and out-of-view objects.
- Why it matters: Provides concrete PersistentObject, RestingLocation, MoveEvent, ContainerState, ObservationHistory, and retrieval fields.
- Branch fit: the work directly contributes to branch C rather than serving only as background.

## Contributions

1. Ledger associates object observations into persistent 3D records, clusters resting locations, confirms moves with repeated evidence, and stores contextual descriptions.
2. HD-EPIC, UCS-Bench, Ego4D, and 100 stitched multi-scene egocentric streams.
3. Ledger raises HD-EPIC accuracy from 29.7% to 42.6%, UCS-Bench from 33.8% to 38.5%, and reports 0.99 m median Ego4D localization error.

## Task

- Input / setting: official source-specific observations, task context, state, geometry, and/or actions.
- Output: Answer later spatial/object-state questions without replaying the original egocentric video.
- Success criterion: the paper's official task metrics and matched evaluation protocol.

## Data

- Dataset / benchmark: HD-EPIC, UCS-Bench, Ego4D, and 100 stitched multi-scene egocentric streams.
- Modalities and splits: use the official paper's definitions; synthetic, simulated, and real components should not be conflated.
- Provenance: scale and collection claims are traced to the primary paper/project below.

## Method

- Core pipeline: Ledger associates object observations into persistent 3D records, clusters resting locations, confirms moves with repeated evidence, and stores contextual descriptions.
- Representation and optimization: retain the source's units, coordinate frames, action conventions, and success definitions when reproducing.
- Deployment target: Answer later spatial/object-state questions without replaying the original egocentric video.

## Key Figures / Architecture

figure_status: linked_official

- Official source: https://ledger-3d.github.io/
- What was inspected: method overview, qualitative panels, benchmark/task examples, and available demo media.
- Visual decision: not_applicable (0/5). This is primarily an evaluation/data contribution; visual generation quality is not an acceptance gate.

## Evidence Trail

| Claim | Source | Status | Notes |
|---|---|---|---|
| Method and data | https://arxiv.org/abs/2610.10538 | verified | Primary paper surface checked. |
| Main reported result | https://arxiv.org/abs/2610.10538 | verified | Author-reported; not independently reproduced. |
| Project/code/demo availability | https://ledger-3d.github.io/ | verified | Official surface checked on 2026-10-12. |

## Evidence

- Main result: Ledger raises HD-EPIC accuracy from 29.7% to 42.6%, UCS-Bench from 33.8% to 38.5%, and reports 0.99 m median Ego4D localization error.
- Demo score: 4/5; evidence strength: 4/5.
- Qualitative evidence: This is primarily an evaluation/data contribution; visual generation quality is not an acceptance gate.
- Comparisons remain protocol-dependent and should be cited as reported by the authors.

## Limitations

- Scope is bounded by the reported tasks, environments, embodiments, sensors, and action conventions.
- Curated demos do not expose the full long-tail failure distribution.
- Headline results were not independently reproduced during this literature-maintenance run.

## Project Relevance

- Provides concrete PersistentObject, RestingLocation, MoveEvent, ContainerState, ObservationHistory, and retrieval fields.
- Reusable fields should preserve source-specific units, coordinate frames, time bases, and simulator/hardware assumptions.
- Suitable as a related-work anchor and a candidate baseline or validator for branch C.

## Reproduction / Follow-up

- Verify licenses, exact data splits, hardware requirements, metric definitions, and checkpoint completeness before reproduction.
- Code/checkpoints: https://github.com/LEDGER-3D/LEDGER
- Cite all metrics as source-reported until independently reproduced.
