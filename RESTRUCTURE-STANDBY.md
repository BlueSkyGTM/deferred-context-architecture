# RESTRUCTURE-STANDBY.md
*At the root of the DCA repo. Written 2026-07-05 as a standing freeze
instruction; executed 2026-07-06. Now the record of the order and its
still-standing fences.*

## Status: EXECUTED 2026-07-06

The operator issued the restructure order in-session on 2026-07-06 and supplied
the required inputs verbatim:

1. **Rename shape:** `silos/` stays untouched as the frozen proof layer (this
   also resolves the conflict that `bin/join-check.py` hardcodes silo paths and
   must never be edited). A new `arms/` directory is the operating layer.
2. **Silo→arm map:** no conversions — producer/consumer remain proof silos.
   The first arm (`arms/arm-01/`) is scaffolded new and empty.
3. **First arm done-when:** `python bin/join-check.py` still exits PASS AND the
   arm has all four required pieces (contract draw, runbook, done-when,
   decision log).
4. **Connectors:** none — strict one-way arm → well / `_core` / `meta-seams`.

The sections below are kept as the record of what was ordered and as standing
law where marked. The "What must NOT change" fences and the sequencing remain
in force permanently.

## What the restructure was, as ordered

Target shape: **README → arms.** Silos are renamed and re-documented as *arms* —
independent operating branches, each with:
- its own contract draw (keystone reference, one-way, well only)
- a runbook (re-runnable cold) and a done-when metric
- a decision log (three lines per decision, copied to well/exhaust on close)

The operator supplied, in the order: which silos become which arms, the
first arm's done-when, and connector permissions (recorded under Status above).

## What must NOT change, ever (STANDING LAW — survives the execution)

- `vault/keystone-task.md` — the contract. Arms conform to it; nothing edits it
  except the operator by hand.
- `bin/join-check.py` — the falsifiable check, including its inject-garbage
  step. A check that cannot fail proves nothing; keep its teeth.
- One-way references: arm → well only. Never arm → arm.
- The operator's three touchpoints (stake / cut / sign). If a session finds
  itself performing one on the operator's behalf: stop.

## What arrives with the restructure

`keystone-forge/` — the keystone creation + testing function (see FORGE.md).
It joins the repo as the demonstration layer: how contracts are authored, and
how they are validated before any production use. Law: **no keystone enters an
arm untested.**

## Sequencing (operator-decided, recorded here so no session relitigates it)

1. This repo restructures to arms — on order, not before.
2. The repo is then **cloned** as the seed of the Deferred Revenue Architecture
   OS (DRA). Keystones are trialed in production **only in the clone**, never
   here. This repo remains the reference implementation and the college-visible
   artifact: engine plain-named (DCA), product big-named (DRA), render backed
   by what runs.
3. The course does NOT use this repo. The course is an ICM workspace
   (LESSON-PLAN.md). Do not couple them.
