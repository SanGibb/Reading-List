# WorldArena 2.0: Extending Embodied World Model Benchmarking on Modality, Functionality and Platform

candidate_id: CAND-0048
branch: E
decision: accepted_for_registry
authors: Shang et al.
year: 2026
venue: arXiv / benchmark

## Source Links

- Paper: https://arxiv.org/abs/2605.17912
- Project: https://world-arena.ai/
- Code: https://world-arena.ai/
- Data / benchmark: https://world-arena.ai/
- Demo / video: https://world-arena.ai/
- Official figures: https://world-arena.ai/

## TL;DR

WorldArena 2.0 is worth adding separately from the original WorldArena because it materially broadens the evaluation surface from vision-only, simulator-centric embodied world-model testing toward visuotactile, interactive-RL, and cross-platform evaluation. For this repository, that makes it a better fit for closed-loop interactive generation and robot-world utility assessment than the earlier benchmark alone. Main caveat: the benchmark site is active and may continue evolving after the paper snapshot.

## Novelty

- What is actually new: extends WorldArena along modality, functionality, and platform, adding visuotactile evaluation, interactive RL environment use, and real-world multi-embodiment testing.
- Difference from prior work: compared with the earlier WorldArena release, this version moves beyond policy evaluation and planning into policy optimization and beyond simulator-only studies into mixed simulated and real-world settings.
- Why the delta matters: our target use case needs evaluation that distinguishes good-looking world models from models that actually help policy learning and action planning in embodied loops.

## Contributions

1. Expands embodied world-model benchmarking from visual prediction to multimodal, functional, and cross-platform testing.
2. Defines evaluation for world models as data engines, policy evaluators, action planners, and interactive RL environments.
3. Keeps a public benchmark site and leaderboard, giving the reading list a living external reference for embodied world-model utility.

## Task

- Input: world-model rollouts conditioned on robot observations, actions, instructions, and in the expanded setting visuotactile signals.
- Output: benchmark scores for perceptual quality, interactive utility, policy evaluation fidelity, action planning quality, and RL-environment usefulness.
- Setting: embodied world-model evaluation across simulated and real-world robotic platforms.
- Success criterion: comprehensive measurement of whether a world model is useful for downstream embodied decision making, not only visually plausible.

## Data

- Dataset / benchmark: WorldArena 2.0 benchmark suite with leaderboard-backed evaluation and robot-world-model test tasks.
- Scale: the official site describes 16 perceptual metrics across 6 sub-dimensions plus three embodied downstream task families; the arXiv abstract adds the modality/functionality/platform extensions.
- Modalities: video and visuotactile signals, robot observations, actions, and instruction-conditioned embodied rollouts.
- Collection / annotation: benchmark-side evaluation integrates automated metrics and human evaluation on the official site.
- Splits / evaluation protocol: the official page details perceptual evaluation, embodied data engine evaluation, embodied policy evaluator correlation, and embodied action planner execution.

## Method

- Core pipeline: evaluate world models on perceptual quality plus three downstream embodied roles, then aggregate results with EWMScore-style summary metrics.
- Model / representation: benchmark and evaluation framework rather than a new generative model.
- Training or optimization: includes evaluation setups where world models are fine-tuned or paired with inverse dynamics models and policy models for data-engine and planner tests.
- Inference / deployment: measures world models as rollout generators, environment proxies, and planning modules in closed-loop embodied tasks.
- Losses or metrics: official site lists 16 normalized perceptual metrics spanning visual quality, motion quality, consistency, physics adherence, 3D accuracy, and controllability.

## Key Figures / Architecture

figure_status: linked_official

- Figure / demo: official overview, benchmark comparison table, evaluation framework, leaderboard, and visualization examples on the benchmark site.
- Source: https://world-arena.ai/
- Render:
  Official figure/demo page: https://world-arena.ai/
- What it shows: the site directly exposes benchmark dimensions, comparison with prior world-model benchmarks, and example good/bad rollout visualizations.
- Why it matters: for a benchmark paper, this is enough official material to validate scope and utility without needing separate demo-quality judgment.

## Evidence Trail

| Claim | Source | Status | Notes |
|---|---|---|---|
| Extends evaluation to visuotactile modality, broader functionality, and real-world platforms | https://arxiv.org/abs/2605.17912 | verified | Central abstract claim. |
| Official benchmark site exposes leaderboard, dataset, challenge, and comparison table | https://world-arena.ai/ | verified | Directly visible on the official page. |
| Perceptual evaluation uses 16 metrics across 6 sub-dimensions | https://world-arena.ai/ | verified | Stated in the overview and evaluation framework sections. |
| Functional evaluation covers data engine, policy evaluator, and action planner roles | https://world-arena.ai/ | verified | Described in the official framework section. |

## Evidence

- Main metrics: the official site documents 16 perceptual metrics and downstream embodied evaluation roles; the paper positions the expanded benchmark as a comprehensive cross-platform testbed.
- Qualitative results: the site includes visualization examples comparing good and bad rollout cases and a public leaderboard surface.
- Ablations: not reproduced locally; benchmark internals should be cited from the paper or official page.
- Baselines: use the official leaderboard and paper tables rather than secondary summaries.
- Reproducibility signals: public website, public submission path, leaderboard, challenge, and dataset links are strong infrastructure signals.

## Limitations

- Method limitations: benchmark scope can still shift as the public site evolves.
- Experimental limitations: this repository did not rerun benchmark protocols or verify leaderboard states locally.
- Demo / visual limitations: visuals are benchmark illustrations rather than model-specific demos, which is acceptable for an infrastructure paper.
- Claims that remain unverified: exact versioning and frozen protocol details should be checked before making longitudinal comparisons with the original WorldArena paper.

## Project Relevance

- Relevance to interactive embodied generation: highly relevant as an evaluation harness for deciding whether world generators and action-conditioned simulators are actually useful for policy learning, policy evaluation, and planning.
- Reusable fields: BenchmarkDimension, PerceptualMetric, FunctionalMetric, DataEngineEvaluation, PolicyEvaluatorCorrelation, ActionPlannerScore, and CrossPlatformSetting.
- Possible baseline role: default external benchmark reference for embodied world-model utility.
- Implications for our task / benchmark: offers a concrete template for evaluating future interactive embodied generation systems on more than image quality.

## Reproduction / Follow-up

- What to check before using: protocol freeze date, leaderboard version, dataset access terms, and whether the challenge rules changed after June 15, 2026.
- Code / checkpoint availability: the official WorldArena site links to submission, leaderboard, challenge, and dataset surfaces.
- Citation or related-work caveats: treat leaderboard and benchmark scope as date-sensitive; cite the exact paper version and access date for the website.
