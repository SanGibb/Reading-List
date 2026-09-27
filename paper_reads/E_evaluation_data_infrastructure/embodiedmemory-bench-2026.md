# EmbodiedMemory-Bench: Benchmarking Embodied Memory for Long-Horizon Embodied Tasks

candidate_id: CAND-0008
branch: E
decision: accepted_for_registry

## Source Links

- Paper: https://arxiv.org/abs/2609.28236
- Project: https://zju-omniai.github.io/EmbodiedMemoryBench/
- Code: https://github.com/ZJU-OmniAI/Embodied-Omni
- Data: https://huggingface.co/datasets/lzLiang/EmbodiedMemoryBench

## TL;DR

EMem-Bench uses 2,554 executable episodes to test whether an embodied agent remembers details, tracks state changes, learns from failed interactions, and transfers learned rules. It is directly useful for persistent-world evaluation; simulator dependence and a noncommercial data license are the main caveats.

## Novelty

- Tests memory through later action in an environment, not static recall alone.
- Separates passive observation, dynamic tracking, interaction-derived state, and experience generalization.
- Supplies external-memory and trained 8B policy baselines.

## Contributions

1. 2,554 executable long-horizon episodes.
2. Spatial, event, and scene memory abstraction.
3. Released media/data plus SR and Error Recurrence Rate protocols.

## Task

- Input: multimodal interaction history without knowledge of the future task.
- Output: later environment actions using remembered and updated state.
- Setting: AI2-THOR and ProcTHOR.
- Success criterion: success rate up; recurrence of known errors down.

## Data

- 1,036 passive-observation and 1,052 dynamic-tracking episodes plus interaction-failure and experience-generalization families.
- Official dataset is 46.9 GB and licensed CC BY-NC 4.0.

## Method

- EMem organizes experience into spatial, event, and scene memories.
- EMem-8B learns to manage and consume these memories.
- Evaluation reports family scores and an equal-family macro average.

## Key Figures / Architecture

figure_status: linked_official

- Figure / demo: four challenge diagram and executable episode media.
- Source: https://huggingface.co/datasets/lzLiang/EmbodiedMemoryBench
- What it shows: how past observation, change, failure, or rules affect later actions.

## Evidence Trail

| Claim | Source | Status | Notes |
|---|---|---|---|
| 2,554 episodes / four families | https://arxiv.org/abs/2609.28236 | verified | Primary report. |
| Complete episode/media package | https://huggingface.co/datasets/lzLiang/EmbodiedMemoryBench | verified | Official dataset card. |
| Simulator evaluation code | https://github.com/ZJU-OmniAI/Embodied-Omni | partial | Public interfaces; setup notes are staged. |

## Evidence

- Current MLLMs and multimodal memory systems remain uneven across the four challenges.
- EMem leads matched-backbone memory systems; EMem-8B improves over its backbone.

## Limitations

- Simulator and asset distributions constrain ecological validity.
- CC BY-NC 4.0 limits commercial reuse.
- Dataset card declares one complete evaluation split, not train/validation splits.

## Project Relevance

Directly maps to `SpatialMemory`, `EventMemory`, `SceneMemory`, `InteractionOutcome`, `StateUpdate`, and `ErrorRecurrence` validators.

## Reproduction / Follow-up

- Pin AI2-THOR/ProcTHOR versions and report family-macro metrics.
- Avoid training on the released evaluation episodes.

