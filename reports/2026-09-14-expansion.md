# Frontier Knowledge Expansion — 2026-09-14

This run checked the September 8-14 release window, all fixed core sources, all watch groups, the VLA leaderboard, and broader primary-source searches. Four candidates passed every gate; one remains local-only undecided.

## Accepted by Branch

### B. Interactive Generation and PCG

- [Gamma-World](../paper_reads/B_interactive_generation_pcg/gamma-world-2026.md) — multi-agent shared video-world generation with permutation-equivalent identity, linear-cost hub communication, 24 FPS streaming, open code, and strong official galleries.

### D. VLA and World-Action Models

- [OpenWAM](../paper_reads/D_vla_world_action_models/openwam-2026.md) — modular infrastructure, controlled WAM studies, approximately 6,400 hours of pretraining data, open models/recipes, eight simulation benchmarks, and three robot platforms.
- [Show-Harness](../paper_reads/D_vla_world_action_models/show-harness-2026.md) — semantic action units, embodiment interpreters, GUMI collection, released data/adapters/code, and strong Franka/AgileX demonstrations.
- [ActSafeGuard](../paper_reads/D_vla_world_action_models/actsafeguard-2026.md) — differentiable ray-scaling for hard per-step feasibility in flow-matching policies; visual generation quality is not applicable.

No candidate passed in A, C, or E this week.

## Followed-source Coverage

- Checked all 15 configured core source groups plus the core VLA leaderboard.
- Spot-checked all four watch groups and the VLA survey index.
- Berkeley RAIL remains unreachable because the configured URL redirects to an unrelated Berkeley IT site; broad primary searches compensated.
- Fixed-source releases already in the registry were deduplicated.

## Top Demos

1. Gamma-World — independently controlled two-agent rollouts, zero-shot four-agent scenes, and real multi-robot coordination.
2. Show-Harness — open-world and cross-embodiment real-robot execution plus GUMI demonstration collection.
3. OpenWAM — one stack spanning simulation, single-arm, bimanual, and dexterous-hand deployment.

## Undecided — Local Only

- HaWMPO passes source, year, impact, relevance, and method-evidence gates, but no official execution video, code, or checkpoint was found. Static G1 task setups and qualitative hallucination panels do not support a confident visual/demo decision. The dossier is at `undecided/2026-09-14/CAND-0004.md` and must remain uncommitted pending human review.

## Watchlist / Rejected

- RoboCasa 365's September 10 leaderboard update is useful monitoring evidence, but it is not a new benchmark artifact and current benchmark coverage already exists.
- *World Model for Robot Learning* remains a valuable primary-source survey/index, not a registry addition.
- No social-media-only claim was accepted.

## Top Project-Relevant Papers

1. OpenWAM — strongest reproducible systems baseline for world/action coupling.
2. Show-Harness — strongest reusable semantic action/interface contract.
3. Gamma-World — fills the synchronized multi-agent interactive-generation gap.

## Collection Notes

- Use OpenWAM as a baseline only with its versioned configuration and benchmark protocol intact.
- Use Gamma-World for multi-agent consistency and communication studies, not as evidence of explicit 3D physics.
- Use Show-Harness to separate model reasoning from embodiment grounding and safety bounds.
- Cite ActSafeGuard's 100% step-safety claim as author-reported until code and independent reproduction appear.

## Validation

- `REQUIRE_UNDECIDED_DOSSIERS=1 python3 scripts/validate_all.py` passed for 110 papers and all completed runs. Only pre-existing missing-local-PDF warnings remain.
