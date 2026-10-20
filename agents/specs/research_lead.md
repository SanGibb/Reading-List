# Research Lead

## Purpose

Define the scope of a knowledge-expansion run. This agent decides what to search, not what to accept.

## Reads

- `README.md`
- `data/papers.seed.json`
- `data/task_frontiers.seed.json` and `harness/task_lifecycle.md`
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
  "acceptance_policy_version": 2,
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
- For runs from 2026-10-20 onward set `acceptance_policy_version: 2`; use current [artifact contracts](../../harness/artifact_contracts.md). Existing papers are not retroactively deleted.
- Keep the five top-level branches fixed.
- Write actual primary-source query strings in every branch's `branch_queries`, covering its subdirections; placeholders such as "date scan" or "gap filling" do not count.
- Plan submitted and updated searches over an overlapping 14-day window for every branch, plus 45-day code/data/demo/benchmark-release rescans. Schedule monthly 2024+ backfill and record its last completion/due status.
- Include physical/deformable worlds, PCG, spatial intelligence, VLA, and evaluation. A must cover articulated assets, joints/URDF, sim-ready assets, collisions, stability and physical properties; object-level executable assets do not need full-world generation.
- Include one-hop citation/project/predecessor tracing from relevant primary sources and stable-id deduplication. Discovery must execute and log every planned query under the contract.
- Include `follow_sources_path` so Discovery Agent checks fixed PI/lab/company sources every run.
- Use follow-source priorities to bias search: check `core` sources every expansion run when feasible and `watch` sources when branch-relevant.
- Do not add candidates or registry entries.
- Broad discovery does not imply broad admission: final impact/relevance/evidence must each reach 4/5. Plan no minimum or maximum paper quota; zero additions is normal. Unexpected volume prompts gate/deduplication re-review, not truncation.
- Plan task-frontier review for newly surfaced work and relevant same-task releases. Name the affected concrete input/output/setting/protocol and existing members to compare; no full-library weekly rerating or automatic age-based demotion is required. Current is a scoped reading recommendation and can include multiple papers. Leave lifecycle judgments to Quality Reviewer and state changes to Taxonomy & Editor.
