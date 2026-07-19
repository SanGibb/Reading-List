# Cosmos 3: Omnimodal World Models for Physical AI

candidate_id: CAND-0006
branch: D
decision: accepted_for_registry
authors: NVIDIA Cosmos team
year: 2026
venue: arXiv / NVIDIA technical report

## Source Links

- Paper: https://arxiv.org/abs/2606.02800
- Project: https://research.nvidia.com/labs/cosmos-lab/cosmos3
- Code: https://github.com/NVIDIA/cosmos
- Data / benchmark: https://research.nvidia.com/labs/cosmos-lab/cosmos3
- Demo / video: https://research.nvidia.com/labs/cosmos-lab/cosmos3
- Official figures: https://research.nvidia.com/labs/cosmos-lab/cosmos3

## TL;DR

Cosmos 3 is one of the most important July 19, 2026 additions because it unifies language, image, video, audio, and action generation/understanding inside one physical-AI world-model family. The official technical report and NVIDIA release surface make a strong case that this is not just another video model but an omnimodal stack meant to subsume VLMs, world simulators, and world-action models. Main caveat: the strongest evidence is still concentrated on NVIDIA-owned evaluation and demo surfaces, so external replication should be monitored over time.

## Novelty

- What is actually new: a family of omnimodal world models that jointly handle understanding, generation, simulation, and action.
- Difference from prior work: earlier systems usually covered only one or two modalities or only one role such as generation or VLA control; Cosmos 3 is explicitly positioned as the unifying stack.
- Why the delta matters: this repository needs anchor references for the direction where embodied stacks stop being siloed into separate perception, generation, and action modules.

## Contributions

1. Unifies text, images, video, audio, and actions within a shared world-model architecture for physical AI.
2. Publicly surfaces code and model cards rather than only a paper.
3. Demonstrates broad official demos spanning reasoning, generation, simulation, and action-adjacent tasks.

## Task

- Input: flexible combinations of language, image, video, audio, and action context.
- Output: flexible combinations of understanding outputs, generated media, predicted futures, or action-conditioned sequences.
- Setting: omnimodal world modeling for physical AI.
- Success criterion: support a wide range of physical-AI tasks without splitting the stack into disconnected specialist models.

## Data

- Dataset / benchmark: official release surface plus source-reported evaluation tasks spanning understanding and generation workloads.
- Scale: positioned as a major omnimodal release with public model cards and code.
- Modalities: language, image, video, audio, and action.
- Collection / annotation: source materials emphasize unified multimodal processing rather than a single benchmark dataset release.
- Splits / evaluation protocol: use the technical report for exact benchmark suites and scores.

## Method

- Core pipeline: shared omnimodal world-model architecture with flexible input-output configurations over multiple physical-AI modalities.
- Model / representation: mixture-of-transformers world-model family.
- Training or optimization: source-reported large-scale multimodal pretraining and evaluation.
- Inference / deployment: serve reasoning, generation, simulation, and action-related tasks from the same model family.
- Losses or metrics: use the technical report for exact performance numbers; this run did not reproduce them locally.

## Key Figures / Architecture

figure_status: linked_official

- Figure / demo: official NVIDIA Cosmos 3 release page with omnimodal capability demos.
- Source: https://research.nvidia.com/labs/cosmos-lab/cosmos3
- Render:
  Official figure/demo page: https://research.nvidia.com/labs/cosmos-lab/cosmos3
- What it shows: the page walks through reasoning, generation, forward dynamics, inverse dynamics, and multimodal task surfaces.
- Why it matters: those official demos are the strongest evidence that the model family really spans the roles it claims to unify.

## Evidence Trail

| Claim | Source | Status | Notes |
|---|---|---|---|
| Cosmos 3 jointly processes and generates language, image, video, audio, and action sequences | https://arxiv.org/abs/2606.02800 | verified | Abstract states the omnimodal scope directly. |
| The release surface presents one shared model family across understanding, generation, simulation, and action | https://research.nvidia.com/labs/cosmos-lab/cosmos3 | verified | Official page frames the system exactly this way. |
| Official code and model cards are public | https://research.nvidia.com/labs/cosmos-lab/cosmos3 | verified | NVIDIA page links GitHub and Hugging Face collection. |

## Evidence

- Main metrics: cite the technical report for exact state-of-the-art claims and modality-specific numbers.
- Qualitative results: the official demos are broad, polished, and physically relevant, spanning reasoning, media generation, and dynamics tasks.
- Ablations: use the technical report for architecture and modality ablations.
- Baselines: compare against other omnimodal or specialist stacks only as source-reported.
- Reproducibility signals: primary technical report, official NVIDIA release page, public GitHub, and public model cards.

## Limitations

- Method limitations: breadth may come with tradeoffs in transparency and independent reproducibility relative to smaller open systems.
- Experimental limitations: this run did not execute the released models locally.
- Demo / visual limitations: strongest evidence remains on NVIDIA-owned surfaces.
- Claims that remain unverified: external benchmark replication, precise license constraints, and how much of the stack is practical for non-NVIDIA embodied pipelines.

## Project Relevance

- Relevance to interactive embodied generation: extremely high as a frontier reference for unified world-model stacks that span perception, generation, and action.
- Reusable fields: OmnimodalContext, WorldSimulator, ForwardDynamics, InverseDynamics, and UnifiedPhysicalAIModel.
- Possible baseline role: branch-D top-tier anchor for unified world-model design.
- Implications for our task / benchmark: important reference for deciding which abstractions should remain separate and which could collapse into one world-model layer.

## Reproduction / Follow-up

- What to check before using: model-card access, supported tasks, license terms, and hardware/runtime constraints.
- Code / checkpoint availability: official public GitHub and public model-card collection are linked from the release page.
- Citation or related-work caveats: keep all performance leadership claims explicitly source-attributed unless rerun externally.
