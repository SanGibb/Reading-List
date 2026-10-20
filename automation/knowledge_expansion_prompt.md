# Frontier Knowledge Expansion Prompt

You are maintaining the interactive embodied generation frontier research repository in `frontier_research`.

Scope:

- This is a frontier paper-collection run, not an autonomous scientist run.
- Use acceptance policy version 2 for runs dated 2026-10-20 or later (`acceptance_policy_version: 2`), following `harness/artifact_contracts.md` for exact fields. Preserve existing registry entries; do not retroactively delete papers under the new policy.
- Discover broadly and admit selectively. Zero additions is a valid outcome; do not add papers to fill a weekly quota. Unexpectedly high additions trigger a second gate/deduplication review, not an arbitrary count cutoff.
- Do not generate research hypotheses, experiment roadmaps, or new project directions as primary outputs.
- Borrow only the useful agent/skill practices for collection quality: narrow role contracts, primary-source tracing, claim checks, deduplication, and explicit uncertainty handling.

Task:

1. Read `README.md`, this prompt, `data/papers.seed.json`, `data/task_frontiers.seed.json`, `data/follow_sources.seed.json`, `agents/multiagent_design.md`, all role specs in `agents/specs/`, `harness/system_harness.md`, `harness/artifact_contracts.md`, `harness/acceptance_harness.md`, `harness/task_lifecycle.md`, and `reports/paper_deep_dive_template.md`.
2. Create or reuse a run directory under `reports/runs/YYYY-MM-DD/`.
3. Execute the consolidated file-driven multi-agent pipeline by writing the required stage artifacts:
   - `00_run_plan.json`
   - `01_discovery.json`
   - `02_evidence.json`
   - `03_review.json`
   - `04_editor_report.md`
   - `05_registry_patch.json`
   - `run_manifest.json`
4. Search the web for new or newly influential **2024+** papers, project pages, code releases, datasets, demos, and benchmarks that may expand the knowledge base in these branches:
   - Executable World Representation
   - Interactive Generation and PCG
   - Spatial Intelligence
   - VLA and World-Action Models
   - Evaluation and Data Infrastructure
   - Record actual queries for each branch's subdirections rather than labels such as "date scan" or "gap filling". A must include articulated assets, joints/URDF, sim-ready assets, physical properties, and collision/stability. Object-level executable assets belong in A; full-world generation is not a requirement.
   - Use an overlapping 14-day window for both first submissions and updated papers, a 45-day rescan for code/data/demo/benchmark releases, and a monthly 2024+ retrospective. Record the retrospective's last completion and whether it is due.
   - Keep query ids, result counts, pagination and stopping reasons in discovery audit records, and connect every candidate to a query id. Follow one citation/project/predecessor link hop from relevant primary sources and deduplicate by stable identifiers.
5. Use primary sources first: arXiv, OpenReview, CVF, PMLR, official project pages, official GitHub repositories, benchmark leaderboards.
   - Do not collect papers with `year < 2024`.
   - Prefer papers/releases from the current and previous two years.
   - If a result is a classic pre-2024 foundation paper, mention it only as background if needed; do not add it to the registry or registry patch.
6. Before broad keyword search, check fixed follow sources in `data/follow_sources.seed.json`.
   - Check all `priority: core` source groups every expansion run when feasible.
   - Check `priority: watch` source groups when relevant to the current branch scope or when recent signals appear.
   - Record checked, skipped, and unreachable sources in `01_discovery.json` under `followed_sources_checked`.
   - Record actual access time, URLs and observed evidence for checks; describe the reason for each skipped or unreachable source. Do not mark a source checked merely because its URL is known.
   - Follow-source hits are discovery signals only; they still need the normal 2024+, source, relevance, visual, and evidence gates.
7. Run the five roles:
   - Research Lead: write `00_run_plan.json`.
   - Discovery Agent: search, deduplicate, and triage into `01_discovery.json`.
   - Evidence Analyst: extract paper/demo evidence into `02_evidence.json`.
   - Quality Reviewer: inspect source quality, demos, and visual/generation results into `03_review.json`.
   - Taxonomy & Editor: write `04_editor_report.md`, `05_registry_patch.json`, accepted-paper deep dives under top-level `paper_reads/<branch>/<slug>.md`, and `run_manifest.json`.
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
9. Use Quality Reviewer to inspect actual figures, videos, GIFs, screenshots, robot executions, and generated samples. Distinguish media actually inspected from media merely linked on a project page. Record URLs, page/figure numbers or video time ranges, sample/task coverage, observations and failure modes. For articulated/physical assets, check joint motion, collisions, stability and task usability where applicable. Do not infer visual quality from success-rate text or venue.
10. If a candidate otherwise meets the acceptance gates but visual quality cannot be judged confidently, write a local dossier under `undecided/YYYY-MM-DD/CAND-xxxx.md` and do not add that candidate to the registry patch. Do not route this case to watchlist to avoid the dossier requirement.
    - This dossier must still be a real paper/deep-dive analysis with source links, novelty, contributions, task, data, method, visual evidence, limitations, and the specific human decision needed.
    - Undecided dossiers are local-only by default. Do not commit or push them unless the human explicitly approves that candidate later.
11. For every candidate in `registry_additions`, write or update `paper_reads/<branch>/<slug>.md` and set `deep_dive_path` in `05_registry_patch.json`.
    - Include original paper/project/code/demo links.
    - Explain novelty, contributions, task, data, method, evidence, limitations, and project relevance.
    - Include a short evidence trail that maps central claims to paper/project/code/demo sources.
    - Include `Key Figures / Architecture` with `figure_status: linked_official|captured_official|redrawn|not_applicable|missing`.
    - Prefer official project figures/videos. If useful, redraw the method architecture in our own style rather than copying a copyrighted paper figure.
    - If no figure is available or appropriate, explicitly set `figure_status: missing` or `figure_status: not_applicable` and explain why.
12. Apply `harness/acceptance_harness.md` for paper relevance and `harness/system_harness.md` for workflow validity.
    - All gates are conjunctive: year >= 2024, primary/official source, branch fit, final `impact_score >= 4`, `project_relevance_score >= 4`, `evidence_strength >= 4`, eligible visual decision, and no acceptance-critical unverified claim.
    - Score impact from substantive technical advances supported by controlled experiments or a reusable release, not citation count, popularity, or venue. New papers need not wait for citations.
    - Project relevance must name a direct interface, validator, or baseline and explain its use; generic usefulness or reusable fields alone is insufficient.
    - Each accepted `quality_review` must include final scores, `selection_basis`, `acceptance_rationale`, and `comparison_to_registry` with `closest_paper`, `material_difference`, and `why_new_entry`. Assess the closest existing paper before creating another entry. A score of 4 needs specific decisive evidence; do not mechanically give every related candidate 4s.
    - Set paper-card `requires_visual_review` and `requires_temporal_demo` explicitly. Motion-dependent acceptance requires actual video/GIF/interactive-demo inspection. Copy the policy version, final three scores and both visual requirement flags into each new registry paper; exact contracts remain authoritative.
    - Acceptance must rest on at least one verified central claim with a primary/official HTTP source. Partial or unverified claims may remain as caveats only with `used_for_acceptance: false`.
    - Related but ordinary or insufficiently evidenced work belongs in a light watchlist with the evidence needed to upgrade and `revisit_trigger`; do not create a full deep dive for every watchlist item. Cases that otherwise qualify but have uncertain required visuals follow step 10.
13. Write a concise run summary under `reports/YYYY-MM-DD-expansion.md` only after the system run validates.
    - This summary is an audit record of what was accepted, rejected, or left undecided.
    - The primary output is the expanded knowledge base: `data/papers.seed.json` plus `paper_reads/`.
14. If there are accepted papers, account for every candidate that passes all gates in the patch.
    - Do not use a fixed top-k cap such as "best 1-2 papers per branch".
    - The selection boundary is the acceptance threshold, not a quota.
    - Add a new entry only for a material increment beyond the existing registry. Put releases or evidence improvements for an existing work in `registry_updates`; use `registry_noops` when the knowledge is already covered.
    - Preserve a complete correspondence between accepted candidates and `registry_additions` / `registry_updates` / `registry_noops`; do not silently omit a passed candidate.
    - Reject, watchlist, or send to `undecided/` only when a candidate fails a documented gate.
    - Assign each new policy-v2 paper real `task_ids` and matching memberships in `data/task_frontiers.seed.json`. For newly admitted work and relevant same-task releases, review the affected task frontier rather than rerating the whole library.
    - Compare concrete input/output/setting/protocol and source-backed improvements, costs, generalization, openness and deployment tradeoffs. Roles are `current|alternative|historical|unreviewed`, scoped per task; current is a reading recommendation, not a global SOTA claim.
    - Only mark an old member historical when verified primary/official evidence supports the same task, comparable protocol, substantive improvement and no material regression. Record dated evidence, `superseded_by`, improvements, tradeoffs and retained value per `harness/task_lifecycle.md`. Preserve alternatives or unreviewed status when comparison is unresolved. Historical chains must be acyclic and end at a same-task current member. Preserve every old registry entry, deep dive and stable link.
    - Record lifecycle decisions in optional `lifecycle_changes` in the run patch and summarize their evidence. These audit items are independent of accepted-candidate additions/updates/noops; do not fabricate replacement-paper updates to store task roles.
    - Regenerate full reading indexes and the task view with `python3 scripts/render_reading_indexes.py`. Initial grouping of existing families is unreviewed and does not justify automatic demotion.
15. Run local validation:

```bash
REQUIRE_UNDECIDED_DOSSIERS=1 python scripts/validate_all.py
```

16. If validation passes, publish all non-undecided changes in one step:

```bash
python scripts/publish_validated_update.py --message "Expand frontier knowledge base YYYY-MM-DD"
```

This script validates, stages publishable files, commits, and pushes to GitHub. It leaves `undecided/**` unstaged except for `undecided/README.md`.

17. Do not add social-media-only claims to the registry. Put them in a watchlist section of the report.

Output expectations:

- concise but source-linked report
- accepted papers grouped by the five branches
- followed-source coverage summary
- deep-dive link for every accepted paper
- strongest inspected demos and why they matter, when any qualify (no minimum count)
- final acceptance scores, closest-registry comparison, and rationale for each addition
- task-level current/alternative/historical decisions, source-backed succession evidence and unresolved comparisons when reviewed; existing deep dives remain accessible
- concise watchlist with missing evidence and revisit triggers
- actual query/source coverage, overlap windows, and retrospective status
- undecided candidates requiring human visual judgment
- local-only undecided deep dives generated but not pushed
- brief collection notes for baseline / related-work usefulness
- validation summary showing the system harness and registry validation passed
