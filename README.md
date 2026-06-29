# M2W — Manifest to Workspace

A mining operation for turning raw, located material into finished deliverables, governed end to end
by deferral: every evaluation and execution is withheld until acting is safe — until the context is
clean enough that committing will not contaminate the result.

```
EXCAVATION → ASSAY/INTAKE → TRANSPORT/MANIFEST → ITERATION → SHIP
  mine         three-way sort    catalogue +          build,
               cart/tailings/    frontmatter,         MVP-first,
               bench             address              done-gate
```

## Read order
The canonical read order lives in `CLAUDE.md` ("Canonical read order"); start there. In short:
1. CLAUDE.md — the law / operating manual + the canonical read order. **Entry point.**
2. platform/ — non-negotiables, MWP principles, deferral points, logs, glossary.
3. M2W.md — the system's governing discipline.
4. ARCHITECTURE.md — the full spec.
5. stages/ — the four stages, in order.
6. BUILD-INSTRUCTIONS.md — what to build this pass + the hard DO-NOT list (for a build pass).
7. pilots/<name>/ — the instantiation, for a run (the operator's supplied domain).

## What this package is
The skeleton + logging. A standing, empty pipeline that runs no work yet. The frame before the
material; the material before the tools.

## What it is NOT (yet)
- Not tool-wired. Tool slots are literal `TODO(tools)` markers, wired in a later pass.
- Not populated. vault/ carts/ tailings/ bench/ manifest/ library/ start empty by design.
- Not a fork of ICM. M2W is a MODIFICATION of ICM (Interpreted Context Methodology): it implements
  ICM's methodology natively and adds the mining front-end (excavation→assay→manifest) that ICM
  assumes you already have. What is forbidden is forking the ICM *repo* and letting it hijack the
  infrastructure — not the methodology, which is the lineage this is built on.
- Not domain-specific. The core is domain-agnostic; the operator supplies the domain via a pilot
  under `pilots/`. Core never references a pilot.
- Not multi-agent. Single-agent, depth-first, by law.

## Core laws (one line each)
- **M2W** — defer every evaluation, execution, and judgment until needed. Deferral keeps the context
  clean; it is the contamination defense, not a delay tactic.
- **You do not think; you execute.** When uncertain, bench it or log it and stop. Never guess.
- **Earned, not given.** Starts empty except the law; everything else clears a deferral point.
- **Glass-box.** State is the filesystem.
- **Deferral points check conformance, never quality.** Quality lives in the shape of the design schema.
- **The assay has three exits** — cart, tailings, bench — so the pipeline never commits to an
  uncertain call.
- **Done-gate = diminishing marginal utility** — ship at the substance-to-surface transition.

> Note: an earlier name for this system was "ECA — Earned Contract Architecture." Retired. ECA
> emphasized performance at every gate; M2W emphasizes deferred commitment that avoids context
> contamination. Same mechanics, corrected emphasis.
