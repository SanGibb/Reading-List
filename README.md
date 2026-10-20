# Interactive Embodied Generation Frontier

面向 **可交互生成、具身智能、空间智能、VLA、可执行物理世界** 的 2024+ 前沿论文精读库。

这个仓库的核心不是堆论文列表，而是维护可复用的结构化精读报告：每篇最终收录论文都要说明原文链接、novelty、contribution、task、data、method、关键图/架构图、证据、局限和对我们任务的启发。

## 精读报告入口

| 内容 | 入口 |
|---|---|
| 层级化精读库 | [paper_reads/README.md](paper_reads/README.md) |
| 最新扩库摘要 | [reports/2026-10-18-expansion.md](reports/2026-10-18-expansion.md) |
| 当前已收录精读 | 168 篇，见 [paper_reads/README.md](paper_reads/README.md) |
| 待人工决定 | `undecided/` local-only，默认不上传 |

每次 run 广泛发现候选，再精选具有实质增量的工作。run 目录只维护审计产物；最终论文精读统一沉淀到 `paper_reads/<branch>/<slug>.md`。新增可以为 0，不为周更凑数；满足全部门槛的候选仍应全部处理，不做固定 top-k 抽样。

## 本周更新内容

本轮扩库日期：2026-10-18。完整审计摘要见 [reports/2026-10-18-expansion.md](reports/2026-10-18-expansion.md)。

### 重点新增与补齐

| Paper | Branch | 简要说明 | 精读 |
|---|---|---|---|
| RoboSimStudio / AutoRSR | A | Editable contact physics and automated executable real-to-sim assets. | [paper_reads/A](paper_reads/A_executable_world_representation/README.md) |
| PhySGA / WEDGE / PAWA | B | Physics-grounded composition, weakness-guided PCG, and shared multiplayer worlds. | [paper_reads/B](paper_reads/B_interactive_generation_pcg/README.md) |
| DeSpatial / DynThinker | C | Unified metric perception and static-dynamic spatial reasoning. | [paper_reads/C](paper_reads/C_spatial_intelligence/README.md) |
| T2-z / GeoState / OneWM | D | Adaptive environment latents, view-decoupled geometry, and unified causal world-action learning. | [paper_reads/D](paper_reads/D_vla_world_action_models/README.md) |
| LIBERO-PeRM / Orbia / ForceBench / TacClaw-Infinity | E | Preference, 3D consistency, force, and tactile-data evaluation infrastructure. | [paper_reads/E](paper_reads/E_evaluation_data_infrastructure/README.md) |

### 全量收录状态

| Branch | Count | Anchor works |
|---|---:|---|
| A. Executable World Representation | 17 | SceneFun3D, PointCast, PhysLDM, FAMOS, FunArt, WonderPlay ... |
| B. Interactive Generation and PCG | 24 | WorldCast, Tetris3D, SimFoundry, AgriGen, Gamma-World, SAGE ... |
| C. Spatial Intelligence | 19 | Ledger, Vesta, SpatialBot, SpaceTools, Point-It-Out, ESI-Bench ... |
| D. VLA and World-Action Models | 61 | DreamTrue, UNITAS, RoboJEPA, Long-WAM, DepthWorld, PLaW-VLA ... |
| E. Evaluation and Data Infrastructure | 47 | LIVIN, MultiWorldBench, OpenViTac, RT-Safe, GaugeBench, BiGym 2.0 ... |

## 研究树

```mermaid
flowchart LR
  R["Interactive Embodied Generation Frontier"]

  R --> A["A. Executable World Representation"]
  A --> A1["sim-ready assets"]
  A --> A2["physical / deformable state"]
  A --> A3["affordance / support / stability"]

  R --> B["B. Interactive Generation and PCG"]
  B --> B1["prompt-to-scene / world"]
  B --> B2["agentic PCG"]
  B --> B3["interactive generation engines"]

  R --> C["C. Spatial Intelligence"]
  C --> C1["3D spatial VLM"]
  C --> C2["multi-view / ego-centric reasoning"]
  C --> C3["tool-augmented spatial reasoning"]

  R --> D["D. VLA and World-Action Models"]
  D --> D1["generalist robot policies"]
  D --> D2["spatial / reasoning VLA"]
  D --> D3["world-action models"]

  R --> E["E. Evaluation and Data Infrastructure"]
  E --> E1["robot / trajectory infrastructure"]
  E --> E2["world generation evaluation"]
  E --> E3["closed-loop embodied world-model benchmarks"]

  classDef root fill:#111827,stroke:#111827,color:#ffffff;
  classDef branch fill:#e0f2fe,stroke:#0369a1,color:#082f49;
  classDef leaf fill:#ffffff,stroke:#cbd5e1,color:#334155;
  class R root;
  class A,B,C,D,E branch;
  class A1,A2,A3,B1,B2,B3,C1,C2,C3,D1,D2,D3,E1,E2,E3 leaf;
```

## 自动化 Workflow

一轮检索会生成：

- `reports/runs/YYYY-MM-DD/`：run plan、discovery、evidence、review、editor report、registry patch、manifest。
- `paper_reads/<branch>/<slug>.md`：最终收录论文的长期精读报告。
- `reports/YYYY-MM-DD-expansion.md`：本轮扩库摘要；主要产物仍是 `paper_reads/` 与 `data/papers.seed.json`。
- `undecided/YYYY-MM-DD/CAND-xxxx.md`：无法判断视觉/demo 质量时的本地待定精读，默认不上传。

常用命令：

```bash
python scripts/scaffold_run.py YYYY-MM-DD
REQUIRE_UNDECIDED_DOSSIERS=1 python scripts/validate_all.py
python scripts/publish_validated_update.py --message "Expand frontier knowledge base YYYY-MM-DD"
```

发布脚本会校验、暂存、提交并 push 非 `undecided/` 变更；待定论文需要人工确认后再单独收录。

## 收录原则

自 2026-10-20 起，新 run 使用 `acceptance_policy_version: 2`。已有 168 篇保留，不因本次规则调整追溯删库。

- 只收录 2024 年及以后的 frontier work。
- 必须有 primary / official source，例如 arXiv、OpenReview、CVF、PMLR、官方项目页或官方 GitHub。
- 必须能回答 `data / method / task / novelty / project_relevance`。
- 最终 `impact_score >= 4`、`project_relevance_score >= 4`、`evidence_strength >= 4` 必须同时满足。影响力按技术实质和受控实验或可复用发布评价，不按引用数、热度或 venue 评价。
- 项目相关性必须指出可直接使用的接口、验证器或 baseline；仅能提取“有用字段”不足以收录。每篇新条目必须解释与库内最接近工作的实质差异；没有新增知识则更新原条目或记录 noop。
- 生成类、交互世界、物理世界、VLA demo 类工作必须实际检查视觉或交互效果并留下页码、图号或视频时间段与观察记录；页面存在视频链接不等于已观看。其他门槛已满足而视觉仍无法判断的候选进入本地 `undecided/` dossier，不能用 watchlist 代替。
- A 分支包含对象级 sim-ready 资产、关节与物理属性，不要求生成完整场景或世界。
- 普通相关论文进入轻量 watchlist，记录缺少的证据和 `revisit_trigger`，无需全部制作精读。通过全部门槛的候选仍完整收录；新增异常增长只触发复审，不按篇数截断。
- 发现阶段覆盖各分支子方向，使用 14 天首发与更新重叠窗口、45 天代码/数据/demo 发布回扫和每月 2024+ 补漏；查询与固定来源访问必须留真实可追溯记录。
- venue 不是硬门槛，效果、证据和项目相关性更重要。

详细规则见 [harness/acceptance_harness.md](harness/acceptance_harness.md) 和 [harness/system_harness.md](harness/system_harness.md)。
