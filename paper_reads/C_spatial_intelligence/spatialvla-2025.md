# SpatialVLA: Exploring Spatial Representations for Visual-Language-Action Models

candidate_id: CAND-0010
branch: C. Spatial Intelligence
decision: accepted_for_registry
registry_status: update

## Source Links

- Paper: https://arxiv.org/abs/2501.15830
- Project: https://spatialvla.github.io/
- Code / release: https://github.com/SpatialVLA/SpatialVLA
- Demo / video: https://spatialvla.github.io/
- Official figure / architecture: https://spatialvla.github.io/static/images/pipeline.png
- Registry URL: https://arxiv.org/abs/2501.15830

## TL;DR

SpatialVLA connects the spatial-intelligence branch to action. It is especially relevant because our generated worlds need agents that can interpret spatial relations like closest, on, in, left/right, and convert them into actions.

## Novelty

- What is actually new: injects explicit 3D spatial context and adaptive action grids into VLA policy learning.
- Difference from prior work: it adds executable, interactive, physical, spatial, or policy-facing structure rather than stopping at static visual quality.
- Why the delta matters: our repository needs works that can become fields, validators, baselines, or generation targets for interactive embodied worlds.

## Contributions

1. Pretrains a spatial VLA on 1.1M real robot episodes.
2. Adds Ego3D position encoding and adaptive spatial grids.
3. Shows improved spatial prompt handling and zero-shot generalization.

## Task

- Input: paper-specific observations, prompts, scenes, assets, robot data, or benchmark tasks.
- Output: spatially grounded generalist manipulation and spatial-prompt execution.
- Setting: RSS / 2025 frontier work, primary branch C with secondary fit D.
- Success criterion: reported benchmark success, qualitative/demo quality, or usefulness as an executable-world data/model/evaluation component.

## Data

- Dataset / benchmark: 1.1M real robot episodes and evaluations across 7 robot learning scenarios, 16 real-robot tasks, and 48 simulation setups.
- Scale: see official paper/project for exact splits; collection-critical scale claims are recorded in the evidence trail below.
- Modalities: 3D geometry, language, scene assets, robot observations/actions, physics/material labels, or benchmark annotations depending on the paper.
- Collection / annotation: primary source reports official construction process; this run did not reproduce the full dataset locally.
- Splits / evaluation protocol: follow the paper/project protocol before using exact numbers in a manuscript.

## Method

- Core pipeline: VLA with 3D Ego3D position encoding and adaptive spatial action grids for spatial action token prediction.
- Model / representation: the work contributes a representation, generator, policy model, or evaluation platform aligned with interactive embodied generation.
- Training or optimization: use the official paper for training schedules; this report records the method-level shape and acceptance evidence.
- Inference / deployment: intended use is as a generator, policy baseline, simulator-ready asset source, spatial-action model, or benchmark component.
- Losses or metrics: central reported metrics are in the paper/project; do not cite precise values without checking the PDF tables.

## Key Figures / Architecture

figure_status: linked_official

- Figure / demo: official project architecture, teaser, benchmark overview, or qualitative demo.
- Source: https://spatialvla.github.io/static/images/pipeline.png
- Render:
  ![SpatialVLA key figure](https://spatialvla.github.io/static/images/pipeline.png)
- What it shows: the artifact most directly supporting the accepted claim for this knowledge-base entry.
- Why it matters: it gives a visual or structural anchor for judging whether the paper is usable for our interactive generation / embodied intelligence tasks.

## Evidence Trail

| Claim | Source | Status | Notes |
|---|---|---|---|
| Paper/source is primary or official. | https://arxiv.org/abs/2501.15830 | verified | Used as registry URL or paper source. |
| Project/demo evidence exists. | https://spatialvla.github.io/ | verified | Demo score 4; visual decision: strong visual/demo evidence from official project page. |
| Data / benchmark / method relevance. | https://spatialvla.github.io/ | partial | Summary follows official page and arXiv/proceedings; exact numerical claims should be checked in the PDF before citation. |
| Key visual or architecture evidence. | https://spatialvla.github.io/static/images/pipeline.png | verified | Official linked figure/demo; no local reproduction was performed. |

## Evidence

- Main metrics: Project page reports evaluations over 7 scenarios, 16 real tasks, and 48 simulation setups, with highlighted spatial-understanding gains and real robot demos.
- Qualitative results: official project page provides visual/demo material used for this acceptance decision.
- Ablations: not exhaustively audited in this initialization pass; check the PDF before using ablation numbers.
- Baselines: paper/project compares against relevant prior methods; this report records only acceptance-level evidence.
- Reproducibility signals: source quality `primary_or_official`, evidence strength 4, demo score 4.

## Limitations

- Method limitations: Spatial improvements are evaluated in VLA settings; it does not itself generate scenes or verify physical world validity.
- Experimental limitations: this initialization run did not run code, download datasets, or reproduce metrics.
- Demo / visual limitations: official demo material can be curated; use local reproduction or independent videos before making strong claims.
- Claims that remain unverified: exact numeric tables, benchmark splits, compute/data cost, and robustness beyond official examples.

## Project Relevance

- Relevance to interactive embodied generation: Useful for Scene.spatial_graph, Ego3DEncoding, SpatialActionToken, and spatial instruction validation.
- Reusable fields: `Scene`, `Object`, `Part`, `Affordance`, `PhysicalProperty`, `SpatialRelation`, `Task`, `Trajectory`, `Policy`, `ValidationReport` as applicable.
- Possible baseline role: use as a baseline, source of validators, dataset schema, or quality bar for generated-world demos.
- Implications for our task / benchmark: keep only if future generated worlds can expose comparable fields or be evaluated by comparable tasks.

## Reproduction / Follow-up

- What to check before using: inspect the PDF tables, released code/data, license, and exact benchmark protocol.
- Code / checkpoint availability: see Source Links; this report only verifies that an official link exists when listed.
- Citation or related-work caveats: phrase central claims as reported by the authors unless reproduced locally.
