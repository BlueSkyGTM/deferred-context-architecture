# DCA — Deferred Context Architecture

**Many independent silos, one shared well.** DCA builds *pillars* — each a self-contained
[ICM](https://github.com/RinDig/Interpreted-Context-Methdology) workspace that produces one kind of
deliverable — over a single shared vault of raw material. Each silo **draws** the thin slice it needs
from the well, on demand, and builds. Silos are independent: built in any order, in parallel, none
waiting on another.

Formerly *M2W (Manifest to Workspace)*. The transform is the same — manifest in, workspace out — but
DCA makes the manifest **shared** (one well feeding many pillars) instead of one pipeline building one
thing.

## The shape

```
DCA/
├── vault/      THE WELL — one shared source pool; enters by extraction or placement; catalogued in account.md
├── silos/      THE PILLARS — each a self-contained ICM workspace; draws from the well; any order
├── _core/      the shared law (thin) + the silo template (_core/templates/silo/)
└── meta-seams/ shared output standards (writing.md) every silo clears
```

## The three ideas

1. **The well (Deferred Context).** All raw material pools in one vault. A silo pulls only what a
   stage needs, when it needs it — nothing speculative. This is why the ICM inside a silo stops
   *inventing on the spot*: it is always fed real drawn assets. Deferral is the contamination defense.

2. **Silos as pillars (ICM per silo).** Each silo is a native ICM workspace — folder-structure-as-
   architecture, five-layer routing, "configure the factory, not the product." One is set up once
   (voice, design, deliverable type); each run draws fresh material and builds. This is how the
   [scriptorium](https://ai-systems-scriptorium.vercel.app/) was built: seven books, any order.

3. **Independence (one-way references).** A silo reads only the well, `_core`, and `meta-seams` —
   never another silo. That is what lets you build one pillar while another is half-done, and why
   finishing one never blocks the next.

## Start

Read `CLAUDE.md` for the canonical read order. To stand up a pillar: copy `_core/templates/silo/`
into `silos/<name>/`, run `setup`, fill the well, draw, build.

DCA is faithful to ICM and does not modify it — it feeds it. Reference:
`RinDig/Interpreted-Context-Methdology`.
