# DreamTrue: Action-Faithful Robot World Model with Counterfactual Post-Training

candidate_id: CAND-0005
branch: D
decision: accepted_for_registry

## Source Links

- Paper: https://arxiv.org/abs/2610.12468
- Project / figures / demos: https://brave-eai.github.io/DreamTrue
- Code: https://github.com/brave-eai/DreamTrue

## TL;DR

Targets success bias in robot video data through counterfactual action post-training and explicit human-rated interaction defects. Strong reference for ActionTrajectory, Calibration, CounterfactualOutcome, InteractionDefect, and world-model reward interfaces. Central results are author-reported and were not independently reproduced in this collection run.

## Novelty

- What is new: Targets success bias in robot video data through counterfactual action post-training and explicit human-rated interaction defects.
- Why it matters: Strong reference for ActionTrajectory, Calibration, CounterfactualOutcome, InteractionDefect, and world-model reward interfaces.
- Branch fit: the work directly contributes to branch D rather than serving only as background.

## Contributions

1. Image-space action trajectories and offline calibration improve action alignment; counterfactual actions broaden failures; an embodied video reward model guides RL post-training.
2. Multi-view AgiBot and cross-embodiment robot video plus a human-annotated interaction-defect reward dataset.
3. The paper reports reducing human-assessed interaction defects from 48.12% to 6.25% and first place in the AgiBot World Challenge 2026 world-model track.

## Task

- Input / setting: official source-specific observations, task context, state, geometry, and/or actions.
- Output: Predict physically plausible, action-faithful multi-view robot futures across embodiments.
- Success criterion: the paper's official task metrics and matched evaluation protocol.

## Data

- Dataset / benchmark: Multi-view AgiBot and cross-embodiment robot video plus a human-annotated interaction-defect reward dataset.
- Modalities and splits: use the official paper's definitions; synthetic, simulated, and real components should not be conflated.
- Provenance: scale and collection claims are traced to the primary paper/project below.

## Method

- Core pipeline: Image-space action trajectories and offline calibration improve action alignment; counterfactual actions broaden failures; an embodied video reward model guides RL post-training.
- Representation and optimization: retain the source's units, coordinate frames, action conventions, and success definitions when reproducing.
- Deployment target: Predict physically plausible, action-faithful multi-view robot futures across embodiments.

## Key Figures / Architecture

figure_status: linked_official

- Official source: https://brave-eai.github.io/DreamTrue
- What was inspected: method overview, qualitative panels, benchmark/task examples, and available demo media.
- Visual decision: strong (4/5). Official project/paper qualitative panels and demo media were inspected; results were coherent and task-relevant.

## Evidence Trail

| Claim | Source | Status | Notes |
|---|---|---|---|
| Method and data | https://arxiv.org/abs/2610.12468 | verified | Primary paper surface checked. |
| Main reported result | https://arxiv.org/abs/2610.12468 | verified | Author-reported; not independently reproduced. |
| Project/code/demo availability | https://brave-eai.github.io/DreamTrue | verified | Official surface checked on 2026-10-12. |

## Evidence

- Main result: The paper reports reducing human-assessed interaction defects from 48.12% to 6.25% and first place in the AgiBot World Challenge 2026 world-model track.
- Demo score: 4/5; evidence strength: 4/5.
- Qualitative evidence: Official project/paper qualitative panels and demo media were inspected; results were coherent and task-relevant.
- Comparisons remain protocol-dependent and should be cited as reported by the authors.

## Limitations

- Scope is bounded by the reported tasks, environments, embodiments, sensors, and action conventions.
- Curated demos do not expose the full long-tail failure distribution.
- Headline results were not independently reproduced during this literature-maintenance run.

## Project Relevance

- Strong reference for ActionTrajectory, Calibration, CounterfactualOutcome, InteractionDefect, and world-model reward interfaces.
- Reusable fields should preserve source-specific units, coordinate frames, time bases, and simulator/hardware assumptions.
- Suitable as a related-work anchor and a candidate baseline or validator for branch D.

## Reproduction / Follow-up

- Verify licenses, exact data splits, hardware requirements, metric definitions, and checkpoint completeness before reproduction.
- Code/checkpoints: https://github.com/brave-eai/DreamTrue
- Cite all metrics as source-reported until independently reproduced.
