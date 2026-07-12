# Frontier Knowledge Expansion Summary - 2026-07-13

This run adds **9 accepted papers** and requires **no undecided dossiers**. The selection boundary was the acceptance harness, not a fixed quota.

## Summary

- New accepted papers: `RoboWM-Bench`, `VLA-Arena`, `Colosseum V2`, `MiraBench`, `iWorld-Bench`, `WBench`, `WorldMark`, `WorldOlympiad`, `WorldBench`
- Followed sources checked: all core source groups were checked or spot-checked; strongest accepted signals came from the embodied/world-model benchmark cluster and the VLA benchmark cluster
- Deep dives in `paper_reads/`: 9 new maintained reports
- Watchlist items: `MIND`, `PhyGround`
- Strong demos: `VLA-Arena`, `iWorld-Bench`, `WorldMark`
- Undecided visual cases: none
- Collection notes: this run materially deepened evaluation coverage for interactive world models, long-horizon world-model diagnostics, and VLA generalization infrastructure

## A. Executable World Representation

No new accepted additions this run.

## B. Interactive Generation and PCG

No new accepted additions this run.

## C. Spatial Intelligence

No new accepted additions this run.

## D. VLA and World-Action Models

No new accepted additions this run.

## E. Evaluation and Data Infrastructure

| Paper | Source | Deep dive | Data | Method | Task | Novelty | Demo | Visual | project relevance |
|---|---|---|---|---|---|---|---:|---|---|
| RoboWM-Bench: A Benchmark for Evaluating World Models in Robotic Manipulation | CVPRW + arXiv + official GitHub | [robowm-bench-2026.md](../paper_reads/E_evaluation_data_infrastructure/robowm-bench-2026.md) | manipulation-centric benchmark that turns generated human-hand and robotic manipulation videos into embodied action sequences and validates them through execution in standardized manipulation scenarios | convert generated behaviors into executable action sequences, replay them in a robotics execution loop, and score physically executable task completion with failure-mode analysis | evaluate whether video world-model predictions can be translated into executable manipulation actions that still complete the intended task | moves world-model evaluation from visual plausibility to embodiment-grounded action executability for robotic manipulation | 4 | not_applicable | Direct benchmark reference for whether generated embodied futures are actionable enough for manipulation-policy learning and validation. |
| VLA-Arena: An Open-Source Framework for Benchmarking Vision-Language-Action Models | arXiv + project + official GitHub | [vla-arena-2026.md](../paper_reads/E_evaluation_data_infrastructure/vla-arena-2026.md) | 170 tasks across 11 specialized suites with three difficulty levels, plus VLA-Arena-S/M/L datasets and orthogonal language and visual perturbation settings | structured benchmark design over task structure, language command, and visual observation axes with unified tooling for task modeling, training, and automated evaluation | systematically benchmark VLA robustness, safety, extrapolation, distractor handling, and long-horizon composition under controlled perturbations | separates VLA capability-frontier measurement into orthogonal structure/language/visual axes instead of collapsing everything into one aggregate success rate | 5 | not_applicable | Strong infrastructure reference for evaluation schemas, perturbation taxonomies, and task-difficulty ladders for embodied policy assessment. |
| Colosseum V2: Benchmarking Generalization for Vision Language Action Models | arXiv HTML/abs | [colosseum-v2-2026.md](../paper_reads/E_evaluation_data_infrastructure/colosseum-v2-2026.md) | large-scale ManiSkill benchmark with 28 tasks spanning 13 categories, two robot morphologies, and controlled in-domain/out-of-domain perturbation settings | GPU-parallelized simulation benchmark that probes VLA generalization along visual, language, and action axes and checks ecological validity against real-world metrics | measure how VLA manipulation performance degrades under distribution shift and whether simulation rankings track real-world robustness | pushes VLA evaluation beyond nominal zero-shot perception into controlled perturbation-based generalization measurement with simulation-to-real correlation checks | 3 | not_applicable | Useful benchmark template for large-scale, perturbation-aware embodied policy evaluation and simulation-to-real validation. |
| MiraBench: Evaluating Action-Conditioned Reliability in Robotic World Models | arXiv | [mirabench-2026.md](../paper_reads/E_evaluation_data_infrastructure/mirabench-2026.md) | human-annotated corpus with 16k+ judgments covering tasks, failure categories, and 12 representative robotic-world-model configurations | hierarchical diagnostic benchmark over physics adherence, action-following fidelity, and optimism-bias detection for action-conditioned robotic world models | test whether action-conditioned robotic world models are physically consistent, obey task-relevant actions, and avoid optimistic false-success predictions | defines action-conditioned reliability as a first-class target rather than assuming image fidelity stands in for robotic faithfulness | 2 | not_applicable | Directly relevant to evaluating whether generated futures are faithful control simulators rather than merely plausible videos. |
| iWorld-Bench: A Benchmark for Interactive World Models with a Unified Action Generation Framework | ICML project page + arXiv + official GitHub | [iworld-bench-2026.md](../paper_reads/E_evaluation_data_infrastructure/iworld-bench-2026.md) | 330k video clips, 2.1k selected high-quality samples, and 4.9k test tasks spanning varied perspectives, weather, and scenes | unified action-generation framework that standardizes interaction control across modalities and scores world models on visual generation, trajectory following, and memory with nine metrics | train and test interactive world models on distance perception, action control, camera control, trajectory following, and memory across diverse scenes | turns interactive world-model evaluation into a multi-input, action-space-unified benchmark instead of model-specific camera-control demos | 5 | not_applicable | High-value benchmark for first-person interactive world-model evaluation, camera control, memory, and multi-scene action responsiveness. |
| WBench: A Comprehensive Multi-turn Benchmark for Interactive Video World Model Evaluation | arXiv + official homepage + official GitHub | [wbench-2026.md](../paper_reads/E_evaluation_data_infrastructure/wbench-2026.md) | 289 multi-turn test cases and 1,058 interaction turns covering navigation, subject action, event editing, and perspective switching | comprehensive multi-turn benchmark with 22 automatic sub-metrics across video quality, setting adherence, interaction adherence, consistency, and physics compliance | evaluate whether interactive video world models sustain coherent multi-turn behavior under heterogeneous control interfaces | brings multi-turn interaction and heterogeneous control-interface unification into one benchmark rather than one-step or single-axis evaluation | 5 | not_applicable | Strong benchmark reference for multi-turn interaction fidelity and physics-compliance evaluation in interactive world generation. |
| WorldMark: A Unified Benchmark Suite for Interactive Video World Models | arXiv + official project + World Model Arena | [worldmark-2026.md](../paper_reads/E_evaluation_data_infrastructure/worldmark-2026.md) | 500 standardized evaluation cases built from 100 test images and 15 shared action sequences across first-person, third-person, real, and stylized scenes | shared WASD-style action vocabulary, cross-model action mapping, and modular metrics for visual quality, control alignment, and world consistency, paired with the World Model Arena website | compare interactive image-to-video world models under identical scenes and identical action sequences | creates the first common playing field for interactive image-to-video world models with standardized scenes, controls, and reusable evaluation toolkit | 5 | not_applicable | Important benchmark and online-comparison reference for standardized interactive world-generation evaluation. |
| WorldOlympiad: Can Your World Model Survive a Triathlon? | arXiv + official project + official GitHub | [worldolympiad-2026.md](../paper_reads/E_evaluation_data_infrastructure/worldolympiad-2026.md) | 1,000 long videos spanning 400 robotics, 400 gaming, and 200 general real-world videos | triathlon-style benchmark with physical, geometry, and interaction tracks using segmentation-based judges, Gaussian-splatting diagnostics, and action-following checks | diagnose long-video world models on physical faithfulness, geometric consistency, and interaction fidelity across multiple downstream domains | unifies physical, geometric, and interaction diagnostics across robotics, gaming, and open-domain world-model scenarios rather than isolating one dimension | 5 | not_applicable | Strong cross-domain benchmark for long-horizon world-model evaluation with direct relevance to robotics and interactive control. |
| WorldBench: Disambiguating Physics for Diagnostic Evaluation of World Models | arXiv + official project | [worldbench-2026.md](../paper_reads/E_evaluation_data_infrastructure/worldbench-2026.md) | video benchmark with 425 configurations over motion physics, object permanence, support relations, and scale/perspective, plus a language subset for VLM evaluation | disentangled physics benchmark that scores future predictions against simulated ground-truth physical outcomes using segmentation-based comparison and concept-specific scenarios | diagnose whether world models and VLMs understand specific physical concepts rather than merely producing visually plausible futures | disentangles physical concepts into more diagnostic tests instead of entangled holistic video-quality proxies | 4 | not_applicable | Useful physics-diagnostic benchmark for checking whether world models preserve support, permanence, and motion rules relevant to executable embodied worlds. |

## Watchlist

- `MIND: Benchmarking Memory Consistency and Action Control in World Models`
  Source: https://arxiv.org/abs/2602.08025
  Reason: strong benchmark, but lower direct embodied/interactive-world fit than the accepted cluster.
- `PhyGround: Benchmarking Physical Reasoning in Generative World Models`
  Source: https://arxiv.org/abs/2605.10806
  Reason: strong physics benchmark, but more generic video-generation evaluation than this repo's embodied benchmark priorities.

## Followed Sources Checked

| Source | Status | New signal | Notes |
|---|---|---|---|
| World-model benchmark cluster | checked | WorldBench, WorldMark, WorldOlympiad, WBench, RoboWM-Bench, MiraBench | main accepted-signal cluster this run |
| Tsinghua AIR / VLA line | checked | iWorld-Bench, VLA-Arena | strongest accepted benchmark/toolchain signals outside the world-model cluster |
| VLA leaderboard / benchmark cluster | checked | VLA-Arena, Colosseum V2 | produced the strongest VLA-evaluation additions |
| NVIDIA Cosmos / Isaac / GR00T research | checked | none accepted | rechecked after prior-run Cosmos additions; no stronger new benchmark release |
| Remaining core source groups | spot_checked | none accepted | no additional A/B/C/D/E candidates cleared dedupe and acceptance gates |

## Undecided

No candidate required a local-only undecided dossier in this run.

## Top Demos

1. VLA-Arena for the clearest end-to-end open-source VLA benchmark and task-suite release.
2. iWorld-Bench for the strongest complete project+code+dataset+leaderboard interactive-world benchmark package.
3. WorldMark for the best combination of standardized benchmark design and live public World Model Arena comparison surface.

## Collection Notes

- Related-work usefulness: WorldBench, MiraBench, and RoboWM-Bench sharply improve the repo's ability to distinguish visual plausibility from physically or action-faithful usefulness.
- Baseline usefulness: VLA-Arena and Colosseum V2 provide complementary VLA evaluation coverage, while WBench, WorldMark, iWorld-Bench, and WorldOlympiad cover interactive world-model evaluation at different granularities.
- Evidence gaps to check before citing: official long-term maintenance of Colosseum V2 code, future frozen protocol versions for World Model Arena, and future release maturity for MiraBench beyond the arXiv paper.

## Validation

- System run validation: passed via `python3 scripts/validate_run.py 2026-07-13`
- Registry validation: passed via `python3 scripts/validate_registry.py`
- Full repository validation: passed via `REQUIRE_UNDECIDED_DOSSIERS=1 python3 scripts/validate_all.py`
- Source quality: all accepted papers use primary or official sources
- Duplicate check: passed manual registry/title check during this run
- Harness exceptions: none
