# Task-Level Reading Frontier and Succession

The registry preserves collected knowledge; the task frontier controls what to read
or reproduce first. A paper can become historical for one task and remain current
or an alternative for another. A historical role never deletes the registry entry,
its deep dive, or its stable links.

## Define a Comparable Task

Maintain `data/task_frontiers.seed.json` separately from `data/papers.seed.json`.
Each task has a stable lower-case, hyphen-separated `task_id`, a title, one A-E
branch, and `scope` with `input`, `output`, `setting`, and `protocol`. Use a concrete
task, not a branch-sized label such as "VLA" or "world generation". The protocol
states the relevant benchmark/split, evaluation axes, and conditions needed to
interpret comparisons, including data, compute, hardware or deployment budget
where material. If these are not yet established, say so explicitly.

Every member references the exact `paper_url` from the registry. A paper occurs at
most once per task; cross-task memberships with different roles are allowed. New
policy-v2 registry papers must have non-empty `task_ids`, each resolving to a real
task and a member for that paper. Existing papers without a policy version need
not be bulk migrated or rated. Absence from this file means unassessed, not current.

## Roles

| Role | Meaning in this task |
|---|---|
| `current` | A supported starting point for current reading or reproduction within the stated scope. Multiple current papers can coexist. |
| `alternative` | A useful option with a distinct strength, cost, openness, generalization or deployment tradeoff. |
| `historical` | Superseded for this task by a named successor, retained for lineage, baselines and its documented value. |
| `unreviewed` | Grouped by task, with no completed comparative recommendation. |

`current` does not claim a universal SOTA. Attribute benchmark claims to their
primary source unless independently reproduced. Publication date, a larger model,
one headline score, or broader marketing claims do not establish succession.

Every member has a non-empty `reason`. Reviewed roles (`current`, `alternative`,
`historical`) also require `reviewed_on` and a non-empty `evidence` array. Each
evidence item contains `source_url`, an exact `locator` such as a table/figure or
section, `claim`, `source_quality: primary|official|primary_or_official`, and
`status: verified`. Links alone are not a comparison. Describe reported results
honestly and distinguish source verification from independent reproduction.

## When a Predecessor Becomes Historical

A historical member additionally records `superseded_by` as another member's exact
registry URL in the same task, and `comparison` containing:

- `same_task: true`: the successor covers the predecessor's relevant task scope.
- `comparable_protocol: true`: inputs, splits, supervision, budgets, metrics and
  conditions are comparable, or controlled evidence resolves their differences.
- `no_material_regression: true`: no material loss on the task's decision-relevant
  quality, capability, efficiency, availability or deployment requirements remains.
- `improvements`: the substantive improvement or more complete coverage, with
  evidence locators and concrete reported results where available.
- `tradeoffs`: examined costs and regressions, including evidence gaps. Explain
  why any remaining tradeoff is immaterial to this task; do not leave this empty.
- `retained_value`: why the old work remains useful as history, a baseline, a
  simpler implementation, or a source of ideas.

All three booleans must be justified by the evidence. A new paper's admission is
independent of whether it displaces an old paper. If protocols are incompatible,
the successor has a material tradeoff, or evidence is insufficient, retain an
`alternative` or `unreviewed` member and record the uncertainty. Do not force a
winner. A wider task scope can be defined separately rather than hiding a useful
narrow-task method beneath it.

Only `historical` members may set `superseded_by`. The directed old-to-successor
links have no self-links or cycles, and every historical chain ends at a `current`
member in the same task. Thus a new successor may itself later become historical
without losing earlier lineage. Generate the reverse new-to-old display from this
single relationship rather than maintaining a second hand-edited edge list.

## Weekly Maintenance and Audit

1. For each admitted paper, identify or define concrete tasks and compare it with
   relevant existing members. Revisit relevant current papers when a same-task
   release or decisive new result appears; a weekly full-library rerating is not
   required.
2. Evidence Analyst collects comparable primary-source results and tradeoffs.
   Quality Reviewer decides task role and whether any predecessor meets every
   succession condition. Uncertain visual evidence still follows the ordinary
   local-only undecided rules for admission.
3. Taxonomy & Editor maintains the task file and records `lifecycle_changes` in the
   run patch when lifecycle decisions occur. Each item contains `task_id`,
   `paper_url`, `action: keep|promote|supersede|retain_alternative|reopen`, and
   `reason`. The task file is the authoritative resulting state; the run item is
   its audit trail. `reopen` means a prior judgment needs review and returns the
   member to `unreviewed`, with relevant succession links re-evaluated.
4. Keep accepted-candidate accounting complete: lifecycle changes are separate
   from `registry_additions`, `registry_updates`, and `registry_noops`. They cannot
   replace a candidate disposition or be disguised as a replacement paper update.
   Report role changes, their source evidence, retained alternatives and unresolved
   comparisons even if there are zero new papers.
5. Run `python3 scripts/render_reading_indexes.py`, then validate the registry,
   lifecycle references/graphs, run artifacts and generated indexes. The generator
   keeps all registry entries in the main and branch indexes and creates
   `paper_reads/task_frontiers.md` with current/alternative entries, expandable
   predecessor history and reverse successor links. `--check` verifies freshness.

Deep dives stay at their existing paths. The task view is the maintained navigation
layer; its task-specific historical label is not a global paper archive. Initial
family groupings may be `unreviewed`; grouping alone does not assert replacement.
