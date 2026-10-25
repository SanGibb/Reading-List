# Sensorimotor Alignment: A Platonic Proxy for Embodied Policy Success

candidate_id: CAND-0006
branch: E
decision: accepted_for_registry
acceptance_policy_version: 2

## Source Links

- Paper: https://arxiv.org/abs/2610.31670
- Project: https://yunfeixie233.github.io/s2/
- Code: https://github.com/yunfeixie233/sensorimotor-alignment
- Data / benchmark: linked from the official code/project release
- Demo / video: not used as an acceptance-critical visual claim
- Official figures: primary paper/project page

## TL;DR

S² compares neighborhoods in sensory-feature space with neighborhoods in end-effector-trajectory space. It is accepted as a released, low-cost screening metric—not as a replacement for closed-loop evaluation.

## Novelty

- What is actually new: Introduces sensorimotor alignment as an inexpensive representation-level proxy for closed-loop success.
- Difference from prior work: Adds a training-free representation metric that predicts policy success before closed-loop rollout.
- Why the delta matters: The metric and released code are not covered by a robustness benchmark.

## Acceptance Rationale / Registry Comparison

- impact_score / justification: 4/5; substantive diagnostic capability with controlled evaluation and reusable release.
- project_relevance_score / direct interface, validator or baseline: 4/5; A direct pre-rollout validator for prioritizing VLA/WAM baselines and backbone candidates.
- evidence_strength / primary supporting evidence: 4/5; primary paper plus official released artifact and limitations.
- selection_basis: reusable_infrastructure
- acceptance_rationale: the artifact is directly callable in evaluation or model selection and is materially different from maintained work.
- comparison_to_registry.closest_paper: https://arxiv.org/abs/2610.07597
- comparison_to_registry.material_difference: Adds a training-free representation metric that predicts policy success before closed-loop rollout.
- comparison_to_registry.why_new_entry: The metric and released code are not covered by a robustness benchmark.

## Contributions

1. Introduces sensorimotor alignment as an inexpensive representation-level proxy for closed-loop success.
2. Provides a concrete benchmark/metric implementation rather than only a taxonomy.
3. Reports controlled agreement or localization evidence and exposes limitations.

## Task

- Input: Twelve VLAs on SimplerEnv plus WAM, real-robot and frozen-backbone analyses.
- Output: diagnostic score, alignment estimate, or localized evaluation trace.
- Setting: offline evaluation of embodied policies or generated physical rollouts.
- Success criterion: controlled correlation/agreement/localization under the paper's stated protocol.

## Task Frontier / Lifecycle

- task_ids: e-offline-embodied-policy-success-proxies
- Task scope / comparison protocol: preserve dataset, model family, annotation protocol, metric and compute budget.
- Role in each task: current within its narrowly reviewed diagnostic sub-scope.
- Reviewed on / verified sources: 2026-10-26; primary arXiv abstract and linked official artifact.
- Closest current / alternative members: https://arxiv.org/abs/2610.07597
- Improvements and tradeoffs: complementary diagnostic, not a global replacement.
- Pending evidence: independent reproduction and cross-domain validation.

## Data

- Dataset / benchmark: Twelve VLAs on SimplerEnv plus WAM, real-robot and frozen-backbone analyses.
- Scale: as stated above; author-reported.
- Modalities: video, model features, language and/or trajectories depending on the method.
- Collection / annotation: see primary paper and released artifact.
- Splits / evaluation protocol: retained from the source; no cross-paper score normalization.

## Method

- Core pipeline: Training-free neighborhood-overlap metric compares sensory representation geometry with end-effector trajectory geometry.
- Model / representation: source-specific evaluator or metric.
- Training or optimization: see primary paper; training-free where stated.
- Inference / deployment: offline scoring and diagnosis.
- Losses or metrics: source protocol only.

## Key Figures / Architecture

figure_status: linked_official

- Figure / demo: architecture and evaluation overview.
- Source: https://yunfeixie233.github.io/s2/
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
| Core scale and result | https://arxiv.org/abs/2610.31670 | verified | true | Author-reported primary source. |
| Code/data availability | https://github.com/yunfeixie233/sensorimotor-alignment | verified | true | Official release surface checked. |
| Cross-domain generalization | https://arxiv.org/abs/2610.31670 | partial | false | Limited to reported domains. |

## Evidence

- Main metrics: Across twelve VLAs on SimplerEnv, the official page reports Pearson r=0.717 between S² and task success; the paper additionally analyzes WAMs, real robots, frozen encoders and model depth.
- Qualitative results: not acceptance-critical.
- Ablations: source paper reports relevant component/protocol comparisons.
- Baselines: closest source baselines retained without cross-paper normalization.
- Reproducibility signals: official code/data/reviewer artifact is public.

## Limitations

- Method limitations: Correlation can be task- and representation-dependent; the evidence does not establish causal improvement or guarantee deployment success.
- Experimental limitations: fresh 2026 release and author-reported results.
- Demo / visual limitations: no visual-quality claim is made.
- Claims that remain unverified: independent reproduction and deployment transfer.

## Project Relevance

- Relevance to interactive embodied generation: diagnoses candidate policies or generated rollouts before costly downstream use.
- Reusable fields: source inputs, per-sample scores/traces, aggregate protocol metadata.
- Direct interface / validator / baseline and how it would be used: A direct pre-rollout validator for prioritizing VLA/WAM baselines and backbone candidates.
- Implications for our task / benchmark: separates evaluation infrastructure from visual plausibility assertions.

## Reproduction / Follow-up

- What to check before using: exact dependencies, annotation license, model weights and compute.
- Code / checkpoint availability: official surface linked above.
- Citation or related-work caveats: cite reported results as author-reported until rerun.
