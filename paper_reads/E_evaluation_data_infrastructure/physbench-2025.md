# PhysBench: Benchmarking and Enhancing Vision-Language Models for Physical World Understanding

candidate_id: CAND-0007
branch: E
decision: accepted_for_registry

## Source Links

- Paper: https://arxiv.org/abs/2501.16411
- OpenReview: https://openreview.net/forum?id=Q6a9W6kzv5
- Project / data: https://physbench.github.io/
- Code: https://github.com/USC-GVL/PhysBench

## TL;DR

PhysBench measures physical properties, relations, scenes and dynamics with 10,002 interleaved image/video/text questions and 75-model evaluation. It is a strong prerequisite test for embodied reasoning, though its multiple-choice interface remains upstream of actual intervention and action success.

## Novelty

- Broad physical-world VLM benchmark across 19 subclasses.
- Large model study shows weak and inconsistent scaling with model/data/frame counts.
- PhysAgent tests whether specialist vision tools can close physical perception gaps.

## Contributions

1. Releases 10,002 benchmark entries and public evaluation code/data.
2. Evaluates 75 representative VLMs and diagnoses error sources.
3. Demonstrates physical-knowledge transfer and a tool-augmented baseline.

## Task

- Input: interleaved image/video/text physical-world questions.
- Output: multiple-choice answers and category scores.
- Setting: perception and reasoning about properties, relations, scenes and dynamics.
- Success criterion: accurate, stable physical understanding across subclasses.

## Data

- Scale: 10,002 entries.
- Categories: physical object properties, object relationships, scene understanding and physics-based dynamics.
- Granularity: 19 subclasses and reported capability dimensions.
- Release: project dataset, code and EvalAI challenge.

## Method

- Curate multimodal physical questions with category labels.
- Evaluate closed/open VLMs and analyze scaling/correlation/error types.
- PhysAgent routes tasks through specialized vision models to augment the VLM.

## Key Figures / Architecture

figure_status: linked_official

- Figure / demo: examples, distributions and model/category charts.
- Source: https://physbench.github.io/
- What it shows: benchmark breadth and physical-reasoning gaps.
- Why it matters: supports capability-level diagnosis before embodied deployment.

## Evidence Trail

| Claim | Source | Status | Notes |
|---|---|---|---|
| 10,002 entries | paper/project | verified | Primary sources agree. |
| 75 VLM evaluation | paper/project | verified | Reported experiment scope. |
| Public data/code/challenge | official project | verified | Links resolve. |

## Evidence

- Main metrics: overall and per-category multiple-choice accuracy.
- Analyses: scaling, correlation, error types and knowledge transfer.
- Baselines: 75 VLMs plus PhysAgent.
- Reproducibility: ICLR paper, code, data and evaluation challenge.

## Limitations

- Multiple-choice tasks permit shortcutting and weak causal grounding.
- No action execution or closed-loop intervention.
- Tool augmentation may improve perception without learning a world model.

## Project Relevance

- Reusable fields: PhysicalProperty, SpatialRelation, DynamicEvent, CapabilityDimension and ErrorType.
- Baseline role: upstream physical-understanding gate for spatial and action models.
- Pair with executable tests to measure whether knowledge supports action.

## Reproduction / Follow-up

- Audit category balance and answer priors.
- Correlate PhysBench gains with intervention and manipulation success.

