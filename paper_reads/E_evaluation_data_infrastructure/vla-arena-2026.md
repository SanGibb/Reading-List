# VLA-Arena: An Open-Source Framework for Benchmarking Vision-Language-Action Models

candidate_id: CAND-0002
branch: E
decision: accepted_for_registry
year: 2026
venue: ICML 2026

## Source Links

- Paper: https://arxiv.org/abs/2512.22539
- Project: https://vla-arena.github.io/
- Code: https://github.com/PKU-Alignment/VLA-Arena
- Data / benchmark: https://vla-arena.github.io/
- Demo / video: https://github.com/PKU-Alignment/VLA-Arena
- Official figures: https://github.com/PKU-Alignment/VLA-Arena

## TL;DR

VLA-Arena: An Open-Source Framework for Benchmarking Vision-Language-Action Models is included because it improves the repository's coverage of evaluation infrastructure for interactive embodied generation rather than adding yet another method paper with unclear downstream value. The key contribution is separates VLA capability-frontier measurement into orthogonal structure/language/visual axes instead of collapsing everything into one aggregate success rate. For this repository, the most important point is that the paper gives a concrete benchmark, protocol, or release surface that can be reused when we need to judge whether world models or VLA systems are actionable, reliable, controllable, and reproducible. Main caveat: It is simulator-centric and VLA-specific, so it does not directly evaluate world-model video rollouts or open-domain interactive generation.

## Novelty

- What is actually new: separates VLA capability-frontier measurement into orthogonal structure/language/visual axes instead of collapsing everything into one aggregate success rate
- Difference from prior work: it evaluates embodied/world-model systems with a more structured and reusable protocol than prior single-metric or model-specific evaluations.
- Why the delta matters: our repository needs validators and benchmark templates that test whether generated worlds are useful for interaction, action, policy evaluation, and physical consistency instead of only looking visually plausible.

## Contributions

1. Defines a benchmark/problem setting centered on: systematically benchmark VLA robustness, safety, extrapolation, distractor handling, and long-horizon composition under controlled perturbations.
2. Provides a reusable evaluation method built around: structured benchmark design over task structure, language command, and visual observation axes with unified tooling for task modeling, training, and automated evaluation.
3. Supplies benchmark/release evidence that is directly reusable for this repository's evaluation branch.

## Task

- Input: benchmark inputs, trajectories, generated futures, or task-conditioned observations described by the official source.
- Output: benchmark scores, diagnostic measurements, or failure analyses for interactive world models or VLA systems.
- Setting: Evaluation and Data Infrastructure within an interactive embodied generation reading list.
- Success criterion: benchmark results expose actionable limits of controllability, physical faithfulness, generalization, or reproducibility rather than only aesthetic quality.

## Data

- Dataset / benchmark: 170 tasks across 11 specialized suites with three difficulty levels, plus VLA-Arena-S/M/L datasets and orthogonal language and visual perturbation settings
- Scale: use the official scale reported by the primary or official source in this report's evidence trail.
- Modalities: video, actions, trajectories, benchmark annotations, robot execution traces, or perturbation settings depending on the paper.
- Collection / annotation: source-specific; this run records only primary-source claims and did not independently reannotate or reproduce the benchmark.
- Splits / evaluation protocol: follow the paper/project page; local reproduction was not performed in this run.

## Method

- Core pipeline: structured benchmark design over task structure, language command, and visual observation axes with unified tooling for task modeling, training, and automated evaluation
- Model / representation: benchmark/infrastructure paper rather than a new deployed world model; the important abstraction is the evaluation protocol and its score schema.
- Training or optimization: when training is involved, treat it as benchmark setup or evaluated-model context rather than the main novelty.
- Inference / deployment: deployment mode is benchmark execution, leaderboard comparison, or evaluation harness use.
- Losses or metrics: use reported metrics only as source-attributed evidence until reproduced locally.

## Key Figures / Architecture

figure_status: linked_official

- Figure / demo: official project / repository / benchmark surface.
- Source: https://github.com/PKU-Alignment/VLA-Arena
- Render:
  Official figure/demo page: https://github.com/PKU-Alignment/VLA-Arena
- What it shows: the official benchmark overview, task structure, metric taxonomy, release surface, or leaderboard view for the method.
- Why it matters: for infrastructure papers, the official benchmark/leaderboard surface is more important than screenshotting generated samples.

## Evidence Trail

| Claim | Source | Status | Notes |
|---|---|---|---|
| VLA-Arena defines 170 tasks grouped into Safety, Distractor, Extrapolation, and Long Horizon dimensions. | https://arxiv.org/abs/2512.22539 | verified | arXiv abstract states the 170-task structure and four dimensions. |
| The benchmark uses orthogonal language and visual perturbations and ships datasets/framework/leaderboard. | https://arxiv.org/abs/2512.22539 | verified | Primary abstract and project links state W0-W4, V0-V4, datasets, and leaderboard. |
| Official open-source framework is public. | https://github.com/PKU-Alignment/VLA-Arena | verified | GitHub repo contains toolchain and task suites. |

## Evidence

- Main metrics: the official sources describe how the benchmark measures controllability, physical faithfulness, robustness, consistency, or reproducibility; use those task-specific metrics instead of generic video quality alone.
- Qualitative results: visual/demo decision is `not_applicable` with score 0 because this is a benchmark or infrastructure paper; official pages were still inspected for benchmark structure and release quality.
- Ablations: not reproduced locally; cite the original paper or official project tables for benchmark ablations.
- Baselines: compare against the benchmark's own baseline list and leaderboard rather than secondary summaries.
- Reproducibility signals: source quality is `primary_or_official`, demo score is 5, evidence strength is 5.

## Limitations

- Method limitations: It is simulator-centric and VLA-specific, so it does not directly evaluate world-model video rollouts or open-domain interactive generation.
- Experimental limitations: this run did not execute the released benchmark code or reproduce reported scores.
- Demo / visual limitations: benchmark illustrations and public release surfaces were inspected, but no claim here should be read as an independent model reproduction.
- Claims that remain unverified: long-term maintenance, future leaderboard drift, or evolving release maturity may change after 2026-07-13.

## Project Relevance

- Relevance to interactive embodied generation: Strong infrastructure reference for evaluation schemas, perturbation taxonomies, and task-difficulty ladders for embodied policy assessment.
- Reusable fields: BenchmarkDimension, PerturbationAxis, ControlSignal, PhysicsMetric, WorldConsistencyMetric, ReliabilityScore, LeaderboardEntry, and ValidationReport.
- Possible baseline role: use this paper as a benchmark or evaluator template inside branch E.
- Implications for our task / benchmark: it helps the repository judge whether generated or predicted worlds are only visually plausible or actually useful for embodied action, control, and evaluation.

## Reproduction / Follow-up

- What to check before using: exact released code/data scope, protocol freeze date, and whether benchmark leaderboards or task definitions changed after 2026-07-13.
- Code / checkpoint availability: https://github.com/PKU-Alignment/VLA-Arena.
- Citation or related-work caveats: phrase all strong results and benchmark rankings as reported by the source unless independently reproduced.
