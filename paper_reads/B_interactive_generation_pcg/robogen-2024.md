# RoboGen: Towards Unleashing Infinite Data for Automated Robot Learning via Generative Simulation

candidate_id: CAND-0009
branch: B. Interactive Generation and PCG
decision: accepted_for_registry
registry_status: update

## Source Links

- Paper: https://arxiv.org/abs/2311.01455
- Project: https://robogen-ai.github.io/
- Code / release: https://github.com/Genesis-Embodied-AI/RoboGen
- Demo / video: https://robogen-ai.github.io/
- Official figure / architecture: https://robogen-ai.github.io/assets/images/long-horizon.png
- Registry URL: https://arxiv.org/abs/2311.01455

## TL;DR

RoboGen is the clearest agentic PCG baseline for robotics. It treats generation as a closed loop over tasks, scenes, supervision, and learning, which is close to our desired automated interactive-generation workflow.

## Novelty

- What is actually new: closes the loop from task proposal to simulated environment to training supervision and learned skill.
- Difference from prior work: it adds executable, interactive, physical, spatial, or policy-facing structure rather than stopping at static visual quality.
- Why the delta matters: our repository needs works that can become fields, validators, baselines, or generation targets for interactive embodied worlds.

## Contributions

1. Defines a self-guided propose-generate-learn pipeline.
2. Generates diverse tasks, scenes, decompositions, and supervision.
3. Shows long-horizon and object-interaction examples across manipulation and locomotion.

## Task

- Input: paper-specific observations, prompts, scenes, assets, robot data, or benchmark tasks.
- Output: automated generation of robot learning tasks and policy training data.
- Setting: ICML / 2024 frontier work, primary branch B with secondary fit D, E.
- Success criterion: reported benchmark success, qualitative/demo quality, or usefulness as an executable-world data/model/evaluation component.

## Data

- Dataset / benchmark: automatically generated tasks, scenes, training supervisions, demonstrations, and learned robotic skills in simulation.
- Scale: see official paper/project for exact splits; collection-critical scale claims are recorded in the evidence trail below.
- Modalities: 3D geometry, language, scene assets, robot observations/actions, physics/material labels, or benchmark annotations depending on the paper.
- Collection / annotation: primary source reports official construction process; this run did not reproduce the full dataset locally.
- Splits / evaluation protocol: follow the paper/project protocol before using exact numbers in a manuscript.

## Method

- Core pipeline: propose-generate-learn loop using foundation/generative models, task decomposition, scene generation, supervision generation, and policy learning.
- Model / representation: the work contributes a representation, generator, policy model, or evaluation platform aligned with interactive embodied generation.
- Training or optimization: use the official paper for training schedules; this report records the method-level shape and acceptance evidence.
- Inference / deployment: intended use is as a generator, policy baseline, simulator-ready asset source, spatial-action model, or benchmark component.
- Losses or metrics: central reported metrics are in the paper/project; do not cite precise values without checking the PDF tables.

## Key Figures / Architecture

figure_status: linked_official

- Figure / demo: official project architecture, teaser, benchmark overview, or qualitative demo.
- Source: https://robogen-ai.github.io/assets/images/long-horizon.png
- Render:
  ![RoboGen key figure](https://robogen-ai.github.io/assets/images/long-horizon.png)
- What it shows: the artifact most directly supporting the accepted claim for this knowledge-base entry.
- Why it matters: it gives a visual or structural anchor for judging whether the paper is usable for our interactive generation / embodied intelligence tasks.

## Evidence Trail

| Claim | Source | Status | Notes |
|---|---|---|---|
| Paper/source is primary or official. | https://arxiv.org/abs/2311.01455 | verified | Used as registry URL or paper source. |
| Project/demo evidence exists. | https://robogen-ai.github.io/ | verified | Demo score 4; visual decision: strong visual/demo evidence from official project page. |
| Data / benchmark / method relevance. | https://robogen-ai.github.io/ | partial | Summary follows official page and arXiv/proceedings; exact numerical claims should be checked in the PDF before citation. |
| Key visual or architecture evidence. | https://robogen-ai.github.io/assets/images/long-horizon.png | verified | Official linked figure/demo; no local reproduction was performed. |

## Evidence

- Main metrics: ICML 2024; project page lists many generated manipulation/locomotion tasks and shows long-horizon decompositions and gallery examples.
- Qualitative results: official project page provides visual/demo material used for this acceptance decision.
- Ablations: not exhaustively audited in this initialization pass; check the PDF before using ablation numbers.
- Baselines: paper/project compares against relevant prior methods; this report records only acceptance-level evidence.
- Reproducibility signals: source quality `primary_or_official`, evidence strength 4, demo score 4.

## Limitations

- Method limitations: Generated tasks and learned skills still depend heavily on simulator coverage, asset validity, and automated reward/supervision quality.
- Experimental limitations: this initialization run did not run code, download datasets, or reproduce metrics.
- Demo / visual limitations: official demo material can be curated; use local reproduction or independent videos before making strong claims.
- Claims that remain unverified: exact numeric tables, benchmark splits, compute/data cost, and robustness beyond official examples.

## Project Relevance

- Relevance to interactive embodied generation: Directly motivates TaskGenerator, SceneGenerator, SupervisionGenerator, PolicyLearner, and validation-loop abstractions.
- Reusable fields: `Scene`, `Object`, `Part`, `Affordance`, `PhysicalProperty`, `SpatialRelation`, `Task`, `Trajectory`, `Policy`, `ValidationReport` as applicable.
- Possible baseline role: use as a baseline, source of validators, dataset schema, or quality bar for generated-world demos.
- Implications for our task / benchmark: keep only if future generated worlds can expose comparable fields or be evaluated by comparable tasks.

## Reproduction / Follow-up

- What to check before using: inspect the PDF tables, released code/data, license, and exact benchmark protocol.
- Code / checkpoint availability: see Source Links; this report only verifies that an official link exists when listed.
- Citation or related-work caveats: phrase central claims as reported by the authors unless reproduced locally.
