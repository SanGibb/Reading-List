# Frontier Knowledge Expansion Run

Date: 2026-06-06

## Summary

This is a local dry-run used to validate the consolidated file-driven multi-agent workflow. It exercises accepted, blocked, and undecided visual-quality paths without applying the registry patch. The editor report is an audit artifact for this expansion run, not the main repository deliverable.

## Followed Sources Checked

| Source | Status | New signal | Notes |
|---|---|---|---|
| huggingface-lerobot | checked | SmolVLA | Candidate found but moved to undecided until visual robot/demo evidence is inspected. |
| meta-fair-embodied | checked | OpenEQA | Accepted as an evaluation benchmark candidate in the dry-run registry patch. |
| vla-leaderboard | spot_checked | none accepted directly | Used only as a discovery signal; no leaderboard-only claim was accepted. |

## Accepted Candidates

| Candidate | Branch | Source | Deep dive | Visual | Why it matters |
|---|---|---|---|---|---|
| OpenEQA | E | https://openaccess.thecvf.com/content/CVPR2024/html/Majumdar_OpenEQA_Embodied_Question_Answering_in_the_Era_of_Foundation_Models_CVPR_2024_paper.html | ../../../paper_reads/E_evaluation_data_infrastructure/openeqa-2024.md | not_applicable | Embodied QA benchmark relevant to evaluating environment understanding. |

## Undecided

| Candidate | Dossier | Reason |
|---|---|---|
| SmolVLA | ../../undecided/2026-06-06/CAND-0001.md | Relevance is clear, but the dry-run could not confidently judge robot/demo visual quality. |

## Rejected / Blocked

| Candidate | Reason |
|---|---|
| RynnVLA-002 social-only announcement | Blocked because this dry-run only had a social source and no verified primary source. |

## Top Demos

1. OpenEQA project page: benchmark examples, demo score 2.
2. SmolVLA: moved to undecided until visual robot execution evidence is inspected.

## Collection Notes

- VLA branch should track efficient and deployable models, but visual/robot execution evidence must be judged before permanent registry inclusion.
- Evaluation branch should include embodied QA benchmarks as downstream tests for generated environments.
- Social-only claims should remain blocked or watchlisted until primary sources are found.

## Validation

- System run validation: passed via `python frontier_research/scripts/validate_run.py 2026-06-06`.
- Registry validation: passed on current registry; dry-run patch not applied.
- Registry patch: draft only, not applied.
