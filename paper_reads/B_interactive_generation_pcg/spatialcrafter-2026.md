# SpatialCrafter: Single Image World Modeling with Generative 3D Proxies

candidate_id: CAND-0003
branch: B
decision: accepted_for_registry

## Source Links

- Paper: https://arxiv.org/abs/2608.27073
- Project / demos: https://fangchuan.github.io/SpatialCrafter/

## TL;DR

SpatialCrafter turns one image into a controllable explorable world by first generating a persistent global 3D proxy and then refining appearance with video diffusion. Its official indoor, outdoor and long-video galleries show strong consistency, but code/checkpoints are still TBA and the representation is not a full physics simulator.

## Novelty

- Introduces a generative global 3D proxy rather than sparse geometric hints or panoramas.
- Uses the proxy as persistent spatial memory across chunked long-video generation.
- Separates geometry/structure from high-fidelity appearance refinement.

## Contributions

1. Point-anchored Sparse Structure Flow for globally aligned proxy generation.
2. Camera-controllable appearance refinement conditioned on the proxy.
3. Long-horizon exploration with reduced geometry drift.

## Task

- Input: a single image and camera trajectory.
- Output: explorable scene video consistent with the initial view.
- Setting: diverse indoor and outdoor scenes.
- Success criterion: fidelity, geometry consistency, controllability and long-range persistence.

## Data

- Dataset / benchmark: paper-curated single-image scene and trajectory evaluations.
- Modalities: image, proxy geometry, camera path and generated video.
- Public release: code and models were TBA at review time.

## Method

- Proxy generation: PaSS Flow predicts spatially aligned sparse 3D structure.
- Refinement: a video diffusion stage renders high-fidelity views along controls.
- Memory: the shared global proxy anchors successive chunks.

## Key Figures / Architecture

figure_status: linked_official

- Figure / demo: indoor/outdoor and long-video galleries.
- Source: https://fangchuan.github.io/SpatialCrafter/
- What it shows: consistent revisits and extended camera travel from a single image.
- Why it matters: visualizes how a persistent 3D substrate reduces drift.

## Evidence Trail

| Claim | Source | Status | Notes |
|---|---|---|---|
| SIGGRAPH Asia 2026 | Official project | verified | Venue shown on project/author pages. |
| Long generation uses global 3D proxy memory | Paper/project | verified | Method and gallery agree. |
| Code/checkpoints available | Project | unverified | Marked TBA. |

## Evidence

- Qualitative results: strong indoor/outdoor fidelity and long-horizon consistency.
- Comparisons: official page shows trajectory and long-video comparisons.
- Reproducibility: currently limited to paper/project evidence.

## Limitations

- No code or weights at review time.
- Generated video does not expose queryable object state or physics.
- Official galleries may favor successful trajectories.

## Project Relevance

- Reusable fields: GlobalProxy, CameraTrajectory, SpatialMemory, AppearanceRefinement, RevisitConsistency.
- Baseline role: strong image-to-explorable-world generation baseline.
- Implication: persistent 3D structure should be first-class rather than implicit in recurrent video context.

## Reproduction / Follow-up

- Recheck code/Hugging Face links.
- Test return trajectories, occlusion recovery and collision-aware camera motion after release.

