# Show-Harness: Just a VLM Agent Can Play Robots

<!-- curation-review:start -->
> 2026-10-20 按新版标准复审：**待视觉复核**。将语义action units确定性接机器人解释器以及GUI数据采集提供具体复用接口；主源已核实架构但本轮未观看执行/确认完整release。
> [本次来源、分数与任务判断](../library_review.md#paper-79d6ea3fdd0d)。下文保留原精读；旧验收标签不代表本次重新通过，所有实验仍为作者报告。
<!-- curation-review:end -->

candidate_id: CAND-0002
branch: D
decision: accepted_for_registry

## Source Links

- Paper: https://arxiv.org/abs/2609.10522
- Project / demos: https://showlab.github.io/Show-Harness/
- Code: https://github.com/showlab/Show-Harness
- Models: https://huggingface.co/collections/showlab/show-harness-vlms
- Data: https://huggingface.co/datasets/showlab/Show-Harness-Data

## TL;DR

Show-Harness exposes a compact semantic action vocabulary that a general VLM can reason over, then grounds each symbol through an embodiment-specific interpreter. The same interface supports zero-shot frontier models, small fine-tuned open VLMs, two robot families, simulators, and GUI-based demonstration collection; the main caveat is that interpreter calibration and discrete action granularity remain important engineering dependencies.

## Novelty

- Treats the interface as the primary robot-control abstraction instead of requiring a new large VLA backbone.
- Preserves model responsibility for fine physical decisions while moving kinematics and limits into deterministic interpreters.
- Reuses the same actions for control and GUMI demonstration collection.

## Contributions

1. Cross-embodiment semantic action units for movement, rotation, grasp, release, and termination.
2. A perceive-reason-act plugin harness with planning, proprioception, adaptive steps, history, and recovery.
3. Open code, six LoRA adapters, datasets, simulation support, and real-robot demonstrations.

## Task

- Input: natural-language instruction, multi-view images, and textualized robot state.
- Output: one semantic action unit or a short chunk, grounded into executable motion.
- Setting: zero-shot and fine-tuned VLMs across Franka, AgileX, and simulators.
- Success criterion: task completion under task, environment, and embodiment shifts.

## Data

- GUMI collects labeled demonstrations through human or GUI-agent keystrokes.
- Released data mixes real teleoperation and real-to-sim demonstrations.
- Six LoRA adapters cover open VLM deployment configurations.

## Method

- Plugins assemble perception and state context.
- The VLM plans and emits semantic action units such as `MV_LEFT`, `GRASP`, or `DONE`.
- An interpreter maps units into calibrated Cartesian steps, rotations, gripper commands, and safety projections.
- Fine-tuned mode replaces the planner/controller stack with a small VLM trained on the same interface.

## Key Figures / Architecture

figure_status: linked_official

- Figure / demos: semantic-action overview, harness loop, GUMI, and real-robot videos.
- Source: https://showlab.github.io/Show-Harness/
- What it shows: one model-facing vocabulary operating across scenes, tasks, and embodiments.
- Why it matters: it is an executable interface contract, not only a policy diagram.

## Evidence Trail

| Claim | Source | Status | Notes |
|---|---|---|---|
| Public harness, collectors, plugins, training pipeline, adapters, and data | https://github.com/showlab/Show-Harness | verified | Official release. |
| Cross-task 89%/86%, best baseline 57% | https://showlab.github.io/Show-Harness/ | verified | Zero-shot/fine-tuned author-reported results. |
| Cross-embodiment 93%/87%, best baseline 52% | https://showlab.github.io/Show-Harness/ | verified | Franka + AgileX result card. |

## Evidence

- Official page reports cross-environment 100%/88% across four shifts.
- Fine-tuned model transfers from simulation to real robot at 13/20 while two trainable VLA baselines score 0/20.
- Project page includes real-robot and GUMI execution videos.
- Repository documents mock-robot dry runs and configuration contracts.

## Limitations

- Discrete incremental control may require many model calls.
- Performance depends on calibrated view conventions and embodiment interpreters.
- API-based frontier VLM latency differs materially from small local adapters.
- Evaluation still covers a limited set of robots and manipulation tasks.

## Project Relevance

- Provides a reusable semantic ActionUnit schema and RobotInterpreter boundary.
- Useful pattern for separating reasoning, safety limits, and hardware control.
- GUMI offers low-cost, uniform demonstration capture across embodiments.

## Reproduction / Follow-up

- Reproduce the mock-robot contracts before using hardware.
- Keep prompt version, camera ordering, action vocabulary, and step calibration fixed.
- Audit workspace/table safety bounds for every new embodiment.
