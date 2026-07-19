# Frontier Knowledge Expansion Summary - 2026-07-19

This July 19, 2026 run adds **6 accepted papers** and requires **no undecided dossiers**. The selection boundary was the acceptance harness, not a fixed quota.

## Summary

- New accepted papers: `ESI-Bench`, `EmbodiedGen V2`, `Interactive World Simulator`, `World Pilot`, `Being-H0.7`, `Cosmos 3`
- Followed sources checked: all core source groups were checked or spot-checked; strongest accepted signals came from the Stanford SVL/BEHAVIOR line, NVIDIA Cosmos, TRI-linked robot world simulation, and broad primary-source VLA/world-model search
- Deep dives in `paper_reads/`: 6 new maintained reports
- Watchlist items: `pi0.7`, `Gemini Robotics ER 1.6`
- Strong demos: `Cosmos 3`, `Interactive World Simulator`, `EmbodiedGen V2`
- Undecided visual cases: none
- Collection notes: this run materially deepened branch-B world-engine coverage, branch-C active spatial-intelligence evaluation, and branch-D world-action/world-model integration coverage

## A. Executable World Representation

No new accepted additions this run.

## B. Interactive Generation and PCG

| Paper | Source | Deep dive | Data | Method | Task | Novelty | Demo | Visual | project relevance |
|---|---|---|---|---|---|---|---:|---|---|
| EmbodiedGen V2: An Agentic, Simulation-Ready 3D World Engine for Embodied AI | arXiv + official project + GitHub + Hugging Face | [embodiedgen-v2-2026.md](../paper_reads/B_interactive_generation_pcg/embodiedgen-v2-2026.md) | sim-ready asset, scene, and task-world generation pipeline with public Hugging Face collection and dataset for cross-simulator embodied world construction | unified generative world engine that composes sim-ready assets, editable scenes, task-driven worlds, dialogue-based state editing, and cross-simulator export into one closed-loop pipeline | turn text, images, and dialogue instructions into executable multi-room 3D worlds deployable across major simulators | pushes embodied world generation from isolated assets toward a reusable, agentic world engine that keeps affordances, state, layout stability, and simulator interfaces aligned | 5 | strong | Very strong fit for the repository’s interactive generation branch because it connects asset generation, affordance/state retention, and executable world assembly. |

## C. Spatial Intelligence

| Paper | Source | Deep dive | Data | Method | Task | Novelty | Demo | Visual | project relevance |
|---|---|---|---|---|---|---|---:|---|---|
| ESI-Bench: Towards Embodied Spatial Intelligence that Closes the Perception-Action Loop | arXiv + official project + GitHub | [esi-bench-2026.md](../paper_reads/C_spatial_intelligence/esi-bench-2026.md) | OmniGibson-grounded benchmark with 10 task categories, 29 subcategories, and 3,081 embodied spatial questions | recasts spatial intelligence as an active perception-action loop and evaluates embodied agents under controlled task families | answer embodied spatial questions that require choosing how to move, inspect, and manipulate the environment to uncover hidden facts | moves spatial intelligence benchmarking from passive or oracle-view settings into an embodied action loop | 4 | not_applicable | Strong benchmark reference for whether generated or reconstructed worlds preserve the active spatial structure needed for embodied decision-making. |

## D. VLA and World-Action Models

| Paper | Source | Deep dive | Data | Method | Task | Novelty | Demo | Visual | project relevance |
|---|---|---|---|---|---|---|---:|---|---|
| Interactive World Simulator for Robot Policy Training and Evaluation | arXiv + RSS project + GitHub | [interactive-world-simulator-2026.md](../paper_reads/D_vla_world_action_models/interactive-world-simulator-2026.md) | moderate-scale robot interaction dataset driving an action-conditioned video world model with multiple manipulation tasks | consistency models for latent dynamics and image decoding deployed as a fast learned interactive simulator | simulate long-horizon robot interaction rollouts for policy training and evaluation | uses a learned world model directly as an interactive simulator for policy loops | 5 | strong | High-value reference for learned world simulators that can sit directly inside embodied training and evaluation loops. |
| World Pilot: Steering Vision-Language-Action Models with World-Action Priors | arXiv + official project + GitHub + Hugging Face | [world-pilot-2026.md](../paper_reads/D_vla_world_action_models/world-pilot-2026.md) | LIBERO-Plus and real-robot evaluations paired with a world-action prior and public weights | injects a World-Action Model into a VLA through latent steering and action steering | improve manipulation policy quality by giving VLA policies anticipatory priors about scene evolution and motion | shows a concrete way to route world-model priors into a VLA without forcing slow explicit pixel rollouts | 4 | strong | Excellent fit for the world-action-model branch because it operationalizes how a learned world prior can improve a deployed VLA policy. |
| Being-H0.7: A Latent World-Action Model from Egocentric Videos | arXiv + official project + GitHub | [being-h0-7-2026.md](../paper_reads/D_vla_world_action_models/being-h0-7-2026.md) | large-scale egocentric video pretraining paired with robot-control evaluation and public code | latent world-action model that carries future-aware interaction structure into a deployable action prior | improve robot control by giving policies future-aware latent dynamics and task-progress signals | keeps predictive benefits of world modeling while moving the reasoning substrate from expensive pixel prediction into a compact latent control interface | 4 | strong | Useful anchor for compact world-action priors that keep embodied reasoning in the control loop without full pixel-rollout cost. |
| Cosmos 3: Omnimodal World Models for Physical AI | arXiv technical report + official NVIDIA page + GitHub + model cards | [cosmos-3-2026.md](../paper_reads/D_vla_world_action_models/cosmos-3-2026.md) | omnimodal physical-AI release surface spanning language, image, video, audio, and action sequences | unified mixture-of-transformers world-model family that jointly processes and generates multimodal physical-world sequences | support understanding, generation, simulation, and action inside one omnimodal world-model stack | collapses several separate embodied model classes into one omnimodal world-model family | 5 | strong | High-impact anchor for world-model systems that unify perception, simulation, and action rather than treating them as separate modules. |

## E. Evaluation and Data Infrastructure

No new accepted additions this run.

## Watchlist

- `pi0.7: General-purpose Robots Learn to Reason from Physical Experience`
  Source: https://www.pi.website/research/physical-reasoning
  Reason: important official signal, but the current public surface is still more release-oriented than the accepted paper-plus-project additions for this run.
- `Gemini Robotics ER 1.6`
  Source: https://deepmind.google/discover/blog/gemini-robotics-er-16/
  Reason: promising official robotics release, but the public technical surface remains less source-complete than the accepted additions.

## Followed Sources Checked

| Source | Status | New signal | Notes |
|---|---|---|---|
| Stanford SVL / BEHAVIOR / OmniGibson line | checked | ESI-Bench | strongest accepted spatial-intelligence signal in this run |
| NVIDIA Cosmos / Isaac / GR00T research | checked | Cosmos 3 | strongest accepted omnimodal world-model signal |
| TRI / robot-world simulation line | checked | Interactive World Simulator | strongest accepted learned-simulator signal |
| Broad primary-source VLA/world-model search | checked | World Pilot, Being-H0.7, EmbodiedGen V2 | strongest accepted D/B additions outside fixed-source hits |
| Remaining core source groups | spot_checked | pi0.7, Gemini Robotics ER 1.6 | useful watchlist signals, but no additional accepted paper-grade candidates |

## Undecided

No candidate required a local-only undecided dossier in this run.

## Top Demos

1. Cosmos 3 for the broadest official omnimodal physical-AI demo surface.
2. Interactive World Simulator for the clearest interactive learned-simulator evidence tied to policy training and evaluation.
3. EmbodiedGen V2 for the best end-to-end simulation-ready world-engine presentation.

## Collection Notes

- Related-work usefulness: ESI-Bench sharpens active spatial reasoning coverage, while World Pilot and Being-H0.7 provide cleaner references for compact world-action priors than generic pixel-rollout papers.
- Baseline usefulness: Interactive World Simulator is the strongest direct learned-simulator baseline in this run, and EmbodiedGen V2 is the best new branch-B world-engine baseline.
- Evidence gaps to check before citing: independent reproduction of Cosmos 3 capability claims, cross-simulator stress testing for EmbodiedGen V2, and reproduced LIBERO-Plus/real-robot gains for World Pilot.

## Validation

- System run validation: passed via `python3 scripts/validate_run.py 2026-07-19`
- Registry validation: passed via `python3 scripts/validate_registry.py`
- Full repository validation: passed via `REQUIRE_UNDECIDED_DOSSIERS=1 python3 scripts/validate_all.py`
- Source quality: all accepted papers use primary or official sources
- Duplicate check: passed manual registry/title check during this run
- Harness exceptions: none
