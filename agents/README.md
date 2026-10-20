# Agents Overview

This folder defines the consolidated, file-driven workflow for the 2024+ frontier research repository.

The system now uses **five agents**. Each agent owns a larger but still coherent chunk of work, so the workflow stays auditable without excessive handoff overhead.

From 2026-10-20, runs use `acceptance_policy_version: 2`: discover broadly, admit selectively. All final impact/relevance/evidence scores must reach 4/5 together. No additions is a valid weekly outcome; there is no count quota or top-k cutoff. Existing entries are preserved rather than retroactively deleted.

## Execution Order

| Stage | Agent | Reads | Writes | Core decision |
|---:|---|---|---|---|
| 00 | Research Lead | taxonomy, registry, harness | `00_run_plan.json` | run scope |
| 01 | Discovery Agent | run plan, registry, web sources | `01_discovery.json` | candidate triage |
| 02 | Evidence Analyst | discovery artifact, primary sources | `02_evidence.json` | evidence extraction |
| 03 | Quality Reviewer | discovery/evidence artifacts, demos, visual evidence | `03_review.json` | pass / revise / block |
| 04/05 | Taxonomy & Editor | all reviewed artifacts | `04_editor_report.md`, `05_registry_patch.json`, `paper_reads/<branch>/<slug>.md` | maintained deep dives, report, and patch assembly |

## Non-Negotiable Rules

- The repository is 2024+ only.
- Agents pass files; they do not freely chat.
- Each agent writes only its assigned artifact.
- Discovery may triage candidates, but it cannot write paper summaries or registry patches.
- Evidence Analyst extracts paper/demo evidence, but it cannot accept papers.
- Quality Reviewer inspects source quality, demos, and visual/generation results. Weak or undecidable visual cases cannot enter the registry.
- A new entry must have a substantive technical increment beyond the closest registry paper, concrete project use as an interface/validator/direct baseline, and strong primary-source evidence. Citation counts or popularity do not substitute for these gates.
- Quality Reviewer records final scores, `selection_basis`, `acceptance_rationale`, and `comparison_to_registry`; exact fields are in [artifact contracts](../harness/artifact_contracts.md).
- Taxonomy & Editor can assemble taxonomy assignments and registry patch drafts, but only from reviewer-passed candidates.
- Every accepted candidate must appear in additions, updates or noops. Related work below the gates belongs in a concise watchlist with missing upgrade evidence and `revisit_trigger`; watchlist does not require a full deep dive.
- Every registry addition must set `deep_dive_path` and point to a complete top-level `paper_reads/<branch>/<slug>.md` report.
- Otherwise qualifying candidates with uncertain required visuals go to local-only `undecided/YYYY-MM-DD/` dossiers for human decision; they cannot be diverted to watchlist to bypass inspection.
- Actual inspected media must be distinguished from page links, with figure/page or time-range locators and observations. Motion-dependent claims require actual video, GIF or interactive-demo evidence.
- Discovery preserves broad coverage with actual subdirection queries, 14-day submitted/updated overlap, 45-day release rescans, monthly 2024+ backfill, and one-hop citation tracing. Query logs and timed fixed-source checks must support the coverage claims.
- A includes object-level articulated/physical sim-ready assets; complete world generation is not required.
- `validate_run.py` must pass before any registry update.

## Local Commands

Create a run scaffold:

```bash
python frontier_research/scripts/scaffold_run.py YYYY-MM-DD
```

Validate a completed run:

```bash
python frontier_research/scripts/validate_run.py YYYY-MM-DD
```

Validate the registry:

```bash
python frontier_research/scripts/validate_registry.py
```

## Detailed Specs

- [Research Lead](specs/research_lead.md)
- [Discovery Agent](specs/discovery_agent.md)
- [Evidence Analyst](specs/evidence_analyst.md)
- [Quality Reviewer](specs/quality_reviewer.md)
- [Taxonomy & Editor](specs/taxonomy_editor.md)
