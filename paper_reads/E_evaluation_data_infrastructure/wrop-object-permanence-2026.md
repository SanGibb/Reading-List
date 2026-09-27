# Training Object Permanence in World Models

candidate_id: CAND-0009
branch: E
decision: accepted_for_registry

## Source Links

- Paper: https://arxiv.org/abs/2609.28654
- Project / benchmark / leaderboard: https://object-permanence.world/
- Code: https://github.com/hokindeng/object-permanence
- Model: https://huggingface.co/Hokin/PWM-WROP

## TL;DR

WROP turns object permanence and solidity into 150 procedural cognitive tasks, a 1.5M-video corpus, and a 300-question exam, then releases generators, outputs, weights, and training code. The infrastructure is exceptionally complete, but synthetic-domain transfer and preference-based Elo remain open concerns.

## Novelty

- Encodes core-cognition structure explicitly while randomizing nuisance factors.
- Couples training data, fixed exam, model answers, human Elo, weights, and native PyTorch infrastructure.
- Studies continuation, reference-to-video, and editing models under one cognitive lens.

## Contributions

1. 150 Blender task generators in six cognitive categories.
2. A 1.5M-sample corpus and 300-question exam.
3. PWM-WROP, a 16B continuation model, plus open evaluation artifacts.

## Task

- Input: reference/start video conditions for occlusion, containment, collision, support, and solidity tasks.
- Output: a physically/cognitively consistent generated continuation or transformation.
- Setting: controlled procedural worlds.
- Success criterion: correct object persistence/solidity and human preference.

## Data

- At least 10,000 randomized samples per task, totaling 1.5M.
- Randomization covers speed, lighting, camera, and related nuisance variables.

## Method

- Hand-designed cognitive task definitions drive Blender generators.
- PWM-WROP fine-tunes a 16B video world model on the corpus.
- Fourteen models are evaluated with a fixed exam and blind pairwise Elo.

## Key Figures / Architecture

figure_status: linked_official

- Figure / demo: searchable task browser and model outputs.
- Source: https://object-permanence.world/
- What it shows: diverse hiding, transport, collision, containment, and solidity probes.

## Evidence Trail

| Claim | Source | Status | Notes |
|---|---|---|---|
| 150 tasks / 1.5M samples / 300 questions | https://arxiv.org/abs/2609.28654 | verified | Primary report. |
| Generators, data, answers, weights, stack | https://object-permanence.world/ | verified | Official links inspected. |
| First among continuation models in Elo | https://arxiv.org/abs/2609.28654 | verified | Author-reported blind study. |

## Evidence

- PWM-WROP ranks third overall behind a statistical tie of two reference-to-video systems.
- Official page exposes the full cognitive task taxonomy and qualitative outputs.

## Limitations

- Blender scenes are visually and causally simpler than natural embodied environments.
- Human Elo does not directly measure action utility or calibrated physical correctness.
- Large-model training cost is substantial.

## Project Relevance

WROP provides reusable `ObjectPermanence`, `Solidity`, `Occlusion`, `Containment`, `Support`, and procedural-test-generator fields.

## Reproduction / Follow-up

- Use the fixed exam without leakage from generators.
- Evaluate whether WROP-trained representations improve interactive control, not only video preference.

