# Weekly Frontier Knowledge Expansion — 2026-08-17

This run checked all 16 core follow-source groups and spot-checked all five watch/meta sources before a broad primary-source sweep. Six new 2026 works passed every acceptance gate; one generation-heavy candidate remains local-only and undecided.

## Accepted

### D. VLA and World-Action Models

- [G0.5](../paper_reads/D_vla_world_action_models/g05-2026.md) — one autoregressive reasoning/action stream with cross-embodiment control and broad physical evidence.
- [StellaVLA](../paper_reads/D_vla_world_action_models/stellavla-2026.md) — structured one-demonstration OOD adaptation across robot, human, and XR sources.
- [SLIM-0.5B](../paper_reads/D_vla_world_action_models/slim-0-5b-2026.md) — compact action-grounded predictive latent policy.
- [World Tokens](../paper_reads/D_vla_world_action_models/world-tokens-2026.md) — training-time video-world supervision removed at deployment.
- [JEPA-WAM](../paper_reads/D_vla_world_action_models/jepa-wam-2026.md) — dense joint-embedding transitions coupled directly to action generation.

### E. Evaluation and Data Infrastructure

- [Sekai2](../paper_reads/E_evaluation_data_infrastructure/sekai2-2026.md) — 2,826 hours of trajectory-annotated long video plus loop/revisit supervision.

## Followed Sources Checked

- Core: 16/16 checked.
- Watch/meta: 5/5 spot-checked.
- All accepted claims trace to primary arXiv papers or official project pages; no social-only claim was accepted.

## Visual / Demo Review

- Strong: G0.5.
- Adequate: StellaVLA, SLIM-0.5B, World Tokens, and JEPA-WAM.
- Not applicable: Sekai2 is a data release.
- Undecided: Alaya-EVOKE.

## Undecided Visual Case

- Alaya-EVOKE is withheld because no stable official long-session gallery could be inspected confidently for geometry, identity, drift, and interaction responsiveness. Detailed local-only dossier: `undecided/2026-08-17/CAND-0007.md`.

## Watchlist / Rejected

- Decoding Task Progress from VLA Representations: useful diagnostic, below the registry impact threshold.
- Embodied Multimodal Grounding via Semantic 3DGS: relevant but narrow evidence and no surfaced official demo/code.
- Gemini Robotics 2, Gamma-World, and Cosmos Policy remain influence/release signals for later paper-grade review; none was accepted from an official blog alone in this run.

## Top Demos

1. G0.5: extensive R1 Lite/Pro and BEHAVIOR rollouts, failures, CoT probes, and cross-embodiment comparisons.
2. JEPA-WAM: real bimanual manipulation under visual/spatial shifts.
3. StellaVLA: robot-, human-, and XR-sourced in-context demonstrations for OOD adaptation.

## Collection Notes

- G0.5 is the strongest generalist policy baseline from this wave.
- World Tokens, SLIM, and JEPA-WAM form a clean comparison among pixel-supervised, compact predictive-latent, and dense JEPA-style world-action learning.
- Sekai2 adds unusually long trajectory/caption supervision and revisits, but licensing and pose quality should be audited before training.

## Validation

`REQUIRE_UNDECIDED_DOSSIERS=1 python3 scripts/validate_all.py` passed. Registry validation reports 89 papers; all run harnesses pass. The only warnings are pre-existing missing local PDF paths.
