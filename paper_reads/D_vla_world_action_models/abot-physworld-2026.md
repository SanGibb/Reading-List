# ABot-PhysWorld: Interactive World Foundation Model for Robotic Manipulation with Physics Alignment

candidate_id: CAND-0004
branch: D
decision: accepted_for_registry

## Source Links

- Paper: https://arxiv.org/abs/2603.23376
- Code, data, model and demos: https://github.com/amap-cvlab/ABot-PhysWorld
- Benchmark: https://github.com/amap-cvlab/ABot-PhysWorld/tree/main/EZS-Bench

## TL;DR

ABot-PhysWorld is an open 14B action-conditioned robot-video world model trained on three million clips and aligned with physics-aware preference objectives. It couples unusually complete artifacts with strong demos and evaluation, while still inheriting the gap between convincing video and executable physical dynamics.

## Novelty

- Decoupled DPO discriminators suppress physical violations without collapsing visual quality.
- Parallel context blocks inject spatial robot actions across embodiments.
- EZS-Bench evaluates unseen robot-task-scene combinations independently of training data.

## Contributions

1. Large physics-annotated robot-video corpus and 14B DiT model.
2. Open inference, SFT, DPO, model/data and evaluation stack.
3. Strong reported WorldArena and CVPR challenge results.

## Task

- Input: observed robot video/state, language and spatial action maps.
- Output: action-controllable future manipulation video.
- Setting: zero-shot and cross-embodiment manipulation.
- Success criterion: action alignment, physical plausibility, trajectory consistency and visual quality.

## Data

- Scale: three million curated manipulation clips with physics-aware annotation.
- Additional release: SFT data and EZS-Bench.
- Modalities: RGB video, action maps, text and robot/task/scene metadata.

## Method

- Fine-tune a 14B video DiT for robot futures.
- Encode action maps in a parallel context stream and inject through zero convolutions.
- Post-train with separate physics and quality preference discriminators.

## Key Figures / Architecture

figure_status: linked_official

- Figure / demo: action-control architecture and robot rollouts.
- Source: https://github.com/amap-cvlab/ABot-PhysWorld
- What it shows: action-map conditioning path and generated manipulation sequences.
- Why it matters: makes the action/world coupling implementable and inspectable.

## Evidence Trail

| Claim | Source | Status | Notes |
|---|---|---|---|
| Three million clips / 14B model | arXiv paper | verified | Stated in abstract. |
| Open training, inference, data, model and benchmark | official repository | verified | Release paths inspected. |
| Leaderboard/challenge placement | official repository | verified | Treated as author-reported. |

## Evidence

- Main metrics: PBench, EZS-Bench, WorldArena and challenge scores.
- Qualitative results: clear action-controlled bimanual/object rollouts.
- Ablations: physics-aware DPO and action-injection components.
- Reproducibility signals: unusually complete public stack.

## Limitations

- 14B training and inference are costly.
- Author-reported leaderboard positions need version-pinned reproduction.
- Video rollouts do not expose a collision/contact state suitable for certification.

## Project Relevance

- Open baseline for action-conditioned embodied world models.
- Reusable fields: ActionMap, FutureVideo, PhysicsPreference and CrossEmbodimentCondition.
- EZS-Bench supports zero-shot evaluation design.

## Reproduction / Follow-up

- Pin checkpoints/datasets and reproduce EZS-Bench.
- Compare rollout scores with real policy execution on matched tasks.

