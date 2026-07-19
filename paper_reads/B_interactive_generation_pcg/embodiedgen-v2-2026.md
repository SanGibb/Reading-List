# EmbodiedGen V2: An Agentic, Simulation-Ready 3D World Engine for Embodied AI

candidate_id: CAND-0002
branch: B
decision: accepted_for_registry
authors: Wang et al.
year: 2026
venue: arXiv / project page

## Source Links

- Paper: https://arxiv.org/abs/2607.07459
- Project: https://horizonrobotics.github.io/EmbodiedGen/
- Code: https://github.com/HorizonRobotics/EmbodiedGen
- Data / benchmark: https://huggingface.co/datasets/HorizonRobotics/EmbodiedGenData
- Demo / video: https://youtu.be/MIkJJSVM8L4
- Official figures: https://horizonrobotics.github.io/EmbodiedGen/

## TL;DR

EmbodiedGen V2 is the strongest new July 19, 2026 addition for interactive generation because it upgrades the earlier EmbodiedGen line from isolated generation assets into a reusable world engine that connects assets, scenes, tasks, dialogue editing, and cross-simulator export. The official project page shows a complete pipeline from intent to executable 3D worlds, with code, video, Hugging Face artifacts, and a public dataset. Main caveat: the full cross-simulator workflow is impressive on paper and on the official surface, but it was not independently executed in this repository.

## Novelty

- What is actually new: an agentic world engine that keeps affordances, scene state, and simulator interfaces intact across asset generation, scene composition, task instantiation, and world editing.
- Difference from prior work: many recent papers stop at asset generation or scene layout; EmbodiedGen V2 explicitly treats executable world assembly as the main product.
- Why the delta matters: this repository needs references for interactive world generation that can actually feed downstream embodied learning loops.

## Contributions

1. Unifies sim-ready assets, large-scale scenes, task-driven worlds, and dialogue-based editing under one world-engine abstraction.
2. Exposes cross-simulator export and reuse instead of simulator-specific handcrafted outputs.
3. Ships public code, video, model collection, and dataset links that make the system materially reusable.

## Task

- Input: text, images, or natural-language dialogue describing assets, scenes, or tasks.
- Output: executable simulation-ready 3D worlds composed of reusable assets, stable layouts, and embodied-task structure.
- Setting: closed-loop embodied world generation for simulator-backed policy learning.
- Success criterion: generate visually coherent and physically usable worlds that can be deployed across simulators without manual reconstruction.

## Data

- Dataset / benchmark: official Hugging Face dataset plus source-reported generated asset and world collections.
- Scale: positioned as a large-scale world-engine release spanning assets, scenes, and multi-room worlds.
- Modalities: 3D assets, layouts, task descriptions, dialogue edits, and simulator export interfaces.
- Collection / annotation: the official project page describes a standardized sim-ready representation that packages geometry, collision, physics properties, and affordances.
- Splits / evaluation protocol: use the paper's source-reported protocols for exact benchmark and export results.

## Method

- Core pipeline: generate sim-ready assets, scale them into scenes, compose task-driven worlds, edit state through dialogue, export across simulators, and use the resulting worlds for learning.
- Model / representation: a unified sim-ready world representation linking geometry, collision proxies, physical properties, affordances, and cross-simulator interfaces.
- Training or optimization: source-reported generative modeling over assets/worlds plus task- and simulator-facing composition stages.
- Inference / deployment: deploy generated worlds into multiple simulator engines with preserved affordance and state structure.
- Losses or metrics: use the paper for exact success, world-quality, and transfer metrics; this run verified the official release surface rather than reproducing them.

## Key Figures / Architecture

figure_status: linked_official

- Figure / demo: official system-overview figure and world-generation examples.
- Source: https://horizonrobotics.github.io/EmbodiedGen/
- Render:
  Official figure/demo page: https://horizonrobotics.github.io/EmbodiedGen/
- What it shows: the page lays out the pipeline from sim-ready assets through scenes, worlds, dialogue edits, and cross-simulator export.
- Why it matters: it makes the system's value obvious as a world engine instead of a one-off content generator.

## Evidence Trail

| Claim | Source | Status | Notes |
|---|---|---|---|
| EmbodiedGen V2 is an agentic simulation-ready 3D world engine | https://arxiv.org/abs/2607.07459 | verified | Title and abstract claim. |
| The system supports assets, scenes, worlds, vibe coding, and cross-simulator export | https://horizonrobotics.github.io/EmbodiedGen/ | verified | Official overview lists each stage. |
| Official code, model collection, and dataset are public | https://horizonrobotics.github.io/EmbodiedGen/ | verified | Official page links GitHub, Hugging Face collection, and dataset. |

## Evidence

- Main metrics: the paper and project page present source-reported world-generation and export results; exact numbers should be cited from the source.
- Qualitative results: the official page shows strong scene/world examples, interactive editing, and multi-room layouts with simulator-facing structure.
- Ablations: use the paper for component-level analysis across assets, scenes, and world editing.
- Baselines: compare against prior world-generation systems only as source-reported.
- Reproducibility signals: primary paper, public code, video, Hugging Face collection, and public dataset.

## Limitations

- Method limitations: cross-simulator success is still source-reported and may depend on representation assumptions that do not transfer perfectly.
- Experimental limitations: this run did not execute the provided exporters or task worlds locally.
- Demo / visual limitations: official examples are strong, but independent stress testing of world-edit stability was not performed here.
- Claims that remain unverified: exact coverage breadth across all supported simulators and long-term maintenance cadence.

## Project Relevance

- Relevance to interactive embodied generation: extremely high because it aligns generated content with executable embodied training environments.
- Reusable fields: SimReadyAsset, CollisionProxy, Affordance, MultiRoomScene, TaskWorld, DialogueEdit, and CrossSimulatorExport.
- Possible baseline role: top branch-B reference for executable world-engine design.
- Implications for our task / benchmark: strong template for what an embodied generation stack should preserve beyond appearance.

## Reproduction / Follow-up

- What to check before using: simulator coverage, license terms, dataset access flow, and exporter assumptions.
- Code / checkpoint availability: official GitHub plus public Hugging Face collection and dataset links are available.
- Citation or related-work caveats: keep benchmark and export claims source-attributed unless independently reproduced.
