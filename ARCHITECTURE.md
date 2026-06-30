# ARCHITECTURE.md — M2W (Manifest to Workspace)

**The architecture OVERVIEW: the shape of the system and *why* it is shaped that way.** It is NOT a
second spec. The stage `CONTRACT.md` files and the `platform/` law files are authoritative and own
ALL mutable detail — formats, field schemas, gate mechanics, log streams. This overview never restates
them; it points (the canonical-homes table is at the bottom).

## The system

- **M2W — Manifest to Workspace** is the transform: catalogued material in, built workspace out. Its
  governing discipline is **deferral** — withhold every evaluation, execution, and judgment until
  acting is safe (the context is clean enough that committing will not contaminate). M2W is not a
  performance model where work proves itself at each gate; it is a contamination-defense model where
  judgment and execution are deferred until genuinely needed.
- **MWP — Model Workspace Protocol** is the engine-principle layer M2W borrows for routing and stage
  execution, implemented natively (no repo to fork). M2W splits MWP in two and places the halves at
  opposite ends: its **intake** half becomes the assay (stage 02); its **stage-building** half becomes
  iteration (stage 04), with transport/manifest between. Principles: `platform/MWP.md`.
- **ICM** (Interpreted Context Methodology) is MWP's lineage, deliberately EXCLUDED from the build —
  borrow the principles, never fork the engine. (The earlier system name "ECA — Earned Contract
  Architecture" is retired: ECA framed work as proving itself at gates; M2W is the opposite — deferred
  commitment that avoids contamination. Same mechanics, corrected emphasis.)

## Why deferral is load-bearing (not stylistic)

- A stage runs because the prior stage produced something that **requests** it — never because it
  exists; nothing fires speculatively, including the start of the next loop.
- Nothing is loaded into context speculatively; material sits addressed on disk until pulled. Context
  stays clean because only what is needed is ever present — that is the contamination defense.
- The pipeline can stop cleanly at any point (nothing downstream is committed), and a bad input dies
  cheap because the expensive downstream work was deferred behind a request it never produces.

This is why the front of the pipeline is allowed to be slow and judgment-free, why the cost of a
mistake is pushed to the cheapest place (the front), and why the context never fills with unneeded work.

## The pipeline (mining-ops model)

```
EXCAVATION → ASSAY/INTAKE → TRANSPORT/MANIFEST → ITERATION → SHIP
  mine        three-way sort   catalogue+address   build, MVP-first, done-gate
```

The mining analogy is exact, not decorative: mine the material, **assay** it at the dig site before
spending a cart on it, transport and catalogue what passes, process it at the destination yard into a
finished product. The hard part is not navigation; it is deciding what material is worth processing —
and deferring that decision until the material is in hand. That is an assay problem, and the assay is
intrinsically THREE-way (on-seam → cart, off-seam → tailings, uncertain → bench), which is how the
pipeline runs without a human on the settled cases while never committing to an uncertain call. Each
stage's exact behavior is owned by its `CONTRACT.md`; the deferral points by `platform/GATES.md`.

## The seam (the one mechanism worth naming here)

The **seam** is the boundary defining what belongs to the domain in play. The operator supplies the
domain; the core is agnostic. The seam is necessarily incomplete at the start and **accretes** — on a
domain's first run the human teaches edges (every assay call logged with its reason), and the seam
grows more complete each run. The highest-value training signal is the *looks-transferable-but-off-seam*
case. The concrete seam shape lives in the pilot (`pilots/<name>/seam.md`); the term is defined in
`platform/glossary.md`; the routing that uses it is `stages/02-assay/CONTRACT.md`.

## What lets it run without a human

Three things, all in MWP's routing: **task routing** runs the settled cases (known route in → known
stage out); **context folders** hand each stage exactly what it needs and nothing else (the
contamination defense); and **the bench** routes the unsettled cases to the human instead of
committing. The human is the *source* of seam judgment, not the permanent *gate* — over runs the system
handles settled edges autonomously and escalates only novel boundaries.

## Single-agent, multi-tier; one loop at a time

One agent, one depth-first path — no parallelism, no big overheads at once (PRINCIPLES #5). That one
agent switches its own MODEL TIER to fit the work (light to fetch, top to build); model-tier policy in
`platform/TOOLING.md`. A run spans many loops: after a deliverable ships and seals, the engine STOPS
and re-enters only on new operator deposits — progress marked by produced state on disk
(`consumed`/`sealed`), not a counter. The loop boundary is itself a deferral point (`platform/GATES.md`).

## Canonical homes (this overview points; it never restates)

| Concept | Authoritative home |
|---|---|
| The non-negotiable laws | `platform/PRINCIPLES.md` |
| Engine principles (five-layer routing, contracts, one-way refs, canonical sources) | `platform/MWP.md` |
| The deferral points / gates (incl. the loop boundary) | `platform/GATES.md` |
| Each stage's exact behavior | `stages/0N-*/CONTRACT.md` |
| Manifest item frontmatter schema | `stages/03-manifest/frontmatter-schema.md` |
| The three log streams + their formats | `platform/LOGS.md` |
| Tool policy, the gstack fence, the model-tier policy | `platform/TOOLING.md` |
| The gstack gate→play map | `platform/SKILLS.md` |
| Authoritative term definitions | `platform/glossary.md` |
| The instantiation (a supplied domain) | `pilots/<name>/` |

The instantiation supplies the domain; core never names one. A domain's FIRST run is its seam's
training run, not a deployment. Tools are wired in a later pass, only the subset a run needs.
