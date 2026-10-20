# CHORUS: Decentralized Multi-Embodiment Collaboration with One VLA Policy

<!-- curation-review:start -->
> 2026-10-20 按新版标准复审：**待视觉复核**。同权重独立副本且无需通信的异构协作是明确新任务能力；主源实验可查，但本轮未观看队友扰动和同步接触时序。
> [本次来源、分数与任务判断](../library_review.md#paper-2036ef164d31)。下文保留原精读；旧验收标签不代表本次重新通过，所有实验仍为作者报告。
<!-- curation-review:end -->

## Source Links

- Paper: https://arxiv.org/abs/2606.12352
- Project and videos: https://chorus-model.github.io/

## TL;DR

CHORUS fine-tunes one pi0.5 backbone for a heterogeneous robot team, then lets each robot run the same weights from only local cameras and a robot-identity prompt. Official real-world videos and evaluations show decentralized collaboration on transport, handover, measurement, and lifting without shared observations or communication.

## Novelty

Weight sharing is used not merely for parameter efficiency but to induce an implicit teammate representation: every embodiment learns from all perspectives while deployment remains local and decentralized.

## Contributions

1. One padded action interface for embodiments with different spaces and control rates.
2. Fully decentralized inference without shared cameras, state, or communication.
3. Controlled comparisons with per-robot and centralized policies.
4. Demonstration of unchanged architecture on a three-robot team.

## Task Definition

Each robot maps its local observations and identity-conditioned task prompt to its own actions while jointly completing a physical task with heterogeneous teammates.

## Data / Dataset / Benchmark

Real multi-robot demonstrations and evaluations cover mobile tape measurement, book handover, laundry-basket lifting, and three-robot transport using ARX, YAM, and Kinova systems.

## Method / Pipeline

A sampler draws single-robot observation/action tuples from pooled multi-robot demonstrations. The shared VLA predicts padded 32-dimensional actions, and identical policy copies run independently at deployment.

## Key Figures / Architecture

figure_status: linked_official

The official page includes the shared-training/decentralized-deployment diagram and side-by-side videos of success, perturbation recovery, and baseline failures: https://chorus-model.github.io/

## Evidence Trail

| Claim | Primary source | Status |
|---|---|---|
| No inference-time communication or shared observation | https://arxiv.org/abs/2606.12352 | verified |
| 64-point gain over decentralized from-scratch models | https://chorus-model.github.io/ | verified, source-reported |
| 40-point reactivity improvement | https://chorus-model.github.io/ | verified, source-reported |
| Three-robot task reaches 90% success | https://chorus-model.github.io/ | verified, source-reported |

## Evidence / Metrics / Qualitative Results

CHORUS reports outperforming centralized VLA baselines despite strictly local inputs. Official videos show re-grasping after teammate perturbations and physically synchronized heterogeneous motion; videos are disclosed as 4× playback.

## Limitations

Tasks and team sizes are small, demonstrations are coordinated offline, and independent copies do not guarantee safety or deadlock avoidance. Results depend on a closed pi0.5 backbone and do not establish open reproducibility.

## Project Relevance

CHORUS motivates explicit RobotIdentity, LocalObservation, SharedPolicy, TeammateState, and CommunicationConstraint fields in multi-agent embodied-world evaluation.

## Reproduction / Follow-up Notes

- Test team-size and embodiment extrapolation beyond training.
- Measure failures under delayed/asymmetric observations and teammate substitution.
- Compare explicit communication with the implicit shared-backbone representation.
