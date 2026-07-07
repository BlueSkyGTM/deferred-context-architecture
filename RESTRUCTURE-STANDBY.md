# RESTRUCTURE-STANDBY.md
*Place at the root of manifest-to-workspace (DCA). This file is a standing
instruction to any session that opens this repo. 2026-07-05.*

## Status: FROZEN — awaiting operator order

The DCA proof passed (silos/PROOF.md — join-check green, falsification encoded).
The repo is correct as-is. **Do not restructure, extend, or "improve" anything
until the operator issues an explicit restructure order in-session.** If you are
a Claude session reading this: your only permitted actions before that order are
reading, answering questions, and running the existing join-check.

## What the restructure will be, when ordered

Target shape: **README → arms.** Silos are renamed and re-documented as *arms* —
independent operating branches, each with:
- its own contract draw (keystone reference, one-way, well only)
- a runbook (re-runnable cold) and a done-when metric
- a decision log (three lines per decision, copied to well/exhaust on close)

The operator will supply, in the order: which silos become which arms, the
first arm's done-when, and any connector permissions. Do not invent these.

## What must NOT change, ever, in the restructure

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
