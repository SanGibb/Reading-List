# Frontier Knowledge Expansion — 2026-08-03

This run checked every fixed core source group before broad primary-source discovery and accepted every discovered candidate that cleared the harness. Two papers were added and one VLA candidate remains local-only pending human visual review.

## Accepted

### C. Spatial Intelligence

- [Self in Space](../paper_reads/C_spatial_intelligence/self-in-space-2026.md) — public UAV benchmark for joint environmental spatial cognition and agent self-motion awareness.

### E. Evaluation and Data Infrastructure

- [Rethinking Video Generation Model for the Embodied World](../paper_reads/E_evaluation_data_infrastructure/rethinking-embodied-video-generation-2026.md) — RBench evaluation, leaderboard, and the 4M-clip RoVid-X corpus.

Branches A, B, and D had no new candidate clear every gate.

## Followed Sources Checked

- All 15 `priority: core` groups were checked.
- All four `priority: watch` groups were spot-checked where relevant.
- Detailed statuses and URLs are recorded in [01_discovery.json](runs/2026-08-03/01_discovery.json).

## Watchlist / Rejected

- Embodied-BenchClaw: relevant benchmark-construction idea, but impact and official release maturity remain below threshold.
- ENACT: useful egocentric world-modeling diagnostic, but narrower impact evidence did not clear this run's gate.
- ActionEQA: useful semantic-to-physical diagnostic, but narrow scope and no broad public release verified.
- No social-media-only claim was accepted.

## Top Demos

1. RBench/RoVid-X — strongest official combination of benchmark, leaderboard, failure gallery, dataset, and introductory video.
2. SIS-Bench — clear task figures, representative UAV videos, public code, and downloadable benchmark.
3. WLA-0 — promising architecture, but excluded until its physical rollouts can be inspected confidently.

## Undecided Visual Cases

- `CAND-0003` WLA-0 has a detailed local-only dossier at `undecided/2026-08-03/CAND-0003.md`. Human review should inspect real-robot diversity, contact quality, failures, and long-horizon consistency.

## Collection Notes

- RBench is the most useful new baseline for ensuring visual fidelity does not substitute for physical or task validity.
- SIS-Bench contributes explicit AgentState and MotionHistory concepts to spatial-intelligence evaluation.
- Treat dataset scale, human-correlation, navigation-transfer, and performance claims as author-reported until reproduced.

## Validation

- `REQUIRE_UNDECIDED_DOSSIERS=1 python3 scripts/validate_all.py`: passed.
- Registry validation passed with 77 papers across five branches; only pre-existing missing-local-PDF warnings remain.
- Run harness passed for `2026-08-03` with six discovered, three analyzed, two accepted, and one local-only undecided case.
