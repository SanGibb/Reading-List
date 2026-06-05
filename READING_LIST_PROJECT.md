# Reading List Project Notes

This file documents the repository project itself: what belongs in this reading-list repo, what should stay local, and how to publish it cleanly.

## Project Identity

Repository name suggestion:

```text
interactive-embodied-generation-frontier
```

This is a curated research reading-list and workflow repository for:

- interactive generation and PCG,
- embodied AI,
- spatial intelligence,
- VLA and world-action models,
- executable physical worlds,
- physical / deformable / simulation-ready assets,
- benchmarks and data infrastructure.

It is not named after a single internal task. Specific tasks can be discussed inside reports and paper deep dives, but the repository should remain field-level.

## Repository Boundary

The standalone GitHub repository should use `frontier_research/` as its root.

Include:

- `README.md`
- `READING_LIST_PROJECT.md`
- `data/papers.seed.json`
- `data/follow_sources.seed.json`
- `data/follow_sources.md`
- `agents/`
- `automation/`
- `harness/`
- `reports/`
- `scripts/`
- `undecided/`
- `.github/workflows/validate.yml`
- `.githooks/`
- `.gitignore`

Do not include:

- local downloaded PDFs,
- screenshots generated during ad hoc exploration,
- Keynote / PowerPoint / local notes,
- browser caches,
- `.DS_Store`,
- Python caches,
- unrelated outer-folder materials such as old guides unless explicitly migrated.

## Core Artifacts

| Artifact | Purpose |
|---|---|
| `data/papers.seed.json` | Curated 2024+ paper registry. |
| `data/follow_sources.seed.json` | Fixed PI/lab/company sources for Discovery Agent. |
| `reports/runs/YYYY-MM-DD/` | Auditable multi-agent run artifacts. |
| `reports/runs/YYYY-MM-DD/paper_reads/` | Mandatory deep dives for accepted registry additions. |
| `undecided/YYYY-MM-DD/` | Human-decision dossiers for papers whose visual/demo quality is uncertain. |
| `harness/acceptance_harness.md` | Paper quality and relevance criteria. |
| `harness/system_harness.md` | Workflow execution rules. |
| `scripts/validate_all.py` | Main local/CI validation entry point. |

## Publishing Checklist

From the standalone project root:

```bash
REQUIRE_UNDECIDED_DOSSIERS=1 python scripts/validate_all.py
git init
git config core.hooksPath .githooks
git add .
git commit -m "Initial frontier reading list workflow"
git branch -M main
git remote add origin <new-github-repo-url>
git push -u origin main
```

If working from the outer `cvpr` folder, either copy only `frontier_research/` into a fresh clone of the GitHub repo, or initialize Git inside `frontier_research/` directly.

## Hook Policy

Hooks are for mechanical checks only:

- JSON parses,
- registry schema is valid,
- no pre-2024 registry papers,
- completed runs validate,
- accepted registry additions have deep-dive Markdown files,
- follow-source checks reference known source ids.
- undecided dossiers exist locally before publishing, but are not pushed automatically.

Hooks should not decide whether a paper is impressive, novel, or worth following. That remains the job of Quality Reviewer plus human review.

## Maintenance Rhythm

Weekly:

- run the scheduled scan,
- inspect accepted / watchlist / undecided items,
- approve or reject undecided visual-quality dossiers,
- keep registry updates conservative.
- run `python scripts/publish_validated_update.py --message "Weekly frontier scan YYYY-MM-DD"` to validate, commit, and push publishable changes.

Monthly:

- review `data/follow_sources.seed.json`,
- promote or demote follow sources,
- prune stale watch sources,
- check whether taxonomy branches remain narrow.

Before writing related work:

- run a manual deep-update scan,
- review top demos,
- read paper deep dives under `reports/runs/*/paper_reads/`,
- export the relevant branch subset from `data/papers.seed.json`.
