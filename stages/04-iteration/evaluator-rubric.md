# Evaluator Rubric — The Independent Checker (Accept / Revise / Block)

The worker does not grade itself. A separate evaluator pass checks each iteration's output and
returns ONE of three verdicts. This is the harness "feedback" layer — the highest-ROI part and the
one most often skipped. The builder cannot mark its own work done.

## The three verdicts (a three-exit gate, like the assay)
- **ACCEPT** — the output applied its design schema and conforms. It advances (toward the done-gate).
- **REVISE** — it does not yet conform, but the gap is fixable in place. Return it to iteration with
  the specific non-conformance named. NOT a failure — a targeted re-run.
- **BLOCK** — it is wrong in a way that in-place revision will not fix (off-schema, off-seam content
  surfaced, structural break). Stop. Route to bench/ or logs/failures.md. Do not revise; escalate.

This mirrors the assay's three exits (cart / tailings / bench) so the back half is structurally
consistent with the front half: no gate collapses to pass/fail; every gate has a middle path and an
escalation path.

## What the evaluator checks (conformance, NOT quality)
- Was the design schema applied?
- Does the output conform to the schema's shape?
- Source-fidelity: does the deliverable contain only what the manifest supports? (the "no facts not in
  my material" constraint — source-pinning is a conformance check). The instantiation states the
  concrete form of this check (see `iteration-workflow.md`).
Verdict is on conformance and source-fidelity, never on "is this good." Quality lives in the schema.

## Worker / checker separation (single-agent compatible)
The builder does NOT grade its own fresh output. This is NOT a second agent — that would violate the
single-agent law (`platform/PRINCIPLES.md` #5). It is a **separate pass with FRESH CONTEXT**: the same
single agent, re-entered with the prior build context cleared (a new session, or context reset), so it
reads the output cold against the rubric instead of from the memory of having written it. The
separation is temporal (build pass, then a cleared check pass), not parallel. "It looks done" is not a
verdict; "it conforms and every fact traces to source" is. Log every verdict to logs/gate-checks.md
(outcome: accept | revise | block).

## TODO(tools)
A later pass MAY wire a review apparatus to run the rubric, but it must stay single-agent (a fresh-
context sequential pass, not concurrent workers — see the gstack fence in `platform/TOOLING.md`). For
now the rubric (this file) is what you build; the verdict is rendered against it.
