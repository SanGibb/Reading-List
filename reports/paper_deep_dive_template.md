# <Paper Title>

candidate_id: CAND-xxxx
branch: A|B|C|D|E
decision: accepted_for_registry
acceptance_policy_version: 2

## Source Links

- Paper:
- Project:
- Code:
- Data / benchmark:
- Demo / video:
- Official figures:

## TL;DR

One short paragraph explaining what the paper does, why it matters, and the main caveat.

## Novelty

- What is actually new:
- Difference from prior work:
- Why the delta matters:

## Acceptance Rationale / Registry Comparison

For policy-version-2 additions, all three final scores must be at least 4/5; no score compensates for another. Use technical substance plus controlled experiments or a reusable release for impact, not citations, popularity or venue.

- impact_score / justification:
- project_relevance_score / direct interface, validator or baseline:
- evidence_strength / primary supporting evidence:
- selection_basis: new_capability|substantial_improvement|reusable_infrastructure|decisive_evaluation
- acceptance_rationale:
- comparison_to_registry.closest_paper:
- comparison_to_registry.material_difference:
- comparison_to_registry.why_new_entry:

If there is no material increment, update the existing entry or record a noop rather than producing a redundant new entry.

## Contributions

1.
2.
3.

## Task

- Input:
- Output:
- Setting:
- Success criterion:

## Data

- Dataset / benchmark:
- Scale:
- Modalities:
- Collection / annotation:
- Splits / evaluation protocol:

## Method

- Core pipeline:
- Model / representation:
- Training or optimization:
- Inference / deployment:
- Losses or metrics:

## Key Figures / Architecture

figure_status: linked_official|captured_official|redrawn|not_applicable|missing

- Figure / demo:
- Source:
- Render:
  ![key figure](https://example.com/official-figure-or-demo.png)
- What it shows:
- Why it matters:

If using paper/project figures, link official sources. If redrawing, keep it visually distinct and cite the paper.

## Visual / Demo Inspection

- requires_visual_review: true|false
- requires_temporal_demo: true|false
- visual_quality_decision: strong|adequate|weak|undecided|not_applicable
- not_applicable_reason (when applicable):

| Official media actually inspected | Modality | Page / figure / time range | Observation and sample/task coverage | Defects / limits |
|---|---|---|---|---|
|  |  |  |  |  |

List media actually inspected separately from unviewed links. Motion-dependent claims require video, GIF or interactive-demo evidence; a paper figure, linked video, or reported success rate alone does not establish motion quality. Check joint motion, collisions, stability, contact and task usability where applicable. If required visuals remain uncertain and the candidate otherwise qualifies, maintain this analysis as a local-only undecided dossier pending human judgment.

## Evidence Trail

Use this section for collection-critical claims only. Do not turn it into a research plan.

| Claim | Source | Status | Used for acceptance? | Notes |
|---|---|---|---|---|
| Dataset scale / benchmark size |  | verified / partial / unverified | true / false |  |
| Main reported result or comparison |  | verified / partial / unverified | true / false |  |
| Code / checkpoint / demo availability |  | verified / partial / unverified | true / false |  |

An accepted candidate needs at least one verified central claim with a primary/official HTTP source. Partial or unverified claims may be retained as caveats only with `used_for_acceptance: false`.

## Evidence

- Main metrics:
- Qualitative results:
- Ablations:
- Baselines:
- Reproducibility signals:

## Limitations

- Method limitations:
- Experimental limitations:
- Demo / visual limitations:
- Claims that remain unverified:

## Project Relevance

- Relevance to interactive embodied generation:
- Reusable fields:
- Direct interface / validator / baseline and how it would be used:
- Implications for our task / benchmark:

Generic relevance or useful fields alone does not justify the policy-version-2 project-relevance threshold. Object-level articulated/physical sim-ready assets can qualify under A without generating a complete world.

## Reproduction / Follow-up

- What to check before using:
- Code / checkpoint availability:
- Citation or related-work caveats:
