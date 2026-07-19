# ESI-Bench: Towards Embodied Spatial Intelligence that Closes the Perception-Action Loop

candidate_id: CAND-0001
branch: C
decision: accepted_for_registry
authors: Hong et al.
year: 2026
venue: arXiv / project page

## Source Links

- Paper: https://arxiv.org/abs/2605.18746
- Project: https://esi-bench.github.io/
- Code: https://github.com/ESI-Bench/ESI-Bench
- Data / benchmark: https://github.com/ESI-Bench/ESI-Bench
- Demo / video: https://esi-bench.github.io/
- Official figures: https://esi-bench.github.io/

## TL;DR

ESI-Bench is one of the clearest July 19, 2026 additions for the spatial-intelligence branch because it forces agents to gather evidence through action instead of answering from passive views or oracle observations. The official paper and project page position the benchmark as an OmniGibson-based perception-action loop with 10 task categories, 29 subcategories, and 3,081 embodied spatial questions. Main caveat: it is still a benchmark rather than a deployed embodied policy system, so its value here is diagnostic and evaluative rather than directly generative.

## Novelty

- What is actually new: a benchmark for embodied spatial intelligence where the observer is an actor that must move, inspect, and manipulate to resolve occlusion, containment, dynamics, and functionality.
- Difference from prior work: prior spatial-intelligence benchmarks often assume passive viewing or oracle observations; ESI-Bench explicitly closes the perception-action loop.
- Why the delta matters: this repository needs evidence that spatial reasoning remains valid when the agent must decide how to collect the observations, not only how to interpret them.

## Contributions

1. Builds an embodied spatial-intelligence benchmark on OmniGibson instead of a passive-view QA setup.
2. Covers 10 task categories and 29 subcategories with 3,081 embodied questions requiring perception, locomotion, and manipulation choices.
3. Shows that active exploration materially changes benchmark behavior relative to passive baselines, making the benchmark relevant to embodied control and world understanding.

## Task

- Input: embodied scene state plus a question whose answer cannot always be resolved from the current viewpoint.
- Output: a correct spatial answer produced after appropriate active exploration and/or manipulation.
- Setting: embodied spatial reasoning in interactive simulated environments.
- Success criterion: answer the question correctly while choosing actions that expose the needed hidden evidence.

## Data

- Dataset / benchmark: ESI-Bench built on OmniGibson.
- Scale: 10 task categories, 29 subcategories, and 3,081 embodied spatial questions.
- Modalities: 3D simulated environments, embodied action, camera/view changes, manipulation, and language questions.
- Collection / annotation: the official project page describes benchmark construction around active information gathering and core spatial knowledge tasks.
- Splits / evaluation protocol: use the source-reported protocol and task taxonomy directly from the paper when citing exact leaderboard numbers.

## Method

- Core pipeline: pose a spatial question, let the agent decide what actions to take to gather evidence, and evaluate whether the final answer closes the perception-action loop correctly.
- Model / representation: benchmark plus evaluation harness rather than a single new model family.
- Training or optimization: benchmark-centric; the main contribution is benchmark design rather than base-model training.
- Inference / deployment: useful for testing whether embodied systems know how to look, move, and manipulate before answering.
- Losses or metrics: use the paper's task-level accuracy and active-versus-passive comparisons when citing exact performance.

## Key Figures / Architecture

figure_status: linked_official

- Figure / demo: official benchmark overview and example embodied question flows.
- Source: https://esi-bench.github.io/
- Render:
  Official figure/demo page: https://esi-bench.github.io/
- What it shows: the project page visualizes the perception-action framing, task taxonomy, and example situations where passive observation is insufficient.
- Why it matters: it makes clear why embodied spatial reasoning must be evaluated as information gathering rather than static recognition.

## Evidence Trail

| Claim | Source | Status | Notes |
|---|---|---|---|
| ESI-Bench closes the perception-action loop for spatial intelligence | https://arxiv.org/abs/2605.18746 | verified | Abstract frames the observer as an actor. |
| The benchmark spans 10 task categories and 29 subcategories | https://esi-bench.github.io/ | verified | Official project page states the counts directly. |
| The benchmark contains 3,081 embodied questions | https://esi-bench.github.io/ | verified | Official project page reports the benchmark size. |
| Official code and dataset are public | https://github.com/ESI-Bench/ESI-Bench | verified | Public repository is linked from the project page. |

## Evidence

- Main metrics: the official sources report substantial gains from active exploration over passive observation, which is exactly the benchmark property that matters here.
- Qualitative results: the project page shows examples where agents must move, reveal hidden geometry, or manipulate objects to answer correctly.
- Ablations: use the paper for per-task breakdowns and active-versus-passive analysis.
- Baselines: cite model comparisons only as source-reported.
- Reproducibility signals: primary paper plus dedicated official project and public code repository.

## Limitations

- Method limitations: benchmark coverage is still bounded by OmniGibson task design and the chosen taxonomy.
- Experimental limitations: this repository did not re-run the benchmark locally.
- Demo / visual limitations: visual quality is not the acceptance gate because this is a benchmark paper, but the official examples are still useful for interpreting behavior.
- Claims that remain unverified: long-term benchmark maintenance, exact dataset packaging details, and downstream reuse friction.

## Project Relevance

- Relevance to interactive embodied generation: directly useful for checking whether generated or reconstructed worlds preserve the active spatial affordances needed for embodied decision-making.
- Reusable fields: ActiveObservation, HiddenState, Containment, Occlusion, ManipulationProbe, and EmbodiedSpatialQuestion.
- Possible baseline role: branch-C benchmark for active spatial reasoning rather than passive spatial QA.
- Implications for our task / benchmark: strong validator for whether a world representation supports action-dependent evidence gathering.

## Reproduction / Follow-up

- What to check before using: download path, exact task taxonomy, OmniGibson version pinning, and evaluation scripts.
- Code / checkpoint availability: official public repository and dataset links are available from the project page.
- Citation or related-work caveats: describe benchmark results as source-reported unless independently rerun.
