# Weekly Frontier Knowledge Expansion — 2026-09-07

The September 1–7 primary-source scan found no brand-new release clearing every gate, but the fixed-source sweep exposed five influential 2026 omissions. All five passed the acceptance harness and were added; none remains undecided.

## Accepted by branch

### D. VLA and World-Action Models

- [SPD](../paper_reads/D_vla_world_action_models/spd-2026.md) — scalable simulation pre-training for real bimanual dexterity.
- [FACT](../paper_reads/D_vla_world_action_models/fact-contact-rich-vla-2026.md) — precision/force failure diagnosis and targeted contact-rich VLA repair.
- [CHORUS](../paper_reads/D_vla_world_action_models/chorus-2026.md) — decentralized heterogeneous collaboration from one shared VLA.
- [VLAW](../paper_reads/D_vla_world_action_models/vlaw-2026.md) — iterative co-improvement of policy and learned video simulator.

### E. Evaluation and Data Infrastructure

- [RoboMME](../paper_reads/E_evaluation_data_infrastructure/robomme-2026.md) — ICML Oral benchmark for temporal, spatial, object, and procedural robot memory.

No candidate passed Branch A, B, or C gates this week.

## Follow-source coverage

- Checked all 15 core groups; the configured Berkeley RAIL URL redirected to an unrelated IT site, so primary author/lab pages compensated for it.
- Spot-checked all four watch groups.
- Broad searches covered recent arXiv, official project, code, dataset, and benchmark surfaces across all five branches.

## Visual and demo review

SPD, FACT, and CHORUS have strong official real-robot videos. VLAW's paper/OpenReview generated-versus-real comparisons were adequate despite a sparse standalone project surface. RoboMME is benchmark infrastructure; its task videos, interactive demo, code, data, and models corroborate execution quality.

## Watchlist and undecided

- *World Model for Robot Learning: A Comprehensive Survey* remains a useful maintained discovery map but does not itself add a novel benchmark artifact.
- No social-media-only claim was accepted.
- No new undecided dossier was required. Historical local-only dossiers remain excluded from publication.

## Most relevant additions

1. VLAW — direct policy/simulator feedback loop.
2. FACT — actionable physical-contact failure taxonomy.
3. RoboMME — reusable persistent-memory task schema.

## Validation

`REQUIRE_UNDECIDED_DOSSIERS=1 python3 scripts/validate_all.py` passed for the 106-paper registry and every run. Only pre-existing missing-local-PDF warnings remain. Publication was attempted, but Git could not create the linked-worktree `index.lock` under the current environment permissions, so no commit or push occurred.
