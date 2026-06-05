# Holodeck: Language Guided Generation of 3D Embodied AI Environments

candidate_id: CAND-0007
branch: B. Interactive Generation and PCG
decision: accepted_for_registry
registry_status: addition

## Source Links

- Paper: https://openaccess.thecvf.com/content/CVPR2024/html/Yang_Holodeck_Language_Guided_Generation_of_3D_Embodied_AI_Environments_CVPR_2024_paper.html
- Project: https://yueyang1996.github.io/holodeck/
- Code / release: https://github.com/allenai/Holodeck
- Demo / video: https://yueyang1996.github.io/holodeck/
- Official figure / architecture: https://yueyang1996.github.io/holodeck/static/images/objnav.jpg
- Registry URL: https://arxiv.org/abs/2312.09067

## TL;DR

Holodeck is a foundational language-to-embodied-environment generator. It is less physics-focused than PhyScene, but it gives a strong prompt-to-scene pipeline and proves that generated scenes can be useful for downstream embodied navigation.

## Novelty

- What is actually new: uses LLM commonsense plus constraint optimization to generate diverse interactive AI2-THOR environments from open-ended prompts.
- Difference from prior work: it adds executable, interactive, physical, spatial, or policy-facing structure rather than stopping at static visual quality.
- Why the delta matters: our repository needs works that can become fields, validators, baselines, or generation targets for interactive embodied worlds.

## Contributions

1. Generates diverse scene types and styles from language.
2. Optimizes object placement using LLM-generated spatial constraints.
3. Demonstrates downstream object-navigation gains in NoveltyTHOR.

## Task

- Input: paper-specific observations, prompts, scenes, assets, robot data, or benchmark tasks.
- Output: generate customized 3D embodied AI environments from natural language.
- Setting: CVPR / 2024 frontier work, primary branch B with secondary fit E.
- Success criterion: reported benchmark success, qualitative/demo quality, or usefulness as an executable-world data/model/evaluation component.

## Data

- Dataset / benchmark: language prompts, Objaverse assets, AI2-THOR environments, human evaluations, and NoveltyTHOR navigation benchmark.
- Scale: see official paper/project for exact splits; collection-critical scale claims are recorded in the evidence trail below.
- Modalities: 3D geometry, language, scene assets, robot observations/actions, physics/material labels, or benchmark annotations depending on the paper.
- Collection / annotation: primary source reports official construction process; this run did not reproduce the full dataset locally.
- Splits / evaluation protocol: follow the paper/project protocol before using exact numbers in a manuscript.

## Method

- Core pipeline: LLM-driven environment generation with spatial relational constraints, asset retrieval, layout optimization, and AI2-THOR integration.
- Model / representation: the work contributes a representation, generator, policy model, or evaluation platform aligned with interactive embodied generation.
- Training or optimization: use the official paper for training schedules; this report records the method-level shape and acceptance evidence.
- Inference / deployment: intended use is as a generator, policy baseline, simulator-ready asset source, spatial-action model, or benchmark component.
- Losses or metrics: central reported metrics are in the paper/project; do not cite precise values without checking the PDF tables.

## Key Figures / Architecture

figure_status: linked_official

- Figure / demo: official project architecture, teaser, benchmark overview, or qualitative demo.
- Source: https://yueyang1996.github.io/holodeck/static/images/objnav.jpg
- Render:
  ![Holodeck key figure](https://yueyang1996.github.io/holodeck/static/images/objnav.jpg)
- What it shows: the artifact most directly supporting the accepted claim for this knowledge-base entry.
- Why it matters: it gives a visual or structural anchor for judging whether the paper is usable for our interactive generation / embodied intelligence tasks.

## Evidence Trail

| Claim | Source | Status | Notes |
|---|---|---|---|
| Paper/source is primary or official. | https://openaccess.thecvf.com/content/CVPR2024/html/Yang_Holodeck_Language_Guided_Generation_of_3D_Embodied_AI_Environments_CVPR_2024_paper.html | verified | Used as registry URL or paper source. |
| Project/demo evidence exists. | https://yueyang1996.github.io/holodeck/ | verified | Demo score 4; visual decision: strong visual/demo evidence from official project page. |
| Data / benchmark / method relevance. | https://yueyang1996.github.io/holodeck/ | partial | Summary follows official page and arXiv/proceedings; exact numerical claims should be checked in the PDF before citation. |
| Key visual or architecture evidence. | https://yueyang1996.github.io/holodeck/static/images/objnav.jpg | verified | Official linked figure/demo; no local reproduction was performed. |

## Evidence

- Main metrics: Project page reports human preference over ProcTHOR for residential scenes and object-navigation gains on NoveltyTHOR.
- Qualitative results: official project page provides visual/demo material used for this acceptance decision.
- Ablations: not exhaustively audited in this initialization pass; check the PDF before using ablation numbers.
- Baselines: paper/project compares against relevant prior methods; this report records only acceptance-level evidence.
- Reproducibility signals: source quality `primary_or_official`, evidence strength 5, demo score 4.

## Limitations

- Method limitations: Physical interaction is limited by AI2-THOR asset/runtime support; generated layouts may not encode fine-grained affordance or material state.
- Experimental limitations: this initialization run did not run code, download datasets, or reproduce metrics.
- Demo / visual limitations: official demo material can be curated; use local reproduction or independent videos before making strong claims.
- Claims that remain unverified: exact numeric tables, benchmark splits, compute/data cost, and robustness beyond official examples.

## Project Relevance

- Relevance to interactive embodied generation: Important baseline for Prompt, SceneSpec, SpatialConstraint, AssetRetrieval, LayoutOptimization, and downstream embodied evaluation.
- Reusable fields: `Scene`, `Object`, `Part`, `Affordance`, `PhysicalProperty`, `SpatialRelation`, `Task`, `Trajectory`, `Policy`, `ValidationReport` as applicable.
- Possible baseline role: use as a baseline, source of validators, dataset schema, or quality bar for generated-world demos.
- Implications for our task / benchmark: keep only if future generated worlds can expose comparable fields or be evaluated by comparable tasks.

## Reproduction / Follow-up

- What to check before using: inspect the PDF tables, released code/data, license, and exact benchmark protocol.
- Code / checkpoint availability: see Source Links; this report only verifies that an official link exists when listed.
- Citation or related-work caveats: phrase central claims as reported by the authors unless reproduced locally.
