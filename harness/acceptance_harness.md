# Acceptance Harness

This harness defines when a paper may enter the repository.

The repository optimizes for **research quality and visible usefulness**, not publication status alone. A recent arXiv paper with excellent demos can be accepted; a peer-reviewed paper with weak or unconvincing generated results can be rejected or sent to human decision.

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

- 5: field-shaping system, strong benchmark, large data release, or widely used open model.
- 4: clear frontier method with strong experiments or public release.
- 3: solid paper with useful project relevance.
- 2: narrow or incremental but relevant.
- 1: weak relevance.
- 0: reject.

## Project Relevance Score

Score from 0 to 5:

- 5: directly provides target-task fields, compiler targets, validators, or benchmark tasks.
- 4: directly conditions/evaluates interactive generation or embodied policies.
- 3: supports one target-task layer such as spatial reasoning, physical properties, or trajectories.
- 2: background only.
- 1: tangential.
- 0: reject.

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

## Acceptance Rule

Accept if:

- source quality is primary or official,
- impact score >= 3,
- project relevance score >= 3,
- generation-heavy visual quality is `strong` or `adequate`, or visual quality is `not_applicable`,
- no unverified major claim is required for the summary or acceptance decision.

Full-coverage rule:

- A run must add every discovered candidate that satisfies the acceptance rule.
- The workflow may not keep only a representative subset or a fixed top-k number per branch.
- Breadth is controlled by the gates above: year, primary source, branch fit, project relevance, evidence strength, and visual/demo quality.
- If the model cannot judge visual/demo quality, the candidate goes to `undecided/` with a detailed dossier instead of being silently dropped.

Fast-track if:

- impact score >= 4 and project relevance score >= 4.

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

## Run Summary Must Include

- New accepted papers by branch.
- Links to deep dives for every accepted paper.
- Watchlist papers needing verification.
- Removed or demoted entries.
- Top 3 demos.
- Undecided candidates requiring human visual judgment.
- Top 3 papers most relevant to this repository.
- Collection notes for related-work, baseline usefulness, and evidence gaps to check before citing.
