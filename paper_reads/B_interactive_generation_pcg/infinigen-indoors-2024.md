# Infinigen Indoors: Photorealistic Indoor Scenes using Procedural Generation

candidate_id: CAND-0008
branch: B. Interactive Generation and PCG
decision: accepted_for_registry
registry_status: addition

## Source Links

- Paper: https://openaccess.thecvf.com/content/CVPR2024/html/Raistrick_Infinigen_Indoors_Photorealistic_Indoor_Scenes_using_Procedural_Generation_CVPR_2024_paper.html
- Project: https://infinigen.org/
- Code / release: https://github.com/princeton-vl/infinigen
- Demo / video: https://infinigen.org/
- Official figure / architecture: https://infinigen.org/img/random_sample_indoors.jpeg
- Registry URL: https://arxiv.org/abs/2406.11824

## TL;DR

Infinigen Indoors is a high-quality PCG backbone. It is less interaction-specific than PhyScene, but its procedural control, real geometry, and dense annotations make it a strong source of scalable synthetic environments.

## Novelty

- What is actually new: extends Infinigen from natural worlds to indoor procedural scenes with real geometry and controllable annotations.
- Difference from prior work: it adds executable, interactive, physical, spatial, or policy-facing structure rather than stopping at static visual quality.
- Why the delta matters: our repository needs works that can become fields, validators, baselines, or generation targets for interactive embodied worlds.

## Contributions

1. Introduces procedural indoor assets and architecture elements.
2. Uses a constraint-based arrangement DSL and solver.
3. Exports dense annotations such as depth, normals, segmentation, optical flow, and scene flow.

## Task

- Input: paper-specific observations, prompts, scenes, assets, robot data, or benchmark tasks.
- Output: generate photorealistic indoor scenes and annotations for vision/embodied research.
- Setting: CVPR / 2024 frontier work, primary branch B with secondary fit A, E.
- Success criterion: reported benchmark success, qualitative/demo quality, or usefulness as an executable-world data/model/evaluation component.

## Data

- Dataset / benchmark: fully procedural indoor scenes, furniture, architecture elements, appliances, and dense synthetic labels from Blender.
- Scale: see official paper/project for exact splits; collection-critical scale claims are recorded in the evidence trail below.
- Modalities: 3D geometry, language, scene assets, robot observations/actions, physics/material labels, or benchmark annotations depending on the paper.
- Collection / annotation: primary source reports official construction process; this run did not reproduce the full dataset locally.
- Splits / evaluation protocol: follow the paper/project protocol before using exact numbers in a manuscript.

## Method

- Core pipeline: procedural indoor asset and layout generation with a constraint DSL and solver for scene composition.
- Model / representation: the work contributes a representation, generator, policy model, or evaluation platform aligned with interactive embodied generation.
- Training or optimization: use the official paper for training schedules; this report records the method-level shape and acceptance evidence.
- Inference / deployment: intended use is as a generator, policy baseline, simulator-ready asset source, spatial-action model, or benchmark component.
- Losses or metrics: central reported metrics are in the paper/project; do not cite precise values without checking the PDF tables.

## Key Figures / Architecture

figure_status: linked_official

- Figure / demo: official project architecture, teaser, benchmark overview, or qualitative demo.
- Source: https://infinigen.org/img/random_sample_indoors.jpeg
- Render:
  ![Infinigen Indoors key figure](https://infinigen.org/img/random_sample_indoors.jpeg)
- What it shows: the artifact most directly supporting the accepted claim for this knowledge-base entry.
- Why it matters: it gives a visual or structural anchor for judging whether the paper is usable for our interactive generation / embodied intelligence tasks.

## Evidence Trail

| Claim | Source | Status | Notes |
|---|---|---|---|
| Paper/source is primary or official. | https://openaccess.thecvf.com/content/CVPR2024/html/Raistrick_Infinigen_Indoors_Photorealistic_Indoor_Scenes_using_Procedural_Generation_CVPR_2024_paper.html | verified | Used as registry URL or paper source. |
| Project/demo evidence exists. | https://infinigen.org/ | verified | Demo score 4; visual decision: strong visual/demo evidence from official project page. |
| Data / benchmark / method relevance. | https://infinigen.org/ | partial | Summary follows official page and arXiv/proceedings; exact numerical claims should be checked in the PDF before citation. |
| Key visual or architecture evidence. | https://infinigen.org/img/random_sample_indoors.jpeg | verified | Official linked figure/demo; no local reproduction was performed. |

## Evidence

- Main metrics: CVPR 2024; official site emphasizes fully procedural generation, real geometry rather than fake bump detail, and customizable dense annotations.
- Qualitative results: official project page provides visual/demo material used for this acceptance decision.
- Ablations: not exhaustively audited in this initialization pass; check the PDF before using ablation numbers.
- Baselines: paper/project compares against relevant prior methods; this report records only acceptance-level evidence.
- Reproducibility signals: source quality `primary_or_official`, evidence strength 5, demo score 4.

## Limitations

- Method limitations: Procedural realism does not automatically imply affordance, task success, or contact-rich interaction validity; it needs additional interaction validators.
- Experimental limitations: this initialization run did not run code, download datasets, or reproduce metrics.
- Demo / visual limitations: official demo material can be curated; use local reproduction or independent videos before making strong claims.
- Claims that remain unverified: exact numeric tables, benchmark splits, compute/data cost, and robustness beyond official examples.

## Project Relevance

- Relevance to interactive embodied generation: Strong generator for Scene, Asset, Annotation, LayoutConstraint, and synthetic data pipelines.
- Reusable fields: `Scene`, `Object`, `Part`, `Affordance`, `PhysicalProperty`, `SpatialRelation`, `Task`, `Trajectory`, `Policy`, `ValidationReport` as applicable.
- Possible baseline role: use as a baseline, source of validators, dataset schema, or quality bar for generated-world demos.
- Implications for our task / benchmark: keep only if future generated worlds can expose comparable fields or be evaluated by comparable tasks.

## Reproduction / Follow-up

- What to check before using: inspect the PDF tables, released code/data, license, and exact benchmark protocol.
- Code / checkpoint availability: see Source Links; this report only verifies that an official link exists when listed.
- Citation or related-work caveats: phrase central claims as reported by the authors unless reproduced locally.
