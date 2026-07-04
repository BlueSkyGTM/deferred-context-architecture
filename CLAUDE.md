# CLAUDE.md — DCA Operating Manual (THE LAW)

This file orients a cold agent to **DCA — Deferred Context Architecture** (formerly M2W). It governs
the *machine*: how the well and the silos relate, what you may and may not do. It is not any silo's
own instruction set — a silo produces that for itself, downstream, at `setup`. Do not confuse the two.

## What DCA is, in one paragraph

DCA builds **silos** — independent pillars, each a self-contained ICM workspace that produces one
kind of deliverable — over **one shared well** (`vault/`). Vanilla ICM configures a factory and feeds
it source material per run; DCA's move is to pool all raw material in one well and let every silo
**draw** the thin slice it needs, on demand. The governing discipline is **deferral**: pull context
from the well only when a stage needs it, nothing speculative — which is exactly why a silo (and the
ICM inside it) stops inventing on the spot, because it is always fed real drawn assets. Silos are
independent: built in any order, in parallel, none waiting on another. The structure is the system —
folder layout carries the architecture; prose is minimal.

## Canonical read order

1. `CLAUDE.md` (this file) — the law / orientation.
2. `_core/CONVENTIONS.md` — how a silo is built (five-layer routing + the stage contract + the laws).
3. `_core/deferral.md` — the Deferred-Context discipline.
4. `_core/well-contract.md` — the shared well and the well↔silo handoff.
5. `silos/CONTEXT.md` — how to spin up a pillar.
6. For a specific silo: `silos/<name>/CLAUDE.md`.

## The shape

```
DCA/
├── vault/     THE WELL — one shared source pool; enters by extraction or placement; catalogued in account.md
├── silos/     THE PILLARS — each a self-contained ICM workspace; draws from the well; built in any order
├── _core/     the shared law + the silo template (_core/templates/silo/)
└── meta-seams/ shared output standards (writing.md) every silo clears
```

## The non-negotiables

1. **Structure is the system.** The folder layout carries the architecture. Keep prose thin; a rule
   has one home (`_core/`), everything else points to it. Never restate.
2. **Deferral.** Pull from the well only what a stage needs, when it needs it. Nothing speculative.
   Deferral is the contamination defense. (`_core/deferral.md`)
3. **Silos are independent.** One-way references only: silo → well / `_core` / `meta-seams`. Never
   silo → silo; never well → silo. This is what lets any pillar be built in any order.
4. **Single-agent, glass-box.** One agent runs one silo's path top to bottom; no subagents. All state
   is on disk and inspectable — if you must remember, write it down.
5. **Configure the factory, not the product.** A silo is set up once (voice, design, deliverable
   type); each run produces a new deliverable from that config + a fresh draw.
6. **Faithful to ICM, do not fix it.** The silo is a native ICM workspace. We feed ICM real assets
   (the well); we do not modify ICM. Reference: `RinDig/Interpreted-Context-Methdology`.

## Before you change the machine (REVERT GUARD)

If asked to modify, refactor, or revert the repo, read `changelog/CHANGELOG.md` FIRST. Do not revert
or overwrite a change whose entry is marked `tested:` without surfacing it to the human.

## Standing orders

Keep it thin — DCA's whole bet is that structure beats prose. Fill the well before you build a silo;
draw before you build; cut before you ship (a unit that tries to matter everywhere matters nowhere).
When uncertain, write it down and stop. Never reference one silo from another.
