# 2026-10-05 Frontier Knowledge Expansion

This run checked all configured core follow sources, spot-checked all watch sources, and searched primary sources across all five branches. It accepted nine newly influential omissions and found no brand-new October 1–5 release that cleared every gate.

## Accepted

- B: [SimFoundry](../paper_reads/B_interactive_generation_pcg/simfoundry-2026.md)
- C: [Vesta](../paper_reads/C_spatial_intelligence/vesta-2026.md)
- D: [DreamDojo](../paper_reads/D_vla_world_action_models/dreamdojo-2026.md), [MolmoB0T](../paper_reads/D_vla_world_action_models/molmobot-2026.md), [Qwen-VLA](../paper_reads/D_vla_world_action_models/qwen-vla-2026.md), [Flow Reversal Steering](../paper_reads/D_vla_world_action_models/flow-reversal-steering-2026.md), and [World Action Verifier](../paper_reads/D_vla_world_action_models/world-action-verifier-2026.md)
- E: [MolmoSpaces](../paper_reads/E_evaluation_data_infrastructure/molmospaces-2026.md) and [Open-H-Embodiment](../paper_reads/E_evaluation_data_infrastructure/open-h-embodiment-2026.md)

## Rejected / watchlist

- Q-Learning With World Models: below the run's impact/demo boundary.
- Robot World Models Are Not Invariant to How the Actions Are Written: narrow diagnostic contribution, impact prior 2.
- No social-only claim was accepted, and no candidate required human visual judgment.

## Top demos and relevance

1. DreamDojo: strongest new action-conditioned neural simulator baseline.
2. SimFoundry: most complete video-to-editable-simulator pipeline.
3. MolmoB0T: strongest open sim-only zero-shot real manipulation release.

The most repository-relevant papers are SimFoundry, DreamDojo, and MolmoSpaces because they directly define compiler targets, executable rollout interfaces, and reusable physical/evaluation infrastructure.

## Follow-source coverage

All 15 core groups plus the VLA leaderboard were checked. Four watch groups and the VLA survey were spot-checked. Physical Intelligence returned HTTP 403; query-indexed official PDFs showed no newer release.

## Validation

`REQUIRE_UNDECIDED_DOSSIERS=1 python3 scripts/validate_all.py` passed for 136 papers and every completed run. Only pre-existing missing-local-PDF warnings remain.
