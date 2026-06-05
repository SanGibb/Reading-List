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

Each dossier should include:

- candidate title and source link,
- branch,
- why it matters,
- available visual/demo links,
- what was inspected,
- why the agent could not decide,
- suggested human decision options: accept, reject, keep watching.

Undecided candidates must not enter `data/papers.seed.json` or `05_registry_patch.json` until a human decision is made.
