# Iteration-Workflow Interface — What the Instantiation Must Supply

The core does NOT prescribe HOW the deliverable is built — that is domain-specific and belongs to the
instantiation (the pilot). The core declares the INTERFACE the build chain must satisfy; a pilot
supplies the concrete chain. This keeps stage 04 domain-agnostic.

## The interface (the contract any build chain must meet)
- **Input:** the manifest at `manifest/` — pulled just-in-time, never loaded wholesale.
- **Output:** a deliverable, built MVP-first, written to `library/` when it ships.
- **Conformance:** each iteration applies the deliverable's design schema; the conformance gate checks
  SHAPE, not quality (`evaluator-rubric.md`, core `platform/GATES.md`).
- **Source-pinning:** the deliverable may contain only what the manifest supports — no facts invented
  outside the material. (This is the generic form of "stay on-seam at generation time." A pilot states
  the concrete form, e.g. "every fact traces to a manifest source.")
- **Stop:** the done-gate (`done-gate.md`) ends the loop at diminishing marginal utility.

## What a pilot supplies
- The concrete build chain (the steps, the tools, the deliverable's shape) and the deliverable `kind`.
- The design schema AND its declared path (recommended `pilots/<name>/design-schema.md`); the
  schema-discovery iteration writes it there (see CONTRACT.md bootstrap rule).
- The concrete source-fidelity check the evaluator enforces.

A concrete instantiation supplies the chain — for example, compile the manifest into a linked
intermediate artifact and then a final deliverable, source-pinned to the manifest. The concrete chain
for any instantiation lives in `pilots/<name>/iteration-workflow.md` — a pilot detail; nothing in core
may reference a specific one.
