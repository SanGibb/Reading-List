# StellaVLA: In-Context Structured Demonstration for Generalizable Vision-Language-Action Models

## Source Links
- Paper: https://arxiv.org/abs/2608.11671
- Official project: https://stelledge.com/blog/stellavla

## TL;DR
StellaVLA turns one retrieved robot, human-hand, or XR trajectory into a structured task plan, subgoals, and verbalized 3D motion, then uses that structure as test-time context for OOD manipulation without fine-tuning.

## Novelty

One retrieved trajectory is converted into transferable structured reasoning rather than copied as a pixel-level demonstration.

## Contributions
- Automated structured-demonstration generation with no human annotation.
- Cross-embodiment in-context guidance from robot, human, or XR demonstrations.
- Dual training internalizes language/action reasoning while retaining action-expert-only real-time inference.

## Task
Test-time adaptation of VLA manipulation policies under new scenes, viewpoints, objects, and embodiments.

## Data
LIBERO, LIBERO-Plus, VLA-Arena, and a real-robot benchmark with robot, human-hand, and XR demonstrations.

## Method
A retrieval stage selects one demonstration; an offline pipeline converts it into plans, subgoals, and 3D motion language. Joint action-language training teaches the policy to use this structure, while inference keeps the high-frequency action path.

## Key Figures / Architecture
figure_status: linked_official

The official paper links the project and includes the structured-demonstration pipeline and cross-embodiment real-robot examples.

## Evidence Trail
| Claim | Source | Status |
|---|---|---|
| Single structured demonstration enables test-time adaptation | paper method | verified |
| VLA-Arena score 0.63 | paper and linked leaderboard snapshot | source-reported |
| 98.8% LIBERO / 85.1% LIBERO-Plus | paper tables | source-reported |
| Human/XR-to-robot transfer | paper real-robot section | source-reported |

## Evidence
The paper reports leading aggregate benchmark results and real-robot OOD gains across demonstration sources. The visual evidence is adequate: architecture and representative cross-embodiment rollouts are legible, though the project page is less extensive than G0.5.

## Limitations
- One-demo retrieval quality is a new failure point.
- Leaderboard comparisons may evolve rapidly.
- No independent replication and limited public implementation detail at this release.

## Project Relevance
Strong reference for reusable demonstration schemas, cross-embodiment prompting, and test-time VLA adaptation.

## Reproduction / Follow-up
Recheck the live VLA-Arena rank, request code/checkpoints, and test sensitivity to poor or semantically mismatched retrieved demonstrations.
