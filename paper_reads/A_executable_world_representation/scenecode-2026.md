# SceneCode: Editable Indoor Scene Generation using Executable World Programs

candidate_id: CAND-0053
branch: A
decision: accepted_for_registry
authors: Chen et al.
year: 2026
venue: arXiv / project page

## Source Links

- Paper: https://arxiv.org/abs/2605.19587
- Project: https://scene-code.github.io/
- Code: https://scene-code.github.io/
- Data / benchmark: https://scene-code.github.io/
- Demo / video: https://scene-code.github.io/
- Official figures: https://scene-code.github.io/

## TL;DR

SceneCode is a strong executable-world addition because it treats indoor scene generation as program synthesis over editable world structure instead of only predicting geometry or images. The important delta for this repository is the representation: floor plans, room programs, and object attributes become explicit executable scene code that supports text-guided generation, image-conditioned reconstruction, and local scene editing. Main caveat: the public evidence is strongest on editable structure and visual consistency, while downstream robot-policy transfer is still indirect.

## Novelty

- What is actually new: an executable scene-program representation that decomposes a large indoor scene into hierarchical floor-plan, room, and object programs.
- Difference from prior work: compared with scene-only generators, SceneCode exposes editable intermediate structure rather than collapsing everything into a latent or mesh output.
- Why the delta matters: our target repository needs typed world structure that can later feed validators, repair passes, or simulator-export pipelines.

## Contributions

1. Defines indoor scene generation and editing through executable world programs instead of opaque scene outputs.
2. Supports text-to-scene, image-to-scene, and single-object editing with one structured scene code interface.
3. Releases a project page with architecture diagrams, editable examples, and code links that make the representation directly inspectable.

## Task

- Input: text prompts, indoor-scene images, or local editing instructions for a target object or region.
- Output: executable scene programs plus reconstructed/generated indoor layouts and object configurations.
- Setting: structured indoor-world generation and editing for large, multi-room scenes.
- Success criterion: generate coherent scene structure that stays editable and semantically aligned across generation and editing modes.

## Data

- Dataset / benchmark: indoor scene layouts and object-rich large-scene examples shown on the official project page and paper.
- Scale: the public sources emphasize large-scene decomposition and editing coverage rather than a headline benchmark size.
- Modalities: text, images, hierarchical scene programs, floor plans, room layouts, and object attributes.
- Collection / annotation: source materials describe programmatic decomposition of indoor scenes into structured world-code components.
- Splits / evaluation protocol: use the paper's reported generation, reconstruction, and editing evaluations when citing exact numbers.

## Method

- Core pipeline: encode a scene into executable floor-plan, room, and object programs; then decode those programs for generation, reconstruction, or editing.
- Model / representation: hierarchical executable world program with explicit scene substructures and editable object attributes.
- Training or optimization: source-reported structured generation training over indoor-scene representations.
- Inference / deployment: supports text-conditioned synthesis, image-conditioned scene reconstruction, and local object edits from the same scene-code backbone.
- Losses or metrics: rely on the paper's reported reconstruction, generation, and editing metrics; this repository did not reproduce them locally.

## Key Figures / Architecture

figure_status: linked_official

- Figure / demo: official project overview showing the scene-code hierarchy and editable generation examples.
- Source: https://scene-code.github.io/
- Render:
  Official figure/demo page: https://scene-code.github.io/
- What it shows: the page illustrates how a large indoor scene is decomposed into executable programs and then edited or regenerated from structured code.
- Why it matters: this is the clearest public evidence that the paper contributes reusable world structure rather than only a polished visual gallery.

## Evidence Trail

| Claim | Source | Status | Notes |
|---|---|---|---|
| SceneCode represents indoor scenes as executable world programs | https://arxiv.org/abs/2605.19587 | verified | Stated directly in the paper title and abstract. |
| The representation decomposes scenes into floor-plan, room, and object programs | https://scene-code.github.io/ | verified | Shown in the official project overview. |
| The system supports generation, reconstruction, and single-object editing | https://scene-code.github.io/ | verified | Demonstrated on the official examples page. |
| Public code/project artifacts exist | https://scene-code.github.io/ | partial | The official site links outward, but exact long-term repository state should be rechecked before downstream use. |

## Evidence

- Main metrics: use the paper's reported generation/reconstruction/editing results rather than secondary summaries.
- Qualitative results: the official page shows diverse editable indoor examples across text generation, image-conditioned reconstruction, and targeted object edits.
- Ablations: not reproduced locally; cite the paper for structured-program and editing ablations.
- Baselines: compare against the paper's own indoor scene generation and editing baselines before making stronger claims.
- Reproducibility signals: primary arXiv source plus an official project page with architecture and example outputs.

## Limitations

- Method limitations: current public evidence focuses on structural editability more than simulator-backed physical validity.
- Experimental limitations: this repository did not run the released code or verify exact benchmark numbers locally.
- Demo / visual limitations: examples are convincing and relevant, but still curated official materials.
- Claims that remain unverified: exact code maturity, dataset release completeness, and export quality for downstream physics engines.

## Project Relevance

- Relevance to interactive embodied generation: highly relevant as a representation-first approach to large indoor worlds that can be edited and potentially compiled into stricter executable formats.
- Reusable fields: FloorPlan, RoomProgram, ObjectProgram, ObjectAttribute, EditInstruction, SceneGraph, and StructuredWorldCode.
- Possible baseline role: representation baseline for scene-program generation and structured repair pipelines.
- Implications for our task / benchmark: useful reference for typed indoor world structure, local scene editing, and explicit intermediate scene state.

## Reproduction / Follow-up

- What to check before using: exact code repository, scene export format, and whether executable scene programs can be converted cleanly into simulator objects and constraints.
- Code / checkpoint availability: the official project page advertises public project artifacts and code links.
- Citation or related-work caveats: emphasize structured editability and executable representation rather than overclaiming physical simulation readiness.
