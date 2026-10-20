# OpenWAM: An Open, Modular Exploration Towards Systematic World-Action Model Pretraining

<!-- curation-review:start -->
> 2026-10-20 按新版标准复审：**优先阅读**。本轮已读官方模块化trainer/server/evaluation代码入口和具体benchmark配置，检查多任务真实时序样例；提供可控消融、统一数据和部署栈，价值超出单一分数。
> [本次来源、分数与任务判断](../library_review.md#paper-f04c45b32889)。下文保留原精读；旧验收标签不代表本次重新通过，所有实验仍为作者报告。
>
> **本轮准入依据**（技术贡献 / 直接相关性 / 证据：4 / 5 / 4）：相对LingBot-VA2的固定native系统，OpenWAM把encoder/backbone/architecture/mask/data/inference变为组合组件；其实际LIBERO-Plus不领先所有基线，不能宣称全任务替代。
> - [Title; Abstract (method and evaluation paragraphs); submission history / Comments when present](https://arxiv.org/abs/2609.07398)：Abstract defines modular OpenWAM-Infra, controlled OpenWAM-Study and pretrained OpenWAM-alpha; alpha uses roughly 6,400 hours of egocentric and robot data and is evaluated on eight simulation benchmarks plus real robots. The authors state release of infrastructure, protocols, models and data recipes.（verified）。
> - [One stack, three layers; What the controlled study found; Figure12 Architecture; Figure13 per-benchmark bars; Real-robot rollouts](https://openwam-official.github.io/)：Modular stack spans encoders/backbones/architectures/masks, controlled studies and released alpha model. Source reports heterogeneous benchmark results rather than a universal best result; single-arm, bimanual and dexterous galleries are distinct.（verified）。
> - [README: What is OpenWAM; Installation; Assets Preparation / Video Backbone / Benchmark Data / Released Checkpoints](https://github.com/OpenWAM-Official/OpenWAM)：Official repository documents modular infrastructure, model/benchmark downloaders, supported LIBERO/RoboTwin/RoboCasa/VLABench/EBench/RoboDojo data and checkpoint paths. This is a concrete reusable experimental/deployment interface; code was not executed.（verified）。
>
> 引用指标、发布规模和比较结果时，以以上已定位来源和本次复审限制为准，不沿用下文旧概括。
<!-- curation-review:end -->

candidate_id: CAND-0001
branch: D
decision: accepted_for_registry

## Source Links

- Paper: https://arxiv.org/abs/2609.07398
- Project: https://openwam-official.github.io/
- Code: https://github.com/OpenWAM-Official/OpenWAM
- Models / data: https://huggingface.co/OpenWAM-Official
- Demo / video: https://openwam-official.github.io/#robot-demos

## TL;DR

OpenWAM turns world-action modeling from a collection of tightly coupled systems into a modular research stack, derives design principles through controlled studies, and instantiates them in an open pretrained model. Its unusually complete code/model/data/evaluation release makes it a strong systems reference, though the headline comparisons remain source-reported and expensive to reproduce.

## Novelty

- Factorizes visual encoders, video backbones, architectures, attention masks, representations, and denoising recipes behind common infrastructure.
- Tests six linked design questions under controlled conditions rather than changing many variables at once.
- Builds OpenWAM-alpha from the resulting principles and releases the supporting stack.

## Contributions

1. OpenWAM-Infra for unified training, inference, deployment, and evaluation.
2. OpenWAM-Study on knowledge inheritance, world/action interaction, data recipes, and joint denoising.
3. OpenWAM-alpha, pretrained at scale and evaluated in simulation and on physical robots.

## Task

- Input: egocentric/robot video, language, robot state, and actions.
- Output: future visual dynamics and executable action chunks.
- Setting: eight simulation benchmarks and three real-robot platforms.
- Success criterion: strong control and generalization under one reproducible WAM stack.

## Data

- Scale: 518.5M frames, approximately 6,400 hours.
- Modalities: egocentric human video, robot video, language, proprioception, actions.
- Representation: an 80-D unified action space spans heterogeneous embodiments.
- Evaluation: single-arm, bimanual, and dexterous-hand tasks.

## Method

- Core pipeline: modular data/encoder/backbone/architecture/action-decoder stack.
- Study: controlled comparisons establish the backbone, representation, information-flow, data, and denoising recipe.
- Model: dedicated action capacity, explicit world-to-action flow, and synchronized joint denoising.
- Deployment: common policy server and evaluation protocol for simulation and real robots.

## Key Figures / Architecture

figure_status: linked_official

- Figure: OpenWAM-Infra -> OpenWAM-Study -> OpenWAM-alpha overview.
- Source: https://openwam-official.github.io/
- What it shows: the separation between reusable infrastructure, controlled evidence, and the final pretrained model.
- Why it matters: this is the cleanest reusable decomposition for comparing WAM design choices.

## Evidence Trail

| Claim | Source | Status | Notes |
|---|---|---|---|
| 518.5M frames / about 6,400 hours | https://openwam-official.github.io/ | verified | Official overview. |
| Eight simulation benchmarks and three physical platforms | https://openwam-official.github.io/ | verified | Official benchmark/demo sections. |
| Code, models, data recipes, and protocols released | https://github.com/OpenWAM-Official/OpenWAM | verified | Repository and linked model organization. |

## Evidence

- Official page lists four visual encoders, five video backbones, six architecture variants, and four attention masks.
- Source reports consistent top-tier results across eight simulation benchmarks and real-robot tests.
- Robot gallery spans single-arm, bimanual, and dexterous-hand settings.
- Public source, pretrained/fine-tuned models, and configuration recipes are available.

## Limitations

- Very new arXiv release without independent reproduction.
- Full pretraining and multi-benchmark reproduction require substantial compute/data provisioning.
- Cross-benchmark headline language should be cited as reported by the authors.

## Project Relevance

- Direct implementation reference for world/action coupling.
- Provides schemas for unified action spaces, modular backbones, simulator adapters, and controlled ablations.
- Strong baseline for testing whether visual prediction supervision improves out-of-domain robot control.

## Reproduction / Follow-up

- Start with released fine-tuned checkpoints and one benchmark adapter before attempting pretraining.
- Preserve the official config/provenance envelope when comparing variants.
- Verify exact benchmark protocols and licenses before aggregating results.
