# Open-H-Embodiment: A Large-Scale Dataset for Enabling Foundation Models in Medical Robotics

candidate_id: CAND-0009
branch: E
decision: accepted_for_registry

## Source Links

- Paper: https://arxiv.org/abs/2604.21017
- Project: https://openhembodiment.org/
- Code: not publicly identified in this run
- Data / benchmark: https://openhembodiment.org/
- Demo / video: https://openhembodiment.org/
- Official figures: https://arxiv.org/abs/2604.21017

## TL;DR

Provides the largest reported open synchronized medical-robot corpus and demonstrates both a VLA and one-checkpoint multi-platform world model on it. Extends embodied data infrastructure with synchronized video-kinematics, clinical embodiment metadata, multi-platform action schemas, and long-horizon procedure evaluation. The main caveat is that the reported gains remain source-reported and were not independently reproduced in this collection run.

## Novelty

- What is actually new: Provides the largest reported open synchronized medical-robot corpus and demonstrates both a VLA and one-checkpoint multi-platform world model on it.
- Difference from prior work: It closes a concrete gap between isolated perception/generation components and reusable embodied execution, policy, or evaluation infrastructure.
- Why the delta matters: Extends embodied data infrastructure with synchronized video-kinematics, clinical embodiment metadata, multi-platform action schemas, and long-horizon procedure evaluation.

## Contributions

1. A cross-institution, multi-embodiment data standard plus GR00T-H VLA and Cosmos-H action-conditioned surgical world-model baselines.
2. Open synchronized medical-robot video and kinematics from 49+ institutions and multiple platforms across surgery, ultrasound, and endoscopy.
3. The paper reports GR00T-H as the only evaluated model completing the structured suturing task (25%) and 64% average success across a 29-step ex-vivo sequence.

## Task

- Input: Source-specific visual observations, language/task context, state, or action signals.
- Output: Train and evaluate medical robot foundation models, action prediction, and multi-embodiment surgical simulation.
- Setting: Embodied simulation and/or real-robot evaluation described by the official source.
- Success criterion: The reported task metrics, transfer performance, or infrastructure validation protocol.

## Data

- Dataset / benchmark: Open synchronized medical-robot video and kinematics from 49+ institutions and multiple platforms across surgery, ultrasound, and endoscopy.
- Scale: See the official paper and project page; central scale claims are source-traced below.
- Modalities: RGB/video plus task-specific actions, kinematics, language, geometry, or simulator state.
- Collection / annotation: Defined by the official source; synthetic and real components are kept distinct.
- Splits / evaluation protocol: Use the paper's official split and matched-baseline protocol before reproducing comparisons.

## Method

- Core pipeline: A cross-institution, multi-embodiment data standard plus GR00T-H VLA and Cosmos-H action-conditioned surgical world-model baselines.
- Model / representation: Task-specific learned representations and explicit embodied state/action interfaces.
- Training or optimization: Follow the official paper; this report does not infer undisclosed settings.
- Inference / deployment: Train and evaluate medical robot foundation models, action prediction, and multi-embodiment surgical simulation.
- Losses or metrics: See the official paper for exact objectives and evaluation definitions.

## Key Figures / Architecture

figure_status: linked_official

- Figure / demo: Official method overview and qualitative/demo evidence.
- Source: https://arxiv.org/abs/2604.21017
- Render: linked rather than copied to preserve provenance and avoid stale assets.
- What it shows: Dataset/infrastructure paper; architecture and corpus figures are linked through the official paper rather than used as a generation-quality gate.
- Why it matters: It directly supports the acceptance gate for architecture, execution, visual quality, or infrastructure completeness.

## Evidence Trail

| Claim | Source | Status | Notes |
|---|---|---|---|
| Dataset scale / benchmark size | https://arxiv.org/abs/2604.21017 | verified | Checked on the primary paper surface. |
| Main reported result or comparison | https://arxiv.org/abs/2604.21017 | verified | Reported by authors; not independently reproduced. |
| Code / checkpoint / demo availability | https://openhembodiment.org/ | verified | Official project surface inspected on 2026-10-05. |

## Evidence

- Main metrics: The paper reports GR00T-H as the only evaluated model completing the structured suturing task (25%) and 64% average success across a 29-step ex-vivo sequence.
- Qualitative results: Dataset/infrastructure paper; architecture and corpus figures are linked through the official paper rather than used as a generation-quality gate.
- Ablations: Consult the official paper for component-level ablations.
- Baselines: Comparisons are accepted only as source-reported and protocol-dependent.
- Reproducibility signals: demo score 3/5; evidence strength 4/5; official project available.

## Limitations

- Method limitations: Scope and robustness remain bounded by the embodiments, environments, tasks, and action interfaces studied.
- Experimental limitations: Cross-paper metric comparisons may be invalid when success definitions or hardware differ.
- Demo / visual limitations: Official demos are curated; long-tail failures and full unedited trial distributions are not always exposed.
- Claims that remain unverified: All headline metrics are author-reported and were not independently reproduced.

## Project Relevance

- Relevance to interactive embodied generation: Extends embodied data infrastructure with synchronized video-kinematics, clinical embodiment metadata, multi-platform action schemas, and long-horizon procedure evaluation.
- Reusable fields: derive typed fields from the nouns named above, while preserving source-specific units and coordinate frames.
- Possible baseline role: High-value reference for its primary branch and for cross-branch integration tests.
- Implications for our task / benchmark: Add source-aligned validators for the claimed transfer, controllability, consistency, or evaluation capability.

## Reproduction / Follow-up

- What to check before using: licenses, exact data splits, success criteria, hardware/action conventions, and whether all checkpoints are public.
- Code / checkpoint availability: No public code URL was confirmed in this run.
- Citation or related-work caveats: Cite results as reported by the authors and avoid treating project-page summaries as independent verification.
