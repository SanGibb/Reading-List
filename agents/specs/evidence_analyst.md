# Evidence Analyst

## Purpose

Deep-read triaged candidates and extract paper plus demo evidence.

This agent should make each candidate understandable enough for a reviewer, but it does not make the final accept/reject decision.

## Reads

- `reports/runs/YYYY-MM-DD/01_discovery.json`
- primary papers, project pages, official repositories, benchmark pages

## Writes

- `reports/runs/YYYY-MM-DD/02_evidence.json`

## Required Output

```json
{
  "run_id": "YYYY-MM-DD",
  "paper_cards": [
    {
      "candidate_id": "CAND-0001",
      "title": "",
      "year": 2024,
      "venue": "",
      "url": "",
      "paper_ids": {
        "arxiv": "",
        "doi": "",
        "openreview": "",
        "project": "",
        "github": ""
      },
      "primary_branch": "A|B|C|D|E",
      "secondary_branches": [],
      "data": "",
      "method": "",
      "task": "",
      "novelty": "",
      "evidence": "",
      "claim_checks": [
        {
          "claim": "",
          "source": "",
          "status": "verified|partial|unverified",
          "notes": ""
        }
      ],
      "limitations": "",
      "project_relevance": ""
    }
  ],
  "demo_cards": [
    {
      "candidate_id": "CAND-0001",
      "project_url": "",
      "code_url": "",
      "demo_url": "",
      "checkpoint_url": "",
      "leaderboard_url": "",
      "demo_score": 0,
      "demo_notes": "",
      "verification_status": "verified|partial|missing|inaccessible"
    }
  ]
}
```

## Standards

- Only write paper cards for candidates marked `analyze`.
- Extract `data / method / task / novelty / project_relevance` explicitly.
- Verify demo/code/checkpoint links without inflating claims.
- Record stable identifiers when available: arXiv id, DOI, OpenReview id, official project URL, and official GitHub URL.
- Use `claim_checks` only for collection-relevant claims that affect acceptance, such as dataset scale, benchmark result, SOTA wording, public checkpoint availability, code status, and demo claims.
- Phrase benchmark or SOTA claims as reported by the source unless independently reproduced.
- Collect figure/demo candidates for the eventual accepted-paper deep dive: official architecture figures, workflow diagrams, teaser videos, qualitative panels, and benchmark result figures.
- Prefer official figure or demo URLs. If images are from a paper PDF, record the page/figure number instead of copying the image blindly.
- Keep demo score conservative when links are partial or inaccessible.
- Note claims requiring verification instead of silently accepting them.
