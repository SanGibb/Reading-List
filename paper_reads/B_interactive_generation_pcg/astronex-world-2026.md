# Astronex-World 1.0: Real-Time Interactive World Model Foundation

<!-- curation-review:start -->
> 2026-10-20 按新版标准复审：**待视觉复核**。Open low-resource training and streaming controls are potentially reusable, but WBench/throughput numbers and curated gallery descriptions do not establish persistent action/world quality.
> [本次来源、分数与任务判断](../library_review.md#paper-60666a1018c8)。下文保留原精读；旧验收标签不代表本次重新通过，所有实验仍为作者报告。
<!-- curation-review:end -->

candidate_id: CAND-0005
branch: B
decision: accepted_for_registry

## Source Links

- Paper: https://arxiv.org/abs/2609.20034
- Project / demos: https://world.astronex.com.cn/
- Code: https://github.com/Astronex-Robotics/Astronex-World
- Models: https://huggingface.co/Astronex-Lab/Astronex-World

## TL;DR

Astronex-World is an open 5B controllable video-world family with both full-context and block-causal streaming variants. It supports camera trajectories, continuous actions, embodiment IDs, and inserted text events at reported 24 FPS; its video states are not explicit executable geometry.

## Novelty

- Unifies bidirectional generation and real-time causal streaming in one open family.
- Conditions every transformer layer on a 64-D action stream and camera geometry.
- Publishes a five-stage low-resource training/distillation recipe.

## Contributions

1. Open code and weights.
2. Real-time causal interactive generation.
3. Broad navigation, robotics, driving, and event-control demos.

## Task

- Input: prompt or image, camera trajectory, continuous action, embodiment ID, optional event.
- Output: persistent action-responsive video rollout.
- Success: visual quality, action/camera adherence, memory, and throughput.

## Data

Mixed controllable video domains; detailed composition should be rechecked before training reuse.

## Method

Wan2.2 prior with pose-aware rotary encoding, per-layer action modulation, block-causal attention/KV caching, few-step distillation, and asymmetric DMD/DMD2.

## Key Figures / Architecture

figure_status: linked_official

- Official gallery: https://world.astronex.com.cn/
- Architecture/training details: https://arxiv.org/html/2609.20034

## Evidence Trail

| Claim | Source | Status | Notes |
|---|---|---|---|
| Code and weights public | https://github.com/Astronex-Robotics/Astronex-World | verified | Official repository links models. |
| 24 FPS at 832x480 | https://arxiv.org/abs/2609.20034 | verified | Author-reported. |
| WBench Navi 73.5 / Full 70.0 | https://arxiv.org/abs/2609.20034 | verified | Not independently reproduced. |
| Diverse action-responsive videos | https://world.astronex.com.cn/ | verified | Official gallery inspected. |

## Evidence

- Strong, diverse demos with generally coherent navigation and event control.
- Public artifacts make the systems claim more reproducible than demo-only releases.

## Limitations

- Video world is not guaranteed physically valid or simulator executable.
- Some geometry/texture drift remains visible.

## Project Relevance

Open reference for `CameraControl`, `ActionStream`, `EmbodimentId`, `WorldEvent`, causal cache, and real-time rollout evaluation.

## Reproduction / Follow-up

- Reproduce WBench scores on released weights.
- Test closed-loop drift and action latency beyond curated gallery horizons.
