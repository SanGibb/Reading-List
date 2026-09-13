# RoboMME: Benchmarking and Understanding Memory for Robotic Generalist Policies

## Source Links

- Paper: https://arxiv.org/abs/2603.04639
- Project, videos, models, and demo: https://robomme.github.io/
- Benchmark code: https://github.com/RoboMME/robomme_benchmark
- Dataset: https://huggingface.co/datasets/Yinpei/robomme_data_h5

## TL;DR

RoboMME is an ICML 2026 Oral benchmark that turns robot memory into 16 executable manipulation tasks spanning temporal counting, spatial permanence, object reference, and procedural imitation. It releases fixed splits, 1,600 demonstrations, code, models, videos, and an interactive VideoQA mode, then compares 14 memory-augmented pi0.5 variants.

## Novelty

It replaces narrow one-off memory tests with a cognitively motivated taxonomy and a controlled matrix of representation and integration choices, exposing that no single memory design dominates all task structures.

## Contributions

1. Four memory suites with four executable tasks each in ManiSkill/SAPIEN.
2. Fixed training/validation/test episodes and multiple action interfaces.
3. Fourteen memory-augmented VLA variants plus human/VideoQA diagnostics.
4. Public benchmark, policy-learning code, datasets, models, leaderboard, and demo.

## Task Definition

Given an instruction and an incrementally observed manipulation history, retain and use the relevant past event, location, object cue, or demonstrated procedure to choose or execute the correct action.

## Data / Dataset / Benchmark

RoboMME contains 16 tasks, 100 training demonstrations per task, and fixed 50-episode validation and test splits. The LeRobot version reports roughly 768K frames; the H5 release is 56.4 GB.

## Method / Pipeline

Tasks are grouped as Counting, Permanence, Reference, and Imitation. The MME-VLA suite tests symbolic and perceptual memory representations through prompt, token, and modulation-style integration on a pi0.5 backbone. The same environments also expose continuous, waypoint, and multiple-choice actions.

## Key Figures / Architecture

figure_status: not_applicable

This is benchmark infrastructure rather than a single model architecture. The official task taxonomy, rollout videos, result plots, and interactive demo are linked at https://robomme.github.io/.

## Evidence Trail

| Claim | Primary source | Status |
|---|---|---|
| 16 tasks across four memory types | https://arxiv.org/abs/2603.04639 | verified |
| 14 pi0.5-based memory variants | https://robomme.github.io/ | verified |
| 1,600 training demos and fixed splits | https://github.com/RoboMME/robomme_benchmark | verified |
| ICML 2026 Oral | https://robomme.github.io/ | verified |

## Evidence / Metrics / Qualitative Results

The official page reports 90.5% human success in online VideoQA and complementary strengths: symbolic memory favors event-salient/counting tasks, perceptual memory favors motion/time-sensitive tasks, and retrieval-style experience memory helps dynamic scene changes.

## Limitations

The benchmark is simulation-only, centers on one Panda/ManiSkill substrate and a pi0.5 experimental backbone, and currently supports imitation-learning spawning more fully than parallel RL. Successful planner demonstrations may underrepresent real failure diversity.

## Project Relevance

RoboMME contributes directly reusable TemporalMemory, SpatialPermanence, ObjectReference, ProceduralMemory, HistoryBudget, and MemoryIntegration dimensions for persistent embodied agents.

## Reproduction / Follow-up Notes

- Use Docker because the benchmark pins older NumPy/Gymnasium versions.
- Reproduce a symbolic and a perceptual baseline before adding new memory designs.
- Extend evaluation to distractor sessions, real rollouts, and world-model-generated histories.
