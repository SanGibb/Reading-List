# Acceptance Harness

This harness defines when a paper may enter the repository.

The repository optimizes for **research quality and visible usefulness**, not publication status alone. A recent arXiv paper with excellent demos can be accepted; a peer-reviewed paper with weak or unconvincing generated results can be rejected or sent to human decision.

## Policy v2: broad discovery, selective admission

Effective **2026-10-20**, new runs declare `acceptance_policy_version: 2` in
`00_run_plan.json`. Earlier runs and the existing registry remain historical records;
this change does not delete, rescore, or retrospectively endorse their papers.

The registry is a maintained reading shortlist. Discover broadly across all five
branches, but add a paper only when it materially improves that shortlist. A weekly
run may add **zero** papers. Do not fill branches or turn every relevant release into
a full deep dive. Do not impose a top-k cutoff on papers passing the stronger gates.

## Required Fields

Every accepted paper must include:

- `title`
- `year`
- `venue`
- `url`
- `branch`
- `data`
- `method`
- `task`
- `novelty`
- `project_relevance`
- `source_quality`
- `demo_score`
- `visual_quality_score`
- `visual_quality_decision`
- `evidence_strength`

V2 additions also require `acceptance_policy_version: 2`, final `impact_score` and
`project_relevance_score`, plus boolean `requires_visual_review` and
`requires_temporal_demo`. The review, patch, and registry scores must agree.

Every paper added to the registry patch must also have a Markdown deep dive under:

```text
paper_reads/<branch>/<slug>.md
```

The registry addition must include `deep_dive_path` pointing to that file. The deep dive is part of the acceptance evidence, not optional notes.

## Evidence Discipline

The workflow borrows claim-tracing discipline from research agents, but only for paper collection.

- Central claims should be traceable to a primary or official source.
- Claims about SOTA, dataset size, benchmark rank, public checkpoints, or demo availability must be phrased as reported by the source unless independently reproduced.
- If a claim is relevant but not verified, keep it under `claims_requiring_verification` or the deep-dive limitations section.
- Unverified claims can motivate watchlist status, but they must not be used as acceptance evidence.
- Social or news mentions are discovery signals only; they do not satisfy evidence requirements.

## Recency Rule

The frontier registry is **2024+ only**.

- Accepted papers must have `year >= 2024`.
- Pre-2024 papers can be mentioned as historical background in prose, but they must not be added to `data/papers.seed.json`.
- If a candidate is an updated benchmark/model with an old predecessor, collect only the new 2024+ paper or release.

## Branch Fit

Accepted papers must fit one primary branch:

- A: Executable World Representation.
- B: Interactive Generation and PCG.
- C: Spatial Intelligence.
- D: VLA and World-Action Models.
- E: Evaluation and Data Infrastructure.

If a candidate fits none of these, reject it unless it exposes a direct missing capability for interactive embodied generation.

Object-level methods can qualify independently under A: articulated parts/joints,
physical properties, collision/stability validation, affordances, and functionally
usable simulation assets do not need to form a complete scene. Appearance-only
object generation or generic robotics does not qualify merely because it might
eventually be useful in simulation.

## Source Quality

Use this order:

1. peer-reviewed venue page or official proceedings
2. arXiv / OpenReview / CVF / PMLR
3. official project page
4. official GitHub repository
5. reputable survey / benchmark page
6. social or news source

Social/news-only candidates are not accepted. They can be tracked in a "watchlist" until a primary source appears.

Venue is evidence, not a gate:

- Peer-reviewed acceptance increases source confidence.
- Lack of acceptance does not block a paper if the method, evidence, and demos are strong.
- Acceptance alone does not rescue weak visual results or poor relevance.

## Impact Score

Score from 0 to 5:

- 5: establishes a major capability or compelling reusable foundation with strong validation.
- 4: substantial method/capability improvement supported by meaningful controls, or a clearly reusable release with strong validation.
- 3: solid but incremental, narrow, or insufficiently distinguished from maintained papers.
- 2: narrow or incremental but relevant.
- 1: weak relevance.
- 0: reject.

`impact_score` measures technical contribution, not popularity. New papers need not
have citations, stars, adoption, or a prestigious venue. A small SOTA improvement,
larger backbone, or code release alone does not justify 4. Record a source-backed
reason; do not mechanically round every relevant candidate up to 4.

## Project Relevance Score

Score from 0 to 5:

- 5: directly provides target-task fields, compiler targets, validators, or benchmark tasks.
- 4: direct method/baseline or reusable infrastructure for a concrete repository task, with a named use rather than a list of plausible schema fields.
- 3: supports one target-task layer such as spatial reasoning, physical properties, or trajectories.
- 2: background only.
- 1: tangential.
- 0: reject.

## Evidence Strength

- 5: multiple complementary convincing checks with inspectable/reusable artifacts.
- 4: primary-source comparisons, protocol, limitations, and relevant visual/functional evidence are inspectable and support the contribution.
- 3: promising but limited evaluation or incomplete release/verification.
- 0-2: weak, missing, or untraceable support.

Record final `impact_score`, `project_relevance_score`, and `evidence_strength` in
`03_review.json.quality_review`. Discovery priors are triage estimates only. All
claims used for acceptance must have verified primary/official traces; use
`used_for_acceptance: false` to retain partial/unverified caveats without treating
them as admission evidence. Open code is helpful but not mandatory by itself.

## Demo Score

Score from 0 to 5:

- 5: public model/checkpoint or benchmark plus demos.
- 4: code plus reproducible demos.
- 3: project page with video or interactive demo.
- 2: project page with qualitative examples.
- 1: static paper figures only.
- 0: no demo.

## Visual Quality Score

For generation-heavy, interactive-world, physical-world, VLA-demo, or embodied-demo papers, Quality Reviewer must inspect the visual evidence.

Score from 0 to 5:

- 5: excellent, diverse, high-fidelity and task-relevant results.
- 4: strong, convincing results with minor artifacts.
- 3: adequate but not outstanding results.
- 2: weak, artifact-heavy, cherry-picked, physically implausible, or not clearly interactive.
- 1: barely assessable.
- 0: no visual evidence.

Decision values:

- `strong`
- `adequate`
- `weak`
- `undecided`
- `not_applicable`

Generation-heavy papers usually require `strong` or `adequate`. If visual quality is `undecided`, the candidate goes to `undecided/YYYY-MM-DD/` for human decision and must not be added to the registry in that run.

`demo_score` measures availability, not quality. Every analyzed paper states
`requires_visual_review` and `requires_temporal_demo`. Claims about movement,
contact, interaction, or robot execution require temporal media or a working
interactive demo. A benchmark/data label does not waive a generation/execution
claim used for acceptance.

For required inspection, record `inspection_evidence`: official media/figure URL,
modality, exact page/figure or time range (`locator`), observed behavior
(`observation`), and limitations/coverage. Inspect representative samples and
failure cases where available. For articulated assets, distinguish appearance,
joint motion, collision, gravity stability, and task usability; for world models,
check control response, persistence, cross-view and physical consistency.

An accessible URL, HTML video tag, caption, or numerical success rate is not proof
of watching an output. Never invent observations or time ranges. If required media
cannot be inspected, preserve uncertainty. `not_applicable` requires score 0 and a
`not_applicable_reason`; it cannot exempt physical generation. `strong` requires
score 4-5, `adequate` score 3. Simplified but physically usable outputs can pass;
photorealism is not the only quality criterion.

## Material Increment over the Library

Every accepted review must record:

- `selection_basis`: `new_capability`, `substantial_improvement`,
  `reusable_infrastructure`, or `decisive_evaluation`.
- `acceptance_rationale`: why it deserves sustained reading rather than monitoring.
- `comparison_to_registry`: `closest_paper`, `material_difference`, `why_new_entry`.
  Name the closest maintained paper, or use `none` with an explained capability gap.

Explain the actual delta: a newly executable representation, important failure
mode resolved, substantial controlled improvement, reusable tool/data, or decisive
evaluation. Plausible relevance, a small fusion module, or a leaderboard gain alone
is insufficient. Check IDs, aliases, predecessors, and project versions. Revisions,
venue acceptances, code/checkpoint releases, and renamings normally update the
existing deep dive or record a no-op. Distinct papers in one family can qualify
separately when their contributions are materially different.

## Acceptance Rule

Accept if:

- source quality is primary or official,
- final impact score >= 4,
- final project relevance score >= 4,
- final evidence strength >= 4,
- a documented material increment and source-backed acceptance rationale,
- generation-heavy visual quality is `strong` or `adequate`, or visual quality is `not_applicable`,
- no unverified major claim is required for the summary or acceptance decision.

Full-coverage rule:

- Every candidate passing all v2 gates must have exactly one editor disposition: addition, update, or no-op. Updates/no-ops explain their reason and identify a real existing entry by `existing_paper_url`; an embedded replacement paper obeys all v2 gates.
- The workflow may not keep only a representative subset or a fixed top-k number per branch.
- Admission is controlled by all gates together: year, source, branch, technical contribution, direct relevance, material increment, evidence, and applicable visual quality.
- If the model cannot judge visual/demo quality, the candidate goes to `undecided/` with a detailed dossier instead of being silently dropped.

There is no fast-track that bypasses another gate. Zero additions is a valid result.
An unusually large batch triggers a second review of scores, duplication, and
material increment, rather than an arbitrary quota or omission of passing papers.

Watchlist if:

- relevant but incremental or below any of the three final-score thresholds,
- promising but insufficiently mature, or primary/release evidence is missing,
- the relationship to an existing paper needs clarification.

Keep a short reason and concrete `revisit_trigger` (what new evidence could change
the decision); ordinary watchlist entries do not need full deep dives. Revisit when
the trigger changes, not merely because a week has passed.

Reject if:

- year < 2024,
- source is only social/news,
- branch fit is unclear,
- method/task cannot be identified,
- generation-heavy visual results are weak,
- demo claims cannot be traced to a primary source,
- the paper is a generic VLM/LLM paper with no spatial, embodied, physical, interactive-generation, or action component.

Move to undecided if:

- visual evidence is insufficient or ambiguous,
- the model cannot confidently judge whether results are good enough,
- demos are inaccessible but the paper otherwise looks relevant,
- the acceptance decision depends on subjective visual quality.

For otherwise plausible admissions, visual uncertainty requires analyzed evidence,
`visual_quality_decision: undecided`, `needs_human_decision: true`, and a detailed
local-only dossier. Do not label these watchlist to avoid the dossier. A clearly
below-threshold incremental paper need not receive a dossier just because it has no video.

## Run Summary Must Include

- New accepted papers by branch.
- Links to deep dives for every accepted paper.
- Watchlist papers needing verification.
- Removed or demoted entries.
- Most useful demos when available; do not fill a top-3 quota.
- Undecided candidates requiring human visual judgment.
- Most relevant accepted papers when available; zero is valid.
- Collection notes for related-work, baseline usefulness, and evidence gaps to check before citing.
- Addition vs. update counts, watchlist promotion triggers, actual discovery coverage, and rationale for any unusually large batch.

Validation checks recorded gates and workflow consistency. It cannot establish
that an observation is honest or that a contribution is scientifically important.
