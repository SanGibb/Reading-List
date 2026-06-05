# Undecided Candidates

This folder stores candidates that require human judgment before acceptance or rejection.

Typical reasons:

- visual generation quality is hard to judge from available evidence,
- demos are inaccessible or ambiguous,
- results look promising but may be cherry-picked,
- the paper is relevant but the model cannot confidently decide whether the visual/interactive effect is good enough,
- the decision depends on taste, domain expectation, or project-specific bar.

Each run may create:

```text
undecided/YYYY-MM-DD/CAND-xxxx.md
```

Each dossier should be detailed enough to support a later human accept/reject decision. It should include:

- candidate title and source link,
- branch,
- TL;DR,
- novelty,
- contributions,
- task,
- data,
- method,
- why it matters for this repository,
- available visual/demo links,
- what was inspected,
- evidence trail for central claims,
- key figures / architecture with `figure_status`,
- limitations,
- why the agent could not decide,
- suggested human decision options: accept, reject, keep watching.

Undecided candidates must not enter `data/papers.seed.json` or `05_registry_patch.json` until a human decision is made.

By default, `undecided/YYYY-MM-DD/CAND-xxxx.md` dossiers are local-only and are not pushed by `scripts/publish_validated_update.py`. After human approval, the candidate can be promoted through a separate update.
