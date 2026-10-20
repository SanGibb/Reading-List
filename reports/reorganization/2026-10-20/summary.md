# 2026-10-20 Existing Library Reorganization

This is an explicit, user-requested retrospective reassessment, not a weekly expansion or an independent reproduction.

All 168 records and deep dives are preserved; 48 concrete task groups cover the complete inventory.

| Review outcome | Count |
|---|---:|
| 优先阅读 | 27 |
| 参考备选 | 31 |
| 观察名单 | 34 |
| 待视觉复核 | 73 |
| 来源待修复 | 3 |

Only priority entries are shown as current recommendations. Reference status does not mean renewed v2 admission. Uncertainty is not proof that a paper is bad.

## Source issues

- **SimWorld Studio: Generation and Evolution of Custom Embodied Agent Learning Environments** — Registry arXiv2606.08498 is an unrelated statistics paper. The real official project points to2605.09423 with a different title and UE5/SimCoder method; old320-task/240-layout claims and the currently404 code link cannot serve as evidence.
- **Cosmos-Predict2.5: A World Foundation Model for Physical AI** — registry纸页URL指向完全无关的随机非线性薛定谔方程数学论文；旧报告的“主源verified”不成立。官方Cosmos项目确实存在，但不能在错误身份上重评质量。
- **A Unified Evaluation Harness for Vision-Language-Action Models** — 原registry arXiv号实际是雷达flow-matching论文，精读的作者和13/657数字也不可沿用。官方仓库和正确论文已找到，身份修复前不进入推荐。

## Evidence and scope

Each paper has a branch-audit record with fresh source checks, task scope, final scores or explicit unknowns, and a decision/revisit trigger. Original admission runs remain unchanged. Source verification is not independent reproduction; linked videos are not watched videos.

Current registry fields describe this reassessment; historical_acceptance preserves the original source/visual/evidence labels. Undecided dossiers are local-only and remain outside publication.

No supersession is inferred from age, version numbers or unmatched benchmark scores. Any historical task link must satisfy the separate comparable-protocol/no-regression evidence gates.

## Entry points

- [Curated reading and full review](../../../paper_reads/library_review.md)
- [Task frontiers](../../../paper_reads/task_frontiers.md)

## Validation

129 regression tests passed. `REQUIRE_UNDECIDED_DOSSIERS=1 python3 scripts/validate_all.py`
passed for all 168 records, 48 task groups, every historical run, the review sidecar,
and all eight generated views. Only the pre-existing missing-local-PDF warnings remain.

An independent preservation check compared every deep-dive body, canonical paper URL,
path, and historical-acceptance snapshot against baseline `9e6e38f`; all 168 were
preserved. Repeating the reorganization changed no deep-dive bytes.

All 73 new visual-review dossiers exist locally and have a local-only backup outside
the Git worktree. No dossier is part of the publication. Missing media verification,
source repair, and incomparable-protocol limitations remain explicit rather than being
reported as solved or independently reproduced.
