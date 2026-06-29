# CONTEXT.md — learned-seam/ (the seam's training, accreted from logged calls)

Where the seam layer accretes across the curriculum loop. It is the OUTPUT of Runs 1a→1c, not an
input the pilot starts with. Canonical state is READABLE files here (and the core logs); GBrain, if
configured, is only a projection of these — never the sole home of a seam decision (core
`platform/SKILLS.md`).

## What lands here
- The carry-forward of every assay call the human makes (cart/tailings/bench) with its curated
  reason, distilled into generalizable edges — NOT a per-item blacklist. The raw per-call record is
  in `logs/gate-checks.md` and `logs/rejections.md`; this folder holds the LEARNED generalization the
  audits inspect.
- The audit notes between sub-runs (1a→1b→1c): consistency checks, corrections, and whether the seam
  is still wrong on settled cases (the gate that keeps the pilot from advancing on bad training).

## Inspectability is the point
The curriculum pass IS the seam layer's training run. Every call is training data. If this were
buried in a blackbox store, the human could not grade whether the seam learned the right boundary.
Keeping it in readable files preserves the answer-key check (`../answer-key/`). This is not a style
preference; it is what makes the dry run gradeable.

Status: _empty — populated as Run 1a begins._
