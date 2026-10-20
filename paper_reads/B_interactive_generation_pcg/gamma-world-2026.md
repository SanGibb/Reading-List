# Gamma-World: Generative Multi-Agent World Modeling Beyond Two Players

<!-- curation-review:start -->
> 2026-10-20 按新版标准复审：**待视觉复核**。Permutation-equivalent agent encoding and linear hub communication are substantial multi-agent world components. Temporal cross-view identity/consistency and speed claims need actual sample inspection.
> [本次来源、分数与任务判断](../library_review.md#paper-dd563d0a7a59)。下文保留原精读；旧验收标签不代表本次重新通过，所有实验仍为作者报告。
<!-- curation-review:end -->

candidate_id: CAND-0005
branch: B
decision: accepted_for_registry

## Source Links

- Paper: https://arxiv.org/abs/2605.28816
- Project / demos: https://research.nvidia.com/labs/sil/projects/gamma-world/
- Code: https://github.com/nv-tlabs/Gamma-World
- Training / inference guide: https://github.com/nv-tlabs/Gamma-World/blob/main/README.md

## TL;DR

Gamma-World generates one synchronized video world from multiple independent agent/action streams. Simplex agent encoding, hub-mediated communication, and causal distillation support permutation-equivalent agents, linear cross-agent attention cost, 24 FPS rollout, and zero-shot two-to-four-agent transfer. It fills a clear multi-agent gap, though the result remains a video simulator rather than explicit executable 3D physics.

## Novelty

- Extends action-conditioned video world models from a single controller to multiple independently controllable agents sharing one evolving world.
- Uses regular-simplex rotary phases to avoid fixed slot identities and arbitrary ordering.
- Uses sparse hubs rather than dense agent-to-agent attention.

## Contributions

1. Simplex Rotary Agent Encoding for permutation-equivalent identities.
2. Sparse Hub Attention with linear rather than quadratic scaling in agent count.
3. Bidirectional-teacher to block-causal-student distillation for real-time streaming.

## Task

- Input: synchronized multi-agent observations and action streams.
- Output: coherent future frames for every agent in one shared environment.
- Setting: multiplayer virtual worlds and real multi-robot scenarios.
- Success criterion: fidelity, action controllability, inter-agent consistency, scaling, and streaming speed.

## Data

- Synchronized two-agent gameplay and multi-agent interaction sequences.
- Evaluation includes zero-shot four-agent rollouts and physical multi-robot examples.
- The repository releases preprocessing, training, teacher/student, and inference workflows.

## Method

- Shared encoders tokenize each observation/action stream.
- Simplex rotary phases encode exchangeable agent identity.
- Learnable hub tokens aggregate and broadcast cross-agent information.
- A full-context diffusion teacher is distilled into a causal student with KV caching.

## Key Figures / Architecture

figure_status: linked_official

- Figure / demos: two-agent interaction, four-agent generalization, real-world robot coordination, and method panels.
- Source: https://research.nvidia.com/labs/sil/projects/gamma-world/
- What it shows: independent controls change each view while shared events remain synchronized.
- Why it matters: inter-agent consistency is visible rather than inferred from a scalar score alone.

## Evidence Trail

| Claim | Source | Status | Notes |
|---|---|---|---|
| Code and training pipeline released | https://github.com/nv-tlabs/Gamma-World | verified | Official NVIDIA repository. |
| 24 FPS causal streaming | https://arxiv.org/abs/2605.28816 | verified | Author-reported. |
| Two-to-four-agent zero-shot generalization | https://research.nvidia.com/labs/sil/projects/gamma-world/ | verified | Official gallery and paper. |

## Evidence

- Paper reports gains over slot-based and dense-attention baselines in fidelity, control, and consistency.
- Official galleries show two-agent control, four-agent transfer, and multi-robot coordination.
- Released code covers inference and training rather than only a presentation demo.

## Limitations

- Pixel/video consistency does not guarantee collision-free, physically valid, or simulator-executable state.
- Real-robot examples demonstrate coordination visually but do not establish broad policy utility.
- Four-agent evidence is extrapolation from two-agent training and needs broader stress tests.

## Project Relevance

- Direct reference for MultiAgentState, AgentIdentity, synchronized ActionStream, and SharedWorldConsistency fields.
- Strong interactive-generation baseline for multi-user or multi-robot worlds.
- Useful demonstration that scalable communication can be separated from agent slot identity.

## Reproduction / Follow-up

- Reproduce two-agent inference before training or four-agent transfer.
- Measure cross-view event consistency separately from perceptual quality.
- Add explicit physics and state-recovery diagnostics before using as an executable simulator.
