# Iteration-Workflow Interface — What the Pilot Must Supply

The core does NOT prescribe HOW the deliverable is built — that is pilot-specific and belongs to the
pilot. The core declares the INTERFACE the build chain must satisfy; a pilot supplies the concrete
chain (a Claude Code default ships in `pilots/_TEMPLATE/iteration-workflow.md`). This keeps stage 04
pilot-agnostic. The deliverable is a Claude Code system, and its ground truth is behavior: the chain
must end in a live dry-run in a real Claude Code session, not a prose read-through.

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

A concrete pilot supplies the chain — for example, scaffold the target system's repo from the
manifest, cut its law files, build its capabilities, then dry-run it live, source-pinned to the
manifest. The concrete chain for any pilot lives in `pilots/<name>/iteration-workflow.md` — a pilot
detail; nothing in core may reference a specific one.
