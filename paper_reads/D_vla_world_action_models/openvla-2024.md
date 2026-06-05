# OpenVLA: An Open-Source Vision-Language-Action Model

candidate_id: CAND-0012
branch: D. VLA and World-Action Models
decision: accepted_for_registry
registry_status: update

## Source Links

- Paper: https://arxiv.org/abs/2406.09246
- Project: https://openvla.github.io/
- Code / release: https://github.com/openvla/openvla
- Demo / video: https://openvla.github.io/
- Official figure / architecture: https://openvla.github.io/static/images/openvla_model.jpg
- Registry URL: https://arxiv.org/abs/2406.09246

## TL;DR

OpenVLA is the default open VLA baseline for our task. It has enough code/model accessibility to be used in downstream generated-world evaluation, while also providing clear failure cases around hard semantic and narrow precision tasks.

## Novelty

- What is actually new: first broadly usable open-source 7B VLA with released checkpoints, training pipeline, and PEFT/quantization support.
- Difference from prior work: it adds executable, interactive, physical, spatial, or policy-facing structure rather than stopping at static visual quality.
- Why the delta matters: our repository needs works that can become fields, validators, baselines, or generation targets for interactive embodied worlds.

## Contributions

1. Releases model checkpoints, code, and finetuning notebooks.
2. Trains on 970k robot episodes with a fused visual encoder.
3. Evaluates out-of-the-box and finetuned performance across multiple robots.

## Task

- Input: paper-specific observations, prompts, scenes, assets, robot data, or benchmark tasks.
- Output: open-source generalist robot manipulation and finetuning to new robot setups.
- Setting: CoRL / 2024 frontier work, primary branch D with secondary fit E.
- Success criterion: reported benchmark success, qualitative/demo quality, or usefulness as an executable-world data/model/evaluation component.

## Data

- Dataset / benchmark: 970k robot manipulation trajectories from Open X-Embodiment.
- Scale: see official paper/project for exact splits; collection-critical scale claims are recorded in the evidence trail below.
- Modalities: 3D geometry, language, scene assets, robot observations/actions, physics/material labels, or benchmark annotations depending on the paper.
- Collection / annotation: primary source reports official construction process; this run did not reproduce the full dataset locally.
- Splits / evaluation protocol: follow the paper/project protocol before using exact numbers in a manuscript.

## Method

- Core pipeline: 7B VLA built from a Prismatic VLM, SigLIP/DINOv2 fused visual encoder, Llama 2 backbone, and tokenized robot actions.
- Model / representation: the work contributes a representation, generator, policy model, or evaluation platform aligned with interactive embodied generation.
- Training or optimization: use the official paper for training schedules; this report records the method-level shape and acceptance evidence.
- Inference / deployment: intended use is as a generator, policy baseline, simulator-ready asset source, spatial-action model, or benchmark component.
- Losses or metrics: central reported metrics are in the paper/project; do not cite precise values without checking the PDF tables.

## Key Figures / Architecture

figure_status: linked_official

- Figure / demo: official project architecture, teaser, benchmark overview, or qualitative demo.
- Source: https://openvla.github.io/static/images/openvla_model.jpg
- Render:
  ![OpenVLA key figure](https://openvla.github.io/static/images/openvla_model.jpg)
- What it shows: the artifact most directly supporting the accepted claim for this knowledge-base entry.
- Why it matters: it gives a visual or structural anchor for judging whether the paper is usable for our interactive generation / embodied intelligence tasks.

## Evidence Trail

| Claim | Source | Status | Notes |
|---|---|---|---|
| Paper/source is primary or official. | https://arxiv.org/abs/2406.09246 | verified | Used as registry URL or paper source. |
| Project/demo evidence exists. | https://openvla.github.io/ | verified | Demo score 5; visual decision: strong visual/demo evidence from official project page. |
| Data / benchmark / method relevance. | https://openvla.github.io/ | partial | Summary follows official page and arXiv/proceedings; exact numerical claims should be checked in the PDF before citation. |
| Key visual or architecture evidence. | https://openvla.github.io/static/images/openvla_model.jpg | verified | Official linked figure/demo; no local reproduction was performed. |

## Evidence

- Main metrics: Official page reports 7B parameters, 970k episodes, outperformance over RT-2-X in absolute task success rate in the paper summary, and strong finetuning/LoRA results.
- Qualitative results: official project page provides visual/demo material used for this acceptance decision.
- Ablations: not exhaustively audited in this initialization pass; check the PDF before using ablation numbers.
- Baselines: paper/project compares against relevant prior methods; this report records only acceptance-level evidence.
- Reproducibility signals: source quality `primary_or_official`, evidence strength 5, demo score 5.

## Limitations

- Method limitations: Action tokenization and semantic forgetting can limit hard OOD semantic tasks; precise narrow tasks may still favor task-specific policies.
- Experimental limitations: this initialization run did not run code, download datasets, or reproduce metrics.
- Demo / visual limitations: official demo material can be curated; use local reproduction or independent videos before making strong claims.
- Claims that remain unverified: exact numeric tables, benchmark splits, compute/data cost, and robustness beyond official examples.

## Project Relevance

- Relevance to interactive embodied generation: Baseline for VLA policy execution, generated-task transfer, action-token interface, and finetuning experiments.
- Reusable fields: `Scene`, `Object`, `Part`, `Affordance`, `PhysicalProperty`, `SpatialRelation`, `Task`, `Trajectory`, `Policy`, `ValidationReport` as applicable.
- Possible baseline role: use as a baseline, source of validators, dataset schema, or quality bar for generated-world demos.
- Implications for our task / benchmark: keep only if future generated worlds can expose comparable fields or be evaluated by comparable tasks.

## Reproduction / Follow-up

- What to check before using: inspect the PDF tables, released code/data, license, and exact benchmark protocol.
- Code / checkpoint availability: see Source Links; this report only verifies that an official link exists when listed.
- Citation or related-work caveats: phrase central claims as reported by the authors unless reproduced locally.
