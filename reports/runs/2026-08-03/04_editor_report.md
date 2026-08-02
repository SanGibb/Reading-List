# Frontier Knowledge Expansion Run — 2026-08-03

All 15 core follow-source groups were checked before broad primary-source search; four watch groups were spot-checked. No fixed branch quota was used.

## Accepted Candidates

- `CAND-0001` Self in Space → C — [deep dive](../../../paper_reads/C_spatial_intelligence/self-in-space-2026.md)
- `CAND-0002` Rethinking Video Generation Model for the Embodied World → E — [deep dive](../../../paper_reads/E_evaluation_data_infrastructure/rethinking-embodied-video-generation-2026.md)

## Watchlist / Rejected

- `CAND-0004` Embodied-BenchClaw: impact/release maturity below the registry threshold.
- `CAND-0005` ENACT: useful but narrower, with impact prior below threshold for this run.
- `CAND-0006` ActionEQA: narrow action-interface diagnostic and no broad public release verified.
- No social-media-only claim was accepted.

## Undecided

- `CAND-0003` WLA-0: local-only dossier written because physical demo quality could not be judged confidently from an official visual surface.

## Top Demos

1. RBench/RoVid-X official comparison gallery and leaderboard.
2. SIS-Bench representative UAV videos and public evaluation stack.
3. WLA-0 remains excluded pending human supplementary-video inspection.

## Collection Notes

- RBench is a high-value baseline for separating visual fidelity from physical/task validity.
- SIS-Bench adds explicit self-motion state to spatial-intelligence evaluation.
- Before citing, phrase scale, correlation, and transfer results as author-reported.

## Validation Status

Strict local validation passed: run harness, registry validation, and `REQUIRE_UNDECIDED_DOSSIERS=1 python3 scripts/validate_all.py`.
