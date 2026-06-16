# Frontier Knowledge Expansion Summary - 2026-06-15

This run adds **4 accepted papers** and preserves **2 local-only undecided dossiers**. The selection boundary was the acceptance harness, not a fixed quota.

## Summary

- New accepted papers: `MolmoAct2`, `WorldArena 2.0`, `Embodied3DBench`, `ESPIRE`
- Followed sources checked: all core source groups were checked or spot-checked; direct accepted signals came from Ai2, the world-model benchmark cluster, and broad primary-source search
- Deep dives in `paper_reads/`: 4 new maintained reports
- Watchlist items: none promoted from social-only sources
- Strong demos: `MolmoAct2`, `WorldArena 2.0` benchmark site
- Undecided visual cases: `GE-Sim 2.0`, `Embodied-R1.5`
- Collection notes: this run strengthened the spatial benchmark branch, refreshed the VLA baseline set, and upgraded evaluation coverage for embodied world models

## C. Spatial Intelligence

| Paper | Source | Deep dive | Data | Method | Task | Novelty | Demo | Visual | project relevance |
|---|---|---|---|---|---|---|---:|---|---|
| Embodied3DBench | arXiv | [embodied3dbench-2026.md](../paper_reads/C_spatial_intelligence/embodied3dbench-2026.md) | 21k+ QA pairs plus 1.3M synthetic QA training set | diagnostic benchmark plus synthetic QA training data | low-level embodied spatial understanding and interaction-oriented perception | separates structural spatial understanding from interaction-oriented perception | 2 | not_applicable | good low-level benchmark for grounding, affordance, grasp-point, and trajectory checks |
| ESPIRE | arXiv | [espire-2026.md](../paper_reads/C_spatial_intelligence/espire-2026.md) | Isaac-Sim benchmark with 148 localization reasoning types | fully generative localization-plus-execution benchmark | action-oriented embodied spatial reasoning | turns spatial reasoning evaluation into a physically grounded generative execution problem | 2 | not_applicable | strong reasoning-to-act validator template |

## D. VLA and World-Action Models

| Paper | Source | Deep dive | Data | Method | Task | Novelty | Demo | Visual | project relevance |
|---|---|---|---|---|---|---|---:|---|---|
| MolmoAct2 | arXiv + official Ai2 page | [molmoact2-2026.md](../paper_reads/D_vla_world_action_models/molmoact2-2026.md) | Molmo 2-ER corpus plus Bimanual YAM and mixed robot data | embodied-reasoning VLM + flow-matching action expert + open tokenizer | open real-world single-arm and bimanual robot manipulation | combines open reasoning, open data/code, and deployment-oriented VLA design | 5 | strong | strong open baseline for reasoning-to-action transfer and low-cost embodiment deployment |

## E. Evaluation and Data Infrastructure

| Paper | Source | Deep dive | Data | Method | Task | Novelty | Demo | Visual | project relevance |
|---|---|---|---|---|---|---|---:|---|---|
| WorldArena 2.0 | arXiv + official benchmark site | [worldarena-2-2026.md](../paper_reads/E_evaluation_data_infrastructure/worldarena-2-2026.md) | visuotactile and cross-platform embodied world-model benchmark infrastructure | modality/functionality/platform benchmark extension | evaluate world models as predictors, data engines, policy evaluators, planners, and RL environments | extends WorldArena into visuotactile, policy-optimization, and real-world settings | 4 | not_applicable | direct evaluation target for closed-loop embodied generation and world-action models |

## Watchlist

No social-only claims were accepted or promoted. Broad-search results without clean primary/official support were ignored rather than added speculatively.

## Followed Sources Checked

| Source | Status | New signal | Notes |
|---|---|---|---|
| Ai2 Embodied AI / PRIOR | checked | MolmoAct2 | strongest accepted action-model addition this run |
| Embodied/world-model benchmark cluster | checked | WorldArena 2.0, GE-Sim 2.0 | one accepted, one routed to undecided |
| Hugging Face LeRobot | checked | MolmoAct2 integration | useful release-strength signal, not standalone evidence |
| Remaining core source groups | spot_checked | none accepted | checked for new 2024+ official candidates; no additional passes this run |

## Undecided

- [CAND-0051](../undecided/2026-06-15/CAND-0051.md): `GE-Sim 2.0` needs human visual judgment on rollout quality and official demo evidence.
- [CAND-0052](../undecided/2026-06-15/CAND-0052.md): `Embodied-R1.5` needs human confirmation of official demos and release artifacts.

## Top Demos

1. MolmoAct2 official Ai2 release for the strongest combined code/data/robot-evidence package.
2. WorldArena official benchmark site for the clearest infrastructure and evaluation framing.
3. ESPIRE for the strongest reasoning-to-act benchmark design signal in the spatial branch.

## Collection Notes

- Related-work usefulness: MolmoAct2 is now the cleanest open reasoning-heavy VLA baseline in the repo for real-world deployment discussion.
- Baseline usefulness: WorldArena 2.0 should be treated as a separate benchmark-era update, not folded into the older WorldArena entry.
- Evidence gaps to check before citing: public artifact URLs and qualitative demos for GE-Sim 2.0 and Embodied-R1.5.

## Validation

- System run validation: passed via `python3 scripts/validate_run.py 2026-06-15`
- Registry validation: passed via `python3 scripts/validate_registry.py`
- Full repository validation: passed via `REQUIRE_UNDECIDED_DOSSIERS=1 python3 scripts/validate_all.py`
- Source quality: all accepted papers use primary or official sources
- Duplicate check: passed manual registry/title check during this run
- Harness exceptions: none; undecided cases were kept local-only
