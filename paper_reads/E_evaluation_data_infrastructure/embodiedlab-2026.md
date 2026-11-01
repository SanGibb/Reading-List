# EmbodiedLab: Benchmarking Embodied Agents That Act to Know

candidate_id: CAND-0002  
branch: E  
decision: accepted_for_registry  
acceptance_policy_version: 2

## Source Links

- Paper: https://arxiv.org/abs/2610.35385
- Project: https://hexafuture.ai/benchmarks/embodiedlab/
- Code: https://github.com/HexaFuture/EmbodiedLab
- Demo: https://media.hexafuture.ai/benchmarks/embodiedlab/demo/EmbodiedLab_demo.mp4

## TL;DR

EmbodiedLab evaluates whether a robot can intervene in a physical apparatus, read instruments and infer a resampled unknown value. It contributes an executable “act to know” bridge between manipulation and scientific discovery, but is simulation-only and was not independently reproduced here.

## Novelty

- New capability: physical experimentation is the means of acquiring the answer.
- Difference: unlike offline success proxies, the agent must change and measure executable state.
- Importance: it tests grounded evidence acquisition rather than only reasoning over supplied observations.

## Acceptance Rationale / Registry Comparison

- impact_score: 4/5; distinct task plus released evaluator and controlled experiments.
- project_relevance_score: 4/5; direct validator for intervention-observation-conclusion loops.
- evidence_strength: 4/5; primary paper, official code and inspected demo.
- selection_basis: new_capability
- acceptance_rationale: no maintained entry covers executable act-to-know scientific tasks.
- comparison_to_registry.closest_paper: Sensorimotor Alignment
- material_difference: executable physical evidence acquisition rather than passive representation-level prediction.
- why_new_entry: distinct task, protocol and runtime.

## Contributions

1. Thirty experiments across five disciplines and 14 apparatus platforms.
2. Hidden parameters resampled each instance, preventing memorized answers.
3. Exact scoring of acquired knowledge and required physical state.

## Task

- Input: objective and camera observations of apparatus.
- Output: actions, instrument readings and a grounded conclusion.
- Setting: physics-based simulated laboratory.
- Success criterion: correct conclusion grounded in episode readings plus required physical state.

## Task Frontier / Lifecycle

- task_ids: `e-embodied-act-to-know-science`
- Role: current; first admitted member of this narrow task.
- Pending: real-lab transfer and matched comparisons.

## Data

- 30 experiments, five disciplines, 14 apparatus platforms.
- Parameters are resampled and every experiment is reported solvable.

## Method

- Agent selects a procedure and operates apparatus through cameras and controls.
- Evaluation checks recorded readings, inferred result and physical end state.

## Key Figures / Architecture

figure_status: linked_official

- Official demo links procedure, manipulation, instrument state and conclusion.

## Visual / Demo Inspection

- requires_visual_review: true
- requires_temporal_demo: true
- visual_quality_decision: strong

| Media | Modality | Locator | Observation | Limits |
|---|---|---|---|---|
| official demo | video | 00:45 and 01:30 | Robot manipulates an electrical apparatus; panels show instrument state and verified capacitor goal state. | Edited overview; not all disciplines inspected. |

## Evidence Trail

| Claim | Source | Status | Used for acceptance? | Notes |
|---|---|---|---|---|
| 30 experiments and released evaluator | https://github.com/HexaFuture/EmbodiedLab | verified | true | Official repository. |
| Six-agent comparison | https://arxiv.org/abs/2610.35385 | verified | true | Author-reported. |

## Evidence

- Official code and demo are public.
- Strongest native agent reportedly remains below half success; no independent reproduction.

## Limitations

- Simulation-only; transfer to physical laboratories is untested here.
- Edited video does not establish full episode continuity or failure distribution.

## Project Relevance

- Direct validator for interventions, state changes, measurements and evidence-backed conclusions in executable worlds.
- Useful as a baseline for agents that must learn properties by acting.

## Reproduction / Follow-up

- Verify apparatus dynamics, hidden-parameter generation and scoring isolation.
- Preserve tool/perception conditions when comparing agents.
