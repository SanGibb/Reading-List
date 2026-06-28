# VLA-REPLICA: A Low-Cost, Reproducible Benchmark for Real-World Evaluation of Vision-Language-Action Models

candidate_id: CAND-0058
branch: E
decision: accepted_for_registry
authors: Huang et al.
year: 2026
venue: arXiv / project page

## Source Links

- Paper: https://arxiv.org/abs/2605.20774
- Project: https://irvlutd.github.io/VLAReplica/
- Code: https://irvlutd.github.io/VLAReplica/
- Data / benchmark: https://irvlutd.github.io/VLAReplica/
- Demo / video: https://irvlutd.github.io/VLAReplica/
- Official figures: https://irvlutd.github.io/VLAReplica/

## TL;DR

VLA-REPLICA is a strong evaluation addition because it tackles a real gap in this repository: reproducible real-world VLA benchmarking that does not depend on expensive custom hardware or centralized external evaluators. The paper and official site describe an off-the-shelf setup built around the SO-101 platform, a small demonstration dataset, and standardized in-distribution and out-of-distribution evaluation tasks that can be replicated across labs. Main caveat: task scale is smaller than large simulation suites, but that is partly the point of the benchmark.

## Novelty

- What is actually new: a low-cost, reproducible real-world benchmark for VLA evaluation.
- Difference from prior work: compared with simulation-only or expensive real-world benchmarks, VLA-REPLICA emphasizes affordability, fast setup, and cross-site reproducibility.
- Why the delta matters: this repository tracks not just stronger VLA models but also better ways to measure them fairly in the real world.

## Contributions

1. Introduces a real-world VLA benchmark built from off-the-shelf hardware and standardized setup instructions.
2. Provides task protocols for both in-distribution adaptation and out-of-distribution generalization.
3. Demonstrates reproducibility across independently constructed setups rather than relying on one lab's hidden environment.

## Task

- Input: a VLA policy plus the benchmark's standardized real-world setup and task protocol.
- Output: reproducible real-world success rates for in-distribution and out-of-distribution tasks.
- Setting: low-cost physical robot evaluation for VLA models.
- Success criterion: obtain consistent and informative real-world benchmark results across independently recreated setups.

## Data

- Dataset / benchmark: VLA-REPLICA task suite and a small real-world demonstration dataset for target-domain adaptation.
- Scale: the official project page highlights 10 manipulation tasks; the paper describes both in-distribution and out-of-distribution evaluation and a reproducibility study across replicated setups.
- Modalities: RGB/RGB-D robot observations, language instructions, actions, task outcomes, and real-world demonstration trajectories.
- Collection / annotation: source materials describe teleoperated demonstrations and a standardized physical setup using off-the-shelf components.
- Splits / evaluation protocol: paper and project page define ID and OOD protocols plus cross-setup reproducibility checks.

## Method

- Core pipeline: build the standardized physical setup, adapt or evaluate a VLA policy with the provided demonstrations, and measure task success under ID and OOD conditions.
- Model / representation: benchmark and evaluation protocol rather than a new model architecture.
- Training or optimization: supports target-domain adaptation using the provided demonstration dataset.
- Inference / deployment: evaluates deployed robot policies in a controlled but reproducible physical environment.
- Losses or metrics: benchmark uses source-reported real-world task success and reproducibility comparisons across setups.

## Key Figures / Architecture

figure_status: linked_official

- Figure / demo: official project overview showing hardware, light-box setup, and task examples.
- Source: https://irvlutd.github.io/VLAReplica/
- Render:
  Official figure/demo page: https://irvlutd.github.io/VLAReplica/
- What it shows: the page clearly visualizes the replicated hardware platform and task suite.
- Why it matters: it makes the benchmark's reproducibility goal concrete and inspectable rather than purely textual.

## Evidence Trail

| Claim | Source | Status | Notes |
|---|---|---|---|
| VLA-REPLICA is a low-cost, reproducible real-world benchmark for VLA evaluation | https://arxiv.org/abs/2605.20774 | verified | Direct title/abstract claim. |
| The setup can be built from off-the-shelf components and assembled quickly | https://irvlutd.github.io/VLAReplica/ | verified | Stated on the official project page. |
| The benchmark includes 10 manipulation tasks and ID/OOD evaluation | https://irvlutd.github.io/VLAReplica/ | verified | Official page and arXiv HTML describe the task suite. |
| Results remain consistent across independently constructed setups | https://arxiv.org/html/2605.20774v1 | verified | Reported in the paper's motivation and validation framing. |

## Evidence

- Main metrics: use the paper's reported real-world success and reproducibility findings directly as source-attributed results.
- Qualitative results: the official page shows hardware setup, task examples, and benchmark framing; visual aesthetics are not the acceptance gate because this is an evaluation benchmark.
- Ablations: not reproduced locally; cite the paper for model-by-model comparisons.
- Baselines: source-reported results include imitation-learning baselines and state-of-the-art VLA models.
- Reproducibility signals: primary paper, official project page, public setup guide, and explicit cross-site reproducibility framing.

## Limitations

- Method limitations: task diversity is smaller than the largest simulation benchmarks and hardware is centered on a specific low-cost setup.
- Experimental limitations: this repository did not rebuild the physical platform or rerun evaluations locally.
- Demo / visual limitations: visuals document the setup well, but benchmark value still depends on independent reuse by other labs.
- Claims that remain unverified: long-term leaderboard activity, exact code maintenance, and how broadly the setup will be adopted.

## Project Relevance

- Relevance to interactive embodied generation: very relevant for the real-world evaluation side of VLA and action-model work, especially when generated environments or task protocols need physically reproducible tests.
- Reusable fields: PhysicalSetup, TaskProtocol, IDSplit, OODSplit, DemonstrationSet, and ReproducibilityCheck.
- Possible baseline role: real-world low-cost benchmark reference for VLA evaluation discussions.
- Implications for our task / benchmark: useful template for designing reproducible physical evaluation protocols without expensive centralized infrastructure.

## Reproduction / Follow-up

- What to check before using: setup guide completeness, hardware bill of materials, exact demonstration data license, and whether evaluation scripts remain maintained.
- Code / checkpoint availability: the official project page links to benchmark artifacts, setup material, and public project resources.
- Citation or related-work caveats: emphasize reproducibility and accessibility as the main contribution, not raw task count alone.
