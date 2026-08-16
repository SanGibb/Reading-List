# World Tokens: Enhancing Embodied Policies with Training-Time World Modeling

## Source Links
- Paper: https://arxiv.org/abs/2608.09730

## TL;DR
World Tokens distills future-video supervision into a fixed set of policy context tokens during training, then removes the video denoiser at deployment so the policy retains VLA-level latency.

## Novelty

Generative future supervision is distilled into fixed world tokens and the expensive denoiser is discarded at deployment.

## Contributions
- A World Adapter is the exclusive context path shared by future-video denoising and action prediction.
- Training gradients force world tokens to encode action-relevant dynamics.
- The generative world branch is discarded at inference.

## Task
Efficient language-conditioned manipulation with training-time world modeling.

## Data
LIBERO, SIMPLER, and real R1 Pro manipulation data; no large embodied action pretraining is claimed for the 2B model.

## Method
VLM features are compressed into fixed world tokens. These tokens condition both a jointly tuned future-video denoiser and the action expert; exclusive routing prevents bypass. Only the VLM, adapter, and action expert remain online.

## Key Figures / Architecture
figure_status: captured_official

The official PDF was rendered locally. Its method diagrams and real-robot evaluation panels provide adequate architecture and physical evidence; no standalone project/code page was found.

## Evidence Trail
| Claim | Source | Status |
|---|---|---|
| Training-only video model | paper method | verified |
| Best reported SIMPLER average | paper tables | source-reported |
| Real R1 Pro improvement over matched action-only baseline | paper evaluation | source-reported |
| Public code/checkpoints | none found | unverified |

## Evidence
The paper reports competitive LIBERO, leading SIMPLER averages, R1 Pro gains, and VLA-level action-chunk latency. Ablations test exclusive routing and world-model supervision.

## Limitations
- No public implementation was verified.
- Future-video quality is instrumental and not itself evaluated as an interactive simulator.
- Results remain author-reported.

## Project Relevance
Direct baseline for distilling a generative dynamics objective into an efficient executable policy representation.

## Reproduction / Follow-up
Request code, reproduce the action-only matched ablation, and measure whether world tokens improve calibration under contact and occlusion shifts.
