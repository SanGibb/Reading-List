# Rolling-WAM: World Action Models with Rolling Imagination

<!-- curation-review:start -->
> 2026-10-20 按新版标准复审：**观察名单**。staggered-noise滑窗提供4.5x steady-state速度，属于有用推理优化；本轮无同硬件warm-up、观测新鲜度与突变场景证据，不能仅速度四分。
> [本次来源、分数与任务判断](../library_review.md#paper-fd40fdd41dea)。下文保留原精读；旧验收标签不代表本次重新通过，所有实验仍为作者报告。
<!-- curation-review:end -->

candidate_id: CAND-0005
branch: D
decision: accepted_for_registry

## Source Links

- Paper: https://arxiv.org/abs/2609.30247
- Project / figures / demos: https://rolling-wam.github.io/
- Code: linked from the official project page

## TL;DR

Rolling-WAM amortizes joint video-action denoising across control cycles: imminent actions finish denoising while farther futures remain partially refined and roll forward. It delivers a reported 4.5x replanning speedup with competitive success, though some direct comparison videos remain pending.

## Novelty

- Maintains a sliding window of video/action chunks at staggered noise levels.
- Carries partially denoised future context across replans instead of restarting.
- Uses chunk-wise masking and noise conditioning in a mixture-of-transformers WAM.

## Contributions

1. Rolling inference schedule for joint WAMs.
2. LIBERO, RoboTwin 2.0, and real Unitree G1 evaluation.
3. Public implementation and precise latency accounting.

## Task

- Input: current image, language/state conditioning, and retained noisy future chunks.
- Output: an executable next action chunk plus progressively refined future chunks.
- Setting: closed-loop robot manipulation.
- Success criterion: task success under low steady-state replanning latency.

## Data

- LIBERO, RoboTwin 2.0, and three real G1 task families (doll placement, plate stacking, bead pouring).

## Method

- Video and action experts share a rolling window.
- The imminent chunk is fully denoised; later chunks receive partial refinement.
- Execution adds a fresh observation and shifts the window.

## Key Figures / Architecture

figure_status: linked_official

- Figure / demo: interactive rolling-window animation and architecture.
- Source: https://rolling-wam.github.io/
- What it shows: how denoising work is distributed across control cycles.

## Evidence Trail

| Claim | Source | Status | Notes |
|---|---|---|---|
| 4.5x steady-state replanning speedup | https://rolling-wam.github.io/ | verified | 215 ms vs 978 ms in controlled setup. |
| 98.1% LIBERO / 93.3% RoboTwin / 85.0% G1 | https://rolling-wam.github.io/ | verified | Official reported averages. |
| Code available | https://rolling-wam.github.io/ | verified | Official code link. |

## Evidence

- Latency includes visual encoding and denoising on one A100, excluding warm-up/initialization.
- Success remains competitive across simulated and physical settings.

## Limitations

- Some comparison videos are marked coming soon.
- Retained future chunks can become stale under abrupt observation changes.

## Project Relevance

Useful fields include `PredictionChunk`, `NoiseLevel`, `RollingWindow`, `ReplanLatency`, and `RetainedFutureContext`.

## Reproduction / Follow-up

- Preserve the paper's latency accounting when comparing systems.
- Stress-test unexpected contacts and observation discontinuities.

