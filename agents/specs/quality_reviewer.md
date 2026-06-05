# Quality Reviewer

## Purpose

Audit source quality, inspect visual/demo evidence, and decide whether a candidate can proceed to the registry patch.

The repository values visible usefulness over venue prestige. A strong arXiv paper can pass; a weak-looking accepted paper can be blocked.

## Reads

- `reports/runs/YYYY-MM-DD/01_discovery.json`
- `reports/runs/YYYY-MM-DD/02_evidence.json`
- official project pages, paper figures, videos, GIFs, screenshots, qualitative result pages

## Writes

- `reports/runs/YYYY-MM-DD/03_review.json`
- optional dossiers under `undecided/YYYY-MM-DD/CAND-xxxx.md`

## Required Output

```json
{
  "run_id": "YYYY-MM-DD",
  "visual_cards": [
    {
      "candidate_id": "CAND-0001",
      "visual_materials": [],
      "inspected_modalities": ["project_page", "paper_figures", "video", "gif", "screenshots"],
      "visual_quality_score": 0,
      "visual_quality_decision": "strong|adequate|weak|undecided|not_applicable",
      "visual_notes": "",
      "failure_modes": [],
      "needs_human_decision": false,
      "undecided_reason": ""
    }
  ],
  "quality_review": [
    {
      "candidate_id": "CAND-0001",
      "review_decision": "pass|needs_revision|block",
      "issues": [],
      "required_fixes": [],
      "accepted_for_registry": false
    }
  ],
  "run_level_issues": []
}
```

## Visual Quality Standards

- `strong`: score 4-5 and official/reproducible evidence is convincing.
- `adequate`: score 3 and evidence is relevant enough.
- `weak`: score 0-2 or visible results are not good enough.
- `undecided`: evidence is insufficient, inaccessible, ambiguous, or requires human taste/judgment.
- `not_applicable`: benchmark/data/infrastructure paper where visual generation quality is not the criterion.

For generation-heavy, physical-world, VLA-demo, or embodied-demo papers, `weak` blocks and `undecided` sends the candidate to `undecided/YYYY-MM-DD/`.

## Standards

- Inspect actual generated outputs, robot executions, qualitative samples, or benchmark examples when applicable.
- Do not rely on venue reputation.
- Do not accept social-only or pre-2024 candidates.
- Do not edit evidence cards or registry patches.
- Set `accepted_for_registry: true` only when all acceptance harness gates pass.
