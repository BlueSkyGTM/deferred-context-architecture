# done-when.md: arm-01

The single metric that says this arm's current objective is DONE. Operator-supplied — a session
never invents or edits this. One metric at a time; when it is met, the operator sets the next one
(or closes the arm).

## Current objective

**Done when:** `python bin/join-check.py` still exits PASS AND this arm has all four required
pieces in place: contract draw (`stages/01-draw/`), runbook (`runbook.md`), done-when metric
(this file), decision log (`decision-log.md`).

**Set by:** operator on 2026-07-06 (restructure order, in-session)

## Met objectives (append-only)

| date met | objective | evidence |
|----------|-----------|----------|
