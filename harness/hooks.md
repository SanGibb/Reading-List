# Hooks

Hooks are mechanical guardrails for this repository. They should block broken files, not make research taste decisions.

For this literature workflow, hooks are useful as guardrails, but the core quality control should be:

1. a narrow taxonomy,
2. a strict acceptance harness,
3. registry validation,
4. weekly human-readable reports,
5. source-linked claims.

## What Hooks Can Do

Hooks can automatically block low-quality changes before they enter the repo.

Useful hook checks:

- JSON registry is valid.
- Completed multi-agent run artifacts are valid.
- Required fields are present.
- Local PDF paths exist when specified.
- URLs look valid.
- No duplicate paper titles.
- Weekly report exists for automated registry updates.

## What Hooks Cannot Do Reliably

Hooks cannot judge:

- whether a paper is truly influential,
- whether a demo is impressive,
- whether a method is actually novel,
- whether a benchmark comparison is fair,
- whether a paper belongs in this repository.

Those require the harness and review agent.

## Recommended Hook Strategy

### Local hooks

Enable hooks from the project root:

```bash
git config core.hooksPath .githooks
```

If you are working from the outer `cvpr` directory instead of the standalone project root, use:

```bash
git config core.hooksPath frontier_research/.githooks
```

The hook runs:

```bash
python scripts/validate_all.py
```

That entry point validates:

- `data/papers.seed.json`
- `data/follow_sources.seed.json`
- the current registry schema
- every completed run under `reports/runs/*`
- accepted-paper deep dives required by registry patches

For publish-time local validation, the publisher sets:

```bash
REQUIRE_UNDECIDED_DOSSIERS=1
```

This means undecided dossiers must exist locally, but `.gitignore` keeps them out of the automatic commit.

### GitHub Actions

The standalone project includes:

```text
.github/workflows/validate.yml
```

It runs `python scripts/validate_all.py` on push and pull request.

## Practical Recommendation

Use hooks only for mechanical checks. Do not encode research judgment into hooks.

The right division is:

- **hooks/scripts**: schema, links, duplicates, required fields, run artifact consistency, required deep dives, local-only undecided dossier checks.
- **agents**: search, summarize, source checking, demo extraction.
- **human/Codex review**: impact, novelty, project relevance, taxonomy changes.
