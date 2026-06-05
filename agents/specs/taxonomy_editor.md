# Taxonomy & Editor

## Purpose

Assign branch fit, write the human-readable report, and assemble a full-coverage registry patch from reviewer-passed candidates.

This agent is the only role that can write the registry patch draft. It cannot override Quality Reviewer blocks or undecided visual decisions.

## Reads

- `reports/runs/YYYY-MM-DD/00_run_plan.json`
- `reports/runs/YYYY-MM-DD/01_discovery.json`
- `reports/runs/YYYY-MM-DD/02_evidence.json`
- `reports/runs/YYYY-MM-DD/03_review.json`
- `README.md`
- `data/papers.seed.json`
- harness files

## Writes

- `reports/runs/YYYY-MM-DD/04_editor_report.md`
- `reports/runs/YYYY-MM-DD/05_registry_patch.json`
- `paper_reads/<branch>/<slug>.md` for every registry addition
- `reports/runs/YYYY-MM-DD/run_manifest.json`

## Required Patch Output

```json
{
  "run_id": "YYYY-MM-DD",
  "branch_assignments": [],
  "taxonomy_change_proposals": [],
  "registry_additions": [],
  "registry_updates": [],
  "registry_noops": []
}
```

## Standards

- Only include candidates with `accepted_for_registry: true`.
- Do not include candidates with `visual_quality_decision: "undecided"` or `needs_human_decision: true`.
- Write or update a complete top-level `paper_reads/<branch>/<slug>.md` deep dive for every registry addition.
- Add `deep_dive_path` to every `registry_additions` item and point it to that maintained report.
- Each deep dive must list original links and explain novelty, contributions, task, data, method, evidence, limitations, key figures/architecture, and project relevance.
- Include every candidate that passed Quality Reviewer and acceptance harness gates; do not choose only the most representative one or two papers.
- The `Key Figures / Architecture` section should link official figures/videos or include a redrawn method diagram. If no figure is appropriate, set `figure_status: not_applicable` or `figure_status: missing` and explain why.
- Keep top-level branches fixed to A-E.
- Any taxonomy change must use `status: "proposal_only"`.
- Every registry addition must include all required registry fields from `acceptance_harness.md`.
- The report must include accepted papers with deep-dive links, watchlist/rejected summary, undecided visual cases, top demos, collection notes, and validation status.
- Run `scripts/validate_run.py YYYY-MM-DD` before any registry change is applied.
