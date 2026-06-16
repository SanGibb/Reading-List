# Embodied3DBench: Benchmarking Low-Level Embodied Spatial Intelligence of Vision Language Models

candidate_id: CAND-0049
branch: C
decision: accepted_for_registry
authors: Zhang et al.
year: 2026
venue: arXiv

## Source Links

- Paper: https://arxiv.org/abs/2605.29074
- Project: https://arxiv.org/abs/2605.29074
- Code: https://arxiv.org/abs/2605.29074
- Data / benchmark: https://arxiv.org/abs/2605.29074
- Demo / video: https://arxiv.org/abs/2605.29074
- Official figures: https://arxiv.org/abs/2605.29074

## TL;DR

Embodied3DBench is a useful new spatial-intelligence benchmark because it targets the low-level embodied perception and grounding skills that many larger embodied-VLM evaluations blur together. The key repository value is that it separates structural spatial understanding from interaction-oriented perception, then pairs evaluation with a large synthetic training set that can expose and partly repair specific capability gaps. Main caveat: the source access in this run is arXiv-first, with no separate official project page discovered.

## Novelty

- What is actually new: a robot-centric benchmark focused on low-level embodied 3D spatial intelligence rather than only high-level instruction reasoning.
- Difference from prior work: it explicitly covers affordance prediction, grasp point prediction, and trajectory prediction alongside grounding, relation prediction, and multi-view correspondence.
- Why the delta matters: these are exactly the fine-grained perceptual bottlenecks that interactive embodied generation systems need when turning generated or reconstructed worlds into action-ready representations.

## Contributions

1. Defines a six-task benchmark for low-level embodied spatial intelligence in 3D environments.
2. Provides 21k+ QA pairs across 12 subcategories and a 1.3M-pair synthetic training set for capability improvement.
3. Diagnoses a gap between high-level spatial reasoning and interaction-oriented embodied perception in current VLMs.

## Task

- Input: embodied 3D observations framed as robot-centric spatial understanding and interaction-oriented perception questions.
- Output: predictions for grounding, spatial relations, multi-view correspondence, affordances, grasp points, and trajectory-relevant perception.
- Setting: benchmark evaluation and synthetic-data-driven improvement for embodied VLM spatial capability.
- Success criterion: accurate low-level spatial and interaction-oriented prediction across the defined subcategories.

## Data

- Dataset / benchmark: Embodied3DBench with more than 21k high-quality question-answer pairs and an additional 1.3M synthetic QA training set.
- Scale: six task categories, 12 subcategories, 21k+ benchmark pairs, and 1.3M synthetic training pairs.
- Modalities: embodied 3D environment observations and question-answer supervision oriented around spatial and interaction understanding.
- Collection / annotation: the abstract positions the benchmark as a systematic robot-centric evaluation set and the synthetic data as a capability-bridging augmentation resource.
- Splits / evaluation protocol: the paper evaluates 13 state-of-the-art models and reports gains from fine-tuning on the synthetic set.

## Method

- Core pipeline: benchmark construction plus model diagnosis, followed by synthetic-data-based finetuning to improve low-level spatial intelligence.
- Model / representation: benchmark and training-data infrastructure for embodied spatial VLMs.
- Training or optimization: synthetic QA finetuning on the 1.3M-pair dataset.
- Inference / deployment: evaluates model responses on structural and interaction-oriented perception tasks rather than closed-loop robot control.
- Losses or metrics: use the paper’s reported model-comparison metrics and finetuning gains when citing.

## Key Figures / Architecture

figure_status: missing

- Figure / demo: no stable official project or figure URL was identified during this run beyond the arXiv paper entry.
- Source: https://arxiv.org/abs/2605.29074
- Render:
  Official source entry: https://arxiv.org/abs/2605.29074
- What it shows: the arXiv abstract provides the benchmark structure, task split, and scale claims used for acceptance.
- Why it matters: this paper is accepted on benchmark relevance and explicit low-level task coverage, not on demo aesthetics.

## Evidence Trail

| Claim | Source | Status | Notes |
|---|---|---|---|
| Six task categories split into structural and interaction-oriented groups | https://arxiv.org/abs/2605.29074 | verified | Stated directly in the abstract. |
| Benchmark spans 12 subcategories and 21k+ QA pairs | https://arxiv.org/abs/2605.29074 | verified | Central scale claim in the abstract. |
| Synthetic training set contains 1.3M QA pairs | https://arxiv.org/abs/2605.29074 | verified | Reported as the data used to bridge identified capability gaps. |
| 13 SOTA models were evaluated and improve after finetuning | https://arxiv.org/abs/2605.29074 | verified | Accept as source-reported benchmark evidence. |

## Evidence

- Main metrics: the abstract reports evaluation on 13 state-of-the-art models and significant improvements after training on the synthetic set.
- Qualitative results: not a generation-demo paper; the important evidence is benchmark/task coverage rather than visual flair.
- Ablations: this run does not inspect full ablation tables beyond abstract-level claims.
- Baselines: use the benchmark paper’s own comparison set when citing specific model rankings.
- Reproducibility signals: primary arXiv source and explicit dataset/benchmark scale are sufficient for acceptance into the benchmark-heavy spatial branch.

## Limitations

- Method limitations: benchmark-first contribution rather than a new execution model or spatial controller.
- Experimental limitations: no separate official code/project page was identified during this run.
- Demo / visual limitations: figure URLs were not extracted from an official project page, so the deep dive records `figure_status: missing`.
- Claims that remain unverified: exact benchmark licensing, release packaging, and fine-grained protocol details should be checked in the full paper before downstream use.

## Project Relevance

- Relevance to interactive embodied generation: directly useful for evaluating whether generated or reconstructed worlds preserve the low-level spatial and affordance cues needed for action.
- Reusable fields: SpatialGroundingTask, MultiViewCorrespondence, AffordancePrediction, GraspPointPrediction, TrajectoryPrediction, and SyntheticSpatialQA.
- Possible baseline role: spatial benchmark and diagnostic set for low-level embodied perception failures.
- Implications for our task / benchmark: helps separate “can describe the scene” from “can act in the scene,” which is critical for this repository’s embodied focus.

## Reproduction / Follow-up

- What to check before using: full benchmark protocol, exact task formats, dataset access terms, and whether code/data release URLs are provided in the full paper.
- Code / checkpoint availability: not confirmed from primary official pages beyond the arXiv source during this run.
- Citation or related-work caveats: cite benchmark scale and task taxonomy from the paper; avoid stronger release claims until code/data URLs are confirmed.
