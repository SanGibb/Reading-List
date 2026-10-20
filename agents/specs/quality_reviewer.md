# Quality Reviewer

## Purpose

Audit source quality, inspect visual/demo evidence, and decide whether a candidate can proceed to the registry patch.

The repository values visible usefulness over venue prestige. A strong arXiv paper can pass; a weak-looking accepted paper can be blocked.

For runs from 2026-10-20, apply acceptance policy version 2. All gates are conjunctive; there is no fast-track bypass and no addition quota. Existing entries are retained under their historical policy.

## Reads

- `reports/runs/YYYY-MM-DD/01_discovery.json`
- `reports/runs/YYYY-MM-DD/02_evidence.json`
- official project pages, paper figures, videos, GIFs, screenshots, qualitative result pages
- `data/task_frontiers.seed.json` and `harness/task_lifecycle.md`

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
      "inspected_modalities": [],
      "inspection_evidence": [
        {
          "url": "official source actually inspected",
          "modality": "video",
          "locator": "00:15-00:30",
          "observation": "specific observed behavior and sample/task coverage",
          "limitations": "visible defects or inspection limits"
        }
      ],
      "visual_quality_score": 0,
      "visual_quality_decision": "strong|adequate|weak|undecided|not_applicable",
      "not_applicable_reason": "required only for not_applicable",
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
      "impact_score": 0,
      "project_relevance_score": 0,
      "evidence_strength": 0,
      "selection_basis": "new_capability|substantial_improvement|reusable_infrastructure|decisive_evaluation",
      "acceptance_rationale": "",
      "comparison_to_registry": {
        "closest_paper": "",
        "material_difference": "",
        "why_new_entry": ""
      },
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

For generation-heavy, interactive-world, physical-world, VLA-demo, or embodied-demo papers, `weak` blocks acceptance. If the candidate otherwise qualifies but required visuals remain `undecided`, write a detailed local-only dossier in `undecided/YYYY-MM-DD/`; do not route it to watchlist to avoid that requirement.

Use `inspection_evidence` for media actually inspected, with the official URL, modality, page/figure or time-range locator, concrete observation and inspection limitations. A project page listing videos is not a viewed video. If `requires_temporal_demo` is true, acceptance requires actual video, GIF or interactive-demo inspection; paper figures and reported success rates are insufficient. Inspect applicable joint motions, collisions, stability, contact behavior and task usability across the observed samples. Do not infer unseen performance. `not_applicable` requires `not_applicable_reason` and cannot override a required visual review.

## Standards

- Inspect actual generated outputs, robot executions, qualitative samples, or benchmark examples when applicable.
- Set final `impact_score >= 4`, `project_relevance_score >= 4` and `evidence_strength >= 4` only when individually justified by primary/official evidence. Lower scores cannot be offset by higher scores elsewhere.
- Judge impact from the technical increment and controlled experiments or a reusable release, not citations, popularity or venue. Judge project relevance from a named interface, validator or direct baseline, not a general "useful fields" claim.
- Scores of 4 are selective judgments, not defaults. Cite the decisive controlled comparison, usable release or verified evidence and explain its significance relative to the closest registry work; avoid mechanically assigning 4 to every related candidate.
- Acceptance must use at least one verified central claim with a concrete claim and primary/official HTTP source. Partial or unverified claims can remain as caveats only when `used_for_acceptance: false`; no unresolved major claim may carry the admission decision.
- Each accepted review must include `selection_basis`, `acceptance_rationale` and `comparison_to_registry` (`closest_paper`, `material_difference`, `why_new_entry`) per [artifact contracts](../../harness/artifact_contracts.md). Explain why the delta deserves a new entry; known work with a release/evidence change should update its existing entry, and redundant knowledge should be a noop.
- Separately review task roles for admitted papers and relevant same-task releases under [task_lifecycle.md](../../harness/task_lifecycle.md). Recommend `current|alternative|historical|unreviewed` with dated, verified primary/official evidence. Current is scoped, can be shared, and is not a global SOTA claim.
- A historical recommendation needs the same task, comparable protocol, substantive improvement and no material regression; give the successor URL, improvements, examined tradeoffs and retained value. A newer paper or one higher score is insufficient. Keep alternatives with meaningful independent advantages, and leave unresolved comparisons unreviewed. Do not edit the task file or fabricate acceptance updates to represent a lifecycle judgment.
- Ordinary related or insufficiently evidenced work can stay on a concise watchlist with missing upgrade evidence and `revisit_trigger`; a full deep dive is not required. Otherwise-qualified visual uncertainty follows the undecided rule above.
- A includes articulated and physical sim-ready object assets; complete scene/world generation is not required.
- Do not rely on venue reputation.
- Do not accept social-only or pre-2024 candidates.
- Do not edit evidence cards or registry patches.
- Set `accepted_for_registry: true` only when all acceptance harness gates pass.
- Do not lower thresholds to produce a weekly update. Zero accepted additions is valid. If a batch is unusually large, re-check final scores, source evidence, registry novelty and duplicates; do not impose a top-k cutoff on qualified work.
