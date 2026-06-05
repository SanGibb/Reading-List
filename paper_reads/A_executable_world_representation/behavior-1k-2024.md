# BEHAVIOR-1K: A Human-Centered, Embodied AI Benchmark with 1,000 Everyday Activities and Realistic Simulation

candidate_id: CAND-0002
branch: A. Executable World Representation
decision: accepted_for_registry
registry_status: update

## Source Links

- Paper: https://arxiv.org/abs/2403.09227
- Project: https://behavior.stanford.edu/
- Code / release: https://github.com/StanfordVL/OmniGibson
- Demo / video: https://behavior.stanford.edu/
- Official figure / architecture: https://behavior.stanford.edu/
- Registry URL: https://arxiv.org/abs/2403.09227

## TL;DR

BEHAVIOR-1K is the task-logic backbone for executable embodied worlds. It gives us a concrete target for what generated environments must support: objects, states, predicates, long-horizon goals, and physics-aware manipulation.

## Novelty

- What is actually new: scales executable household tasks with semantic and physical properties, including rigid bodies, deformables, and liquids.
- Difference from prior work: it adds executable, interactive, physical, spatial, or policy-facing structure rather than stopping at static visual quality.
- Why the delta matters: our repository needs works that can become fields, validators, baselines, or generation targets for interactive embodied worlds.

## Contributions

1. Defines 1000 human-grounded household activities.
2. Connects BDDL symbolic goal logic to OmniGibson simulation.
3. Exposes long-horizon manipulation and sim-to-real challenges for embodied AI.

## Task

- Input: paper-specific observations, prompts, scenes, assets, robot data, or benchmark tasks.
- Output: long-horizon household activity execution and evaluation in simulation.
- Setting: arXiv / 2024 frontier work, primary branch A with secondary fit E.
- Success criterion: reported benchmark success, qualitative/demo quality, or usefulness as an executable-world data/model/evaluation component.

## Data

- Dataset / benchmark: 1000 everyday activities, 50 scenes, more than 9000 objects, BDDL task predicates, and OmniGibson simulation support.
- Scale: see official paper/project for exact splits; collection-critical scale claims are recorded in the evidence trail below.
- Modalities: 3D geometry, language, scene assets, robot observations/actions, physics/material labels, or benchmark annotations depending on the paper.
- Collection / annotation: primary source reports official construction process; this run did not reproduce the full dataset locally.
- Splits / evaluation protocol: follow the paper/project protocol before using exact numbers in a manuscript.

## Method

- Core pipeline: human-centered task benchmark with formal predicate/task definitions and realistic simulator-backed execution.
- Model / representation: the work contributes a representation, generator, policy model, or evaluation platform aligned with interactive embodied generation.
- Training or optimization: use the official paper for training schedules; this report records the method-level shape and acceptance evidence.
- Inference / deployment: intended use is as a generator, policy baseline, simulator-ready asset source, spatial-action model, or benchmark component.
- Losses or metrics: central reported metrics are in the paper/project; do not cite precise values without checking the PDF tables.

## Key Figures / Architecture

figure_status: linked_official

- Figure / demo: official project architecture, teaser, benchmark overview, or qualitative demo.
- Source: https://behavior.stanford.edu/
- Render:
  ![BEHAVIOR-1K key figure](https://behavior.stanford.edu/)
- What it shows: the artifact most directly supporting the accepted claim for this knowledge-base entry.
- Why it matters: it gives a visual or structural anchor for judging whether the paper is usable for our interactive generation / embodied intelligence tasks.

## Evidence Trail

| Claim | Source | Status | Notes |
|---|---|---|---|
| Paper/source is primary or official. | https://arxiv.org/abs/2403.09227 | verified | Used as registry URL or paper source. |
| Project/demo evidence exists. | https://behavior.stanford.edu/ | verified | Demo score 3; visual decision: not applicable: benchmark/dataset/infrastructure work. |
| Data / benchmark / method relevance. | https://behavior.stanford.edu/ | partial | Summary follows official page and arXiv/proceedings; exact numerical claims should be checked in the PDF before citation. |
| Key visual or architecture evidence. | https://behavior.stanford.edu/ | verified | Official linked figure/demo; no local reproduction was performed. |

## Evidence

- Main metrics: 1000 activities, 50 scenes, 9000+ objects, BDDL predicates, and OmniGibson execution; reported experiments show current methods struggle with long-horizon tasks.
- Qualitative results: official project page provides visual/demo material used for this acceptance decision.
- Ablations: not exhaustively audited in this initialization pass; check the PDF before using ablation numbers.
- Baselines: paper/project compares against relevant prior methods; this report records only acceptance-level evidence.
- Reproducibility signals: source quality `primary_or_official`, evidence strength 5, demo score 3.

## Limitations

- Method limitations: It is a benchmark and simulator stack, not a generative method; transferring generated scenes into its task logic still needs robust asset/state annotation.
- Experimental limitations: this initialization run did not run code, download datasets, or reproduce metrics.
- Demo / visual limitations: official demo material can be curated; use local reproduction or independent videos before making strong claims.
- Claims that remain unverified: exact numeric tables, benchmark splits, compute/data cost, and robustness beyond official examples.

## Project Relevance

- Relevance to interactive embodied generation: Directly informs Task, StatePredicate, GoalCondition, SceneObject, PhysicalProperty, and validation protocol design.
- Reusable fields: `Scene`, `Object`, `Part`, `Affordance`, `PhysicalProperty`, `SpatialRelation`, `Task`, `Trajectory`, `Policy`, `ValidationReport` as applicable.
- Possible baseline role: use as a baseline, source of validators, dataset schema, or quality bar for generated-world demos.
- Implications for our task / benchmark: keep only if future generated worlds can expose comparable fields or be evaluated by comparable tasks.

## Reproduction / Follow-up

- What to check before using: inspect the PDF tables, released code/data, license, and exact benchmark protocol.
- Code / checkpoint availability: see Source Links; this report only verifies that an official link exists when listed.
- Citation or related-work caveats: phrase central claims as reported by the authors unless reproduced locally.
