# Weekly Frontier Knowledge Expansion — 2026-08-24

This run checked all 16 core follow-source groups and spot-checked all five watch/meta groups before broad primary-source searches. Seven newly influential registry gaps passed every gate; no new candidate required an undecided dossier.

## Accepted

### A. Executable World Representation

- [WonderPlay](../paper_reads/A_executable_world_representation/wonderplay-2025.md) — hybrid multi-material physics and generative-video refinement for action-conditioned dynamic 3D scenes.

### B. Interactive Generation and PCG

- [WonderWorld](../paper_reads/B_interactive_generation_pcg/wonderworld-2024.md) — low-latency user-steered expansion of connected 3D worlds.

### D. VLA and World-Action Models

- [ABot-PhysWorld](../paper_reads/D_vla_world_action_models/abot-physworld-2026.md) — open physics-aligned action-to-video robot world model with EZS-Bench.
- [PAIWorld](../paper_reads/D_vla_world_action_models/paiworld-2026.md) — geometry-aware multi-view robot future generation.

### E. Evaluation and Data Infrastructure

- [PBench](../paper_reads/E_evaluation_data_infrastructure/pbench-2025.md) — physical-domain QA plus video-quality evaluation for world models.
- [PAI-Bench](../paper_reads/E_evaluation_data_infrastructure/pai-bench-2025.md) — generation, conditional-generation and understanding suite for Physical AI.
- [PhysBench](../paper_reads/E_evaluation_data_infrastructure/physbench-2025.md) — 10,002-example benchmark for physical properties, relations, scenes and dynamics.

## Followed Sources Checked

- Core: 16/16 checked.
- Watch/meta: 5/5 spot-checked.
- Primary/official sources only were used for acceptance evidence.

## Visual / Demo Review

- Strong: WonderWorld, WonderPlay, ABot-PhysWorld and PAIWorld.
- Not applicable: PBench, PAI-Bench and PhysBench are evaluation/data works.
- Undecided: none newly created; historical local-only dossiers remain unchanged.

## Watchlist / Rejected

- Gemini Robotics 2: official demos and metrics, but no paper-grade disclosure sufficient for registry acceptance.
- Infinigen 2.0 preview: meaningful code update, but not a distinct new paper/research object.
- No social-media-only claim was accepted.

## Top Demos

1. ABot-PhysWorld: open bimanual/action-controlled robot video rollouts plus training and evaluation artifacts.
2. PAIWorld: synchronized multi-view futures and depth maps showing improved geometric agreement.
3. WonderPlay: action-driven dynamics over rigid, elastic, cloth, smoke, liquid and granular scenes.

## Top Project-Relevant Papers

1. WonderPlay for explicit material/force/state schemas and hybrid simulation.
2. PAIWorld for multi-camera geometry consistency before policy consumption.
3. PBench for separating physical-domain correctness from visual fidelity.

## Collection Notes

- WonderWorld is a strong interactive prototyping baseline, not a simulator-ready geometry guarantee.
- ABot-PhysWorld is the best reproduction candidate in this batch because its model/data/training/evaluation stack is open.
- PBench, PAI-Bench and PhysBench should be treated as complementary diagnostics; none alone proves closed-loop embodied competence.

## Validation

`REQUIRE_UNDECIDED_DOSSIERS=1 python3 scripts/validate_all.py` passed. Registry validation reports 96 papers; all run harnesses pass. Pre-existing missing local-PDF warnings remain.
