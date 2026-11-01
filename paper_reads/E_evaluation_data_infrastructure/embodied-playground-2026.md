# Embodied Playground: A Long-Horizon Agentic Robotics Benchmark for Physical, Strategic, and Spatial Reasoning

candidate_id: CAND-0003  
branch: E  
decision: accepted_for_registry  
acceptance_policy_version: 2

## Source Links

- Paper: https://arxiv.org/abs/2610.27039
- Project: https://winniechen2002.github.io/Agent-bench-website/
- Code: https://github.com/Winniechen2002/Embodied-Playground
- Demo provenance: https://winniechen2002.github.io/Agent-bench-website/evidence/demo-manifest.json

## TL;DR

Embodied Playground releases 410 robot task environments spanning manipulation, puzzles and multi-stage household work, evaluated with independent goal, rule and physical-validity checks. Its official videos convincingly show contact-rich reference executions, but those clips must not be read as external-agent scores.

## Novelty

- Broad long-horizon catalog with strategic and spatial constraints.
- Independent checks for endpoint goal, task rules and physical validity.
- Machine-readable task/results indexes and explicit media provenance.

## Acceptance Rationale / Registry Comparison

- impact_score: 4/5; substantial reusable environment/evaluation release.
- project_relevance_score: 4/5; direct harness for generated-scene tasks and physics/rule checks.
- evidence_strength: 4/5; primary paper, official code, indexes and inspected temporal evidence.
- selection_basis: reusable_infrastructure
- acceptance_rationale: provides a broad, explicit long-horizon physical reasoning protocol.
- comparison_to_registry.closest_paper: RobotAgentBench
- material_difference: strategic puzzles, 410 environments and independent physical/rule checks versus open-world household autonomy dimensions.
- why_new_entry: complementary task families and validation semantics.

## Contributions

1. 410 environments and EP-100/EP-20 curated subsets.
2. Five suites and 16 task types with difficulty splits.
3. Shared interface and independent validity checks.

## Task

- Input: goal, visual/proprioceptive observations and declared tools.
- Output: robot control code/actions and completion signal.
- Setting: simulated manipulation, puzzles and household activities.
- Success criterion: goal reached without violating task rules or physical validity.

## Task Frontier / Lifecycle

- task_ids: `e-long-horizon-physical-strategic-reasoning`
- Role: current; first admitted member of this narrow scope.
- Pending: matched repeated-trial comparison with other agent benchmarks.

## Data

- 410 environments; EP-100, EP-Easy/Hard and EP-20.
- Five suites and 16 task types; public indexes document membership and results.

## Method

- Shared describe/observe/step/finish-style agent loop.
- Declared observation/tool access, resource budgets and repeated trials.
- Goal, rule and physical-validity checks remain independent.

## Key Figures / Architecture

figure_status: linked_official

- Official project task catalog and provenance-linked reference videos.

## Visual / Demo Inspection

- requires_visual_review: true
- requires_temporal_demo: true
- visual_quality_decision: strong

| Media | Modality | Locator | Observation | Limits |
|---|---|---|---|---|
| Rubik reference cycle | video | 00:05, 00:20 | Franka maintains contact while rotating the cube. | Privileged reference; not full solve or agent score. |
| Kongming assembly | video | 00:05, 00:20, 00:40 | Dual-arm multi-piece assembly progresses with visually coherent pieces. | 6x derivative; official provenance reports 1.064 mm max penetration. |

## Evidence Trail

| Claim | Source | Status | Used for acceptance? | Notes |
|---|---|---|---|---|
| 410 environments and validity checks | https://winniechen2002.github.io/Agent-bench-website/ | verified | true | Official page and indexes. |
| Reference-video provenance | https://winniechen2002.github.io/Agent-bench-website/evidence/demo-manifest.json | verified | true | Limits retained explicitly. |

## Evidence

- Public benchmark code, task index, result index and media provenance.
- Temporal media supports task executability, not external-agent performance.

## Limitations

- Reference-controller recordings do not establish policy scores.
- Broad suites may have heterogeneous difficulty and compute costs.

## Project Relevance

- Direct evaluation harness for interactive generated scenes, multi-stage rules and physical validity.
- Useful baseline for long-horizon agentic PCG evaluation.

## Reproduction / Follow-up

- Record observation level, tool access, budgets and trial counts.
- Keep goal, rule and physical-validity failures separate.
