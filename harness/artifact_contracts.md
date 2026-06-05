# Artifact Contracts

This file summarizes the JSON contracts used by the system harness.

## Common Rules

- Every JSON artifact must include `run_id`.
- Candidate ids must be stable and match `CAND-0001`.
- Branch ids must be one of `A`, `B`, `C`, `D`, `E`.
- Scores must be integers from 0 to 5.
- Accepted paper cards and registry additions must have `year >= 2024`.
- Unknown or missing evidence should be explicit, not silently omitted.

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

### `paper_reads/CAND-xxxx.md`

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
