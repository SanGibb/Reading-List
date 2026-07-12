# RoboWM-Bench: A Benchmark for Evaluating World Models in Robotic Manipulation

candidate_id: CAND-0001
branch: E
decision: accepted_for_registry
year: 2026
venue: CVPR Workshops 2026

## Source Links

- Paper: https://arxiv.org/abs/2604.19092
- Project: https://github.com/fffstrong/RoboWM-Bench
- Code: https://github.com/fffstrong/RoboWM-Bench
- Data / benchmark: https://github.com/fffstrong/RoboWM-Bench
- Demo / video: https://github.com/fffstrong/RoboWM-Bench
- Official figures: https://github.com/fffstrong/RoboWM-Bench

## TL;DR

RoboWM-Bench: A Benchmark for Evaluating World Models in Robotic Manipulation is included because it improves the repository's coverage of evaluation infrastructure for interactive embodied generation rather than adding yet another method paper with unclear downstream value. The key contribution is moves world-model evaluation from visual plausibility to embodiment-grounded action executability for robotic manipulation. For this repository, the most important point is that the paper gives a concrete benchmark, protocol, or release surface that can be reused when we need to judge whether world models or VLA systems are actionable, reliable, controllable, and reproducible. Main caveat: Workshop-paper scope is narrower than broader cross-domain world-model benchmarks, and the benchmark is centered on manipulation rather than navigation or open-domain interaction.

## Novelty

- What is actually new: moves world-model evaluation from visual plausibility to embodiment-grounded action executability for robotic manipulation
- Difference from prior work: it evaluates embodied/world-model systems with a more structured and reusable protocol than prior single-metric or model-specific evaluations.
- Why the delta matters: our repository needs validators and benchmark templates that test whether generated worlds are useful for interaction, action, policy evaluation, and physical consistency instead of only looking visually plausible.

## Contributions

1. Defines a benchmark/problem setting centered on: evaluate whether video world-model predictions can be translated into executable manipulation actions that still complete the intended task.
2. Provides a reusable evaluation method built around: convert generated behaviors into executable action sequences, replay them in a robotics execution loop, and score physically executable task completion with failure-mode analysis.
3. Supplies benchmark/release evidence that is directly reusable for this repository's evaluation branch.

## Task

- Input: benchmark inputs, trajectories, generated futures, or task-conditioned observations described by the official source.
- Output: benchmark scores, diagnostic measurements, or failure analyses for interactive world models or VLA systems.
- Setting: Evaluation and Data Infrastructure within an interactive embodied generation reading list.
- Success criterion: benchmark results expose actionable limits of controllability, physical faithfulness, generalization, or reproducibility rather than only aesthetic quality.

## Data

- Dataset / benchmark: manipulation-centric benchmark that turns generated human-hand and robotic manipulation videos into embodied action sequences and validates them through execution in standardized manipulation scenarios
- Scale: use the official scale reported by the primary or official source in this report's evidence trail.
- Modalities: video, actions, trajectories, benchmark annotations, robot execution traces, or perturbation settings depending on the paper.
- Collection / annotation: source-specific; this run records only primary-source claims and did not independently reannotate or reproduce the benchmark.
- Splits / evaluation protocol: follow the paper/project page; local reproduction was not performed in this run.

## Method

- Core pipeline: convert generated behaviors into executable action sequences, replay them in a robotics execution loop, and score physically executable task completion with failure-mode analysis
- Model / representation: benchmark/infrastructure paper rather than a new deployed world model; the important abstraction is the evaluation protocol and its score schema.
- Training or optimization: when training is involved, treat it as benchmark setup or evaluated-model context rather than the main novelty.
- Inference / deployment: deployment mode is benchmark execution, leaderboard comparison, or evaluation harness use.
- Losses or metrics: use reported metrics only as source-attributed evidence until reproduced locally.

## Key Figures / Architecture

figure_status: linked_official

- Figure / demo: official project / repository / benchmark surface.
- Source: https://github.com/fffstrong/RoboWM-Bench
- Render:
  Official figure/demo page: https://github.com/fffstrong/RoboWM-Bench
- What it shows: the official benchmark overview, task structure, metric taxonomy, release surface, or leaderboard view for the method.
- Why it matters: for infrastructure papers, the official benchmark/leaderboard surface is more important than screenshotting generated samples.

## Evidence Trail

| Claim | Source | Status | Notes |
|---|---|---|---|
| Manipulation benchmark converts generated behaviors into embodied action sequences and validates them through execution. | https://openaccess.thecvf.com/content/CVPR2026W/GigaBrainChallenge/html/Jiang_RoboWM-Bench_A_Benchmark_for_Evaluating_World_Models_in_Robotic_Manipulation_CVPRW_2026_paper.html | verified | CVPRW abstract states execution-grounded conversion and validation. |
| Benchmark exposes failure modes in spatial reasoning, contact prediction, and deformation. | https://openaccess.thecvf.com/content/CVPR2026W/GigaBrainChallenge/html/Jiang_RoboWM-Bench_A_Benchmark_for_Evaluating_World_Models_in_Robotic_Manipulation_CVPRW_2026_paper.html | verified | Primary abstract lists these persistent failure modes. |
| Official code is public. | https://github.com/fffstrong/RoboWM-Bench | verified | Public GitHub repository exists. |

## Evidence

- Main metrics: the official sources describe how the benchmark measures controllability, physical faithfulness, robustness, consistency, or reproducibility; use those task-specific metrics instead of generic video quality alone.
- Qualitative results: visual/demo decision is `not_applicable` with score 0 because this is a benchmark or infrastructure paper; official pages were still inspected for benchmark structure and release quality.
- Ablations: not reproduced locally; cite the original paper or official project tables for benchmark ablations.
- Baselines: compare against the benchmark's own baseline list and leaderboard rather than secondary summaries.
- Reproducibility signals: source quality is `primary_or_official`, demo score is 4, evidence strength is 4.

## Limitations

- Method limitations: Workshop-paper scope is narrower than broader cross-domain world-model benchmarks, and the benchmark is centered on manipulation rather than navigation or open-domain interaction.
- Experimental limitations: this run did not execute the released benchmark code or reproduce reported scores.
- Demo / visual limitations: benchmark illustrations and public release surfaces were inspected, but no claim here should be read as an independent model reproduction.
- Claims that remain unverified: long-term maintenance, future leaderboard drift, or evolving release maturity may change after 2026-07-13.

## Project Relevance

- Relevance to interactive embodied generation: Direct benchmark reference for whether generated embodied futures are actionable enough for manipulation-policy learning and validation.
- Reusable fields: BenchmarkDimension, PerturbationAxis, ControlSignal, PhysicsMetric, WorldConsistencyMetric, ReliabilityScore, LeaderboardEntry, and ValidationReport.
- Possible baseline role: use this paper as a benchmark or evaluator template inside branch E.
- Implications for our task / benchmark: it helps the repository judge whether generated or predicted worlds are only visually plausible or actually useful for embodied action, control, and evaluation.

## Reproduction / Follow-up

- What to check before using: exact released code/data scope, protocol freeze date, and whether benchmark leaderboards or task definitions changed after 2026-07-13.
- Code / checkpoint availability: https://github.com/fffstrong/RoboWM-Bench.
- Citation or related-work caveats: phrase all strong results and benchmark rankings as reported by the source unless independently reproduced.
