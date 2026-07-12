# WorldOlympiad: Can Your World Model Survive a Triathlon?

candidate_id: CAND-0008
branch: E
decision: accepted_for_registry
year: 2026
venue: arXiv

## Source Links

- Paper: https://arxiv.org/abs/2606.11129
- Project: https://alibaba-damo-academy.github.io/WorldOlympiad/
- Code: https://github.com/alibaba-damo-academy/WorldOlympiad
- Data / benchmark: https://github.com/alibaba-damo-academy/WorldOlympiad
- Demo / video: https://alibaba-damo-academy.github.io/WorldOlympiad/
- Official figures: https://alibaba-damo-academy.github.io/WorldOlympiad/

## TL;DR

WorldOlympiad: Can Your World Model Survive a Triathlon? is included because it improves the repository's coverage of evaluation infrastructure for interactive embodied generation rather than adding yet another method paper with unclear downstream value. The key contribution is unifies physical, geometric, and interaction diagnostics across robotics, gaming, and open-domain world-model scenarios rather than isolating one dimension. For this repository, the most important point is that the paper gives a concrete benchmark, protocol, or release surface that can be reused when we need to judge whether world models or VLA systems are actionable, reliable, controllable, and reproducible. Main caveat: Because it spans robotics, gaming, and general video, some metrics are less tightly aligned to embodied manipulation than manipulation-specific benchmarks.

## Novelty

- What is actually new: unifies physical, geometric, and interaction diagnostics across robotics, gaming, and open-domain world-model scenarios rather than isolating one dimension
- Difference from prior work: it evaluates embodied/world-model systems with a more structured and reusable protocol than prior single-metric or model-specific evaluations.
- Why the delta matters: our repository needs validators and benchmark templates that test whether generated worlds are useful for interaction, action, policy evaluation, and physical consistency instead of only looking visually plausible.

## Contributions

1. Defines a benchmark/problem setting centered on: diagnose long-video world models on physical faithfulness, geometric consistency, and interaction fidelity across multiple downstream domains.
2. Provides a reusable evaluation method built around: triathlon-style benchmark with physical, geometry, and interaction tracks using segmentation-based judges, Gaussian-splatting diagnostics, and action-following checks.
3. Supplies benchmark/release evidence that is directly reusable for this repository's evaluation branch.

## Task

- Input: benchmark inputs, trajectories, generated futures, or task-conditioned observations described by the official source.
- Output: benchmark scores, diagnostic measurements, or failure analyses for interactive world models or VLA systems.
- Setting: Evaluation and Data Infrastructure within an interactive embodied generation reading list.
- Success criterion: benchmark results expose actionable limits of controllability, physical faithfulness, generalization, or reproducibility rather than only aesthetic quality.

## Data

- Dataset / benchmark: 1,000 long videos spanning 400 robotics, 400 gaming, and 200 general real-world videos
- Scale: use the official scale reported by the primary or official source in this report's evidence trail.
- Modalities: video, actions, trajectories, benchmark annotations, robot execution traces, or perturbation settings depending on the paper.
- Collection / annotation: source-specific; this run records only primary-source claims and did not independently reannotate or reproduce the benchmark.
- Splits / evaluation protocol: follow the paper/project page; local reproduction was not performed in this run.

## Method

- Core pipeline: triathlon-style benchmark with physical, geometry, and interaction tracks using segmentation-based judges, Gaussian-splatting diagnostics, and action-following checks
- Model / representation: benchmark/infrastructure paper rather than a new deployed world model; the important abstraction is the evaluation protocol and its score schema.
- Training or optimization: when training is involved, treat it as benchmark setup or evaluated-model context rather than the main novelty.
- Inference / deployment: deployment mode is benchmark execution, leaderboard comparison, or evaluation harness use.
- Losses or metrics: use reported metrics only as source-attributed evidence until reproduced locally.

## Key Figures / Architecture

figure_status: linked_official

- Figure / demo: official project / repository / benchmark surface.
- Source: https://alibaba-damo-academy.github.io/WorldOlympiad/
- Render:
  Official figure/demo page: https://alibaba-damo-academy.github.io/WorldOlympiad/
- What it shows: the official benchmark overview, task structure, metric taxonomy, release surface, or leaderboard view for the method.
- Why it matters: for infrastructure papers, the official benchmark/leaderboard surface is more important than screenshotting generated samples.

## Evidence Trail

| Claim | Source | Status | Notes |
|---|---|---|---|
| Benchmark covers physical, geometric, and interactive tracks. | https://alibaba-damo-academy.github.io/WorldOlympiad/ | verified | Official repo/project states the triathlon decomposition. |
| Dataset contains 1,000 long videos including 400 robotics videos. | https://github.com/alibaba-damo-academy/WorldOlympiad | verified | Official repository overview lists the domain split. |
| Official repository is public. | https://github.com/alibaba-damo-academy/WorldOlympiad | verified | Public GitHub repo exists. |

## Evidence

- Main metrics: the official sources describe how the benchmark measures controllability, physical faithfulness, robustness, consistency, or reproducibility; use those task-specific metrics instead of generic video quality alone.
- Qualitative results: visual/demo decision is `not_applicable` with score 0 because this is a benchmark or infrastructure paper; official pages were still inspected for benchmark structure and release quality.
- Ablations: not reproduced locally; cite the original paper or official project tables for benchmark ablations.
- Baselines: compare against the benchmark's own baseline list and leaderboard rather than secondary summaries.
- Reproducibility signals: source quality is `primary_or_official`, demo score is 5, evidence strength is 4.

## Limitations

- Method limitations: Because it spans robotics, gaming, and general video, some metrics are less tightly aligned to embodied manipulation than manipulation-specific benchmarks.
- Experimental limitations: this run did not execute the released benchmark code or reproduce reported scores.
- Demo / visual limitations: benchmark illustrations and public release surfaces were inspected, but no claim here should be read as an independent model reproduction.
- Claims that remain unverified: long-term maintenance, future leaderboard drift, or evolving release maturity may change after 2026-07-13.

## Project Relevance

- Relevance to interactive embodied generation: Strong cross-domain benchmark for long-horizon world-model evaluation with direct relevance to robotics and interactive control.
- Reusable fields: BenchmarkDimension, PerturbationAxis, ControlSignal, PhysicsMetric, WorldConsistencyMetric, ReliabilityScore, LeaderboardEntry, and ValidationReport.
- Possible baseline role: use this paper as a benchmark or evaluator template inside branch E.
- Implications for our task / benchmark: it helps the repository judge whether generated or predicted worlds are only visually plausible or actually useful for embodied action, control, and evaluation.

## Reproduction / Follow-up

- What to check before using: exact released code/data scope, protocol freeze date, and whether benchmark leaderboards or task definitions changed after 2026-07-13.
- Code / checkpoint availability: https://github.com/alibaba-damo-academy/WorldOlympiad.
- Citation or related-work caveats: phrase all strong results and benchmark rankings as reported by the source unless independently reproduced.
