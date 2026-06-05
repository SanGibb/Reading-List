# PhysX-Omni: Unified Simulation-Ready Physical 3D Generation for Rigid, Deformable, and Articulated Objects

candidate_id: CAND-0003
branch: A. Executable World Representation
decision: accepted_for_registry
registry_status: update

## Source Links

- Paper: https://arxiv.org/abs/2605.21572
- Project: https://physx-omni.github.io/
- Code / release: https://github.com/ziangcao0312/PhysX-Omni
- Demo / video: https://physx-omni.github.io/
- Official figure / architecture: https://physx-omni.github.io/static/videos/framework.png
- Registry URL: https://arxiv.org/abs/2605.21572

## TL;DR

PhysX-Omni is a very recent but highly aligned physical-asset generation paper. It is especially important for soft/deformable directions because it treats deformable state as part of the same sim-ready asset problem as rigid and articulated objects.

## Novelty

- What is actually new: unifies rigid, deformable, and articulated physical 3D generation instead of treating them as separate asset categories.
- Difference from prior work: it adds executable, interactive, physical, spatial, or policy-facing structure rather than stopping at static visual quality.
- Why the delta matters: our repository needs works that can become fields, validators, baselines, or generation targets for interactive embodied worlds.

## Contributions

1. Builds a unified sim-ready generation target across rigid, deformable, and articulated objects.
2. Introduces PhysXVerse and PhysX-Bench with physical/functional dimensions.
3. Shows downstream potential for scene generation and robotic policy learning.

## Task

- Input: paper-specific observations, prompts, scenes, assets, robot data, or benchmark tasks.
- Output: generate simulation-ready physical 3D assets and evaluate physical/functional attributes.
- Setting: arXiv / 2026 frontier work, primary branch A with secondary fit B, E.
- Success criterion: reported benchmark success, qualitative/demo quality, or usefulness as an executable-world data/model/evaluation component.

## Data

- Dataset / benchmark: PhysXVerse plus PhysX-Bench for geometry, scale, material, affordance, kinematics, and function description across rigid, deformable, and articulated objects.
- Scale: see official paper/project for exact splits; collection-critical scale claims are recorded in the evidence trail below.
- Modalities: 3D geometry, language, scene assets, robot observations/actions, physics/material labels, or benchmark annotations depending on the paper.
- Collection / annotation: primary source reports official construction process; this run did not reproduce the full dataset locally.
- Splits / evaluation protocol: follow the paper/project protocol before using exact numbers in a manuscript.

## Method

- Core pipeline: VLM-oriented physical 3D generation with an efficient geometry representation and benchmarked physical attribute understanding.
- Model / representation: the work contributes a representation, generator, policy model, or evaluation platform aligned with interactive embodied generation.
- Training or optimization: use the official paper for training schedules; this report records the method-level shape and acceptance evidence.
- Inference / deployment: intended use is as a generator, policy baseline, simulator-ready asset source, spatial-action model, or benchmark component.
- Losses or metrics: central reported metrics are in the paper/project; do not cite precise values without checking the PDF tables.

## Key Figures / Architecture

figure_status: linked_official

- Figure / demo: official project architecture, teaser, benchmark overview, or qualitative demo.
- Source: https://physx-omni.github.io/static/videos/framework.png
- Render:
  ![PhysX-Omni key figure](https://physx-omni.github.io/static/videos/framework.png)
- What it shows: the artifact most directly supporting the accepted claim for this knowledge-base entry.
- Why it matters: it gives a visual or structural anchor for judging whether the paper is usable for our interactive generation / embodied intelligence tasks.

## Evidence Trail

| Claim | Source | Status | Notes |
|---|---|---|---|
| Paper/source is primary or official. | https://arxiv.org/abs/2605.21572 | verified | Used as registry URL or paper source. |
| Project/demo evidence exists. | https://physx-omni.github.io/ | verified | Demo score 4; visual decision: strong visual/demo evidence from official project page. |
| Data / benchmark / method relevance. | https://physx-omni.github.io/ | partial | Summary follows official page and arXiv/proceedings; exact numerical claims should be checked in the PDF before citation. |
| Key visual or architecture evidence. | https://physx-omni.github.io/static/videos/framework.png | verified | Official linked figure/demo; no local reproduction was performed. |

## Evidence

- Main metrics: PhysX-Bench covers six attributes: geometry, absolute scale, material, affordance, kinematics, and function description; project page shows qualitative generation and robotics application examples.
- Qualitative results: official project page provides visual/demo material used for this acceptance decision.
- Ablations: not exhaustively audited in this initialization pass; check the PDF before using ablation numbers.
- Baselines: paper/project compares against relevant prior methods; this report records only acceptance-level evidence.
- Reproducibility signals: source quality `primary_or_official`, evidence strength 4, demo score 4.

## Limitations

- Method limitations: Very recent arXiv work; independent reproduction and long-horizon robot use remain to be checked.
- Experimental limitations: this initialization run did not run code, download datasets, or reproduce metrics.
- Demo / visual limitations: official demo material can be curated; use local reproduction or independent videos before making strong claims.
- Claims that remain unverified: exact numeric tables, benchmark splits, compute/data cost, and robustness beyond official examples.

## Project Relevance

- Relevance to interactive embodied generation: Strong candidate for PhysicalProperty, Material, DeformableState, KinematicJoint, and simulator export fields.
- Reusable fields: `Scene`, `Object`, `Part`, `Affordance`, `PhysicalProperty`, `SpatialRelation`, `Task`, `Trajectory`, `Policy`, `ValidationReport` as applicable.
- Possible baseline role: use as a baseline, source of validators, dataset schema, or quality bar for generated-world demos.
- Implications for our task / benchmark: keep only if future generated worlds can expose comparable fields or be evaluated by comparable tasks.

## Reproduction / Follow-up

- What to check before using: inspect the PDF tables, released code/data, license, and exact benchmark protocol.
- Code / checkpoint availability: see Source Links; this report only verifies that an official link exists when listed.
- Citation or related-work caveats: phrase central claims as reported by the authors unless reproduced locally.
