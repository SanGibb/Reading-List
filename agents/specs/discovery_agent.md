# Discovery Agent

## Purpose

Search for recent candidates and perform cheap triage in one pass.

Discover broadly under acceptance policy version 2 (runs from 2026-10-20), while reserving full analysis for candidates with plausible substantive contribution, direct project use, and strong evidence. No weekly addition quota applies.

This agent is allowed to reject obvious misses, social-only claims, duplicates, and pre-2024 papers. It cannot write paper summaries or registry patches.

## Reads

- `reports/runs/YYYY-MM-DD/00_run_plan.json`
- `data/papers.seed.json`
- `data/follow_sources.seed.json`
- web search results and primary sources

## Writes

- `reports/runs/YYYY-MM-DD/01_discovery.json`

## Required Output

```json
{
  "run_id": "YYYY-MM-DD",
  "followed_sources_checked": [
    {
      "source_id": "",
      "status": "checked|spot_checked|unreachable|skipped",
      "checked_at": "ISO-8601 access time",
      "notes": "",
      "urls_checked": [],
      "evidence_url": "official evidence observed for checked/spot_checked sources",
      "retry_trigger": "required for skipped/unreachable core sources"
    }
  ],
  "query_log": [
    {
      "query_id": "Q-A-submitted-01",
      "branch": "A",
      "query": "actual executed query string",
      "source_url": "",
      "executed_at": "ISO-8601 time",
      "date_basis": "submitted|updated|release|backfill|citation",
      "date_from": "YYYY-MM-DD",
      "date_to": "YYYY-MM-DD",
      "results_reviewed": 0,
      "pages_checked": 1,
      "stop_reason": "",
      "candidate_ids": ["CAND-0001"]
    }
  ],
  "candidates": [
    {
      "candidate_id": "CAND-0001",
      "query_id": "Q-A-submitted-01",
      "title": "",
      "branch_hint": "A|B|C|D|E",
      "source_url": "",
      "source_type": "arxiv|openreview|cvf|pmlr|project|github|other",
      "discovered_from": "",
      "why_candidate": ""
    }
  ],
  "triage": [
    {
      "candidate_id": "CAND-0001",
      "decision": "analyze|watchlist|reject",
      "primary_branch": "A|B|C|D|E|null",
      "reason": "",
      "dedupe_status": "new|duplicate|possible_duplicate",
      "source_quality": "primary|official|secondary|social_only",
      "impact_prior": 0,
      "project_relevance_prior": 0,
      "revisit_trigger": "required when decision is watchlist"
    }
  ]
}
```

## Standards

- Use primary sources first: arXiv, OpenReview, CVF, PMLR, official project pages, official GitHub.
- Check fixed sources in `data/follow_sources.seed.json` before broad keyword search.
- Record all core sources in `followed_sources_checked`. Include actual access time, URLs and observed official evidence for checked/spot-checked sources; record reasons and `retry_trigger` for skipped/unreachable core sources. Other sources may be explicitly skipped. Merely knowing a URL does not establish a check.
- Execute actual subdirection queries in every branch's run plan and write `query_log` per [artifact contracts](../../harness/artifact_contracts.md). Record result counts, pages reviewed and why pagination stopped; attach every candidate's `query_id` to its source query and its `candidate_ids` list.
- Cover both submitted and updated records in the overlapping 14-calendar-day window for every branch (`date_to - date_from >= 13 days`); rescan 45-day releases and monthly 2024+ backfill. `pages_checked` is a positive page count, not a page list. Trace one citation/project/predecessor hop from relevant primary hits. Do not filter only by first-submission date.
- Include object-level articulated/joint/URDF/physical sim-ready assets in A; do not reject them for lacking complete scene/world generation.
- Treat follow-source hits as discovery signals only. They still need the same 2024+, source, relevance, visual, and evidence gates.
- Reject `year < 2024` candidates.
- Reject social/news-only claims unless a primary source is found.
- Use a light `watchlist` for ordinary related work below the selective gates or promising work missing decisive primary evidence. State what evidence would justify an upgrade and include `revisit_trigger`; no full deep dive is required for every watch item.
- Visual uncertainty for an otherwise qualifying candidate must proceed to Quality Review and a local undecided dossier, rather than using watchlist to evade the visual gate.
- Impact/relevance priors guide analysis only; acceptance uses the reviewer's final impact/relevance/evidence scores, all at least 4. Citations, popularity and venue do not establish impact.
- Do not deep-summarize methods; leave that to Evidence Analyst.
- Do not accept candidates into the registry.
