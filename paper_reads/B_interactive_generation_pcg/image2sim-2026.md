# Image2Sim: Scaling Embodied Navigation via Generative Neural Simulator

candidate_id: CAND-0001
branch: B
decision: accepted_for_registry

## Source Links

- Paper: https://arxiv.org/abs/2607.05765
- Project / code: https://github.com/MrZihan/Image2Sim
- Demo / official figures: https://github.com/MrZihan/Image2Sim

## TL;DR

Image2Sim turns posed RGB-D image or video collections into real-time neural navigation simulators and an automatic instruction/action data engine. Its main value is the coupling of photorealistic panoramic RGB-D rendering, executable motion, and large-scale navigation supervision; the main caveat is that this run verified reported results and official demos but did not reproduce scene conversion or robot transfer.

## Novelty

- What is actually new: a neural simulator that decouples 3D spatial anchoring from one-step photorealistic panoramic observation synthesis.
- Difference from prior work: it converts ordinary captured imagery into interactive environments instead of requiring hand-built meshes or a fixed synthetic asset library.
- Why the delta matters: it makes real-image diversity usable as executable navigation training infrastructure.

## Contributions

1. Feed-forward feature-Gaussian construction from posed RGB-D sequences.
2. Geometry-aware one-step pixel-flow rendering for panoramic RGB-D observations.
3. Automatic trajectories, actions, and navigation instructions at nearly 20K-scene / 10M-sample scale.

## Task

- Input: posed pinhole or panoramic RGB-D images/videos.
- Output: an interactive neural scene plus rendered observations, executable actions, trajectories, and instructions.
- Setting: embodied navigation training and zero-shot transfer.
- Success criterion: scalable scene construction and improved navigation benchmark / real-world performance.

## Data

- Dataset / benchmark: nearly 20K converted interactive scenes and more than 10M generated navigation samples, as reported by the paper.
- Modalities: RGB-D, camera poses, feature Gaussians, panoramic observations, trajectories, actions, and language instructions.
- Collection / annotation: source imagery is reconstructed and the simulator automatically generates action-aligned supervision.
- Evaluation protocol: major embodied-navigation benchmarks plus real-world zero-shot deployment reported by the authors.

## Method

- Core pipeline: posed RGB-D sequence -> feature-Gaussian encoder -> neural scene -> motion simulation and one-step panoramic rendering -> automatic annotation.
- Model / representation: 3D feature Gaussians provide geometry and semantics; a Geometry-Aware One-Step Pixel Flow model refines sparse projections.
- Training or optimization: rendering learns to map Gaussian projections to high-quality panoramic RGB-D.
- Inference / deployment: real-time observations are generated along executable navigation trajectories.
- Metrics: scene/data scale and downstream navigation success are the collection-critical outcomes.

## Key Figures / Architecture

figure_status: linked_official

- Figure / demo: official framework diagram and navigation videos.
- Source: https://github.com/MrZihan/Image2Sim/blob/main/examples/framework.png
- What it shows: the split between feature-Gaussian anchoring, one-step rendering, motion simulation, and instruction generation.
- Why it matters: the figure makes clear that this is executable data infrastructure rather than a view-synthesis-only system.

## Evidence Trail

| Claim | Source | Status | Notes |
|---|---|---|---|
| Nearly 20K interactive scenes and 10M+ navigation samples | https://arxiv.org/abs/2607.05765 | verified | Reported in the abstract; not independently regenerated. |
| Feature-Gaussian scene plus geometry-aware one-step renderer | https://arxiv.org/abs/2607.05765 | verified | Method is explicit in abstract and official diagram. |
| Official code/demo surface exists | https://github.com/MrZihan/Image2Sim | verified | Public repository contains the framework figure and qualitative videos. |

## Evidence

- Main metrics: the paper reports downstream gains on major navigation benchmarks and zero-shot real-world transfer.
- Qualitative results: official videos show interactive navigation observations in reconstructed neural environments.
- Ablations: paper attributes quality to geometry-aware one-step refinement and scalable simulator-generated supervision.
- Baselines: scanned/synthetic mesh pipelines and prior navigation simulators.
- Reproducibility signals: public GitHub repository; full training/reconstruction was not run locally.

## Limitations

- Method limitations: requires posed RGB-D input and focuses on navigation rather than contact-rich object manipulation.
- Experimental limitations: all scale and performance numbers are author-reported.
- Demo / visual limitations: official examples are convincing but cannot establish robustness over the full 20K-scene distribution.
- Claims that remain unverified: exact reconstruction throughput and real-world transfer were not reproduced.

## Project Relevance

- Relevance to interactive embodied generation: directly converts captured worlds into executable training environments.
- Reusable fields: NeuralScene, FeatureGaussian, CameraPose, PanoramicObservation, NavigableTrajectory, Instruction.
- Possible baseline role: image-to-interactive-navigation-world and data-engine baseline.
- Implications for our task / benchmark: generated worlds should be tested for both visual fidelity and action-aligned navigability.

## Reproduction / Follow-up

- What to check before using: input pose/depth assumptions, simulator action semantics, and scene failure rates.
- Code / checkpoint availability: public repository confirmed; check release completeness before reproduction.
- Citation or related-work caveats: describe benchmark improvements as reported, not independently reproduced.

