# AgriGen: Large-Scale Scene Generation Framework for Photorealistic Agricultural Robotics Simulation

<!-- curation-review:start -->
> 2026-10-20 按新版标准复审：**观察名单**。Agricultural parameterized scenes are relevant but domain-specialized; verified abstract supplies no reusable release, controlled policy gains or sim-to-real evidence that clears core thresholds. Workshop prestige alone does not raise impact.
> [本次来源、分数与任务判断](../library_review.md#paper-a3a413137f1d)。下文保留原精读；旧验收标签不代表本次重新通过，所有实验仍为作者报告。
<!-- curation-review:end -->

candidate_id: CAND-0002
branch: B
decision: accepted_for_registry

## Source Links

- Paper: https://arxiv.org/abs/2609.25725
- Project / official figures: https://baj31415.github.io/agrigen/
- OpenReview: https://openreview.net/forum?id=VWDd4ueN2T

## TL;DR

AgriGen is a ROS-integrated Isaac Sim PCG framework for row crops, orchards, and vineyards with physics and domain randomization. It is a useful domain-specific executable-world generator with convincing scene/layout samples, but code, data, and documentation are still marked coming soon.

## Novelty

- Encodes agricultural crop morphology, row layouts, scale, lighting, and physics as controllable simulation parameters.
- Targets seasonal and geographic data scarcity with repeatable procedural worlds.

## Contributions

1. Built-in row-crop, orchard, and vineyard generators.
2. ROS/Isaac Sim integration with photorealistic rendering and physics.
3. Layout and lighting randomization designed for robotics datasets and evaluation.

## Task

- Input: crop category, bed/row/plant counts, row shape, environment and lighting parameters.
- Output: executable agricultural simulation scenes.
- Setting: perception, navigation, and manipulation research in controlled field environments.
- Success criterion: scalable, diverse, physically simulated scene generation.

## Data

- Procedurally generated lemon/apple orchards, vineyards, sugar-beet and cabbage fields.
- The project shows straight, slightly curved, and curved layouts across multiple scales.

## Method

- Scene grammar exposes crop and row-layout parameters.
- Isaac Sim supplies assets, rendering, dynamics, and sensors; ROS connects robot stacks.
- Domain randomization includes layout and illumination conditions.

## Key Figures / Architecture

figure_status: linked_official

- Figure / demo: teaser, crop categories, layout grids, and lighting variants.
- Source: https://baj31415.github.io/agrigen/
- What it shows: adequate visual diversity and controllable layouts.
- Why it matters: demonstrates a usable PCG surface rather than a single static environment.

## Evidence Trail

| Claim | Source | Status | Notes |
|---|---|---|---|
| Physics-enabled ROS/Isaac Sim generator | https://arxiv.org/abs/2609.25725 | verified | Primary abstract/report. |
| ICRA workshop best applied contribution | https://baj31415.github.io/agrigen/ | verified | Official project page. |
| Code/data/docs public | https://baj31415.github.io/agrigen/ | partial | Listed as coming soon. |

## Evidence

- Official figures cover five crop types, variable row geometry, field scale, and illumination.
- Workshop award is a useful impact signal, but downstream robot metrics are absent.

## Limitations

- No current code/data release or reproducible benchmark.
- No downstream policy performance or sim-to-real study on the project page.
- Agricultural specialization limits direct transfer to indoor worlds.

## Project Relevance

Reusable fields include `CropType`, `Bed`, `RowCurve`, `PlantSpacing`, `Lighting`, `Terrain`, `PhysicsConfig`, and `DomainRandomizationSeed`.

## Reproduction / Follow-up

- Recheck the release links before treating the framework as reproducible.
- Evaluate navigation/perception robustness across generated parameter sweeps.

