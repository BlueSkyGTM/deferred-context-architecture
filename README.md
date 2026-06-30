# M2W — Manifest to Workspace

M2W turns raw, located material into finished deliverables — **manifest in, workspace out** — governed
end to end by one discipline: **deferral**. Every evaluation, execution, and judgment is withheld until
acting is safe — until the context is clean enough that committing will not contaminate the result. The
payoff is a pipeline that runs without a human steering it, never carries more than the one thing it is
working on, and can stop cleanly at any point.

```
EXCAVATION → ASSAY/INTAKE → TRANSPORT/MANIFEST → ITERATION → SHIP
  mine         three-way sort    catalogue +          build,
               cart/tailings/    frontmatter,         MVP-first,
               bench             address              done-gate
```

Each arrow is a **deferral point** (a "gate"): a stage runs only when the one before it produces
something that *requests* it. Nothing fires on its own initiative — including the start of the next
loop.

## What makes it different: orchestration is structural, not prompted

Most "agent orchestration" is prompt engineering — you re-tell the model, every session, what to do and
when. M2W inverts that. **The orchestration is compiled into the files.** The stage contracts declare
what each stage produces; the gates declare when work may commit; and the gate→play map declares exactly
which tool fires at which point, on which model tier. A cold agent reads the structure and executes it
deterministically — the same way every time — instead of being coaxed into behavior per prompt. The
schedule below is not documentation bolted on after the fact; it is the engine's wiring.

| Deferral point | what fires (the gstack team) | tier |
|---|---|---|
| **Excavation** (→ vault) | the gstack browser (`/browse`, `/open-gstack-browser`) + `/scrape` + `/skillify` — mechanical haul, no relevance filtering | LIGHT |
| **Assay** (seam sort) | Confusion Protocol → bench; **no review skill** (the seam is the engine's own brain) | MID |
| **Manifest** (catalogue) | — mechanical cataloguing + frontmatter | LIGHT |
| **Iteration — pre-build** | `/spec` always; `/autoplan` when the deliverable warrants it | TOP |
| **Iteration — conformance** | `/review` + `/codex` (sequential, no subagents); `/qa` `/design-review` `/cso` as the surface applies | TOP |
| **Done-gate → ship** | `/ship` `/land-and-deploy`; `/make-pdf` `/document-*` `/canary` | TOP |
| **Loop boundary** | save-memory + gbrain + `/context-save`/`/context-restore` — session continuity, never auto-loop | LIGHT–MID |

Two things make it more than a checklist. **gstack is the operating team**, not a tool in a box —
ponytail, LLMLingua, gbrain, and the memory skills are the instruments that team wields. And the map is
**open**: a pilot wakes whatever its domain warrants (a website pilot pulls up `/qa`, `/design-html`,
`/canary`; an iOS pilot wakes the `/ios-*` suite). Only the parallel/multi-agent plays are rejected by
law. The full, cross-model-validated map lives in `platform/SKILLS.md`.

## Tasks you can pick up whenever

A single run spans many sessions. Continuation is built the same structural way. When a deliverable
ships and seals, the engine **stops** — it does not check for more work and it does not auto-loop. A new
loop begins only when the operator drops in new material, and the engine already knows what is finished
because **progress is marked by production, not by a counter**: every piece carries `consumed` /
`sealed` state on disk. A second loop ignores what is done, never collides on ids, never re-processes.
Stop any time; resume any time; the filesystem *is* the cursor.

## One agent, many tiers — no big overheads at once

Single-agent, depth-first, **by law**: the context never carries more than the one thing it is working
on. (Parallel subagents would violate exactly that — big overheads at once is the failure mode the whole
design avoids.) But single-agent is **not** single-model. The one agent switches its own tier to fit the
work — a light model to fetch and catalogue, the top model where judgment actually lives — self-directed,
not the operator's to drive. Cheaper, more focused, and bounded by a hard rule: a heavier tier never
earns the right to *resolve* what a gate defers (ambiguity at the assay still benches, on any tier). See
`platform/TOOLING.md`.

## Core vs pilot — the operator supplies the domain

This repo is the **domain-agnostic core**; it never names a domain. The operator supplies the domain as
a **pilot** under `pilots/` (copy `pilots/_TEMPLATE/` and fill the extension points — seam, deposits,
design schema, build workflow, any domain-woken skills). A pilot may reference core; **core never
references a pilot.** Delete `pilots/` and the engine still stands.

## Read order

The canonical read order lives in `CLAUDE.md`; start there. In short:
1. **`CLAUDE.md`** — the law / operating manual + the canonical read order. **Entry point.**
2. `platform/` — non-negotiables (PRINCIPLES), engine principles (MWP), the deferral points (GATES),
   logs, tool policy + the gstack-at-gates map (TOOLING, SKILLS), glossary.
3. `M2W.md` — the governing discipline, explained.
4. `ARCHITECTURE.md` — the full spec.
5. `stages/` — the four stages, in order (each with its authoritative `CONTRACT.md`).
6. `BUILD-INSTRUCTIONS.md` — what to build this pass + the hard DO-NOT list (for a build pass).
7. `pilots/<name>/` — the instantiation, for a run.

Before any run, `bash bin/scan-tools.sh` reports what tools are present/missing on this machine. State
that is per-machine or in-flight is glass-box on disk; changes to the engine are recorded in
`changelog/CHANGELOG.md` under a revert guard.

## The laws (one line each)

- **Deferral.** Defer every evaluation, execution, and judgment until needed — the contamination defense.
- **You do not think; you execute.** When uncertain, bench it or log it and stop. Never guess.
- **Earned, not given.** Starts empty except the law; everything else clears a deferral point.
- **Glass-box.** State is the filesystem; no hidden state.
- **Single-agent (not single-model).** One agent, one path, depth-first — switching its own model tier.
- **Gates check conformance, never quality.** Quality lives in the shape of the design schema.
- **The assay has three exits** — cart, tailings, bench — so the pipeline never commits to an uncertain call.
- **Done-gate = diminishing marginal utility** — ship at the substance-to-surface transition; then stop.

## Lineage

M2W is a **modification of ICM** (Interpreted Context Methodology): it implements ICM's methodology
natively and adds the mining front-end (excavation → assay → manifest) that ICM assumes you already
have. Forbidden is forking the ICM *repo* and letting it hijack the infrastructure — not the methodology,
which is the lineage this is built on. An earlier name for this system was "ECA — Earned Contract
Architecture," retired: ECA emphasized performance at every gate; M2W emphasizes deferred commitment that
avoids context contamination. Same mechanics, corrected emphasis.
