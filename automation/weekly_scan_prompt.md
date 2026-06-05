# Weekly Frontier Scan Prompt

You are maintaining the interactive embodied generation frontier research repository in `frontier_research`.

Scope:

- This is a frontier paper-collection run, not an autonomous scientist run.
- Do not generate research hypotheses, experiment roadmaps, or new project directions as primary outputs.
- Borrow only the useful agent/skill practices for collection quality: narrow role contracts, primary-source tracing, claim checks, deduplication, and explicit uncertainty handling.

Task:

1. Read `README.md`, `data/papers.seed.json`, `data/follow_sources.seed.json`, `agents/multiagent_design.md`, `harness/system_harness.md`, `harness/artifact_contracts.md`, and `harness/acceptance_harness.md`.
2. Create or reuse a run directory under `reports/runs/YYYY-MM-DD/`.
3. Execute the consolidated file-driven multi-agent pipeline by writing the required stage artifacts:
   - `00_run_plan.json`
   - `01_discovery.json`
   - `02_evidence.json`
   - `03_review.json`
   - `04_editor_report.md`
   - `05_registry_patch.json`
   - `run_manifest.json`
4. Search the web for new or newly influential **2024+** papers, project pages, code releases, datasets, demos, and benchmarks in these branches:
   - Executable World Representation
   - Interactive Generation and PCG
   - Spatial Intelligence
   - VLA and World-Action Models
   - Evaluation and Data Infrastructure
5. Use primary sources first: arXiv, OpenReview, CVF, PMLR, official project pages, official GitHub repositories, benchmark leaderboards.
   - Do not collect papers with `year < 2024`.
   - Prefer papers/releases from the current and previous two years.
   - If a result is a classic pre-2024 foundation paper, mention it only as background if needed; do not add it to the registry or registry patch.
6. Before broad keyword search, check fixed follow sources in `data/follow_sources.seed.json`.
   - Check all `priority: core` source groups every scheduled scan when feasible.
   - Check `priority: watch` source groups when relevant to the current branch scope or when recent signals appear.
   - Record checked, skipped, and unreachable sources in `01_discovery.json` under `followed_sources_checked`.
   - Follow-source hits are discovery signals only; they still need the normal 2024+, source, relevance, visual, and evidence gates.
7. Run the five roles:
   - Research Lead: write `00_run_plan.json`.
   - Discovery Agent: search, deduplicate, and triage into `01_discovery.json`.
   - Evidence Analyst: extract paper/demo evidence into `02_evidence.json`.
   - Quality Reviewer: inspect source quality, demos, and visual/generation results into `03_review.json`.
   - Taxonomy & Editor: write `04_editor_report.md`, `05_registry_patch.json`, accepted-paper deep dives under `paper_reads/CAND-xxxx.md`, and `run_manifest.json`.
8. For each analyzed candidate, extract:
   - title
   - authors when available
   - date / venue
   - source URL
   - stable paper identifiers when available: arXiv id, DOI, OpenReview id, project URL, official GitHub URL
   - code/project/demo links
   - data / dataset
   - core method
   - task
   - novelty
   - reported evidence or benchmark result
   - source trace for central claims, especially SOTA, dataset scale, public model/checkpoint availability, and demo claims
   - demo quality
   - visual/generation quality when applicable
   - why it matters for this repository
9. Use Quality Reviewer to inspect project pages, figures, videos, GIFs, screenshots, robot demos, and generated samples. Do not rely on venue alone.
10. If visual quality cannot be judged confidently, write a local dossier under `undecided/YYYY-MM-DD/CAND-xxxx.md` and do not add that candidate to the registry patch.
    - This dossier must still be a real paper/deep-dive analysis with source links, novelty, contributions, task, data, method, visual evidence, limitations, and the specific human decision needed.
    - Undecided dossiers are local-only by default. Do not commit or push them unless the human explicitly approves that candidate later.
11. For every candidate in `registry_additions`, write `reports/runs/YYYY-MM-DD/paper_reads/CAND-xxxx.md`.
    - Include original paper/project/code/demo links.
    - Explain novelty, contributions, task, data, method, evidence, limitations, and project relevance.
    - Include a short evidence trail that maps central claims to paper/project/code/demo sources.
    - Include `Key Figures / Architecture` with `figure_status: linked_official|captured_official|redrawn|not_applicable|missing`.
    - Prefer official project figures/videos. If useful, redraw the method architecture in our own style rather than copying a copyrighted paper figure.
    - If no figure is available or appropriate, explicitly set `figure_status: missing` or `figure_status: not_applicable` and explain why.
12. Apply `harness/acceptance_harness.md` for paper relevance and `harness/system_harness.md` for workflow validity.
13. Write a weekly markdown report under `reports/YYYY-MM-DD-weekly.md` only after the system run validates.
14. If there are strong accepted papers, update `data/papers.seed.json` conservatively.
15. Run local validation:

```bash
REQUIRE_UNDECIDED_DOSSIERS=1 python scripts/validate_all.py
```

16. If validation passes, publish all non-undecided changes in one step:

```bash
python scripts/publish_validated_update.py --message "Weekly frontier scan YYYY-MM-DD"
```

This script validates, stages publishable files, commits, and pushes to GitHub. It leaves `undecided/**` unstaged except for `undecided/README.md`.

17. Do not add social-media-only claims to the registry. Put them in a watchlist section of the report.

Output expectations:

- concise but source-linked report
- accepted papers grouped by the five branches
- followed-source coverage summary
- deep-dive link for every accepted paper
- top demos and why they matter
- undecided candidates requiring human visual judgment
- local-only undecided deep dives generated but not pushed
- brief collection notes for baseline / related-work usefulness
- validation summary showing the system harness and registry validation passed
