# Taxonomy & Editor

## Purpose

Assign branch fit, write the human-readable report, and assemble a complete registry patch from candidates that passed every selective acceptance gate.

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
- For runs from 2026-10-20, require `acceptance_policy_version: 2` and final impact/relevance/evidence scores each >= 4. Do not use priors or old 3/5 thresholds to override the final review. Existing library entries are preserved rather than retroactively deleted.
- Do not include candidates with `visual_quality_decision: "undecided"` or `needs_human_decision: true`.
- Write or update a complete top-level `paper_reads/<branch>/<slug>.md` deep dive for every registry addition.
- Add `deep_dive_path` to every `registry_additions` item and point it to that maintained report.
- Each deep dive must list original links and explain novelty, contributions, task, data, method, evidence, limitations, key figures/architecture, and project relevance.
- Account for every candidate that passed Quality Reviewer and all acceptance gates exactly once in `registry_additions`, `registry_updates` or `registry_noops`; do not choose only the most representative one or two papers.
- Check each accepted review's `selection_basis`, `acceptance_rationale` and `comparison_to_registry`. Create a new entry only for material new knowledge beyond the closest library work; release/evidence changes to an existing work belong in `registry_updates`, and already covered knowledge in `registry_noops`.
- Updates/no-ops identify a real registry entry with `existing_paper_url` and a specific `reason`; a no-op cannot carry a paper mutation. Replacement papers in updates obey the same v2 gates and score consistency as additions.
- Copy the active policy version, final three scores, `requires_visual_review` and `requires_temporal_demo` into each new registry paper as specified in [artifact contracts](../../harness/artifact_contracts.md).
- Zero additions is valid and should be reported plainly. If the batch is unusually large, request/repeat gate and deduplication review instead of filling a quota or cutting off qualified candidates.
- The `Key Figures / Architecture` section should link official figures/videos or include a redrawn method diagram. If no figure is appropriate, set `figure_status: not_applicable` or `figure_status: missing` and explain why.
- Keep top-level branches fixed to A-E.
- Any taxonomy change must use `status: "proposal_only"`.
- Every registry addition must include all required registry fields from `acceptance_harness.md`.
- The report must include accepted papers with deep-dive links, watchlist/rejected summary, undecided visual cases, top demos, collection notes, and validation status.
- Keep watchlist entries concise: explain missing upgrade evidence and `revisit_trigger`; do not require a long-term deep dive for every related paper. Otherwise-qualifying candidates with unresolved required visuals must have local-only undecided dossiers, not watchlist substitutes.
- Include actual query/source coverage and window/backfill status in the run summary; do not claim complete discovery merely because artifact validation passes.
- Run `scripts/validate_run.py YYYY-MM-DD` before any registry change is applied.
