# Mask2Real-WM: Segmentation Masks as a Sim-to-Real Bridge for Controllable Dexterous World Models

candidate_id: CAND-0002
branch: D
decision: accepted_for_registry

## Source Links

- Paper: https://arxiv.org/abs/2607.04546
- Project / interactive demo: https://srl-ethz.github.io/Mask2Real-WM/
- Supplementary policy rollouts: https://srl-ethz.github.io/Mask2Real-WM/supplementary.html
- Code: listed as coming soon on the official project page as inspected 2026-07-27

## TL;DR

Mask2Real-WM separates action-conditioned dexterous dynamics from photorealistic rendering by predicting segmentation masks before RGB. This enables more than 50 hours of simulation pretraining and fine-tuning with under 2.5 hours of real data while preserving 23-DoF action controllability. Official long-horizon and policy-rollout demos are strong; code was not yet public at inspection time.

## Novelty

- What is actually new: segmentation masks act as the low-gap interface between simulated dexterous dynamics and real-video rendering.
- Difference from prior work: monolithic RGB predictors entangle dynamics and appearance and often collapse fine-grained joint effects.
- Why the delta matters: the split makes synthetic dynamics data useful for controllable real-world prediction.

## Contributions

1. Two-stage Dynamics-WM / Rendering-WM design for action-conditioned video prediction.
2. Joint conditioning on a 6-DoF end-effector pose and 17 hand joints.
3. Long-horizon world-model and policy-evaluation experiments with strong controllability evidence.

## Task

- Input: past masks/RGB and past/future 23-DoF robot actions.
- Output: future segmentation masks and photorealistic RGB rollouts.
- Setting: dexterous pick-and-place, policy evaluation, planning, and augmentation.
- Success criterion: perceptual quality plus per-DoF action controllability and faithful policy ranking.

## Data

- Dataset / benchmark: over 50 hours of IsaacLab simulation and fewer than 2.5 hours of real demonstrations.
- Modalities: RGB, masks, 6-DoF arm motion, and 17-DoF ORCA-hand joints.
- Collection / annotation: simulation pretraining followed by limited real-data fine-tuning.
- Splits / evaluation protocol: in-distribution and OOD dexterous rollouts plus multiple real-robot policies.

## Method

- Core pipeline: mask/action history -> dynamics model -> future masks -> ControlNet-augmented Stable Video Diffusion renderer -> future RGB.
- Model / representation: masks are the sim-to-real dynamics interface.
- Training or optimization: synthetic pretraining for dynamics and real fine-tuning for appearance.
- Inference / deployment: autoregressive long-horizon rollout conditioned on proposed actions.
- Losses or metrics: perceptual metrics and per-DoF action controllability.

## Key Figures / Architecture

figure_status: linked_official

- Figure / demo: teaser, architecture, long-horizon comparisons, and OOD policy rollouts.
- Source: https://srl-ethz.github.io/Mask2Real-WM/
- What it shows: segmentation-mediated dynamics, RGB rendering, and visible separation between intended joint motions.
- Why it matters: official side-by-side results make the controllability claim visually assessable rather than relying on static tables.

## Evidence Trail

| Claim | Source | Status | Notes |
|---|---|---|---|
| >50 h simulation and <2.5 h real demonstrations | https://arxiv.org/abs/2607.04546 | verified | Abstract and project page agree. |
| 23-DoF controllability | https://srl-ethz.github.io/Mask2Real-WM/ | verified | Official page defines 6+17 DoF and provides comparisons. |
| Code availability | https://srl-ethz.github.io/Mask2Real-WM/ | partial | Official page says code coming soon. |

## Evidence

- Main metrics: official page reports in-distribution controllability of 0.95 versus 0.60 for a baseline.
- Qualitative results: inspected official teaser and long-horizon rollout material; hand/object motions remain task-aligned with modest blur.
- Ablations: mask conditioning and simulation pretraining are both reported as necessary.
- Baselines: monolithic RGB world models that retain coarse arm motion but lose individual joint control.
- Reproducibility signals: paper, project page, interactive/supplementary demos; no released code yet.

## Limitations

- Method limitations: depends on segmentation masks and a constrained dexterous setup.
- Experimental limitations: one task family and hardware configuration limit broad generalization claims.
- Demo / visual limitations: renderings retain mild blur and official examples cannot rule out selection bias.
- Claims that remain unverified: results were not rerun and code remains pending.

## Project Relevance

- Relevance to interactive embodied generation: a direct design for controllable learned physical rollouts.
- Reusable fields: ActionDoF, DynamicsMask, RenderingState, PolicyRollout, ControllabilityScore.
- Possible baseline role: sim-to-real action-conditioned world-model baseline.
- Implications for our task / benchmark: dynamics and appearance should be evaluated separately, especially under fine-grained controls.

## Reproduction / Follow-up

- What to check before using: segmentation dependency, OOD object coverage, and policy-ranking calibration.
- Code / checkpoint availability: recheck the official page; code was marked coming soon on 2026-07-27.
- Citation or related-work caveats: performance and scale are reported by the authors and not independently reproduced.

