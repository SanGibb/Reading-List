# PAWBench: How Far Are We from Probabilistically Aligned World Modeling?

candidate_id: CAND-0004
branch: E
decision: accepted_for_registry

## Source Links

- Paper: https://arxiv.org/abs/2608.27345
- Project / benchmark / code: https://pawbench.github.io/

## TL;DR

PAWBench evaluates a world model as a distribution over possible physical futures, not as a generator of one plausible video. Fifty scenarios separate probability calibration from valid-support coverage; the abstraction is unusually useful for stochastic simulation, though it evaluates terminal outcomes rather than complete trajectory distributions.

## Novelty

- Defines probabilistic alignment for repeated world-model rollouts.
- Separates support recovery from probability-mass calibration.
- Tests how language, initial noise and fine-tuning reshape future distributions.

## Contributions

1. Fifty-scenario benchmark across eight physical mechanisms.
2. PAW-Calibration and PAW-Coverage tracks.
3. Eleven-model diagnosis and distribution-shaping probes.

## Task

- Input: fixed source image and atomic action prompt, sampled repeatedly.
- Output: an empirical distribution over mapped terminal outcomes.
- Success criterion: recover valid outcomes and, where known, their reference probabilities.

## Data

- Scale: 50 scenarios; 25 calibrated and 25 coverage-only.
- Modalities: conditioning images, prompts, generated videos, terminal-outcome schemas.
- Protocol: identical conditions across repeated samples.

## Method

- Map each rollout to a readable terminal outcome.
- Aggregate the empirical support and probability mass.
- Score calibration and support separately.
- Probe language steering, noise exploration and fine-tuning.

## Key Figures / Architecture

figure_status: linked_official

- Figure / demo: possible-future branching and benchmark protocol.
- Source: https://pawbench.github.io/
- What it shows: why a single plausible future cannot establish a calibrated simulator.
- Why it matters: converts stochasticity into an explicit evaluation object.

## Evidence Trail

| Claim | Source | Status | Notes |
|---|---|---|---|
| 50 scenarios / eight mechanisms | Official project | verified | Benchmark description. |
| 25 calibration and 25 coverage cases | Official project | verified | Track definitions. |
| Eleven-model diagnosis | Official project | verified | Author-reported evaluation. |

## Evidence

- Main finding: no evaluated model jointly delivers accurate probabilities, broad support and reliable cross-scene behavior.
- Qualitative evidence: official pages show multi-future outcomes and failure patterns.
- Reproducibility: benchmark/code links are exposed on the project page.

## Limitations

- Terminal outcomes discard intermediate trajectory differences.
- Reference probabilities exist for only half the benchmark.
- Fifty scenarios cannot cover open-world stochastic physics.

## Project Relevance

- Reusable fields: PossibleOutcome, OutcomeSupport, ReferenceProbability, EmpiricalProbability, CalibrationError.
- Baseline role: stochastic world-model evaluation protocol.
- Implication: interactive generation needs repeated-rollout tests, not single-sample aesthetics alone.

## Reproduction / Follow-up

- Fix sampling budget and random seeds when comparing models.
- Keep calibration and coverage results separate.
- Audit the outcome mapper for ambiguous terminal states.

