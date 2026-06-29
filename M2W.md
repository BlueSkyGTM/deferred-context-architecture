# M2W — Manifest to Workspace (THE SYSTEM)

M2W is the name of this system: the transformation it performs. Raw material enters; a built
workspace comes out. The arc runs from the **manifest** (catalogued, typed, sealed material) to the
**workspace** (the built deliverable environment). The name is the function — manifest in, workspace
out — and the system is agnostic to what domain the material belongs to. The operator supplies the
domain; M2W supplies the transform.

## The governing discipline: deferral

M2W is governed by one law, inherited from its lineage (the system formerly named D2E, "Deferred
Evaluation and Execution," retired in favor of naming the transform rather than the law). The law did
not go away; it stopped being the headline. It is this:

**Defer every evaluation, execution, and judgment until something explicitly requests it.**

1. **Deferred evaluation.** Do not compute, judge, or assess a value until it is needed. The system
   never wastes work on things that may never be used — and never lets premature evaluation
   contaminate a context that is not yet clean.
2. **Deferred execution.** Construct the sequence of steps but do not run it until the output is
   requested. The whole pipeline is assembled before anything irreversible fires.

Deferral is the contamination defense, not a delay tactic: a context that admits only what is needed
cannot be polluted by work that was never needed.

## Why the transform is the name (not the law)

D2E named the law; M2W names the work. The shift is deliberate. What the operator cares about is
starting from zero and getting to a built workspace with little waste — the *generative* property,
manifest → workspace. Deferral is *how* that stays clean, but the *what* is the transform. Every
component is still an instance of "defer until needed," and the arc those components trace is
manifest-to-workspace:

- **Excavation** hauls but does not evaluate — evaluation is deferred to the assay.
- **The assay** evaluates seam-fit only when material arrives, never speculatively, and defers the
  uncertain call to the bench rather than committing.
- **The manifest** catalogues only what was carted — the structured-input layer the name starts from.
- **Iteration** executes only what the manifest requests and stops (done-gate) the moment further
  execution would add nothing — producing the workspace the name ends at.
- **A bad input dies cheap and clean** because the expensive downstream work was deferred until a
  request the bad input never produces.

## Single-agent is the law; parallelism is a latent property, NOT an enabled setting

The standing law is single-agent (platform/PRINCIPLES.md #5): one agent, one path, depth-first. That
is not negotiable in this build. What follows is an observation about the architecture, explicitly
SUBORDINATE to that law — it does not authorize parallel execution now.

The file architecture happens to encode a parallel decomposition: every folder with its CONTEXT.md is
an agent boundary — it hands whatever model enters both its knowledge (the contract) and its scope
(the folder). So single-agent and divide-and-conquer are the same architecture at two concurrency
settings; the contracts would not change. But the law says build and PROVE single-agent first (one
inspectable path, spec proven against it), because parallel execution against an unproven spec only
reaches the wrong result faster — that is the scar, learned the hard way. Parallelism is therefore a
LATENT property the architecture could later support, not a knob this system currently exposes.
Flipping it on is a FUTURE decision that requires (a) the spec proven single-agent and (b) an explicit
change to the law — until both happen, #5 governs and parallel/multi-agent execution is forbidden.
(See platform/PRINCIPLES.md #5 and platform/TOOLING.md.)

## What this means for the builder

Do not run a stage because it exists. Do not load material into context because it is available. Do
not evaluate quality before the stage that owns that evaluation. Do not execute an irreversible step
until the output that needs it is actually requested. When in doubt about whether something is
"needed yet," it is not — defer it. Deferral is never the wrong call here; premature commitment is.
