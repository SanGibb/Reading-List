# How to Use Codex for This Literature Workflow

This workflow uses Codex as a file-driven research-maintenance system, not as an unconstrained browser.

Current scope: maintain a high-quality frontier paper registry. Codex should help search, verify, summarize, and conservatively update collection artifacts; it should not act as an autonomous scientist or produce research roadmaps as the main output.

## Recommended Operating Modes

### 1. Manual deep-update mode

Use this when you want a substantial update.

Prompt:

```text
请阅读 frontier_research 的 taxonomy、paper registry 和 harness。
联网搜索最近 2-4 周关于 interactive generation、spatial intelligence、VLA、world-action models、physical/deformable worlds 的最新论文和项目，只收录 2024 年及以后的工作。
按 harness 过滤，扩充 data/papers.seed.json 和 paper_reads；报告只作为本次检索的审计摘要。
```

Use cases:

- before writing a related work section
- before a group meeting
- before checking which baselines are worth reading or citing
- after major conferences or arXiv waves

### 2. Knowledge expansion mode

Use Codex automation to run the prompt in `automation/knowledge_expansion_prompt.md`.

Recommended trigger:

- run when you want to expand the knowledge base with newly surfaced papers
- additionally run around CVPR/ICCV/ECCV/NeurIPS/CoRL/ICRA/RSS deadlines or major arXiv/project-release waves

Expected output:

- `reports/runs/YYYY-MM-DD/` with consolidated stage artifacts
- `reports/YYYY-MM-DD-expansion.md` as a run summary, not the main deliverable
- `01_discovery.json` with `followed_sources_checked`
- maintained deep dives under `paper_reads/<branch>/<slug>.md`
- conservative registry updates
- watchlist for unverified but potentially important work
- local-only undecided dossiers under `undecided/YYYY-MM-DD/`
- a validated commit pushed to GitHub when publishable changes exist

### 3. Paper deep-dive mode

Use this when one paper is important enough to analyze deeply.

Prompt:

```text
请对 <paper title / PDF / project page> 做可交互生成/具身智能视角深读。
输出数据集、方法、任务、创新点、实验指标、demo 质量、可复用字段、局限、关键 claim 来源和 related-work / baseline 收录价值。
```

Expected output:

- a paper card
- a deep-dive Markdown report using `reports/paper_deep_dive_template.md`
- possible figures/demos
- collection notes for related-work and baseline usefulness

## Multi-Agent Execution in Codex

Use one focused Codex task per role when quality matters. Each phase reads previous artifacts and writes exactly one assigned artifact, except the final editor role which writes the report and patch:

1. **Research Lead** writes `00_run_plan.json`.
2. **Discovery Agent** checks `data/follow_sources.seed.json`, then writes `01_discovery.json`.
3. **Evidence Analyst** writes `02_evidence.json`.
4. **Quality Reviewer** writes `03_review.json` and optional undecided dossiers.
5. **Taxonomy & Editor** writes `04_editor_report.md`, `05_registry_patch.json`, accepted-paper `paper_reads/<branch>/<slug>.md` reports, and `run_manifest.json`.
6. **System Harness** validates the run.
7. **Publisher** runs `python scripts/publish_validated_update.py --message "Expand frontier knowledge base YYYY-MM-DD"`.

This is less fragmented than the original nine-agent setup while still separating search, evidence extraction, judgment, and registry editing.

To create an empty run folder:

```bash
python frontier_research/scripts/scaffold_run.py YYYY-MM-DD
```

To validate a completed run:

```bash
python frontier_research/scripts/validate_run.py YYYY-MM-DD
```

To validate, commit, and push publishable changes:

```bash
python scripts/publish_validated_update.py --message "Expand frontier knowledge base YYYY-MM-DD"
```

The publisher leaves `undecided/**` local-only by default. Those dossiers should still be generated and detailed, but they are uploaded only after explicit human approval.

## What Codex Should Not Do Automatically

- Do not accept papers from social posts unless there is a primary paper/project URL.
- Do not download large videos unless needed.
- Do not rewrite the taxonomy in routine expansion runs.
- Do not generate autonomous research hypotheses or experiment roadmaps as a primary output.
- Do not add every new arXiv paper; keep impact and project relevance thresholds.
- Do not claim SOTA unless the source reports a clear benchmark and comparison.
- Do not let one agent write another agent's artifact.
- Do not skip fixed follow sources silently; record `checked`, `spot_checked`, `unreachable`, or `skipped`.
- Do not update the registry if `validate_run.py` fails.
- Do not add a paper to `registry_additions` unless it has `deep_dive_path` pointing to a top-level `paper_reads/<branch>/<slug>.md` report with source links, novelty, contributions, task, data, method, key figures/architecture, evidence, limitations, and project relevance.
- Do not commit or push `undecided/YYYY-MM-DD/CAND-xxxx.md` during the automatic publish step.

## Suggested Prompt Contract

Every automated run should end with:

- `Accepted`
- `Followed sources checked`
- `Deep dives`
- `Rejected`
- `Watchlist`
- `Top demos`
- `Undecided visual cases`
- `Local-only undecided deep dives`
- `Collection notes`
- `Validation`

The final validation must state:

- run harness validates
- registry validates
- all accepted papers have primary URLs
- all accepted papers satisfy branch fit
- no social-only claims were accepted
