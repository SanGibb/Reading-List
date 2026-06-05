# Discovery Agent

## Purpose

Search for recent candidates and perform cheap triage in one pass.

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
      "notes": "",
      "urls_checked": []
    }
  ],
  "candidates": [
    {
      "candidate_id": "CAND-0001",
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
      "project_relevance_prior": 0
    }
  ]
}
```

## Standards

- Use primary sources first: arXiv, OpenReview, CVF, PMLR, official project pages, official GitHub.
- Check fixed sources in `data/follow_sources.seed.json` before broad keyword search.
- Record every checked source in `followed_sources_checked`; use `unreachable` if a site cannot be accessed.
- Treat follow-source hits as discovery signals only. They still need the same 2024+, source, relevance, visual, and evidence gates.
- Reject `year < 2024` candidates.
- Reject social/news-only claims unless a primary source is found.
- Mark candidates `watchlist` when promising but missing primary evidence.
- Do not deep-summarize methods; leave that to Evidence Analyst.
- Do not accept candidates into the registry.
