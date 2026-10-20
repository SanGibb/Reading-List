# Artifact Contracts

This file summarizes the JSON contracts used by the system harness.

## Common Rules

- Every JSON artifact must include `run_id`.
- Candidate ids must be stable and match `CAND-0001`.
- Branch ids must be one of `A`, `B`, `C`, `D`, `E`.
- Scores must be integers from 0 to 5.
- Accepted paper cards and registry additions must have `year >= 2024`.
- Unknown or missing evidence should be explicit, not silently omitted.

## V2 extension (effective 2026-10-20)

New runs must declare `00_run_plan.json.acceptance_policy_version: 2`; omitting the
version does not grandfather a new run. Historical runs keep their original format.
The contracts below remain the baseline, with the following mandatory v2 fields.

### Discovery coverage

`00_run_plan.json.branch_queries` maps A-E to lists of **actual query strings**.
`01_discovery.json.query_log` records their execution, not an inferred search plan:

```json
{
  "query_id": "Q-A-001",
  "branch": "A",
  "query": "articulated sim-ready assets joint collision physics",
  "source_url": "https://export.arxiv.org/api/query",
  "executed_at": "2026-10-26T00:05:00+08:00",
  "date_basis": "submitted",
  "date_from": "2026-10-13",
  "date_to": "2026-10-26",
  "results_reviewed": 40,
  "pages_checked": 2,
  "stop_reason": "All results in the requested window were reviewed.",
  "candidate_ids": ["CAND-0001"]
}
```

- `date_basis`: `submitted|updated|release|backfill|citation`. Every branch must log
  submitted and updated searches covering >=14 calendar days, plus release searches
  covering >=45 calendar days. These windows end on the run date or previous day;
  execution timestamps are within one calendar day of the run, allowing timezone
  differences and midnight crossings. Periodically backfill 2024+ work as specified
  in the workflow; stale queries cannot stand in for the current weekly sweep.
- `pages_checked` is an integer >=1; `results_reviewed` an integer >=0. Record actual
  pagination and stopping reason, including tool/result limits and incomplete coverage.
- Every planned query has an executed log. Each candidate has `query_id`; the
  referenced log contains that candidate in `candidate_ids`.
- Every core follow-source ID is recorded. Actually visited sources need `checked_at`
  (timezone-aware timestamp) and `urls_checked`; `checked|spot_checked` also needs
  `evidence_url`. Core `skipped|unreachable` needs a concrete `retry_trigger` plus
  `notes`. Do not turn a blocked URL into `checked` just by copying its address.
- The canonical `follow_sources_path` is `data/follow_sources.seed.json` and
  `known_registry_path` is `data/papers.seed.json`; a plan cannot substitute an empty
  or unrelated file to disable coverage requirements.
- Watchlist triage needs `revisit_trigger`: what evidence/release would change the
  decision. A short record suffices; ordinary watchlist papers need no full dossier.

### Final selection and inspection

Every accepted `quality_review` includes final integer `impact_score`,
`project_relevance_score`, `evidence_strength` (each >=4), `acceptance_rationale`,
`selection_basis` (`new_capability|substantial_improvement|reusable_infrastructure|decisive_evaluation`),
and `comparison_to_registry` with non-empty `closest_paper`, `material_difference`,
`why_new_entry`. Discovery priors do not substitute for final scores.

Each analyzed `paper_card` states boolean `requires_visual_review` and
`requires_temporal_demo`. At least one collection-critical `claim_checks` entry must
be verified with a primary/official source URL for acceptance. Partial/unverified
caveats must set `used_for_acceptance: false`.

Required visual inspection adds `visual_card.inspection_evidence`:

```json
{
  "url": "https://official-project.example/demos/articulation.mp4",
  "modality": "video",
  "locator": "00:10-00:24, cabinet opening and closing",
  "observation": "Door remains attached and clears the frame through its motion range.",
  "limitations": "One displayed example; long-tail collision behavior is not established."
}
```

`modality` is `video|gif|interactive_demo|paper_figure|image`. Required temporal review
needs at least one of the first three. These must be real observations: substitute
the actual URL/time/figure and observed behavior, never copy example evidence into a
run. `not_applicable` needs `not_applicable_reason` and visual score 0; `strong` uses
4-5 and `adequate` 3. Undecided candidates are analyzed, set
`needs_human_decision: true`, have a local-only dossier, and cannot be accepted.

### Editor and registry

The accepted candidate set equals the union of candidate IDs in `registry_additions`,
`registry_updates`, and `registry_noops`, with exactly one disposition per candidate.
Updates/no-ops include a non-empty `reason` and `existing_paper_url` pointing to a
real entry in the canonical registry. A no-op carries no `paper` mutation. If an
update includes a replacement `paper`, it must satisfy v2 gates and match the final
review just like an addition. New papers copy `acceptance_policy_version: 2`,
final `impact_score`, `project_relevance_score`, `evidence_strength`, both visual
requirement booleans, and existing visual score/decision fields. Numeric values must
match the review. The ordinary registry fields and full deep dive are still required.
Empty addition sets are valid after real discovery has been performed.

## Stage Files

### `00_run_plan.json`

Required:

- `run_id`
- `created_at`
- `branches`
- `minimum_year`: must be `2024`
- `branch_queries`
- `known_registry_path`
- `follow_sources_path`
- `harness_paths`

### `01_discovery.json`

Required:

- `run_id`
- `followed_sources_checked`
- `candidates`
- `triage`

Each followed source check:

- `source_id`
- `status`: `checked`, `spot_checked`, `unreachable`, or `skipped`
- `notes`
- `urls_checked`

Each candidate:

- `candidate_id`
- `title`
- `branch_hint`
- `source_url`
- `source_type`
- `discovered_from`
- `why_candidate`

Each triage item:

- `candidate_id`
- `decision`: `analyze`, `watchlist`, or `reject`
- `primary_branch`
- `reason`
- `dedupe_status`
- `source_quality`
- `impact_prior`
- `project_relevance_prior`

### `02_evidence.json`

Required:

- `run_id`
- `paper_cards`
- `demo_cards`

Each paper card:

- `candidate_id`
- `title`
- `year`
- `venue`
- `url`
- `paper_ids` when available: `arxiv`, `doi`, `openreview`, `project`, `github`
- `primary_branch`
- `secondary_branches`
- `data`
- `method`
- `task`
- `novelty`
- `evidence`
- `claim_checks` for central source-traced claims when available
- `limitations`
- `project_relevance`

`claim_checks` is a collection-quality aid, not an autonomous research step. Use it for claims that affect acceptance: dataset scale, benchmark result, model/checkpoint availability, demo quality, source status, and public code.

Each demo card:

- `candidate_id`
- `demo_score`
- `verification_status`
- `demo_notes`

### `03_review.json`

Required:

- `run_id`
- `visual_cards`
- `quality_review`
- `run_level_issues`

Each visual card:

- `candidate_id`
- `visual_materials`
- `inspected_modalities`
- `visual_quality_score`
- `visual_quality_decision`: `strong`, `adequate`, `weak`, `undecided`, or `not_applicable`
- `visual_notes`
- `failure_modes`
- `needs_human_decision`
- `undecided_reason`

Each quality review item:

- `candidate_id`
- `review_decision`: `pass`, `needs_revision`, or `block`
- `issues`
- `required_fixes`
- `accepted_for_registry`

### `05_registry_patch.json`

Required:

- `run_id`
- `branch_assignments`
- `taxonomy_change_proposals`
- `registry_additions`
- `registry_updates`
- `registry_noops`

Each `registry_additions` item must include:

- `candidate_id`
- `branch`
- `deep_dive_path`: `paper_reads/<branch>/<slug>.md`
- `paper`

### `paper_reads/<branch>/<slug>.md`

Required for every candidate in `registry_additions`.

Each deep dive must include:

- original paper/source links,
- one-paragraph TL;DR,
- novelty,
- contributions,
- task definition,
- data / dataset / benchmark,
- method / pipeline,
- evidence trail for central claims,
- key figures or architecture section,
- evidence / metrics / qualitative results,
- limitations,
- project relevance,
- reproduction or follow-up notes.

The `Key Figures / Architecture` section must include `figure_status:` with one of:

- `linked_official`: official figure/demo links are provided,
- `captured_official`: local screenshot or image captured from official page,
- `redrawn`: architecture was redrawn by us,
- `not_applicable`: benchmark/data paper where architecture diagram is not central,
- `missing`: figure evidence unavailable; explain why.

### `undecided/YYYY-MM-DD/CAND-xxxx.md`

Local-only by default. Required during publish-time local validation for every candidate with `visual_quality_decision: "undecided"` or `needs_human_decision: true`.

Each dossier should use the same analytical standard as a deep dive, plus a clear human decision request:

- source links,
- TL;DR,
- novelty,
- contributions,
- task,
- data,
- method,
- visual/demo evidence inspected,
- evidence trail,
- key figures / architecture with `figure_status`,
- limitations,
- why the candidate is undecided,
- accept / reject / keep-watching options.
