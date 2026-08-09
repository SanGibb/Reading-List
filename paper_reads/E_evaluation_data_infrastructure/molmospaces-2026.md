# MolmoSpaces: A Large-Scale Open Ecosystem for Robot Navigation and Manipulation

candidate_id: CAND-0001
branch: E
decision: accepted_for_registry

## Source Links

- Paper: https://arxiv.org/abs/2602.11337
- Project: https://allenai.github.io/molmospaces/
- Code: https://github.com/allenai/molmospaces
- Data / benchmark and demo: https://molmospaces.allen.ai/
- Official figures: https://allenai.github.io/molmospaces/

## TL;DR

MolmoSpaces is an open, simulator-agnostic ecosystem of more than 230,000 indoor environments, 130,000 object assets, 48,000 manipulable objects, and 42 million stable grasps, paired with eight embodied benchmark tasks. The same assets support data generation, policy training, and evaluation across MuJoCo, Isaac, and ManiSkill; current benchmark tooling is most mature in MuJoCo.

## Novelty

- Unifies scenes, objects, grasps, tasks, adapters, and evaluation at unusual scale.
- Combines handcrafted, procedural, Objaverse-derived, and LLM-generated scenes.
- Makes controlled long-tail generalization and cross-simulator reuse practical.

## Contributions

1. Releases 230K+ environments and 130K objects with manipulation metadata.
2. Provides 42M stable grasps and eight navigation/manipulation tasks.
3. Publishes code, assets, leaderboards, and policy integrations with sim-to-real analysis.

## Task

- Input: scene, robot, instruction, and task configuration.
- Output: navigation/manipulation trajectory and success result.
- Setting: static/mobile manipulation, navigation, and multi-room tasks.
- Success criterion: completion under controlled scene/object variation.

## Data

- Dataset / benchmark: MolmoSpaces and MolmoSpaces-Bench.
- Scale: 230K+ scenes, 130K objects, 48K manipulable objects, 42M grasps, eight tasks.
- Modalities: 3D scenes/assets, MJCF/USD, grasps, task JSON, observations, trajectories.
- Collection / annotation: THOR/Objaverse assets plus procedural and Holodeck-derived families.
- Splits / evaluation protocol: task configurations, policy comparisons, and sim-to-real rank analysis.

## Method

- Core pipeline: asset normalization, scene conversion, grasp generation, rollout, evaluation.
- Model / representation: portable assets with explicit physical/grasp metadata.
- Training or optimization: supports scripted generation and external policies.
- Inference / deployment: adapters for MuJoCo, Isaac, and ManiSkill.
- Losses or metrics: task success and policy-ranking correlation.

## Key Figures / Architecture

figure_status: linked_official

- Figure / demo: ecosystem overview and interactive environment browser.
- Source: https://allenai.github.io/molmospaces/
- What it shows: diverse furnished scenes, manipulable objects, interactions, and leaderboard.
- Why it matters: scene diversity and executable coverage are directly inspectable.

## Evidence Trail

| Claim | Source | Status | Notes |
|---|---|---|---|
| 230K+ environments, 130K objects, 42M grasps | https://arxiv.org/abs/2602.11337 | verified | Paper and repository agree. |
| Eight tasks and multi-simulator assets | https://github.com/allenai/molmospaces | verified | Public configs and asset table. |
| Sim-to-real R=0.96, rho=0.98 | https://arxiv.org/abs/2602.11337 | verified | Reported, not reproduced. |

## Evidence

- Main metrics: reported Pearson 0.96 and Spearman 0.98 policy-ranking correlation.
- Qualitative results: official browser exposes diverse environments and interactions.
- Ablations: prompt wording, joint initialization, and camera occlusion sensitivities.
- Baselines: multiple zero-shot policies on the shared suite.
- Reproducibility signals: public code, versioned assets, configs, docs, and leaderboard.

## Limitations

- Source-asset and generated-layout quality varies.
- Eight tasks cover only part of household interaction complexity.
- The browser is a curated snapshot, and correlation claims remain source-reported.

## Project Relevance

- Direct source of executable worlds and policy-facing tests.
- Reusable fields: SceneFamily, ObjectAsset, StableGrasp, SimulatorAdapter, TaskConfig.
- Baseline role: common substrate for generated-scene validation.
- Generated scenes should export portable physics assets and task definitions.

## Reproduction / Follow-up

- Check per-family licenses, quality distribution, and simulator parity.
- Code, assets, benchmark configs, and policies are public.
- Distinguish ecosystem scale from task diversity when citing.
