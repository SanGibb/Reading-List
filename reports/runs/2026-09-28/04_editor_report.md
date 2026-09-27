# Editor Report — 2026-09-28

## Accepted candidates

- A: PointCast — unified executable point dynamics for rigid, articulated, and deformable manipulation.
- B: AgriGen — domain-specific procedural agricultural simulation.
- D: AD-WM, Self-Adaptive VLA, Rolling-WAM, Streaming-WAM, and InternW0.
- E: EmbodiedMemory-Bench, Training Object Permanence in World Models, and RoboTwin-Phys.
- C: no candidate cleared every gate this week.

Every reviewer-passed candidate appears in the registry patch and has a maintained deep dive.

## Undecided / rejected

- CAND-0011 Fysiverse-3D-Vision: local-only dossier; needs official moving/interactive evidence of executable edits and collision behavior.
- CAND-0012 World Action Agent: local-only dossier; needs official continuous robot execution/rehearsal evidence.
- CAND-0013 Ego-Exo4D Human Meshes: rejected because repository project relevance was below threshold.

## Top demos

1. InternW0 — 15-stage MOF synthesis and force-aware dexterous pipetting.
2. Streaming-WAM — continuous asynchronous execution with released implementation/models.
3. WROP — unusually complete browser of cognitive tasks, outputs, data, code, weights, and leaderboard.

## Collection notes

- InternW0 is the strongest new general baseline for asynchronous multi-modal world-action modeling.
- PointCast is a reusable executable-state reference for cross-topology object dynamics.
- EMem-Bench and RoboTwin-Phys add orthogonal memory and physical-condition axes missing from many current evaluations.
- AgriGen is accepted at the threshold because official visuals and workshop evidence are adequate, but reproducibility remains pending.
- No social-media-only claim was accepted.

## Validation

The manifest is finalized only after `REQUIRE_UNDECIDED_DOSSIERS=1 python3 scripts/validate_all.py` passes.

