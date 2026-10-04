# DreamDojo: A Generalist Robot World Model from Large-Scale Human Videos

candidate_id: CAND-0001
branch: D
decision: accepted_for_registry

## Source Links

- Paper: https://arxiv.org/abs/2602.06949
- Project: https://dreamdojo-world.github.io/
- Code: https://github.com/NVlabs/DreamDojo
- Data / benchmark: https://dreamdojo-world.github.io/
- Demo / video: https://dreamdojo-world.github.io/
- Official figures: https://dreamdojo-world.github.io/

## TL;DR

Transfers interaction knowledge from unprecedented-scale unlabeled human video into a controllable robot world model and distills it to sustained real-time generation. A strong reference for latent action fields, action-conditioned rollout, real-time simulation, cross-embodiment adaptation, and neural policy-evaluation interfaces. The main caveat is that the reported gains remain source-reported and were not independently reproduced in this collection run.

## Novelty

- What is actually new: Transfers interaction knowledge from unprecedented-scale unlabeled human video into a controllable robot world model and distills it to sustained real-time generation.
- Difference from prior work: It closes a concrete gap between isolated perception/generation components and reusable embodied execution, policy, or evaluation infrastructure.
- Why the delta matters: A strong reference for latent action fields, action-conditioned rollout, real-time simulation, cross-embodiment adaptation, and neural policy-evaluation interfaces.

## Contributions

1. A video foundation world model pretrained with continuous latent proxy actions on unlabeled human video, robot-action post-training, and few-step autoregressive distillation for real-time rollout.
2. 44,000+ hours of egocentric human video spanning daily environments, objects, and dexterous interactions, followed by small target-robot post-training sets.
3. The official project reports 10.81 FPS generation, stable rollouts beyond one minute, and applications to live teleoperation, policy evaluation, and planning.

## Task

- Input: Source-specific visual observations, language/task context, state, or action signals.
- Output: Generate action-conditioned robot futures for teleoperation, policy evaluation, and model-based planning across embodiments.
- Setting: Embodied simulation and/or real-robot evaluation described by the official source.
- Success criterion: The reported task metrics, transfer performance, or infrastructure validation protocol.

## Data

- Dataset / benchmark: 44,000+ hours of egocentric human video spanning daily environments, objects, and dexterous interactions, followed by small target-robot post-training sets.
- Scale: See the official paper and project page; central scale claims are source-traced below.
- Modalities: RGB/video plus task-specific actions, kinematics, language, geometry, or simulator state.
- Collection / annotation: Defined by the official source; synthetic and real components are kept distinct.
- Splits / evaluation protocol: Use the paper's official split and matched-baseline protocol before reproducing comparisons.

## Method

- Core pipeline: A video foundation world model pretrained with continuous latent proxy actions on unlabeled human video, robot-action post-training, and few-step autoregressive distillation for real-time rollout.
- Model / representation: Task-specific learned representations and explicit embodied state/action interfaces.
- Training or optimization: Follow the official paper; this report does not infer undisclosed settings.
- Inference / deployment: Generate action-conditioned robot futures for teleoperation, policy evaluation, and model-based planning across embodiments.
- Losses or metrics: See the official paper for exact objectives and evaluation definitions.

## Key Figures / Architecture

figure_status: linked_official

- Figure / demo: Official method overview and qualitative/demo evidence.
- Source: https://dreamdojo-world.github.io/
- Render: linked rather than copied to preserve provenance and avoid stale assets.
- What it shows: Official project overview and extensive action-conditioned rollout videos across GR-1, G1, AgiBot, and YAM.
- Why it matters: It directly supports the acceptance gate for architecture, execution, visual quality, or infrastructure completeness.

## Evidence Trail

| Claim | Source | Status | Notes |
|---|---|---|---|
| Dataset scale / benchmark size | https://arxiv.org/abs/2602.06949 | verified | Checked on the primary paper surface. |
| Main reported result or comparison | https://arxiv.org/abs/2602.06949 | verified | Reported by authors; not independently reproduced. |
| Code / checkpoint / demo availability | https://dreamdojo-world.github.io/ | verified | Official project surface inspected on 2026-10-05. |

## Evidence

- Main metrics: The official project reports 10.81 FPS generation, stable rollouts beyond one minute, and applications to live teleoperation, policy evaluation, and planning.
- Qualitative results: Official project overview and extensive action-conditioned rollout videos across GR-1, G1, AgiBot, and YAM.
- Ablations: Consult the official paper for component-level ablations.
- Baselines: Comparisons are accepted only as source-reported and protocol-dependent.
- Reproducibility signals: demo score 5/5; evidence strength 5/5; official project and code available.

## Limitations

- Method limitations: Scope and robustness remain bounded by the embodiments, environments, tasks, and action interfaces studied.
- Experimental limitations: Cross-paper metric comparisons may be invalid when success definitions or hardware differ.
- Demo / visual limitations: Official demos are curated; long-tail failures and full unedited trial distributions are not always exposed.
- Claims that remain unverified: All headline metrics are author-reported and were not independently reproduced.

## Project Relevance

- Relevance to interactive embodied generation: A strong reference for latent action fields, action-conditioned rollout, real-time simulation, cross-embodiment adaptation, and neural policy-evaluation interfaces.
- Reusable fields: derive typed fields from the nouns named above, while preserving source-specific units and coordinate frames.
- Possible baseline role: High-value reference for its primary branch and for cross-branch integration tests.
- Implications for our task / benchmark: Add source-aligned validators for the claimed transfer, controllability, consistency, or evaluation capability.

## Reproduction / Follow-up

- What to check before using: licenses, exact data splits, success criteria, hardware/action conventions, and whether all checkpoints are public.
- Code / checkpoint availability: https://github.com/NVlabs/DreamDojo
- Citation or related-work caveats: Cite results as reported by the authors and avoid treating project-page summaries as independent verification.
