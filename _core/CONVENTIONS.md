# _core/CONVENTIONS.md — how a silo is built (the canonical rules)

DCA is folder-structure-as-architecture. The structure IS the system; prose is minimal. Every silo
follows these patterns. This file is the canonical source for them — a silo references it, never
restates it.

## Five-layer routing (a silo is read top-down; stop when you have what you need)

```
Layer 0  silo/CLAUDE.md        "Where am I?"            folder map + triggers + routing (~800 tok)
Layer 1  silo/CONTEXT.md       "Where do I go?"          task → stage routing table  (~300 tok)
Layer 2  stages/NN/CONTEXT.md  "What do I do?"           the stage contract          (~200-500 tok)
Layer 3  reference/, skills/   "What rules apply?"       the factory (voice, design, conventions)
Layer 4  stages/NN/output/     "What am I working with?" this run's material + prior stage output
```

No agent reads everything. A stage's Layer-2 **Inputs** table decides exactly which Layer-3 and
Layer-4 files load. Every token of irrelevant context is a token of diluted attention — loading more
does not make output better, it makes it worse.

**Layer 3 is the factory; Layer 4 is the product.** Layer 3 (voice, design, conventions) is
configured once at `setup` and is stable across every run. Layer 4 (drawn source, prior output)
changes every run. Configure the factory, not the product.

## Stage contract (every `stages/NN-*/CONTEXT.md` has this exact shape)

```markdown
## Inputs
| Source | File/Location | Scope | Why |
|--------|--------------|-------|-----|

## Process
1. …

## Outputs
| Artifact | Location | Format |
|----------|----------|--------|
```

One stage, one job. A stage that draws does not build; a stage that builds does not draw.

## The laws that bind every silo

- **One-way references.** A silo reads down and outward only: silo → `../../vault` (the well),
  silo → `../../_core`, silo → `../../meta-seams`. **Never silo → another silo. Never well → silo.**
  No cycles. This is what keeps silos independent — buildable in any order, in parallel.
- **Canonical sources.** Each concept has one home; everything else points to it. A duplicate that
  drifts is where bugs hide.
- **Glass-box.** All state is on disk and inspectable. What a stage did is a file, not memory.
- **Single-agent.** One agent runs one silo's path top to bottom. No subagents, no parallel workers
  inside a silo. (Silos themselves are independent, but each is run single-agent.)
- **Deferral.** Pull from the well only what a stage needs, when it needs it. See `deferral.md`.
