# System Harness for Multi-Agent Runs

This harness validates the **multi-agent system execution**. It is separate from the paper acceptance harness.

- System harness: did the pipeline run correctly?
- Paper acceptance harness: is a paper good and relevant enough to collect?

## Run Unit

Each run has one run id:

```text
YYYY-MM-DD
```

All artifacts are stored under:

```text
reports/runs/YYYY-MM-DD/
```

## Required Stage Artifacts

| Stage | Agent | Artifact | Purpose |
|---:|---|---|---|
| 00 | Research Lead | `00_run_plan.json` | defines run id, branches, queries, search window |
| 01 | Discovery Agent | `01_discovery.json` | followed-source checks, candidates, and analyze/watchlist/reject triage |
| 02 | Evidence Analyst | `02_evidence.json` | paper cards plus demo/code/project verification |
| 03 | Quality Reviewer | `03_review.json` | visual inspection plus pass/revise/block review |
| 04 | Taxonomy & Editor | `04_editor_report.md` | final human-readable report |
| 05 | Taxonomy & Editor | `05_registry_patch.json`, `paper_reads/CAND-xxxx.md` | branch assignments, taxonomy proposals, registry patch draft, accepted-paper deep dives |
| manifest | Research Lead / Editor | `run_manifest.json` | records status and validation result |

## System Invariants

### 1. Stable candidate ids

- Every candidate id must match `CAND-0001`, `CAND-0002`, etc.
- Every later artifact must refer only to ids from `01_discovery.json`.
- Candidate ids cannot be reused for different titles in the same run.

### 2. Stage dependency

- Triage cannot reference unknown candidates.
- Paper cards can only reference candidates marked `analyze`.
- Demo cards can reference `analyze` or `watchlist`, but not `reject`.
- Visual cards can reference `analyze` or `watchlist`, but not `reject`.
- Quality review can reference any discovered candidate, including rejected candidates.
- Registry patch can include only candidates with `accepted_for_registry: true`.
- Every registry addition must have a corresponding `paper_reads/CAND-xxxx.md` deep dive.
- Discovery must record which fixed PI/lab/company sources were checked.
- Undecided dossiers are required for local publish validation but remain local-only unless explicitly approved.

### 3. Authority boundaries

- Research Lead cannot add candidates or registry entries.
- Discovery Agent can triage, but cannot write evidence cards or registry patches.
- Evidence Analyst can extract paper/demo evidence, but cannot accept papers.
- Quality Reviewer can pass/block candidates, but cannot write registry patches.
- Taxonomy & Editor cannot override blocked, rejected, watchlist-only, or undecided visual cases.

The harness checks these boundaries through artifact shape and cross-file references.

### 4. Taxonomy safety

- Top-level branches are fixed to `A`, `B`, `C`, `D`, `E`.
- Taxonomy changes must appear only in `taxonomy_change_proposals`.
- Every proposal must have `status: "proposal_only"`.
- A new top-level branch proposal cannot be applied by the weekly run.

### 5. Registry safety

- `05_registry_patch.json` is a patch draft, not the registry itself.
- Rejected, blocked, or watchlist-only candidates cannot appear in `registry_additions`.
- Candidates with `visual_quality_decision: "undecided"` or `needs_human_decision: true` cannot appear in `registry_additions`.
- Registry additions must have `year >= 2024`.
- Registry additions must include the required registry fields.
- Registry additions must include a per-paper deep dive with source links, novelty, contributions, task, data, method, key figures/architecture, evidence, limitations, and project relevance.
- Actual registry changes must pass `scripts/validate_registry.py`.

### 6. Report safety

The final report must include:

- accepted candidates,
- rejected/watchlist summary,
- undecided candidates requiring human decision,
- top demos,
- collection notes for related-work / baseline usefulness,
- validation status.

## Pass / Fail

A run passes if:

- all required artifacts exist,
- all JSON artifacts parse,
- all run ids match,
- `00_run_plan.json` declares `minimum_year: 2024`,
- `00_run_plan.json` points to `data/follow_sources.seed.json`,
- `01_discovery.json` includes `followed_sources_checked`,
- all cross-file references are valid,
- no rejected or blocked candidate appears in the registry patch,
- no undecided visual-quality candidate appears in the registry patch,
- publish-time validation can require local undecided dossiers without uploading them,
- taxonomy changes are proposal-only,
- report and manifest exist,
- every registry addition has a complete deep-dive Markdown file,
- registry patch is structurally valid.

A run fails if any invariant is violated.

## Validation Command

```bash
python frontier_research/scripts/validate_run.py YYYY-MM-DD
```

This command validates the run structure. It does not judge whether a paper is scientifically important.
