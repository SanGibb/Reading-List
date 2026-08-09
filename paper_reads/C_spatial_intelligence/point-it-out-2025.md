# Point-It-Out: Benchmarking Embodied Reasoning for Vision Language Models in Multi-Stage Visual Grounding

candidate_id: CAND-0003
branch: C
decision: accepted_for_registry

## Source Links

- Paper: https://arxiv.org/abs/2509.25794
- Project: https://research.nvidia.com/labs/cosmos-lab/pio/
- Data / benchmark: https://huggingface.co/datasets/pio-benchmark/PIO
- Demo / official figures: https://research.nvidia.com/labs/cosmos-lab/pio/
- TMLR: https://openreview.net/forum?id=9e0hRhFsal

## TL;DR

Point-It-Out (PIO), published in TMLR in May 2026, evaluates embodied reasoning through pixel-level outputs rather than multiple-choice answers. Its stages progress from object localization to task-driven pointing and visual trace prediction across household, kitchen, driving, and manipulation scenes, bridging spatial understanding and action geometry.

## Novelty

- Hierarchical evaluation through boxes, points, and trajectories.
- Replaces indirect multiple choice with precise spatial grounding.
- Attributes failures to localization, affordance/contact grounding, or trace planning.

## Contributions

1. Defines S1 localization, S2 task-driven pointing, and S3 trace prediction.
2. Covers four domains with 600+ human-annotated QA instances.
3. Releases data and evaluates 10+ VLMs with fine-grained scoring.

## Task

- Input: embodied image and natural-language question.
- Output: box, point, or 2D trajectory.
- Setting: household, kitchen, driving, and manipulation.
- Success criterion: stage-specific spatial agreement.

## Data

- Dataset / benchmark: PIO.
- Scale: 600+ human-annotated QA pairs.
- Modalities: RGB, questions, boxes, points, traces.
- Collection / annotation: human annotation across four scenario families.
- Splits / evaluation protocol: three hierarchical stages.

## Method

- Core pipeline: prompt VLMs for structured spatial outputs and score each stage.
- Model / representation: model-agnostic pixel coordinates/traces.
- Training or optimization: benchmark only.
- Inference / deployment: direct VLM output.
- Losses or metrics: localization and point/trace agreement.

## Key Figures / Architecture

figure_status: linked_official

- Figure / demo: teaser contrasting multiple choice with box/point/trace evaluation.
- Source: https://research.nvidia.com/labs/cosmos-lab/pio/
- What it shows: three stages and four scenario types.
- Why it matters: makes the diagnostic hierarchy explicit.

## Evidence Trail

| Claim | Source | Status | Notes |
|---|---|---|---|
| Three-stage pixel-level benchmark | https://arxiv.org/abs/2509.25794 | verified | Paper and TMLR agree. |
| 600+ QA across four scenarios | https://openreview.net/forum?id=9e0hRhFsal | verified | Paper description. |
| Public dataset | https://huggingface.co/datasets/pio-benchmark/PIO | verified | Official dataset. |

## Evidence

- Main metrics: stage scores for more than ten VLMs.
- Qualitative results: project page shows point, box, and trajectory examples.
- Ablations: analysis separates grounding and trace-planning failure.
- Baselines: proprietary and open VLM families.
- Reproducibility signals: TMLR paper and public dataset.

## Limitations

- 2D traces omit depth, force, and kinematics.
- 600+ examples are diagnostic but modest.
- Static examples do not prove closed-loop execution; standalone evaluation code is unclear.

## Project Relevance

- Tests spatial affordance and trajectory grounding directly.
- Reusable fields: GroundingStage, TargetBox, ActionPoint, VisualTrace.
- Baseline role: pre-execution spatial-to-action diagnostic.
- Add pixel-level traces alongside language-only spatial QA.

## Reproduction / Follow-up

- Check coordinate normalization, judge tolerance, and licensing.
- Dataset is public; standalone code was not verified.
- TMLR publication is 2026 although the arXiv id is 2025.
