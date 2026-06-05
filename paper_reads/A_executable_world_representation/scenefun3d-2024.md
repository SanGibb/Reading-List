# SceneFun3D: Fine-Grained Functionality and Affordance Understanding in 3D Scenes

candidate_id: CAND-0001
branch: A. Executable World Representation
decision: accepted_for_registry
registry_status: update

## Source Links

- Paper: https://openaccess.thecvf.com/content/CVPR2024/html/Delitzas_SceneFun3D_Fine-Grained_Functionality_and_Affordance_Understanding_in_3D_Scenes_CVPR_2024_paper.html
- Project: https://scenefun3d.github.io/
- Code / release: https://github.com/SceneFun3D/scenefun3d
- Demo / video: https://www.youtube.com/watch?v=NA
- Official figure / architecture: https://scenefun3d.github.io/static/images/framework.png
- Registry URL: https://scenefun3d.github.io/

## TL;DR

SceneFun3D is a core representation paper for executable worlds: it tells us where an agent can interact, what action an element affords, and how that element moves. It is not a generator, but it is a high-value supervision source for turning generated or scanned scenes into action-ready worlds.

## Novelty

- What is actually new: moves 3D scene understanding from object-level semantics to actionable functional elements in real scanned indoor scenes.
- Difference from prior work: it adds executable, interactive, physical, spatial, or policy-facing structure rather than stopping at static visual quality.
- Why the delta matters: our repository needs works that can become fields, validators, baselines, or generation targets for interactive embodied worlds.

## Contributions

1. Creates a large real-scene dataset of functional interactive elements with affordance and motion labels.
2. Defines three tasks that connect 3D geometry, language, affordance, and action.
3. Provides closed/open-vocabulary baselines showing that fine-grained functionality remains hard.

## Task

- Input: paper-specific observations, prompts, scenes, assets, robot data, or benchmark tasks.
- Output: identify functional interactive elements, ground language tasks to affordance masks, and infer interaction motion parameters.
- Setting: CVPR Oral / 2024 frontier work, primary branch A with secondary fit B, C.
- Success criterion: reported benchmark success, qualitative/demo quality, or usefulness as an executable-world data/model/evaluation component.

## Data

- Dataset / benchmark: 710 high-resolution real-world indoor scenes with 14.8k functional interaction annotations, affordance labels, motion parameters, and task-language descriptions.
- Scale: see official paper/project for exact splits; collection-critical scale claims are recorded in the evidence trail below.
- Modalities: 3D geometry, language, scene assets, robot observations/actions, physics/material labels, or benchmark annotations depending on the paper.
- Collection / annotation: primary source reports official construction process; this run did not reproduce the full dataset locally.
- Splits / evaluation protocol: follow the paper/project protocol before using exact numbers in a manuscript.

## Method

- Core pipeline: large-scale 3D functionality annotation plus functionality segmentation, task-driven affordance grounding, and 3D motion estimation baselines.
- Model / representation: the work contributes a representation, generator, policy model, or evaluation platform aligned with interactive embodied generation.
- Training or optimization: use the official paper for training schedules; this report records the method-level shape and acceptance evidence.
- Inference / deployment: intended use is as a generator, policy baseline, simulator-ready asset source, spatial-action model, or benchmark component.
- Losses or metrics: central reported metrics are in the paper/project; do not cite precise values without checking the PDF tables.

## Key Figures / Architecture

figure_status: linked_official

- Figure / demo: official project architecture, teaser, benchmark overview, or qualitative demo.
- Source: https://scenefun3d.github.io/static/images/framework.png
- Render:
  ![SceneFun3D key figure](https://scenefun3d.github.io/static/images/framework.png)
- What it shows: the artifact most directly supporting the accepted claim for this knowledge-base entry.
- Why it matters: it gives a visual or structural anchor for judging whether the paper is usable for our interactive generation / embodied intelligence tasks.

## Evidence Trail

| Claim | Source | Status | Notes |
|---|---|---|---|
| Paper/source is primary or official. | https://openaccess.thecvf.com/content/CVPR2024/html/Delitzas_SceneFun3D_Fine-Grained_Functionality_and_Affordance_Understanding_in_3D_Scenes_CVPR_2024_paper.html | verified | Used as registry URL or paper source. |
| Project/demo evidence exists. | https://scenefun3d.github.io/ | verified | Demo score 3; visual decision: not applicable: benchmark/dataset/infrastructure work. |
| Data / benchmark / method relevance. | https://scenefun3d.github.io/ | partial | Summary follows official page and arXiv/proceedings; exact numerical claims should be checked in the PDF before citation. |
| Key visual or architecture evidence. | https://scenefun3d.github.io/static/images/framework.png | verified | Official linked figure/demo; no local reproduction was performed. |

## Evidence

- Main metrics: 710 scenes, 14.8k annotations, nine affordance categories, plus benchmark tasks for functionality segmentation, affordance grounding, and motion estimation.
- Qualitative results: official project page provides visual/demo material used for this acceptance decision.
- Ablations: not exhaustively audited in this initialization pass; check the PDF before using ablation numbers.
- Baselines: paper/project compares against relevant prior methods; this report records only acceptance-level evidence.
- Reproducibility signals: source quality `primary_or_official`, evidence strength 5, demo score 3.

## Limitations

- Method limitations: It is annotation and benchmark infrastructure rather than a scene generator; motion labels describe simple interaction primitives rather than full closed-loop manipulation policies.
- Experimental limitations: this initialization run did not run code, download datasets, or reproduce metrics.
- Demo / visual limitations: official demo material can be curated; use local reproduction or independent videos before making strong claims.
- Claims that remain unverified: exact numeric tables, benchmark splits, compute/data cost, and robustness beyond official examples.

## Project Relevance

- Relevance to interactive embodied generation: Defines reusable fields Object, Part, Affordance, FunctionalElement, TaskLanguage, MotionParameter for our typed interactive-world representation.
- Reusable fields: `Scene`, `Object`, `Part`, `Affordance`, `PhysicalProperty`, `SpatialRelation`, `Task`, `Trajectory`, `Policy`, `ValidationReport` as applicable.
- Possible baseline role: use as a baseline, source of validators, dataset schema, or quality bar for generated-world demos.
- Implications for our task / benchmark: keep only if future generated worlds can expose comparable fields or be evaluated by comparable tasks.

## Reproduction / Follow-up

- What to check before using: inspect the PDF tables, released code/data, license, and exact benchmark protocol.
- Code / checkpoint availability: see Source Links; this report only verifies that an official link exists when listed.
- Citation or related-work caveats: phrase central claims as reported by the authors unless reproduced locally.
