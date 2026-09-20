# SlugTrails: An Egocentric Benchmark for Floor Plan Localization in Large Buildings

candidate_id: CAND-0008
branch: E
decision: accepted_for_registry

## Source Links

- Paper: https://arxiv.org/abs/2609.19876
- Code / data / protocols: https://github.com/Head-inthe-Cloud/SlugTrails

## TL;DR

SlugTrails benchmarks egocentric floor-plan localization in large public buildings, where stock residential checkpoints nearly fail. It releases surveyed alignments and three sensing protocols across 22,089 square meters.

## Novelty

- Deployment-scale public-building rather than residential localization.
- One benchmark unifies single-frame, multi-view sweep, and sequential-odometry regimes.

## Contributions

1. Aria data across three buildings and six floors.
2. CAD-semantic floor plans with laser-surveyed alignment.
3. Released protocols/tools and five-system study.

## Task

- Input: limited-FOV egocentric image(s), optional odometry, and floor plan.
- Output: camera pose in the floor-plan frame.
- Success: recall under position/orientation thresholds.

## Data

30 Hz recordings covering 22,089 square meters of outline, semantic floor plans, circulation masks, and aligned trajectories.

## Method

Evaluation separates walking single frames, stationary sweeps, and walking streams so native sensing configurations remain comparable.

## Key Figures / Architecture

figure_status: linked_official

- Paper maps/protocols: https://arxiv.org/html/2609.19876
- Released tools: https://github.com/Head-inthe-Cloud/SlugTrails

## Evidence Trail

| Claim | Source | Status | Notes |
|---|---|---|---|
| 22,089 square meters, three buildings, six floors | https://arxiv.org/abs/2609.19876 | verified | Primary abstract. |
| Three sensing protocols | https://arxiv.org/abs/2609.19876 | verified | Primary paper. |
| Data/tools release | https://github.com/Head-inthe-Cloud/SlugTrails | verified | Official repository. |

## Evidence

- Stock checkpoints reach at most 0.004 R@1m30° on walking single frames.
- Fine-tuned sequential F3Loc rises from 0.03 to 0.66 and improves cross-dataset LaMAR results.

## Limitations

- Only three campus buildings.
- Hard single-frame performance remains low after fine-tuning.

## Project Relevance

Strong benchmark for map grounding, persistent spatial memory, egocentric localization, and multi-view accumulation.

## Reproduction / Follow-up

- Reproduce split/alignment tooling.
- Compare against VLM-based spatial agents as well as geometric localization systems.
