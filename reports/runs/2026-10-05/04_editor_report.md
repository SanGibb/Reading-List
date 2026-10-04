# Editor Report — 2026-10-05

## Accepted candidates

- B: SimFoundry.
- C: Vesta.
- D: DreamDojo, MolmoB0T, Qwen-VLA, Flow Reversal Steering, and World Action Verifier.
- E: MolmoSpaces and Open-H-Embodiment.
- A: no candidate cleared every gate this week.

Every reviewer-passed candidate appears in the registry patch and has a maintained deep dive. These are newly influential fixed-source omissions; no brand-new October 1–5 release cleared all gates.

## Undecided / rejected

- No candidate required a local-only undecided dossier.
- Q-Learning With World Models was rejected at impact/demo triage.
- Robot World Models Are Not Invariant to How the Actions Are Written was rejected as a narrow diagnostic below the impact threshold.

## Top demos

1. DreamDojo — diverse cross-embodiment action-conditioned futures plus minute-long real-time rollouts.
2. SimFoundry — video-to-simulator construction, editable digital cousins, and real robot transfer.
3. MolmoB0T — continuous zero-shot sim-to-real manipulation across Franka and mobile manipulation.

## Collection notes

- DreamDojo is the strongest general robot-world-model baseline in this run.
- SimFoundry and MolmoSpaces provide complementary compiler and infrastructure references.
- Vesta adds an explicit memory/progress interface for long-horizon embodied reasoning.
- No social-media-only claim was accepted.

## Validation

The manifest is finalized after `REQUIRE_UNDECIDED_DOSSIERS=1 python3 scripts/validate_all.py` passes.
