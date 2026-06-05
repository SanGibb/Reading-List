# OpenEQA: Embodied Question Answering in the Era of Foundation Models

candidate_id: CAND-0002
branch: E. Evaluation and Data Infrastructure
decision: accepted_for_registry

## Source Links

- Paper: https://openaccess.thecvf.com/content/CVPR2024/html/Majumdar_OpenEQA_Embodied_Question_Answering_in_the_Era_of_Foundation_Models_CVPR_2024_paper.html
- Project: https://open-eqa.github.io/
- PDF: https://open-eqa.github.io/assets/pdfs/paper.pdf
- Code / benchmark: https://github.com/facebookresearch/open-eqa
- Blog: https://ai.meta.com/blog/openeqa-embodied-question-answering-robotics-ar-glasses/
- Official figures:
  - Dataset statistics: https://open-eqa.github.io/assets/images/figure-3.png
  - Evaluation workflow: https://open-eqa.github.io/assets/images/workflow.png
  - Model performance: https://open-eqa.github.io/assets/images/multi-modal-llms.svg

## TL;DR

OpenEQA reformulates embodied question answering as open-vocabulary environment understanding and provides a benchmark plus LLM-based answer matching protocol. It is not a generation method, but it is valuable for this repository because generated embodied worlds need downstream tests that ask whether an agent can understand object locations, attributes, world knowledge, and episode history. The main caveat is that it evaluates understanding and QA, not whether a generated world is physically executable.

## Novelty

- What is actually new: OpenEQA makes EQA open-vocabulary and supports both episodic-memory and active-exploration settings.
- Difference from prior work: instead of closed answer sets or templated QA, the benchmark uses human-generated questions and natural-language answers over real-world environments.
- Why the delta matters: interactive generated worlds should be evaluated by realistic environment questions, not only static visual fidelity or object-count metrics.

## Contributions

1. Defines a modern EQA benchmark around open-vocabulary natural-language answers.
2. Provides a dataset with more than 1600 human-generated questions from over 180 real-world environments, according to the official project and CVF page.
3. Provides an automatic LLM-Match evaluation workflow intended to correlate with human judgment for free-form answers.
4. Benchmarks current foundation models and shows a gap between multimodal models and human performance.

## Task

- Input: an embodied episode history, visual observations, or active exploration setting, plus a natural-language question about the environment.
- Output: a natural-language answer.
- Setting: embodied question answering under episodic-memory EQA and active EQA variants.
- Success criterion: answer correctness judged against reference answers using human or LLM-based matching.

## Data

- Dataset / benchmark: OpenEQA.
- Scale: the official project/CVF pages report 1600+ questions over 180+ real-world environments.
- Modalities: environment observations, episode histories, natural-language questions, and natural-language answers.
- Collection / annotation: human-generated questions and answers, organized into EQA categories.
- Splits / evaluation protocol: benchmark protocol includes model answer generation and LLM-Match style answer evaluation; exact split details should be checked in the PDF before reproduction.

## Method

- Core pipeline: gather embodied context, ask an open-vocabulary question, produce a natural-language answer, then evaluate the answer using an LLM-based matching protocol or human judgment.
- Model / representation: OpenEQA is primarily a benchmark and evaluation framework, not a new model architecture.
- Training or optimization: no central training method is proposed; evaluated systems are existing foundation models or embodied QA agents.
- Inference / deployment: models use visual or text context to answer questions about the environment.
- Losses or metrics: answer quality is evaluated with human judgment and LLM-Match style scoring; the paper emphasizes correlation between automatic and human evaluation.

## Key Figures / Architecture

figure_status: linked_official

- Figure / demo: Evaluation workflow.
- Source: https://open-eqa.github.io/assets/images/workflow.png
- Render:
  ![OpenEQA evaluation workflow](https://open-eqa.github.io/assets/images/workflow.png)
- What it shows: the LLM-Match evaluation loop for comparing free-form model answers against reference answers.
- Why it matters: for this repository, it is a useful reference for evaluating generated embodied worlds with natural-language environment questions rather than only geometric or perceptual metrics.

Additional official visual evidence:

- Dataset/statistics figure: https://open-eqa.github.io/assets/images/figure-3.png
  ![OpenEQA dataset statistics](https://open-eqa.github.io/assets/images/figure-3.png)
- Performance figure: https://open-eqa.github.io/assets/images/multi-modal-llms.svg
  ![OpenEQA model performance](https://open-eqa.github.io/assets/images/multi-modal-llms.svg)
- Teaser video: https://open-eqa.github.io/assets/videos/open-eqa-teaser.mp4

## Evidence Trail

| Claim | Source | Status | Notes |
|---|---|---|---|
| OpenEQA is a CVPR 2024 embodied QA benchmark. | https://openaccess.thecvf.com/content/CVPR2024/html/Majumdar_OpenEQA_Embodied_Question_Answering_in_the_Era_of_Foundation_Models_CVPR_2024_paper.html | verified | Primary proceedings page. |
| The benchmark contains 1600+ questions over 180+ real-world environments. | https://open-eqa.github.io/ | verified | Reported on official project page and repeated in this dry-run summary. |
| Official code / benchmark materials are available. | https://github.com/facebookresearch/open-eqa | partial | Repository exists; this dry run did not execute the benchmark locally. |
| LLM-Match is used as an automatic evaluation workflow for free-form answers. | https://open-eqa.github.io/assets/images/workflow.png | verified | Official workflow figure; exact prompt details should be checked before citing implementation specifics. |

## Evidence

- Main metrics: official pages report comparisons between multimodal models, text-only baselines, and human performance.
- Qualitative results: project page provides example questions, dataset statistics, performance by category, and an episode-history teaser.
- Ablations: not verified in this dry run; the PDF should be checked before using detailed claims.
- Baselines: the project page mentions evaluations of several foundation models, including multimodal and text-only baselines.
- Reproducibility signals: official code/benchmark repository is linked, but this dry run did not reproduce results locally.

## Limitations

- Method limitations: OpenEQA is an evaluation benchmark, not an executable world generator or robot policy.
- Experimental limitations: detailed metric values, splits, and ablations were not independently checked in this dry run.
- Demo / visual limitations: visual generation quality is not applicable; its value is benchmark design and evaluation examples.
- Claims that remain unverified: exact correlation values for LLM-Match and category-level model scores should be deep-checked in the PDF before citing precise numbers.

## Project Relevance

- Relevance to interactive embodied generation: generated environments should support meaningful embodied QA; OpenEQA supplies a downstream evaluation framing.
- Reusable fields: `Question`, `Answer`, `EpisodeHistory`, `EnvironmentObservation`, `EvaluationProtocol`, `AnswerMatcher`.
- Possible baseline role: downstream benchmark for whether generated worlds preserve object identity, spatial relations, and semantic affordances.
- Implications for our task / benchmark: when building interactive generated worlds, include QA probes that test spatial, object, attribute, and world-knowledge consistency.

## Reproduction / Follow-up

- What to check before using: inspect the PDF and GitHub repository for split files, evaluation scripts, answer-matching prompt, and expected input format.
- Minimal reproduction plan: install the official benchmark, run a small subset with one open multimodal model and one text-only baseline, then compare automatic scores with manual inspection.
- Open questions: how robust is LLM-Match to prompt wording, ambiguous questions, and generated environments whose object names or layouts differ from real scans?
