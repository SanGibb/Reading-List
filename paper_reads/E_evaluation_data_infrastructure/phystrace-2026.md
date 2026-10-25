# PhysTrace: Interpretable Temporal Evaluation of Physical Consistency in Video Generative Models

candidate_id: CAND-0007
branch: E
decision: accepted_for_registry
acceptance_policy_version: 2

## Source Links

- Paper: https://arxiv.org/abs/2610.31429
- Project: not available
- Code: https://github.com/PhysTrace/PhysTrace
- Data / benchmark: linked from the official code/project release
- Demo / video: not used as an acceptance-critical visual claim
- Official figures: primary paper/project page

## TL;DR

PhysTrace compares history-conditioned expected physical events with overlapping observed video windows and returns violation intervals plus descriptions. It is accepted because the code and IntPhys2-Timing annotations make temporal diagnosis directly reusable.

## Novelty

- What is actually new: Moves beyond scalar plausibility to time-localized, interpretable physical violations and releases annotations/code.
- Difference from prior work: Adds temporal intervals and explanations rather than only concept-level or clip-level physical scores.
- Why the delta matters: Released evaluator and timing annotations create new diagnostic knowledge.

## Acceptance Rationale / Registry Comparison

- impact_score / justification: 4/5; substantive diagnostic capability with controlled evaluation and reusable release.
- project_relevance_score / direct interface, validator or baseline: 4/5; A direct validator for generated world-model rollouts and reconstruction trajectories.
- evidence_strength / primary supporting evidence: 4/5; primary paper plus official released artifact and limitations.
- selection_basis: decisive_evaluation
- acceptance_rationale: the artifact is directly callable in evaluation or model selection and is materially different from maintained work.
- comparison_to_registry.closest_paper: https://arxiv.org/abs/2601.21282
- comparison_to_registry.material_difference: Adds temporal intervals and explanations rather than only concept-level or clip-level physical scores.
- comparison_to_registry.why_new_entry: Released evaluator and timing annotations create new diagnostic knowledge.

## Contributions

1. Moves beyond scalar plausibility to time-localized, interpretable physical violations and releases annotations/code.
2. Provides a concrete benchmark/metric implementation rather than only a taxonomy.
3. Reports controlled agreement or localization evidence and exposes limitations.

## Task

- Input: IntPhys2 plus new interval annotations for solidity, permanence, immutability and continuity.
- Output: diagnostic score, alignment estimate, or localized evaluation trace.
- Setting: offline evaluation of embodied policies or generated physical rollouts.
- Success criterion: controlled correlation/agreement/localization under the paper's stated protocol.

## Task Frontier / Lifecycle

- task_ids: e-physical-future-outcome-evaluation
- Task scope / comparison protocol: preserve dataset, model family, annotation protocol, metric and compute budget.
- Role in each task: current within its narrowly reviewed diagnostic sub-scope.
- Reviewed on / verified sources: 2026-10-26; primary arXiv abstract and linked official artifact.
- Closest current / alternative members: https://arxiv.org/abs/2601.21282
- Improvements and tradeoffs: complementary diagnostic, not a global replacement.
- Pending evidence: independent reproduction and cross-domain validation.

## Data

- Dataset / benchmark: IntPhys2 plus new interval annotations for solidity, permanence, immutability and continuity.
- Scale: as stated above; author-reported.
- Modalities: video, model features, language and/or trajectories depending on the method.
- Collection / annotation: see primary paper and released artifact.
- Splits / evaluation protocol: retained from the source; no cross-paper score normalization.

## Method

- Core pipeline: History-conditioned expected events are aligned with overlapping observed video windows to localize violations.
- Model / representation: source-specific evaluator or metric.
- Training or optimization: see primary paper; training-free where stated.
- Inference / deployment: offline scoring and diagnosis.
- Losses or metrics: source protocol only.

## Key Figures / Architecture

figure_status: linked_official

- Figure / demo: architecture and evaluation overview.
- Source: https://arxiv.org/abs/2610.31429
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
| Core scale and result | https://arxiv.org/abs/2610.31429 | verified | true | Author-reported primary source. |
| Code/data availability | https://github.com/PhysTrace/PhysTrace | verified | true | Official release surface checked. |
| Cross-domain generalization | https://arxiv.org/abs/2610.31429 | partial | false | Limited to reported domains. |

## Evidence

- Main metrics: The paper reports up to 70.7% hit rate on IntPhys2-Timing and improved possible/impossible discrimination; the official repository exposes batch evaluation and a result-inspection demo.
- Qualitative results: not acceptance-critical.
- Ablations: source paper reports relevant component/protocol comparisons.
- Baselines: closest source baselines retained without cross-paper normalization.
- Reproducibility signals: official code/data/reviewer artifact is public.

## Limitations

- Method limitations: The evaluator depends on pretrained alignment/MLLM components, covers four IntPhys2 principles, and does not establish real-robot utility.
- Experimental limitations: fresh 2026 release and author-reported results.
- Demo / visual limitations: no visual-quality claim is made.
- Claims that remain unverified: independent reproduction and deployment transfer.

## Project Relevance

- Relevance to interactive embodied generation: diagnoses candidate policies or generated rollouts before costly downstream use.
- Reusable fields: source inputs, per-sample scores/traces, aggregate protocol metadata.
- Direct interface / validator / baseline and how it would be used: A direct validator for generated world-model rollouts and reconstruction trajectories.
- Implications for our task / benchmark: separates evaluation infrastructure from visual plausibility assertions.

## Reproduction / Follow-up

- What to check before using: exact dependencies, annotation license, model weights and compute.
- Code / checkpoint availability: official surface linked above.
- Citation or related-work caveats: cite reported results as author-reported until rerun.
