# MolmoAct2: Action Reasoning Models for Real-world Deployment

candidate_id: CAND-0047
branch: D
decision: accepted_for_registry
authors: Fang et al.
year: 2026
venue: arXiv / Ai2 release

## Source Links

- Paper: https://arxiv.org/abs/2605.02881
- Project: https://allenai.org/blog/molmoact2
- Code: https://allenai.org/blog/molmoact2
- Data / benchmark: https://allenai.org/blog/molmoact2
- Demo / video: https://allenai.org/blog/molmoact2
- Official figures: https://allenai.org/blog/molmoact2

## TL;DR

MolmoAct2 is a strong open VLA baseline for this repository because it combines an embodied-reasoning backbone, an open action tokenizer, new low-cost robot data, and extensive simulation plus real-robot evaluation in one release. The most important delta for us is not just higher benchmark scores, but that Ai2 publicly ties embodied reasoning, bimanual data, deployment latency, and reproducible release artifacts into a usable action-model stack. Main caveat: the official release is broad, but it is still concentrated on supported embodiments rather than universal cross-robot deployment.

## Novelty

- What is actually new: a fully open action-reasoning VLA stack with Molmo 2-ER, a KV-cache bridge to a flow-matching action expert, adaptive-depth reasoning, and newly released training data.
- Difference from prior work: compared with earlier open VLA releases, MolmoAct2 emphasizes deployment speed, bimanual support, and public release completeness instead of only benchmark wins or single-arm finetuning.
- Why the delta matters: for our reading list, this is a reusable reference for action-token interfaces, embodied reasoning to action transfer, and practical open-model deployment on manipulators.

## Contributions

1. Introduces Molmo 2-ER plus MolmoAct2 as an open reasoning-to-action pipeline for robot control.
2. Releases MolmoAct2-Bimanual YAM and a broader mixed robot-data recipe spanning Franka, SO100/101, Bridge, and Open X-Embodiment subsets.
3. Reports simulation, zero-shot real-world, post-training, and third-party benchmark results with strong qualitative and latency evidence.

## Task

- Input: visual robot observations, language instructions, and optionally depth-aware reasoning tokens or user-provided visual traces.
- Output: robot action sequences for single-arm and bimanual manipulation, with optional deeper spatial reasoning via MolmoAct2-Think.
- Setting: open VLA deployment and adaptation across household, tabletop, and wet-lab-like manipulation settings.
- Success criterion: strong task success in simulation and real-robot execution while retaining practical inference speed and open reproducibility.

## Data

- Dataset / benchmark: MolmoAct2-Bimanual YAM, filtered DROID Franka, SO100/101 data, Google Robot BC-Z, Fractal, Bridge WidowX, legacy MolmoAct data, MolmoBot, RoboEval, LIBERO, and embodied-reasoning benchmarks.
- Scale: the arXiv abstract reports a 3.3M-sample embodied-reasoning corpus; the Ai2 blog reports more than 700 to 720 hours of bimanual demonstrations and over 30x more robot data than MolmoAct.
- Modalities: RGB robot observations, language instructions, action tokens, continuous actions, and selective depth reasoning.
- Collection / annotation: the official blog says robot demonstrations were re-annotated with an open VLM to improve instruction diversity and quality.
- Splits / evaluation protocol: official evaluation spans simulation, zero-shot Franka tests, post-training on single-arm and bimanual tasks, LIBERO, and a Cortex AI third-party benchmark.

## Method

- Core pipeline: Molmo 2-ER encodes embodied reasoning; a dedicated action expert predicts actions through flow matching; a KV-cache bridge connects the VLM and action stack; MolmoAct2-Think routes depth reasoning only when useful.
- Model / representation: embodied-reasoning VLM plus open action tokenizer and continuous-action expert.
- Training or optimization: specialize-then-rehearse embodied-reasoning training plus multi-source robot-data mixing and annotation cleanup.
- Inference / deployment: near-real-time action calls relative to the prior MolmoAct release, with optional adaptive-depth reasoning for harder 3D cases.
- Losses or metrics: source-reported metrics include MolmoBot success, RoboEval score, per-task real-world success, LIBERO post-training success, and third-party bimanual evaluation.

## Key Figures / Architecture

figure_status: linked_official

- Figure / demo: official Ai2 release images showing architecture, benchmark tables, and robot rollouts.
- Source: https://allenai.org/blog/molmoact2
- Render:
  Official figure/demo page: https://allenai.org/blog/molmoact2
- What it shows: the page includes the MolmoAct2 architecture summary, simulation and real-world quantitative comparisons, and qualitative robot task examples.
- Why it matters: this is enough official evidence to judge that the release is not a paper-only claim and that robot execution quality clears the acceptance bar.

## Evidence Trail

| Claim | Source | Status | Notes |
|---|---|---|---|
| 3.3M embodied-reasoning corpus for Molmo 2-ER | https://arxiv.org/abs/2605.02881 | verified | Stated in the abstract. |
| Largest open-source bimanual dataset and 700 to 720 hours of demonstrations | https://allenai.org/blog/molmoact2 | verified | Official release page states the dataset size and positioning. |
| Full code, training data, and LeRobot integration are publicly released | https://allenai.org/blog/molmoact2 | verified | Explicitly stated in the 2026-05-28 update section. |
| Real-world and third-party evaluation outperform pi0.5 / OpenVLA-OFT baselines | https://allenai.org/blog/molmoact2 | verified | Use as source-attributed reported results, not independently reproduced facts. |

## Evidence

- Main metrics: the official blog reports 20.6% MolmoBot success versus 10.3% for pi0.5, 0.443 RoboEval versus 0.405 for pi0.5, 87.1% average zero-shot Franka success, 97.2% LIBERO post-training success for MolmoAct2, and 98.1% for MolmoAct2-Think.
- Qualitative results: the official release page shows multiple real robot tasks, including apple-on-plate, pipette placement, knife-in-box, towel folding, tray lifting, and wet-lab manipulation.
- Ablations: adaptive-depth routing and tokenizer/open-data choices are discussed, but this run does not reproduce them locally.
- Baselines: reported comparisons include MolmoAct, pi0.5, OpenVLA-OFT, Cosmos Policy, and X-VLA in different settings.
- Reproducibility signals: primary arXiv source, official release page, explicit code/data release update, and LeRobot integration together make this one of the cleaner recent open VLA releases.

## Limitations

- Method limitations: the official blog notes batchwise planning rather than fully reactive control, and limited out-of-the-box support to the robot setups emphasized during training.
- Experimental limitations: benchmark claims are source-reported and not reproduced locally in this repository.
- Demo / visual limitations: the visuals are official and convincing, but still curated release materials.
- Claims that remain unverified: exact GitHub/Hugging Face artifact structure, licenses, and long-term maintenance should be rechecked before downstream use.

## Project Relevance

- Relevance to interactive embodied generation: strong baseline for the action side of our world-to-policy stack, especially where spatial reasoning, intervention traces, and simulator-generated data need to land in executable robot behavior.
- Reusable fields: Observation, ActionToken, ContinuousAction, DepthReasoning, TrajectoryTrace, Embodiment, PostTrainingProtocol, and ThirdPartyEvaluation.
- Possible baseline role: open VLA baseline for reasoning-heavy manipulation and low-cost/bimanual deployment comparisons.
- Implications for our task / benchmark: useful anchor when deciding whether generated or reconstructed worlds are rich enough to support policy finetuning, action rollout evaluation, or cross-embodiment adaptation.

## Reproduction / Follow-up

- What to check before using: exact code repo path, supported robot configurations, model licenses, and whether the released training data matches the claims needed for a given comparison.
- Code / checkpoint availability: the official Ai2 release page states that model weights, training data, evaluation rollouts, tokenizer recipe, and full code are released.
- Citation or related-work caveats: when citing benchmark wins, phrase them explicitly as reported by Ai2 or the arXiv paper unless independently reproduced.
