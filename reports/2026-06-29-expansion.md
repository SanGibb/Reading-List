# Frontier Knowledge Expansion Summary - 2026-06-29

This run adds **6 accepted papers** and requires **no undecided dossiers**. The selection boundary was the acceptance harness, not a fixed quota.

## Summary

- New accepted papers: `SceneCode`, `SimWorld Studio`, `SpatialAct`, `Cosmos-Predict2.5`, `vla-eval`, `VLA-REPLICA`
- Followed sources checked: all core source groups were checked or spot-checked; direct accepted signals came from NVIDIA Cosmos, Ai2 evaluation infrastructure, broad primary-source scene-generation search, and VLA benchmark searches
- Deep dives in `paper_reads/`: 6 new maintained reports
- Watchlist items: `Cosmos-Reason1`
- Strong demos: `Cosmos-Predict2.5`, `SimWorld Studio`, `SceneCode`
- Undecided visual cases: none
- Collection notes: this run added one accepted paper to each top-level technical branch and materially improved evaluation-infrastructure coverage

## A. Executable World Representation

| Paper | Source | Deep dive | Data | Method | Task | Novelty | Demo | Visual | project relevance |
|---|---|---|---|---|---|---|---:|---|---|
| SceneCode: Editable Indoor Scene Generation using Executable World Programs | arXiv + official project | [scenecode-2026.md](../paper_reads/A_executable_world_representation/scenecode-2026.md) | indoor scene-program examples for generation, reconstruction, and editing | hierarchical executable scene programs over floor plans, rooms, and objects | generate and edit indoor scenes through structured world code | makes large indoor scenes executable and editable instead of opaque outputs | 4 | strong | strong representation reference for structured world code and local scene edits |

## B. Interactive Generation and PCG

| Paper | Source | Deep dive | Data | Method | Task | Novelty | Demo | Visual | project relevance |
|---|---|---|---|---|---|---|---:|---|---|
| SimWorld Studio: Generation and Evolution of Custom Embodied Agent Learning Environments | arXiv + official project + GitHub | [simworld-studio-2026.md](../paper_reads/B_interactive_generation_pcg/simworld-studio-2026.md) | 320 embodied tasks and 240 held-out layouts | environment generation-and-evolution loop | generate and iteratively refine custom embodied learning environments | turns embodied PCG into a closed-loop world evolution system | 4 | strong | strong baseline for curriculum-style environment generation and custom embodied worlds |

## C. Spatial Intelligence

| Paper | Source | Deep dive | Data | Method | Task | Novelty | Demo | Visual | project relevance |
|---|---|---|---|---|---|---|---:|---|---|
| SpatialAct: Probing Spatial Reasoning-to-Action Capabilities of Vision-Language Models in 3D Scenes | arXiv + official project | [spatialact-2026.md](../paper_reads/C_spatial_intelligence/spatialact-2026.md) | 333 synthetic 3D scenes and 4,355 QA pairs | 3D benchmark with tool-based repair analysis | evaluate spatial reasoning-to-action in 3D scenes | directly benchmarks whether spatial reasoning survives the jump to action-relevant decisions | 4 | not_applicable | strong validator for action-grounded spatial reasoning |

## D. VLA and World-Action Models

| Paper | Source | Deep dive | Data | Method | Task | Novelty | Demo | Visual | project relevance |
|---|---|---|---|---|---|---|---:|---|---|
| Cosmos-Predict2.5: A World Foundation Model for Physical AI | arXiv + official NVIDIA release | [cosmos-predict2-5-2026.md](../paper_reads/D_vla_world_action_models/cosmos-predict2-5-2026.md) | 200M training clips and official release artifacts | large action-conditioned world foundation model | predict physically meaningful futures for control and simulation use | positions predictive world modeling directly as physical-AI infrastructure | 5 | strong | strong world-model anchor for action-conditioned rollout prediction |

## E. Evaluation and Data Infrastructure

| Paper | Source | Deep dive | Data | Method | Task | Novelty | Demo | Visual | project relevance |
|---|---|---|---|---|---|---|---:|---|---|
| A Unified Evaluation Harness for Vision-Language-Action Models | arXiv + official GitHub | [vla-eval-2026.md](../paper_reads/E_evaluation_data_infrastructure/vla-eval-2026.md) | multi-benchmark VLA adapters and result reporting | standardized evaluation orchestration harness | benchmark VLA models consistently across suites | unifies fragmented VLA evaluation infrastructure | 4 | not_applicable | direct infrastructure reference for benchmark adapters and result schemas |
| VLA-REPLICA: A Low-Cost, Reproducible Benchmark for Real-World Evaluation of Vision-Language-Action Models | arXiv + official project | [vla-replica-2026.md](../paper_reads/E_evaluation_data_infrastructure/vla-replica-2026.md) | 10 real-world tasks with ID/OOD protocols and reproducibility checks | standardized low-cost physical setup and evaluation protocol | measure VLA performance in a reproducible real-world setting | brings affordability and cross-site reproducibility into real-world VLA benchmarking | 4 | not_applicable | strong real-world evaluation template for low-cost embodied testing |

## Watchlist

- `Cosmos-Reason1: From Physical Common Sense To Embodied Reasoning`
  Source: https://arxiv.org/abs/2503.15558
  Reason: official and influential, but closer to embodied reasoning background than to the repository's current executable-world, spatial-to-action, or action-model priorities.

## Followed Sources Checked

| Source | Status | New signal | Notes |
|---|---|---|---|
| NVIDIA Cosmos / Isaac / GR00T research | checked | Cosmos-Predict2.5 | strongest accepted D-branch signal this run |
| Ai2 Embodied AI / PRIOR | checked | vla-eval | strongest accepted evaluation-infrastructure signal this run |
| MIT CSAIL / scene-generation line | checked | SceneCode | yielded the strongest structured executable-world addition |
| World-model / VLA benchmark cluster | checked | SpatialAct, VLA-REPLICA | produced one accepted C-branch benchmark and one accepted E-branch benchmark |
| Remaining core source groups | spot_checked | none accepted | checked for 2024+ primary-source additions; no additional candidates cleared the harness |

## Undecided

No candidate required a local-only undecided dossier in this run.

## Top Demos

1. Cosmos-Predict2.5 for the clearest official world-model release evidence and action-conditioned rollout visuals.
2. SimWorld Studio for the strongest PCG-style embodied environment generation and evolution evidence.
3. SceneCode for the clearest representation-level view of executable scene editing.

## Collection Notes

- Related-work usefulness: SceneCode gives the repo a clean structured-world-program reference that complements simulator-ready reconstruction papers.
- Baseline usefulness: vla-eval and VLA-REPLICA together improve both simulation-facing and real-world VLA evaluation coverage.
- Evidence gaps to check before citing: exact repository maturity for SceneCode, exact evolving benchmark counts for vla-eval, and long-term adoption signals for VLA-REPLICA.

## Validation

- System run validation: passed via `python3 scripts/validate_run.py 2026-06-29`
- Registry validation: passed via `python3 scripts/validate_registry.py`
- Full repository validation: passed via `REQUIRE_UNDECIDED_DOSSIERS=1 python3 scripts/validate_all.py`
- Source quality: all accepted papers use primary or official sources
- Duplicate check: passed manual registry/title check during this run
- Harness exceptions: none
