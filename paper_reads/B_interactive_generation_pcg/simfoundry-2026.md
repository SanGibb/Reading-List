# SimFoundry: Modular and Automated Scene Generation for Policy Learning and Evaluation

candidate_id: CAND-0002
branch: B
decision: accepted_for_registry

## Source Links

- Paper: https://arxiv.org/abs/2606.28276
- Project: https://research.nvidia.com/labs/gear/simfoundry/
- Code: https://github.com/NVlabs/simfoundry
- Data / benchmark: https://research.nvidia.com/labs/gear/simfoundry/
- Demo / video: https://research.nvidia.com/labs/gear/simfoundry/
- Official figures: https://research.nvidia.com/labs/gear/simfoundry/

## TL;DR

Connects automated real-to-sim reconstruction with systematic digital-cousin generation and validates both policy ranking and zero-shot real transfer. Direct compiler reference for SceneAsset, Articulation, PhysicalParameter, DigitalTwin, DigitalCousin, TaskVariant, and sim-real validation fields. The main caveat is that the reported gains remain source-reported and were not independently reproduced in this collection run.

## Novelty

- What is actually new: Connects automated real-to-sim reconstruction with systematic digital-cousin generation and validates both policy ranking and zero-shot real transfer.
- Difference from prior work: It closes a concrete gap between isolated perception/generation components and reusable embodied execution, policy, or evaluation infrastructure.
- Why the delta matters: Direct compiler reference for SceneAsset, Articulation, PhysicalParameter, DigitalTwin, DigitalCousin, TaskVariant, and sim-real validation fields.

## Contributions

1. A modular extraction-generation-augmentation pipeline segments a video, reconstructs objects and background, estimates physics and articulation, compiles an OmniGibson scene, and generates affordance-preserving cousins.
2. Short real-world videos converted into digital twins plus object, scene, and task digital cousins across seven manipulation tasks and five policy architectures.
3. The paper reports mean sim-real Pearson correlation 0.911 and zero-shot real success gains of 17%, 21%, and 40% from object, scene, and task cousins.

## Task

- Input: Source-specific visual observations, language/task context, state, or action signals.
- Output: Automatically build editable simulation-ready scenes for robot-policy training and evaluation from real video.
- Setting: Embodied simulation and/or real-robot evaluation described by the official source.
- Success criterion: The reported task metrics, transfer performance, or infrastructure validation protocol.

## Data

- Dataset / benchmark: Short real-world videos converted into digital twins plus object, scene, and task digital cousins across seven manipulation tasks and five policy architectures.
- Scale: See the official paper and project page; central scale claims are source-traced below.
- Modalities: RGB/video plus task-specific actions, kinematics, language, geometry, or simulator state.
- Collection / annotation: Defined by the official source; synthetic and real components are kept distinct.
- Splits / evaluation protocol: Use the paper's official split and matched-baseline protocol before reproducing comparisons.

## Method

- Core pipeline: A modular extraction-generation-augmentation pipeline segments a video, reconstructs objects and background, estimates physics and articulation, compiles an OmniGibson scene, and generates affordance-preserving cousins.
- Model / representation: Task-specific learned representations and explicit embodied state/action interfaces.
- Training or optimization: Follow the official paper; this report does not infer undisclosed settings.
- Inference / deployment: Automatically build editable simulation-ready scenes for robot-policy training and evaluation from real video.
- Losses or metrics: See the official paper for exact objectives and evaluation definitions.

## Key Figures / Architecture

figure_status: linked_official

- Figure / demo: Official method overview and qualitative/demo evidence.
- Source: https://research.nvidia.com/labs/gear/simfoundry/
- Render: linked rather than copied to preserve provenance and avoid stale assets.
- What it shows: Official project videos show reconstruction, editing, articulated interaction, bimanual tasks, and sim-to-real executions.
- Why it matters: It directly supports the acceptance gate for architecture, execution, visual quality, or infrastructure completeness.

## Evidence Trail

| Claim | Source | Status | Notes |
|---|---|---|---|
| Dataset scale / benchmark size | https://arxiv.org/abs/2606.28276 | verified | Checked on the primary paper surface. |
| Main reported result or comparison | https://arxiv.org/abs/2606.28276 | verified | Reported by authors; not independently reproduced. |
| Code / checkpoint / demo availability | https://research.nvidia.com/labs/gear/simfoundry/ | verified | Official project surface inspected on 2026-10-05. |

## Evidence

- Main metrics: The paper reports mean sim-real Pearson correlation 0.911 and zero-shot real success gains of 17%, 21%, and 40% from object, scene, and task cousins.
- Qualitative results: Official project videos show reconstruction, editing, articulated interaction, bimanual tasks, and sim-to-real executions.
- Ablations: Consult the official paper for component-level ablations.
- Baselines: Comparisons are accepted only as source-reported and protocol-dependent.
- Reproducibility signals: demo score 4/5; evidence strength 5/5; official project and code available.

## Limitations

- Method limitations: Scope and robustness remain bounded by the embodiments, environments, tasks, and action interfaces studied.
- Experimental limitations: Cross-paper metric comparisons may be invalid when success definitions or hardware differ.
- Demo / visual limitations: Official demos are curated; long-tail failures and full unedited trial distributions are not always exposed.
- Claims that remain unverified: All headline metrics are author-reported and were not independently reproduced.

## Project Relevance

- Relevance to interactive embodied generation: Direct compiler reference for SceneAsset, Articulation, PhysicalParameter, DigitalTwin, DigitalCousin, TaskVariant, and sim-real validation fields.
- Reusable fields: derive typed fields from the nouns named above, while preserving source-specific units and coordinate frames.
- Possible baseline role: High-value reference for its primary branch and for cross-branch integration tests.
- Implications for our task / benchmark: Add source-aligned validators for the claimed transfer, controllability, consistency, or evaluation capability.

## Reproduction / Follow-up

- What to check before using: licenses, exact data splits, success criteria, hardware/action conventions, and whether all checkpoints are public.
- Code / checkpoint availability: https://github.com/NVlabs/simfoundry
- Citation or related-work caveats: Cite results as reported by the authors and avoid treating project-page summaries as independent verification.
