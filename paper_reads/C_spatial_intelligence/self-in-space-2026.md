# Self in Space: Benchmarking Self-Awareness and Spatial Cognition in UAV Embodied Intelligence

candidate_id: CAND-0001
branch: C
decision: accepted_for_registry

## Source Links

- Paper: https://arxiv.org/abs/2607.12477
- Project: https://choucisan.github.io/publications/self-in-space/
- Code: https://github.com/IntelliSensing/Self-in-Space
- Data / benchmark: https://huggingface.co/datasets/choucsan/SIS-Bench
- Demo / video: official project page video selector
- Official figures: official project Figures 1–3

## TL;DR

SIS-Bench tests whether aerial video MLLMs understand both the surrounding space and the UAV's own evolving motion state. Its public code/data and explicit perception-memory-reasoning hierarchy make it a strong embodied spatial evaluation reference; the main caveat is its UAV-specific, multiple-choice setting.

## Novelty

- What is actually new: joint evaluation of external spatial cognition and internal/self motion awareness.
- Difference from prior work: the agent is modeled as a moving entity, not only as an observer of the environment.
- Why the delta matters: action prediction and path planning require a coherent estimate of both world and self-state.

## Contributions

1. SIS-Bench: 4,856 QA pairs across 13 tasks from 1,646 real UAV videos.
2. A space/self × perception/memory/reasoning capability hierarchy and evaluation of 26 video MLLMs.
3. SIS-Motion, an optical-flow feature-fusion baseline whose gains transfer to UAV navigation in author-reported experiments.

## Task

- Input: single, concatenated, long, or shuffled UAV videos and a four-choice question.
- Output: an answer about space, self-motion, memory, consistency, action prediction, or path planning.
- Setting: zero-shot video MLLM evaluation on real aerial footage.
- Success criterion: exact-match accuracy by task and capability level.

## Data

- Dataset / benchmark: SIS-Bench from AirScape, UrbanVideo-Bench, and VisDrone.
- Scale: 4,856 QA pairs, 1,646 videos, about 14.9 hours, 13 tasks.
- Modalities: video, multiple-choice language questions, action/spatial annotations.
- Collection / annotation: task-conditioned processing, VLM-assisted metadata where appropriate, and dual-expert verification.
- Splits / evaluation protocol: deterministic zero-shot decoding with adaptive sampling up to 32 frames; exact-match accuracy.

## Method

- Core pipeline: video processing → task-specific annotation → QA construction → dual-expert verification.
- Model / representation: SIS-Motion fuses optical-flow motion features with visual embeddings.
- Training or optimization: controlled fine-tuning study on a Qwen2.5-VL baseline.
- Inference / deployment: standard video MLLM evaluation scripts are public.
- Losses or metrics: task-level and aggregate accuracy.

## Key Figures / Architecture

figure_status: linked_official

- Figure / demo: Figures 1–3 and representative UAV videos.
- Source: https://choucisan.github.io/publications/self-in-space/
- What it shows: capability taxonomy, construction process, data distribution, and representative motion/spatial scenarios.
- Why it matters: the figures make the benchmark's self/world decomposition and temporal demands auditable.

## Evidence Trail

| Claim | Source | Status | Notes |
|---|---|---|---|
| 4,856 QA pairs, 13 tasks, 1,646 videos | official project and dataset card | verified | Both primary surfaces agree. |
| 26 video MLLMs evaluated | official project full results | verified | Six proprietary and 20 open models. |
| Code and benchmark availability | GitHub and Hugging Face | verified | Evaluation scripts and data card are public. |

## Evidence

- Main metrics: human overall accuracy is reported at 91.7%; the strongest listed proprietary model is 71.6% overall, exposing a large gap.
- Qualitative results: official videos span urban, residential, construction, campus, lakeside, and low-light scenes.
- Ablations: SIS-Motion isolates the value of explicit motion cues.
- Baselines: 26 video-capable proprietary and open MLLMs.
- Reproducibility signals: public code, dataset, model collection, and explicit frame-sampling protocol.

## Limitations

- Method limitations: SIS-Motion is a controlled baseline rather than a general embodied policy.
- Experimental limitations: UAV footage and four-choice QA constrain transfer to manipulation or free-form control.
- Demo / visual limitations: videos demonstrate benchmark coverage, not closed-loop flight execution.
- Claims that remain unverified: navigation transfer is author-reported and not independently reproduced here.

## Project Relevance

- Relevance to interactive embodied generation: evaluates whether generated/observed worlds preserve agent-relative spatial and motion cues.
- Reusable fields: AgentState, MotionHistory, SpatialMemory, ActionPrediction, PathPlanning.
- Possible baseline role: diagnostic benchmark for video spatial intelligence and ego-motion awareness.
- Implications for our task / benchmark: world representations should encode self-state explicitly, not only scene geometry.

## Reproduction / Follow-up

- What to check before using: dataset licenses inherited from source video corpora and exact split definitions.
- Code / checkpoint availability: evaluation code and dataset are public.
- Citation or related-work caveats: distinguish passive video QA from closed-loop embodied control.
