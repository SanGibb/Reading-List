# JEPA-WAM: Learning Vision-Language-Action Policies with Joint-Embedding World Modeling

## Source Links
- Paper: https://arxiv.org/abs/2608.09381
- Official project: https://spritewithoutice.github.io/JEPA-WAM/

## TL;DR
JEPA-WAM couples spatially structured current/future prediction in V-JEPA space with continuous action generation through one shared predictor, preserving dense correspondences without online video generation.

## Novelty

Dense current/future JEPA targets and action generation are coupled through a shared predictor.

## Contributions
- Joint current-future dense target rather than compressed global latent prediction.
- Shared predictor directly connects transition learning and action generation.
- Can be added to a pretrained VLA while retaining its original perception/action paths.

## Task
Generalizable language-conditioned manipulation under visual and spatial distribution shifts.

## Data
LIBERO-Plus, RoboTwin 2.0, and real-world bimanual manipulation.

## Method
A frozen/pretrained V-JEPA representation supplies structured targets; a Qwen-based predictor learns transitions and provides features to the action head. A pi0.5 instantiation tests compatibility with pretrained VLAs.

## Key Figures / Architecture
figure_status: linked_official

The official project and PDF Figure 1 show architecture, benchmark frontier, and in-/out-of-domain comparisons; later figures cover real-world manipulation.

## Evidence Trail
| Claim | Source | Status |
|---|---|---|
| Shared transition/action predictor | Figure 1 + method | verified |
| 79.2% LIBERO-Plus without large robot-policy pretraining | paper tables | source-reported |
| pi0.5 instantiation reaches 86.3% | paper tables | source-reported |
| Real bimanual evaluation | paper/project | source-reported |

## Evidence
The paper reports strong OOD improvements on LIBERO-Plus, RoboTwin 2.0, and real bimanual tasks, with ablations for target structure and supervision integration.

## Limitations
- Depends on pretrained V-JEPA representations.
- The pi0.5 comparison changes both initialization and capacity.
- Independent reproduction and released checkpoints remain to be verified.

## Project Relevance
High-value latent WAM baseline for dense spatial correspondence, training efficiency, and VLA-compatible world supervision.

## Reproduction / Follow-up
Reproduce the no-pretraining variant, test target collapse/shortcut behavior, and compare dense versus pooled latent targets.
