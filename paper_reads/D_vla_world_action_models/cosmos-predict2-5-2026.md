# Cosmos-Predict2.5: A World Foundation Model for Physical AI

candidate_id: CAND-0056
branch: D
decision: accepted_for_registry
authors: NVIDIA Cosmos team
year: 2026
venue: arXiv / NVIDIA release

## Source Links

- Paper: https://arxiv.org/abs/2605.10309
- Project: https://research.nvidia.com/labs/cosmos-lab/cosmos-predict2.5/
- Code: https://research.nvidia.com/labs/cosmos-lab/cosmos-predict2.5/
- Data / benchmark: https://research.nvidia.com/labs/cosmos-lab/cosmos-predict2.5/
- Demo / video: https://research.nvidia.com/labs/cosmos-lab/cosmos-predict2.5/
- Official figures: https://research.nvidia.com/labs/cosmos-lab/cosmos-predict2.5/

## TL;DR

Cosmos-Predict2.5 is worth adding because it is one of the clearest official 2026 releases that positions a generative world model as physical-AI infrastructure rather than generic video synthesis. NVIDIA reports training on 200 million video clips, releasing a 14B model family, and evaluating closed-loop action-conditioned prediction, simulated driving, and robotics-oriented world modeling. Main caveat: the evidence is strong and official, but still centered on NVIDIA's release stack and curated demos.

## Novelty

- What is actually new: a large world foundation model explicitly framed for physical AI with action-conditioned prediction and downstream control-oriented use cases.
- Difference from prior work: compared with generic video world models, Cosmos-Predict2.5 is positioned around controllability, action grounding, and embodiment-facing prediction.
- Why the delta matters: this repository needs strong references for the world-model side of action-conditioned generation, planning, and imagined rollout evaluation.

## Contributions

1. Releases a large-scale world foundation model for physical-AI prediction and simulation.
2. Trains on 200 million video clips and exposes an official model family through NVIDIA's Cosmos release surface.
3. Shows action-conditioned qualitative examples and downstream physical-AI framing relevant to robotics and control.

## Task

- Input: visual observations, optional actions or control context, and prompts describing future physical behavior.
- Output: future video/world predictions that can support control, planning, or simulation-style evaluation.
- Setting: action-conditioned world modeling for physical AI.
- Success criterion: generate coherent, controllable future predictions that preserve physically and behaviorally relevant dynamics.

## Data

- Dataset / benchmark: NVIDIA reports training on 200 million video clips; the release page also positions the model against driving and robotics-style world-model tasks.
- Scale: 200 million clips and a 14B model family, as reported on the official NVIDIA surface.
- Modalities: video, action-conditioned future prediction, and physical-scene dynamics.
- Collection / annotation: described as large-scale video pretraining on the official release page and paper.
- Splits / evaluation protocol: use the paper's reported benchmark and qualitative protocol when citing exact comparisons.

## Method

- Core pipeline: pretrained world foundation model that predicts future observations under action or control context for physical-AI scenarios.
- Model / representation: large generative world model optimized for controllable future prediction.
- Training or optimization: large-scale video pretraining followed by task-facing adaptation/evaluation as reported by the source.
- Inference / deployment: supports world prediction for embodied planning, simulation, and control workflows.
- Losses or metrics: use source-reported benchmark numbers and qualitative evaluations; this repository did not reproduce them locally.

## Key Figures / Architecture

figure_status: linked_official

- Figure / demo: official NVIDIA release page with architecture summaries, result videos, and benchmark framing.
- Source: https://research.nvidia.com/labs/cosmos-lab/cosmos-predict2.5/
- Render:
  Official figure/demo page: https://research.nvidia.com/labs/cosmos-lab/cosmos-predict2.5/
- What it shows: the page presents future-prediction examples, model framing, and quantitative release claims for physical-AI world modeling.
- Why it matters: it provides enough official visual evidence to judge rollout quality as strong rather than leaving the model at abstract benchmark level.

## Evidence Trail

| Claim | Source | Status | Notes |
|---|---|---|---|
| Cosmos-Predict2.5 is framed as a world foundation model for physical AI | https://arxiv.org/abs/2605.10309 | verified | Title and abstract claim. |
| The release reports training on 200 million video clips | https://research.nvidia.com/labs/cosmos-lab/cosmos-predict2.5/ | verified | Official release page states the scale. |
| Official model release includes a 14B family and public release artifacts | https://research.nvidia.com/labs/cosmos-lab/cosmos-predict2.5/ | verified | Stated on the official NVIDIA page. |
| Public demos show action-conditioned future prediction examples | https://research.nvidia.com/labs/cosmos-lab/cosmos-predict2.5/ | verified | Official qualitative examples are visible on the release surface. |

## Evidence

- Main metrics: source-reported comparisons on the NVIDIA release surface and paper should be cited directly as reported.
- Qualitative results: official videos and image sequences show strong future-prediction fidelity and control relevance.
- Ablations: not reproduced locally; use the paper for scaling and architecture ablations.
- Baselines: compare against the official source's listed baselines rather than informal summaries.
- Reproducibility signals: primary arXiv source, official NVIDIA page, and explicit release framing make this a strong world-model entry.

## Limitations

- Method limitations: release artifacts and examples are tied to NVIDIA's ecosystem and may not translate directly into open embodied stacks.
- Experimental limitations: this repository did not run the released models or verify benchmark results.
- Demo / visual limitations: visuals are convincing and varied, but still official release materials rather than independent evaluations.
- Claims that remain unverified: exact license terms, open-weight accessibility details, and breadth of robotics-specific downstream support.

## Project Relevance

- Relevance to interactive embodied generation: highly relevant to the world-model and imagined-rollout side of embodied systems, especially when generated futures feed policy evaluation or planning.
- Reusable fields: WorldPrediction, ActionCondition, FutureRollout, PhysicalDynamics, and ImaginedTrajectory.
- Possible baseline role: large-scale world-model baseline for action-conditioned future generation.
- Implications for our task / benchmark: useful anchor for judging whether embodied world generators should also support control-facing rollout prediction.

## Reproduction / Follow-up

- What to check before using: weight access path, license terms, supported control interfaces, and whether the released artifacts can be integrated into third-party embodied evaluation loops.
- Code / checkpoint availability: the official NVIDIA release page advertises public release artifacts for the model family.
- Citation or related-work caveats: phrase scale and benchmark claims explicitly as source-reported unless independently reproduced.
