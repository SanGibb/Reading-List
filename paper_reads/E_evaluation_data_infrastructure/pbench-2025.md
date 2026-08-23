# PBench: A Physical AI Benchmark for World Models

candidate_id: CAND-0001
branch: E
decision: accepted_for_registry

## Source Links

- Paper / project: https://research.nvidia.com/labs/dir/pbench/
- Data: https://huggingface.co/datasets/nvidia/PBench
- Code ecosystem: https://github.com/nvidia-cosmos/cosmos-predict2.5

## TL;DR

PBench evaluates image-conditioned world-model videos with both physical-domain questions and conventional quality metrics. Its useful split between domain correctness and visual quality is directly reusable, but results depend on an automated VLM judge and do not establish closed-loop policy utility.

## Novelty

- Couples a Physical AI ontology with generated-video QA.
- Covers AV, robotics, industry, physics, human and commonsense domains.
- Separates domain score from eight-component video quality score.

## Contributions

1. Releases 1,044 samples and 5,636 manually corrected QA pairs.
2. Defines space, time and fundamental-physics diagnostic categories.
3. Publishes data, examples, evaluation code links and baseline breakdowns.

## Task

- Input: conditioning image, prompt and generated future video.
- Output: domain and quality scores.
- Setting: open world-model evaluation across six physical domains.
- Success criterion: correct physical answers without sacrificing video quality.

## Data

- Dataset / benchmark: NVIDIA PBench.
- Scale: 1,044 samples; 5,636 QA pairs; about 5.4 QA pairs per sample.
- Modalities: images, prompts, generated videos and binary QA.
- Collection / annotation: VLM-drafted descriptions/questions with manual correction.
- Protocol: average domain QA accuracy plus VBench-derived quality metrics.

## Method

- Generate a future video for each image/prompt pair.
- Judge ontology-grounded binary questions with Qwen2.5-VL-72B-Instruct.
- Average domain performance and eight quality dimensions into the final score.

## Key Figures / Architecture

figure_status: linked_official

- Figure / demo: PBench overview, examples and score tables.
- Source: https://research.nvidia.com/labs/dir/pbench/
- What it shows: domain coverage, QA design and model comparison.
- Why it matters: makes the physical-correctness/visual-quality split auditable.

## Evidence Trail

| Claim | Source | Status | Notes |
|---|---|---|---|
| 1,044 samples / 5,636 QA pairs | official project | verified | Stated in overview. |
| Cosmos-Predict2-14B overall 77.4 | official result table | verified | Reported benchmark result. |
| Data and code availability | official data/project links | verified | Public links resolve. |

## Evidence

- Main metrics: overall, domain and quality scores plus domain/category breakdowns.
- Qualitative results: interactive examples pair generated videos with QA.
- Baselines: open I2V models and Cosmos-Predict variants.
- Reproducibility signals: public data and implementation ecosystem.

## Limitations

- VLM judge bias can become part of the metric.
- Averaging can conceal robotics-specific failures.
- Video correctness is not equivalent to real policy success.

## Project Relevance

- Reusable fields: PhysicalDomain, OntologyCategory, DomainScore, QualityScore and JudgeTrace.
- Baseline role: diagnostic evaluation for embodied world-model generation.
- Implication: report physical correctness separately from perceptual fidelity.

## Reproduction / Follow-up

- Pin judge/model versions and reproduce category-level scores.
- Add closed-loop and human-audit subsets before using for policy claims.

