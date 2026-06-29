# CONTRACT — Stage 02: Assay / Intake

## Purpose
Sort every piece of material from vault/ three ways by seam-fit. The system's primary deferral point
and the front half of MWP. Seam-fit is evaluated only when material arrives — never speculatively. An
assay is intrinsically THREE-way; this is not a feature, it is what assaying is.

## Inputs
- Raw addressed material in vault/.
- The seam definition (what belongs to this domain). On the pilot the seam is held by the human; the
  seam layer accretes from the human's calls. See ARCHITECTURE.md §2.2.

## Process (per piece)
1. Test seam-fit against known on-seam edges.
2. Route by the THREE-WAY rule below.
3. For tailings, write the curated reason to logs/rejections.md (item + reason, not verdict-only).
4. For bench, write the escalation context (what it is, which edges it was near, why uncertain).
5. Log the firing to logs/gate-checks.md (outcome: carted | tailed | benched).

## The three-way rule (mechanical) — each exit needs POSITIVE evidence
- CART  → carts/    : matched a known ON-SEAM edge with NO conflicting near-miss. Clean yes.
- TAILINGS → tailings/ : positive evidence of OFF-SEAM — it matches a known off-seam pattern or
  clearly belongs to an identified OTHER domain. Good material, wrong seam. Tail it WITH a reason.
- BENCH → bench/    : neither a clean on-seam match NOR positive off-seam evidence. ANY ambiguity
  benches. ANY conflicting near-miss benches.

The two failure tests are SEPARATE, and this is what keeps the bench from swallowing everything:
- Cart test: "matched a known on-seam edge with no conflicting near-miss, yes/no?"
- Tailings test: "is there POSITIVE evidence it is off-seam (a known off-seam pattern, or membership
  in another domain), yes/no?"
A clean yes on cart carts. A clean yes on tailings tails. Only the absence of BOTH benches. Tailings
is NOT "failed the cart test" — mere absence of an on-seam match is not evidence of off-seam; that is a
bench. You do NOT resolve ambiguity — you defer it to the bench. The bench is the third exit that lets
the pipeline run without committing to an uncertain call.

## Outputs
- carts/    : on-seam material, ready for transport.
- tailings/ : off-seam material, each item tailed with a reason (reviewable, never deleted).
- bench/    : uncertain material, escalated to the human.

## Deferral point
The assay IS the deferral point. Three exits. No fourth option. No guessing. No deleting (off-seam is
tailed, not destroyed). Uncertain commitment is deferred to the human via the bench.

## Instantiation note (training the seam)
On a domain's first run the HUMAN makes the cart/tailings/bench call and the system RECORDS each with
its reason. The seam layer is the OUTPUT of that run, not the tool it starts with. Tag the highest-
value cases distinctly: `looks-transferable-but-off-seam` (resembles the seam via a shared principle
but sits off it) — these are the cases the seam layer exists to catch. The concrete on-seam edges,
off-seam patterns, and near-miss examples are domain-specific and supplied by the instantiation (the
pilot's `seam.md`), NOT by core.

## TODO(tools)
The seam-matching tool (the seam brain) is wired in a LATER pass. For this pass, the assay routes by
HUMAN call and the structure (three exits, three folders, the reason-logging) is what you build.
Leave tool wiring as TODO(tools).

## Do not
- Do not collapse the three exits into two. The bench is non-negotiable.
- Do not delete off-seam material. Tail it with a reason.
- Do not resolve an uncertain call yourself. Bench it.
