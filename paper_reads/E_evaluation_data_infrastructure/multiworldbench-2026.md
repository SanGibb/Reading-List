# MultiWorldBench: Do Independently Controlled Views Describe One Shared World?

candidate_id: CAND-0012
branch: E
decision: accepted_for_registry

## Source Links

- Paper: https://arxiv.org/abs/2610.11723
- Project / figures / demos: https://arxiv.org/abs/2610.11723

## TL;DR

Separates plausible single views from persistent multi-client world consistency with capability-level diagnostics. Essential evaluation layer for SharedState, Persistence, ConcurrentInteraction, CrossViewMotion, DelayedRevisit, and StructuralConsistency. Central results are author-reported and were not independently reproduced in this collection run.

## Novelty

- What is new: Separates plausible single views from persistent multi-client world consistency with capability-level diagnostics.
- Why it matters: Essential evaluation layer for SharedState, Persistence, ConcurrentInteraction, CrossViewMotion, DelayedRevisit, and StructuralConsistency.
- Branch fit: the work directly contributes to branch E rather than serving only as background.

## Contributions

1. Diagnostic automatic and human evaluation of control, cross-view motion, shared state, persistence, concurrency, delayed revisit, and structure.
2. 495 Minecraft case configurations across seven suites and ten multiplayer world-consistency capabilities.
3. Generated systems score at most 8.00 on persistence and 1.33 on structural consistency versus 91.69 overall for engine ground truth.

## Task

- Input / setting: official source-specific observations, task context, state, geometry, and/or actions.
- Output: Measure whether independently controlled generated views remain one coherent shared world.
- Success criterion: the paper's official task metrics and matched evaluation protocol.

## Data

- Dataset / benchmark: 495 Minecraft case configurations across seven suites and ten multiplayer world-consistency capabilities.
- Modalities and splits: use the official paper's definitions; synthetic, simulated, and real components should not be conflated.
- Provenance: scale and collection claims are traced to the primary paper/project below.

## Method

- Core pipeline: Diagnostic automatic and human evaluation of control, cross-view motion, shared state, persistence, concurrency, delayed revisit, and structure.
- Representation and optimization: retain the source's units, coordinate frames, action conventions, and success definitions when reproducing.
- Deployment target: Measure whether independently controlled generated views remain one coherent shared world.

## Key Figures / Architecture

figure_status: linked_official

- Official source: https://arxiv.org/abs/2610.11723
- What was inspected: method overview, qualitative panels, benchmark/task examples, and available demo media.
- Visual decision: not_applicable (0/5). This is primarily an evaluation/data contribution; visual generation quality is not an acceptance gate.

## Evidence Trail

| Claim | Source | Status | Notes |
|---|---|---|---|
| Method and data | https://arxiv.org/abs/2610.11723 | verified | Primary paper surface checked. |
| Main reported result | https://arxiv.org/abs/2610.11723 | verified | Author-reported; not independently reproduced. |
| Project/code/demo availability | https://arxiv.org/abs/2610.11723 | verified | Official surface checked on 2026-10-12. |

## Evidence

- Main result: Generated systems score at most 8.00 on persistence and 1.33 on structural consistency versus 91.69 overall for engine ground truth.
- Demo score: 2/5; evidence strength: 4/5.
- Qualitative evidence: This is primarily an evaluation/data contribution; visual generation quality is not an acceptance gate.
- Comparisons remain protocol-dependent and should be cited as reported by the authors.

## Limitations

- Scope is bounded by the reported tasks, environments, embodiments, sensors, and action conventions.
- Curated demos do not expose the full long-tail failure distribution.
- Headline results were not independently reproduced during this literature-maintenance run.

## Project Relevance

- Essential evaluation layer for SharedState, Persistence, ConcurrentInteraction, CrossViewMotion, DelayedRevisit, and StructuralConsistency.
- Reusable fields should preserve source-specific units, coordinate frames, time bases, and simulator/hardware assumptions.
- Suitable as a related-work anchor and a candidate baseline or validator for branch E.

## Reproduction / Follow-up

- Verify licenses, exact data splits, hardware requirements, metric definitions, and checkpoint completeness before reproduction.
- Code/checkpoints: See the official paper/project; no separate fully verified repository was recorded in this run.
- Cite all metrics as source-reported until independently reproduced.
