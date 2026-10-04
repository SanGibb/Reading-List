# MolmoB0T: Large-Scale Simulation Enables Zero-Shot Manipulation

candidate_id: CAND-0003
branch: D
decision: accepted_for_registry

## Source Links

- Paper: https://arxiv.org/abs/2603.16861
- Project: https://allenai.github.io/MolmoBot/
- Code: https://github.com/allenai/MolmoBot
- Data / benchmark: https://allenai.github.io/MolmoBot/
- Demo / video: https://allenai.github.io/MolmoBot/
- Official figures: https://allenai.github.io/MolmoBot/

## TL;DR

Demonstrates a fully open sim-only manipulation stack that transfers zero-shot to two real robot platforms without target-domain fine-tuning. Useful baseline for synthetic-only policy training, procedural diversity, domain randomization, embodiment transfer, and open sim-to-real evaluation. The main caveat is that the reported gains remain source-reported and were not independently reproduced in this collection run.

## Novelty

- What is actually new: Demonstrates a fully open sim-only manipulation stack that transfers zero-shot to two real robot platforms without target-domain fine-tuning.
- Difference from prior work: It closes a concrete gap between isolated perception/generation components and reusable embodied execution, policy, or evaluation infrastructure.
- Why the delta matters: Useful baseline for synthetic-only policy training, procedural diversity, domain randomization, embodiment transfer, and open sim-to-real evaluation.

## Contributions

1. A suite of behavior-cloned policies trained only on aggressively randomized procedural simulation data, with VLM-based, lightweight-transformer, and pi0-compatible architectures.
2. 1.7M expert manipulation trajectories over 11K+ objects, 94K+ procedurally generated environments, eight tasks, and Franka FR3 plus RB-Y1 embodiments.
3. Ai2 reports full models, data, engine, training and evaluation code; the paper reports 79.2% Franka pick-and-place success versus 39.2% for the matched pi0.5-DROID comparison.

## Task

- Input: Source-specific visual observations, language/task context, state, or action signals.
- Output: Zero-shot sim-to-real pick-and-place, articulated-object manipulation, and door opening on unseen objects and environments.
- Setting: Embodied simulation and/or real-robot evaluation described by the official source.
- Success criterion: The reported task metrics, transfer performance, or infrastructure validation protocol.

## Data

- Dataset / benchmark: 1.7M expert manipulation trajectories over 11K+ objects, 94K+ procedurally generated environments, eight tasks, and Franka FR3 plus RB-Y1 embodiments.
- Scale: See the official paper and project page; central scale claims are source-traced below.
- Modalities: RGB/video plus task-specific actions, kinematics, language, geometry, or simulator state.
- Collection / annotation: Defined by the official source; synthetic and real components are kept distinct.
- Splits / evaluation protocol: Use the paper's official split and matched-baseline protocol before reproducing comparisons.

## Method

- Core pipeline: A suite of behavior-cloned policies trained only on aggressively randomized procedural simulation data, with VLM-based, lightweight-transformer, and pi0-compatible architectures.
- Model / representation: Task-specific learned representations and explicit embodied state/action interfaces.
- Training or optimization: Follow the official paper; this report does not infer undisclosed settings.
- Inference / deployment: Zero-shot sim-to-real pick-and-place, articulated-object manipulation, and door opening on unseen objects and environments.
- Losses or metrics: See the official paper for exact objectives and evaluation definitions.

## Key Figures / Architecture

figure_status: linked_official

- Figure / demo: Official method overview and qualitative/demo evidence.
- Source: https://allenai.github.io/MolmoBot/
- Render: linked rather than copied to preserve provenance and avoid stale assets.
- What it shows: Official technical site provides side-by-side simulation and continuous real-robot executions for all task families.
- Why it matters: It directly supports the acceptance gate for architecture, execution, visual quality, or infrastructure completeness.

## Evidence Trail

| Claim | Source | Status | Notes |
|---|---|---|---|
| Dataset scale / benchmark size | https://arxiv.org/abs/2603.16861 | verified | Checked on the primary paper surface. |
| Main reported result or comparison | https://arxiv.org/abs/2603.16861 | verified | Reported by authors; not independently reproduced. |
| Code / checkpoint / demo availability | https://allenai.github.io/MolmoBot/ | verified | Official project surface inspected on 2026-10-05. |

## Evidence

- Main metrics: Ai2 reports full models, data, engine, training and evaluation code; the paper reports 79.2% Franka pick-and-place success versus 39.2% for the matched pi0.5-DROID comparison.
- Qualitative results: Official technical site provides side-by-side simulation and continuous real-robot executions for all task families.
- Ablations: Consult the official paper for component-level ablations.
- Baselines: Comparisons are accepted only as source-reported and protocol-dependent.
- Reproducibility signals: demo score 5/5; evidence strength 5/5; official project and code available.

## Limitations

- Method limitations: Scope and robustness remain bounded by the embodiments, environments, tasks, and action interfaces studied.
- Experimental limitations: Cross-paper metric comparisons may be invalid when success definitions or hardware differ.
- Demo / visual limitations: Official demos are curated; long-tail failures and full unedited trial distributions are not always exposed.
- Claims that remain unverified: All headline metrics are author-reported and were not independently reproduced.

## Project Relevance

- Relevance to interactive embodied generation: Useful baseline for synthetic-only policy training, procedural diversity, domain randomization, embodiment transfer, and open sim-to-real evaluation.
- Reusable fields: derive typed fields from the nouns named above, while preserving source-specific units and coordinate frames.
- Possible baseline role: High-value reference for its primary branch and for cross-branch integration tests.
- Implications for our task / benchmark: Add source-aligned validators for the claimed transfer, controllability, consistency, or evaluation capability.

## Reproduction / Follow-up

- What to check before using: licenses, exact data splits, success criteria, hardware/action conventions, and whether all checkpoints are public.
- Code / checkpoint availability: https://github.com/allenai/MolmoBot
- Citation or related-work caveats: Cite results as reported by the authors and avoid treating project-page summaries as independent verification.
