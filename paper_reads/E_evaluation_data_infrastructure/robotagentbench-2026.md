# RobotAgentBench: Towards Open-world Robot Autonomy

candidate_id: CAND-0001  
branch: E  
decision: accepted_for_registry  
acceptance_policy_version: 2

## Source Links

- Paper: https://arxiv.org/abs/2610.34649
- Project: https://aetherlabsai.github.io/RobotAgentBench/
- Code: https://github.com/AetherLabsAI/RobotAgentBench
- Data / benchmark: https://huggingface.co/datasets/AetherLabs-AI/RobotAgentBench-assets
- Demo / video: https://aetherlabsai.github.io/RobotAgentBench/assets/video/demo.mp4

## TL;DR

RobotAgentBench is a released Isaac-Sim benchmark for household robot agents that expands evaluation from fixed instruction execution to task discovery, contextual choice, recovery, robustness and open-ended assistance. Its major caveat is the substantial native simulation setup and lack of independent reproduction in this review.

## Novelty

- What is actually new: a unified planning-execution-verification protocol spanning six autonomy dimensions and scenario-level needs.
- Difference from prior work: compared with BiGym 2.0, it directly evaluates discovery, context reasoning and recovery rather than only a fixed manipulation curriculum.
- Why the delta matters: it exposes whether an agent can identify and recover the right physical work, not only execute a known trajectory.

## Acceptance Rationale / Registry Comparison

- impact_score / justification: 5/5; released runtime, scoring, assets, saved configurations and model clients form a reusable foundation.
- project_relevance_score / direct interface: 5/5; its observation/action worker and process scores can directly validate generated household scenes and agent recovery.
- evidence_strength: 5/5; primary paper, official code, hashed assets, documentation and temporal media are inspectable.
- selection_basis: reusable_infrastructure
- acceptance_rationale: sustained reading value comes from the complete, executable autonomy evaluation stack.
- comparison_to_registry.closest_paper: BiGym 2.0
- comparison_to_registry.material_difference: open-world discovery, context, recovery and high-level need fulfillment.
- comparison_to_registry.why_new_entry: the autonomy protocol is not covered by the closest manipulation benchmark.

## Contributions

1. Fifty household layouts and multi-level task/scenario evaluation.
2. Released task backends, runtime, scoring, assets and saved configurations.
3. Process scores for physical progress plus failure-recovery and robustness dimensions.

## Task

- Input: synchronized cameras, robot state, context and explored map.
- Output: physical action chunks and task completion.
- Setting: AgiBot G1 in simulated household layouts.
- Success criterion: task-specific process/completion scores and scenario fulfillment.

## Task Frontier / Lifecycle

- task_ids: `e-open-world-household-robot-autonomy`
- Role: current; first admitted member of this narrow scope.
- Pending comparison: matched-cost comparison with other household agent benchmarks remains open.

## Data

- 50 layouts; 90 atomic, 18 short, 8 long and 4 open-ended scenarios.
- Versioned assets and 1,470 saved configurations; author-provided evaluation instances differ from paper instances.

## Method

- Agent-assisted, human-in-the-loop real-to-sim construction.
- Generic observation/action worker with task-owned backends and scoring.
- Version-pinned native environment and immutable resource manifests.

## Key Figures / Architecture

figure_status: linked_official

- Official overview: https://github.com/AetherLabsAI/RobotAgentBench/blob/main/docs/images/robotagentbench-overview.png
- It links task-level capabilities to scenario-level autonomous assistance.

## Visual / Demo Inspection

- requires_visual_review: true
- requires_temporal_demo: true
- visual_quality_decision: strong

| Official media actually inspected | Modality | Locator | Observation and coverage | Limits |
|---|---|---|---|---|
| official demo | video | 00:10, 00:35 | Diverse household tasks; context labels map multiple cleanup actions to ongoing execution. | Edited montage; not benchmark-rate evidence. |
| recovery clip | video | 00:03-00:08 | Humanoid manipulates a cup in a repeated-attempt recovery scene. | One selected case. |

## Evidence Trail

| Claim | Source | Status | Used for acceptance? | Notes |
|---|---|---|---|---|
| Evaluator, assets and six dimensions are released | https://github.com/AetherLabsAI/RobotAgentBench | verified | true | Official repository. |
| 50 layouts and task counts | https://arxiv.org/abs/2610.34649 | verified | true | Author-reported. |

## Evidence

- Public Apache-2.0 evaluator; versioned assets and model examples.
- Visuals demonstrate task and context diversity; no independent metric reproduction.

## Limitations

- Requires Linux, Docker, NVIDIA tooling and Isaac Sim-compatible GPU.
- Paper results remain author-reported; selected clips do not establish long-tail reliability.

## Project Relevance

- Direct interface: use the JSONL worker and process scorers as a downstream validator for generated household worlds and autonomous agents.
- Reusable fields: observation/action contracts, saved state, recovery and robustness perturbations.

## Reproduction / Follow-up

- Pin the evaluator, asset and configuration versions before comparison.
- Separate setup/runtime failures from scored episodes.
