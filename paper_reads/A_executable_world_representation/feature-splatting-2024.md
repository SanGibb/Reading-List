# Feature Splatting: Language-Driven Physics-Based Scene Synthesis and Editing

candidate_id: CAND-0005
branch: A. Executable World Representation
decision: accepted_for_registry
registry_status: addition

## Source Links

- Paper: https://arxiv.org/abs/2404.01223
- Project: https://feature-splatting.github.io/
- Code / release: https://github.com/feature-splatting/feature-splatting
- Demo / video: https://feature-splatting.github.io/
- Official figure / architecture: https://feature-splatting.github.io/resources/physics_pipeline.jpg
- Registry URL: https://arxiv.org/abs/2404.01223

## TL;DR

Feature Splatting is valuable because it connects language, 3D representation, material properties, and physics simulation. It is not a full embodied generator, but it is a strong representation/tool line for turning reconstructed or generated scenes into editable physical worlds.

## Novelty

- What is actually new: turns 3DGS from a visual representation into a semantic/material/physics-aware editing and simulation substrate.
- Difference from prior work: it adds executable, interactive, physical, spatial, or policy-facing structure rather than stopping at static visual quality.
- Why the delta matters: our repository needs works that can become fields, validators, baselines, or generation targets for interactive embodied worlds.

## Contributions

1. Embeds object-centric VLM features into 3D Gaussians.
2. Uses text queries to decompose scenes and assign physical properties.
3. Demonstrates physics effects such as elastic stems, jelly motion, sand conversion, and falling objects.

## Task

- Input: paper-specific observations, prompts, scenes, assets, robot data, or benchmark tasks.
- Output: language-driven physics-based scene synthesis, editing, and material-aware simulation.
- Setting: ECCV / 2024 frontier work, primary branch A with secondary fit B, C.
- Success criterion: reported benchmark success, qualitative/demo quality, or usefulness as an executable-world data/model/evaluation component.

## Data

- Dataset / benchmark: 3D Gaussian scenes with distilled foundation-model features, text-grounded decomposition, material queries, and physics-simulation examples.
- Scale: see official paper/project for exact splits; collection-critical scale claims are recorded in the evidence trail below.
- Modalities: 3D geometry, language, scene assets, robot observations/actions, physics/material labels, or benchmark annotations depending on the paper.
- Collection / annotation: primary source reports official construction process; this run did not reproduce the full dataset locally.
- Splits / evaluation protocol: follow the paper/project protocol before using exact numbers in a manuscript.

## Method

- Core pipeline: feature-bearing 3D Gaussians plus text-query segmentation and particle-based physics simulation with automatically assigned material properties.
- Model / representation: the work contributes a representation, generator, policy model, or evaluation platform aligned with interactive embodied generation.
- Training or optimization: use the official paper for training schedules; this report records the method-level shape and acceptance evidence.
- Inference / deployment: intended use is as a generator, policy baseline, simulator-ready asset source, spatial-action model, or benchmark component.
- Losses or metrics: central reported metrics are in the paper/project; do not cite precise values without checking the PDF tables.

## Key Figures / Architecture

figure_status: linked_official

- Figure / demo: official project architecture, teaser, benchmark overview, or qualitative demo.
- Source: https://feature-splatting.github.io/resources/physics_pipeline.jpg
- Render:
  ![Feature Splatting key figure](https://feature-splatting.github.io/resources/physics_pipeline.jpg)
- What it shows: the artifact most directly supporting the accepted claim for this knowledge-base entry.
- Why it matters: it gives a visual or structural anchor for judging whether the paper is usable for our interactive generation / embodied intelligence tasks.

## Evidence Trail

| Claim | Source | Status | Notes |
|---|---|---|---|
| Paper/source is primary or official. | https://arxiv.org/abs/2404.01223 | verified | Used as registry URL or paper source. |
| Project/demo evidence exists. | https://feature-splatting.github.io/ | verified | Demo score 4; visual decision: strong visual/demo evidence from official project page. |
| Data / benchmark / method relevance. | https://feature-splatting.github.io/ | partial | Summary follows official page and arXiv/proceedings; exact numerical claims should be checked in the PDF before citation. |
| Key visual or architecture evidence. | https://feature-splatting.github.io/resources/physics_pipeline.jpg | verified | Official linked figure/demo; no local reproduction was performed. |

## Evidence

- Main metrics: Project page reports fast feature extraction, interactive NerfStudio editing, and multiple physics-simulation demos over Gaussian scenes and Objaverse assets.
- Qualitative results: official project page provides visual/demo material used for this acceptance decision.
- Ablations: not exhaustively audited in this initialization pass; check the PDF before using ablation numbers.
- Baselines: paper/project compares against relevant prior methods; this report records only acceptance-level evidence.
- Reproducibility signals: source quality `primary_or_official`, evidence strength 4, demo score 4.

## Limitations

- Method limitations: Physics is demonstrated in selected examples; robustness for large cluttered embodied environments and robot-policy training is not yet established.
- Experimental limitations: this initialization run did not run code, download datasets, or reproduce metrics.
- Demo / visual limitations: official demo material can be curated; use local reproduction or independent videos before making strong claims.
- Claims that remain unverified: exact numeric tables, benchmark splits, compute/data cost, and robustness beyond official examples.

## Project Relevance

- Relevance to interactive embodied generation: Useful for SceneRepresentation, MaterialProperty, SegmentByText, PhysicsEdit, and simulator-backed validation.
- Reusable fields: `Scene`, `Object`, `Part`, `Affordance`, `PhysicalProperty`, `SpatialRelation`, `Task`, `Trajectory`, `Policy`, `ValidationReport` as applicable.
- Possible baseline role: use as a baseline, source of validators, dataset schema, or quality bar for generated-world demos.
- Implications for our task / benchmark: keep only if future generated worlds can expose comparable fields or be evaluated by comparable tasks.

## Reproduction / Follow-up

- What to check before using: inspect the PDF tables, released code/data, license, and exact benchmark protocol.
- Code / checkpoint availability: see Source Links; this report only verifies that an official link exists when listed.
- Citation or related-work caveats: phrase central claims as reported by the authors unless reproduced locally.
