# platform/SKILLS.md — Standing Skills (State / Memory Harness Layer)

These skills run periodically across the pipeline's life. They are the State/Memory harness layer:
what keeps the agent from losing the thread across sessions. CRITICAL RULE: they write durable
output to READABLE FILES (logs, learned-seam files, session-handoff), never silently into a blackbox
store. The pilot depends on the seam learning being inspectable so the human can grade it. A skill
that buries decisions in an unreadable index defeats the answer-key check.

## context-compressor (periodic)
When context grows long or a session is wrapping, compress history into a structured summary WITHOUT
losing critical state. Writes the summary to a readable session file, not into hidden memory. Used
to hand off between sessions during long runs (a first run can span sessions).

## memory-manager (on durable decisions)
When a standing decision is made — a seam call with its reason, a schema cut, a routing rule —
memory-manager records it. RULE: it writes to the readable learned-seam files and the logs, which are
THEN optionally indexed into a retrieval store IF the instantiation wires one (the concrete store is a
domain choice, named in the pilot). The file is canonical; the store is only a projection. Never write a seam decision only into a store — the
human must be able to read and grade it from the files alone. (If no store is configured, the readable
files ARE the system and nothing is lost.)

## session-handoff.md (the clock-out note)
At the end of each working session, write/update session-handoff.md at root: what is verified, what
changed, what is broken, the single next-best step. The next session reads this first. This is the
cross-session thread the agent would otherwise lose.

## Why readable-file-canonical matters here specifically
A domain's first run IS the seam layer's training run. Every seam call the human makes is training
data. If memory-manager compresses those calls into a blackbox, the human cannot check whether the
seam layer learned the right boundary. Readable files preserve the answer-key check. This is not a
style preference; it is what makes a run gradeable.

## gstack at the gates — where the team's plays fire (the gate→play map)
gstack is the **operating TEAM** that runs this engine, not an item in the toolbox; the actual *tools*
(ponytail, LLMLingua, gbrain, the memory skills) are instruments the team wields. This map says WHICH
of the team's plays fire at WHICH deferral point. A play fires ONLY in its adopted single-agent
surface (the fence in `platform/TOOLING.md`); none may spawn subagents (PRINCIPLES #5) or judge
quality where a gate owns conformance. The map names only the engine's own deferral points and the
team's plays — never a pilot or domain.

| Deferral point | gstack play | constraint (so it stays inside the law) |
|---|---|---|
| SETUP (cold boot) | tool scan; `/guard` | `/guard` is an edit-lock harness, never a decision gate |
| Excavation (web/video deposits) | `/scrape`, `/browse`; Confusion → bench | MECHANICAL extraction only — haul the bounded space to addressable markdown, NO relevance filtering (selection is the assay's, deferred); ambiguous route → bench / logs/failures.md |
| Assay (seam sort) | Confusion Protocol → bench ONLY | NO `/spec`, `/review`, or `/autoplan` — the seam is the engine's own brain; a review/plan skill here contaminates the routing call. Any ambiguity benches |
| Iteration — pre-build | `/spec` ALWAYS; `/autoplan` CONDITIONAL | `/spec` is the craftsmanship floor, NOT the seam gate; `/autoplan` fires ONLY when the deliverable has real eng/design/DX surface — never on a trivial / pure-content build (M2W's MVP-first + done-gate already govern completeness; wire late, the subset needed) |
| Iteration — conformance | `/review` + `/codex` (cross-model); `/design-review` if visual | a SEQUENTIAL fresh-context evaluator pass (worker ≠ checker) checking schema CONFORMANCE + source-fidelity, never "is it good"; NO subagents / concurrent workers |
| Done-gate → ship | `/ship` or `/land-and-deploy` | only AFTER the done-gate fires (substance→surface = ship); never before |
| Loop boundary (after ship) | save-memory combo + gbrain push/query; `/context-save` + `/context-restore` | SESSION continuity ONLY — persist/recall via readable files at session end/start. This is NOT loop auto-continuation: the loop restarts solely on operator-supplied deposits (the loop-boundary deferral point, GATES.md §4) |

**Tools the team wields freely (NOT gated):** **ponytail** (code minimization — engine-maintenance
only, OFF during a content build), **LLMLingua** (context compression), **gbrain** (the optional
recall projection), the **memory skills**. These are instruments, not gates; the team reaches for them
whenever useful within any deferral point.

(This map was settled by deferring to gstack's own reviewed-plan voice — "who knows when gstack should
fire better than gstack" — and validated cross-model. See changelog 2026-06-30.)
