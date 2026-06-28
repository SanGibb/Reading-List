# SpatialAct: Probing Spatial Reasoning-to-Action Capabilities of Vision-Language Models in 3D Scenes

candidate_id: CAND-0055
branch: C
decision: accepted_for_registry
authors: Liu et al.
year: 2026
venue: arXiv / project page

## Source Links

- Paper: https://arxiv.org/abs/2605.31148
- Project: https://tianhui-liu.github.io/projects/SpatialAct/
- Code: https://tianhui-liu.github.io/projects/SpatialAct/
- Data / benchmark: https://tianhui-liu.github.io/projects/SpatialAct/
- Demo / video: https://tianhui-liu.github.io/projects/SpatialAct/
- Official figures: https://tianhui-liu.github.io/projects/SpatialAct/

## TL;DR

SpatialAct is a strong spatial-intelligence addition because it turns 3D VLM evaluation into a reasoning-to-action benchmark rather than stopping at static description or question answering. The official project page reports 333 synthetic 3D scenes, 4,355 QA pairs, three task families, and a tool-based repair stage that improves performance by grounding answers back into geometry and action checks. Main caveat: it is still a benchmark and repair pipeline, not a deployed embodied policy system.

## Novelty

- What is actually new: a benchmark that explicitly tests whether spatial reasoning can be converted into action-relevant decisions in 3D scenes.
- Difference from prior work: compared with pure spatial QA benchmarks, SpatialAct emphasizes reasoning-to-action and includes a repair-stage analysis.
- Why the delta matters: our repository needs spatial reasoning signals that are close to executable embodied behavior, not only textual correctness.

## Contributions

1. Builds a 3D-scene benchmark for spatial reasoning-to-action evaluation.
2. Covers three task types with 333 synthetic scenes and 4,355 question-answer pairs.
3. Adds a tool-based repair agent that measures how much geometry-aware checking can recover VLM failures.

## Task

- Input: 3D scene observations and spatially grounded questions that imply an action or decision.
- Output: action-relevant spatial answers and associated benchmark scores.
- Setting: diagnostic evaluation of VLM spatial reasoning in synthetic 3D scenes.
- Success criterion: answer spatial questions correctly and robustly enough that the result is useful for downstream action or planning.

## Data

- Dataset / benchmark: 333 synthetic 3D scenes and 4,355 QA pairs across three task categories, as reported on the official project page.
- Scale: 333 scenes and 4,355 QA pairs.
- Modalities: 3D scenes, language questions, spatial relations, and action-relevant answers.
- Collection / annotation: source materials describe a synthetic 3D benchmark construction pipeline with tool-grounded evaluation.
- Splits / evaluation protocol: use the paper's source-reported benchmark protocol and repair-stage analysis when citing exact metrics.

## Method

- Core pipeline: pose spatial reasoning-to-action questions over 3D scenes, evaluate VLM outputs, then optionally run a tool-based repair stage for grounded correction.
- Model / representation: benchmark plus repair framework for 3D spatial reasoning.
- Training or optimization: benchmark-centric evaluation; the main method contribution is the diagnostic/repair design rather than a new base VLM.
- Inference / deployment: useful as an analysis harness for VLMs that must connect scene reasoning to action choices.
- Losses or metrics: the official page reports baseline accuracy and repair-stage improvements for multiple VLM families.

## Key Figures / Architecture

figure_status: linked_official

- Figure / demo: official benchmark overview and qualitative 3D-scene task examples.
- Source: https://tianhui-liu.github.io/projects/SpatialAct/
- Render:
  Official figure/demo page: https://tianhui-liu.github.io/projects/SpatialAct/
- What it shows: the page visualizes scene setup, task categories, and the gap between raw VLM reasoning and repaired grounded performance.
- Why it matters: it makes the benchmark's geometry-to-action framing immediately legible for this repository.

## Evidence Trail

| Claim | Source | Status | Notes |
|---|---|---|---|
| SpatialAct targets spatial reasoning-to-action in 3D scenes | https://arxiv.org/abs/2605.31148 | verified | Direct abstract/title claim. |
| The benchmark contains 333 synthetic scenes and 4,355 QA pairs | https://tianhui-liu.github.io/projects/SpatialAct/ | verified | Reported on the official project page. |
| The benchmark spans three task families and includes a repair agent | https://tianhui-liu.github.io/projects/SpatialAct/ | verified | Described in the official overview. |
| Multiple VLMs remain below strong performance even after repair | https://tianhui-liu.github.io/projects/SpatialAct/ | partial | Treat specific leaderboard numbers as source-reported and date-sensitive. |

## Evidence

- Main metrics: the official page reports low baseline performance and meaningful gains from the repair stage, highlighting that current VLMs still struggle with embodied spatial grounding.
- Qualitative results: the project page shows 3D scene examples and action-relevant failure cases.
- Ablations: use the paper for repair-agent ablations and per-task breakdowns.
- Baselines: cite source-reported model comparisons only as reported by the project page or paper.
- Reproducibility signals: primary paper plus a dedicated official project page with benchmark details.

## Limitations

- Method limitations: benchmark conclusions still depend on synthetic scene coverage and question design.
- Experimental limitations: this repository did not rerun benchmark evaluations locally.
- Demo / visual limitations: visual quality is not the acceptance gate here because the paper is a benchmark, but the official examples are still useful for interpreting failure modes.
- Claims that remain unverified: exact repository maturity, annotation tooling, and long-term benchmark maintenance.

## Project Relevance

- Relevance to interactive embodied generation: directly useful as a validator for whether generated or reconstructed scenes preserve the spatial structure needed for action.
- Reusable fields: SpatialRelation, ActionableQuestion, 3DSceneContext, RepairTool, and GroundedAnswer.
- Possible baseline role: diagnostic benchmark for spatial reasoning-to-action competence.
- Implications for our task / benchmark: strong fit for evaluating whether our future world representations support grounded spatial decisions instead of only surface-level semantics.

## Reproduction / Follow-up

- What to check before using: benchmark download path, exact task taxonomy, and whether the repair tools can be reused as standalone validators.
- Code / checkpoint availability: the official project page hosts benchmark and project artifacts.
- Citation or related-work caveats: describe results as benchmark evidence for current VLM limitations rather than as a complete embodied-policy evaluation.
