# RoboJudge: Multimodal Language Models as Judges for Embodied Video Generation

candidate_id: CAND-0008
branch: E
decision: accepted_for_registry
acceptance_policy_version: 2

## Source Links

- Paper: https://arxiv.org/abs/2610.27782
- Project: https://siyuanmacs.github.io/robojudge-iclr2027/
- Code: https://github.com/SiyuanMaCS/robojudge-iclr2027
- Data / benchmark: linked from the official code/project release
- Demo / video: not used as an acceptance-critical visual claim
- Official figures: primary paper/project page

## TL;DR

RoboJudge benchmarks whether multimodal judges agree with humans on physical adherence and instruction alignment, then trains a specialized 9B judge. It is accepted as reusable evaluation infrastructure for generated embodied rollouts.

## Novelty

- What is actually new: Systematically validates judge-human agreement for embodied rollouts and releases a specialized training/evaluation bundle.
- Difference from prior work: Validates automated judge agreement on generated embodied videos and releases human labels plus a specialized judge.
- Why the delta matters: Existing rollout benchmarks score model outputs/tasks but do not benchmark the judge itself at this scale.

## Acceptance Rationale / Registry Comparison

- impact_score / justification: 4/5; substantive diagnostic capability with controlled evaluation and reusable release.
- project_relevance_score / direct interface, validator or baseline: 4/5; A direct automated evaluator for candidate embodied-video/world-model rollouts.
- evidence_strength / primary supporting evidence: 4/5; primary paper plus official released artifact and limitations.
- selection_basis: reusable_infrastructure
- acceptance_rationale: the artifact is directly callable in evaluation or model selection and is materially different from maintained work.
- comparison_to_registry.closest_paper: https://openaccess.thecvf.com/content/CVPR2026W/GigaBrainChallenge/html/Jiang_RoboWM-Bench_A_Benchmark_for_Evaluating_World_Models_in_Robotic_Manipulation_CVPRW_2026_paper.html
- comparison_to_registry.material_difference: Validates automated judge agreement on generated embodied videos and releases human labels plus a specialized judge.
- comparison_to_registry.why_new_entry: Existing rollout benchmarks score model outputs/tasks but do not benchmark the judge itself at this scale.

## Contributions

1. Systematically validates judge-human agreement for embodied rollouts and releases a specialized training/evaluation bundle.
2. Provides a concrete benchmark/metric implementation rather than only a taxonomy.
3. Reports controlled agreement or localization evidence and exposes limitations.

## Task

- Input: 800 benchmark videos from 8 corpora/10 generators and 12,351 training videos with human-verified scores.
- Output: diagnostic score, alignment estimate, or localized evaluation trace.
- Setting: offline evaluation of embodied policies or generated physical rollouts.
- Success criterion: controlled correlation/agreement/localization under the paper's stated protocol.

## Task Frontier / Lifecycle

- task_ids: e-physical-future-outcome-evaluation
- Task scope / comparison protocol: preserve dataset, model family, annotation protocol, metric and compute budget.
- Role in each task: current within its narrowly reviewed diagnostic sub-scope.
- Reviewed on / verified sources: 2026-10-26; primary arXiv abstract and linked official artifact.
- Closest current / alternative members: https://openaccess.thecvf.com/content/CVPR2026W/GigaBrainChallenge/html/Jiang_RoboWM-Bench_A_Benchmark_for_Evaluating_World_Models_in_Robotic_Manipulation_CVPRW_2026_paper.html
- Improvements and tradeoffs: complementary diagnostic, not a global replacement.
- Pending evidence: independent reproduction and cross-domain validation.

## Data

- Dataset / benchmark: 800 benchmark videos from 8 corpora/10 generators and 12,351 training videos with human-verified scores.
- Scale: as stated above; author-reported.
- Modalities: video, model features, language and/or trajectories depending on the method.
- Collection / annotation: see primary paper and released artifact.
- Splits / evaluation protocol: retained from the source; no cross-paper score normalization.

## Method

- Core pipeline: Benchmark plus a 9B MLLM judge trained with supervised learning and reinforcement learning.
- Model / representation: source-specific evaluator or metric.
- Training or optimization: see primary paper; training-free where stated.
- Inference / deployment: offline scoring and diagnosis.
- Losses or metrics: source protocol only.

## Key Figures / Architecture

figure_status: linked_official

- Figure / demo: architecture and evaluation overview.
- Source: https://siyuanmacs.github.io/robojudge-iclr2027/
- Render: linked official source; not copied locally.
- What it shows: metric inputs, scoring stages and validation protocol.
- Why it matters: exposes the exact interface used by the repository.

## Visual / Demo Inspection

- requires_visual_review: false
- requires_temporal_demo: false
- visual_quality_decision: not_applicable
- not_applicable_reason: acceptance concerns evaluation methodology, released artifacts and controlled alignment/localization results, not generated visual quality.

| Official media actually inspected | Modality | Page / figure / time range | Observation and sample/task coverage | Defects / limits |
|---|---|---|---|---|
| Primary paper/project page | paper_figure | Abstract and method/evaluation overview | Protocol and reported results were checked. | No independent rerun; videos were not used as acceptance evidence. |

## Evidence Trail

| Claim | Source | Status | Used for acceptance? | Notes |
|---|---|---|---|---|
| Core scale and result | https://arxiv.org/abs/2610.27782 | verified | true | Author-reported primary source. |
| Code/data availability | https://github.com/SiyuanMaCS/robojudge-iclr2027 | verified | true | Official release surface checked. |
| Cross-domain generalization | https://arxiv.org/abs/2610.27782 | partial | false | Limited to reported domains. |

## Evidence

- Main metrics: The primary paper reports 800 benchmark videos, 12K training videos and Pearson r=0.719, a significant +0.089 over its strongest proprietary baseline; an official reviewer bundle exposes labels, prompts, predictions and checkpoint links.
- Qualitative results: not acceptance-critical.
- Ablations: source paper reports relevant component/protocol comparisons.
- Baselines: closest source baselines retained without cross-paper normalization.
- Reproducibility signals: official code/data/reviewer artifact is public.

## Limitations

- Method limitations: Training rationales are model-assisted then human-verified; generalization beyond the eight source corpora and ten generators remains uncertain.
- Experimental limitations: fresh 2026 release and author-reported results.
- Demo / visual limitations: no visual-quality claim is made.
- Claims that remain unverified: independent reproduction and deployment transfer.

## Project Relevance

- Relevance to interactive embodied generation: diagnoses candidate policies or generated rollouts before costly downstream use.
- Reusable fields: source inputs, per-sample scores/traces, aggregate protocol metadata.
- Direct interface / validator / baseline and how it would be used: A direct automated evaluator for candidate embodied-video/world-model rollouts.
- Implications for our task / benchmark: separates evaluation infrastructure from visual plausibility assertions.

## Reproduction / Follow-up

- What to check before using: exact dependencies, annotation license, model weights and compute.
- Code / checkpoint availability: official surface linked above.
- Citation or related-work caveats: cite reported results as author-reported until rerun.
