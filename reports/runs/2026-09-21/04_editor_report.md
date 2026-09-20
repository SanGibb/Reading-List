# Editor Report — 2026-09-21

## Accepted

- A: FAMOS — sparse multi-state articulation with official moving comparisons.
- A: FunArt — functional elements and executable articulation decoded from 3D latents.
- B: Astronex-World 1.0 — open real-time controllable video world model.
- D: Agile-WAM — efficient tactile WAM with strong contact-rich robot demos.
- E: PersistBench — panoramic-ground-truth benchmark for off-screen world memory.
- E: Universal Navigation Interface — robot-free wheeled navigation data and transfer.
- E: BinoGen — 20M+ embodiment-aware binocular frames with dense labels.
- E: SlugTrails — large-building egocentric floor-plan localization benchmark.

## Undecided

- Workspace Models is documented locally at `undecided/2026-09-21/CAND-0009.md`; no continuous official hardware demo was found.

## Watchlist / Rejected

- HIL-UMI and DexTouch-WM remain watchlist-only pending stronger official demo/release surfaces.
- GeoAAC, MoWAM, and StageGuard were below the run's impact threshold.
- The robot-world-model survey remains discovery context only.

## Follow-source Coverage

- All 15 core source groups and the core VLA leaderboard were checked; Berkeley RAIL remains unreachable/redirected.
- All four watch groups and the VLA survey were spot-checked.

## Top Demos

1. Astronex-World: diverse real-time camera/action/event-controlled worlds with code and weights.
2. Agile-WAM: contact-rich assembly/insertion plus corrective-recovery executions.
3. FAMOS: moving multi-state comparisons that visibly disambiguate articulated joints.

## Collection Notes

- PersistBench is the strongest evaluation addition and complements R2M-Bench.
- FAMOS and FunArt expose complementary observation-to-executable-articulation fields.
- Astronex is a reproducible streaming baseline; do not equate video coherence with physical executability.
- BinoGen's release availability should be rechecked before reproduction.

## Validation

- Passed `REQUIRE_UNDECIDED_DOSSIERS=1 python3 scripts/validate_all.py`: 118 papers and all completed runs validated; only pre-existing missing-local-PDF warnings remain.
