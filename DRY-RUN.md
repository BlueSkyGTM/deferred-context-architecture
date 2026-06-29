# DRY-RUN.md — The Validation Ladder (generic interface)

The only way to know whether the open items work is to RUN the pipeline. A run is staged by FIDELITY
and CONSEQUENCE: each pass carries more consequence than the last. This is M2W applied to its own
validation — **defer consequence, not just execution.** This file defines the generic ladder; a
concrete run (its domain, material, and grading) is an instantiation detail — see
`pilots/<name>/dry-run.md`.

## The two staging axes
- **Fidelity** — how close the run is to the real thing. Start with a stand-in that exercises the
  walls (flow, the three assay exits, the gates, the logs) before the real material.
- **Consequence** — how reversible a wrong call is. Start where a wrong call costs a thrown-out dig,
  not a burned irreversible action.

## The reversible-first law (why the first pass is reversible ground)
A seam (or any learned component) must act AUTONOMOUSLY on REVERSIBLE ground BEFORE it touches
anything irreversible. Without that, the first time the component acts on its own is on live,
irreversible work — backwards. So the ladder's early passes are deliberately reversible: the
DELIVERABLE is throwable, even though the LEARNING is sticky. Because the learning persists, the
between-pass AUDITS are REQUIRED, not optional — bad training carries forward.

## The apprenticeship shape (watch → propose → act)
Autonomy is earned across a LOOP, not granted in one run. A learned component progresses:
1. **Watch / train** — the human makes every call; the system logs each WITH its reason. The
   component records, does not act. AUDIT: are the calls consistent and the reasoning generalizable
   (not a per-item blacklist)? Correct bad training now.
2. **Propose / correct** — the component proposes; the human confirms or corrects. Corrections are the
   highest-value training. AUDIT: did corrections drop? If it is still wrong on settled cases, do not
   advance.
3. **Act / grade (blind)** — the component acts autonomously on material it has not seen, graded
   against a QUARANTINED answer key the human holds and the component does NOT. Still reversible.
   PASS CONDITION: it handles blind material correctly with rare escalation to the bench.

Only after the blind grade holds does a run advance to LIVE, irreversible work — and even then it is
not the component's first autonomous act, which was the entire point of the loop.

## What a run exists to answer (not to-do items)
A run produces evidence the spec deferred: whether conformance-by-shape holds (first tested when
material flows the gates), whether the done-gate's substance-to-surface signal fires, whether the
learned component discovers the boundary blind. These are BLOCKED-ON-RUN: waiting on evidence, not
unfinished work. The instantiation lists its own.

## The instantiation supplies the concrete ladder
An instantiation's concrete ladder — its watch/propose/act sub-runs, its blind-discovery experiment,
its answer key, its live pass — lives in `pilots/<name>/dry-run.md`. Nothing in this core file names a
specific domain; the pilot does.
