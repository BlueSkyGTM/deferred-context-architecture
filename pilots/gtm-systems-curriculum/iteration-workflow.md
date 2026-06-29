# iteration-workflow.md — This Pilot's Concrete Build Chain (sources → wiki → graph → course)

The core declares iteration as an INTERFACE: pull from the manifest, build a deliverable MVP-first,
check conformance against a design schema, stop at the done-gate (see `stages/04-iteration/`). This
file supplies the CONCRETE build chain for a curriculum deliverable. A different pilot would supply a
different chain; the core gates do not change.

## The chain
1. **MANIFEST** is the source of truth (core stage 03 output): catalogued, frontmatter-typed material
   at its declared location.
2. **WIKI COMPILE** (Karpathy LLM wiki, principles applied natively — structure NOT forked): compile
   the manifest into linked articles, one per concept, cross-linked, with an index ordered
   beginner → advanced (the learning order). Immutable raw preserved; the wiki is the compiled layer.
3. **GRAPH** (Understand-Anything `/understand-knowledge`): turn the wiki into a navigable graph for
   HUMAN comprehension and inspection. This is the inspectable layer.
4. **COURSE** (capstone): build ONE self-contained deliverable from the wiki + index as the SINGLE
   SOURCE OF TRUTH. Lessons in the index's learning order; per-lesson objective, explanation, worked
   example, and a short comprehension check; a final assessment; review-pointers for misses.

## Source-pinning IS this pilot's conformance discipline
The constraint enforced by the evaluator: **do NOT add facts not in the material.** The deliverable
is pinned to the manifest, so it cannot drift off-seam by inventing content. This is how the
curriculum stays on-seam at GENERATION time, not just at intake. For the core, this is the concrete
form of "conform to the design schema" (core `stages/04-iteration/evaluator-rubric.md`): in this
domain the schema's shape includes "every fact traces to a manifest source."

## Design-schema bootstrap for this pilot
The core notes that on a first run the design schema may not yet exist (it is cut from logs of
proven-good work). For this pilot the FIRST iteration runs in **schema-discovery mode** (explicitly
ungated for conformance): it produces the MVP course and the logs from which the schema is cut.
Conformance gating begins on the SECOND iteration, once a schema exists. See core
`stages/04-iteration/CONTRACT.md` (Inputs → design schema, bootstrap rule).

## MVP-first applies
Iteration one produces a viable, unfinished course (structure stands, some lessons stubbed). Later
iterations finish or dismantle, gated by the done-gate (substance-to-surface) and the evaluator
(Accept/Revise/Block). Ship when another pass adds only surface.
