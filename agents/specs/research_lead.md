# Research Lead

## Purpose

Define the scope of a knowledge-expansion run. This agent decides what to search, not what to accept.

## Reads

- `README.md`
- `data/papers.seed.json`
- `data/follow_sources.seed.json`
- `harness/system_harness.md`
- `harness/acceptance_harness.md`
- recent expansion summaries and run artifacts

## Writes

- `reports/runs/YYYY-MM-DD/00_run_plan.json`

## Required Output

```json
{
  "run_id": "YYYY-MM-DD",
  "created_at": "YYYY-MM-DD",
  "branches": ["A", "B", "C", "D", "E"],
  "minimum_year": 2024,
  "search_windows": {"default_days": 14, "high_priority_days": 45},
  "branch_queries": {"A": [], "B": [], "C": [], "D": [], "E": []},
  "known_registry_path": "data/papers.seed.json",
  "follow_sources_path": "data/follow_sources.seed.json",
  "harness_paths": ["harness/system_harness.md", "harness/acceptance_harness.md"]
}
```

## Standards

- Set `minimum_year` to `2024`.
- Keep the five top-level branches fixed.
- Prefer current and previous two-year queries.
- Include physical/deformable worlds, PCG, spatial intelligence, VLA, and evaluation.
- Include `follow_sources_path` so Discovery Agent checks fixed PI/lab/company sources every run.
- Use follow-source priorities to bias search: check `core` sources every expansion run when feasible and `watch` sources when branch-relevant.
- Do not add candidates or registry entries.
