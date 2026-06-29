# dry-run.md — This Pilot's Validation Ladder (curriculum loop → live GTM)

The core defines the validation ladder GENERICALLY (stage runs by fidelity and consequence; defer
consequence, not just execution — see core `DRY-RUN.md`). This file supplies the CONCRETE ladder for
the GTM-curriculum pilot: the reversible curriculum loop that trains and grades the seam before any
live, irreversible work.

## Why Pass 1 is a LOOP, not a single run
The apprenticeship is watch → propose → act. ONE run cannot contain it. So Pass 1 is the curriculum
RE-RUN — the same reversible domain, the seam taking over progressively across sub-runs. The loop IS
the apprenticeship. Without it, the FIRST time the seam acts autonomously would be on live,
irreversible GTM (Pass 2) — backwards. The seam must act autonomously on REVERSIBLE ground first.

## Pass 1 scoping (do not over-load)
Wire ONLY:
- the core skeleton + logs (built)
- ONE excavation extractor (matched to the deposit type — see `deposits.md`)
- the manifest + frontmatter (core stage 03)
- iteration with this pilot's capstone workflow + evaluator (`iteration-workflow.md`; Accept/Revise/Block)
- context-compressor + memory-manager writing to READABLE files
Do NOT wire the full tool set. If everything is loaded and something breaks, the failure could be the
maze OR any of several tools — an undiagnosable haystack. Test the walls first.

## PASS 1 — CURRICULUM-MAZE (a loop)

### Run 1a — HUMAN CALLS (train)
- The HUMAN makes every cart/tailings/bench call; the system logs each WITH its reason.
- Tests the walls (flow excavation→assay→manifest→iteration; the three assay exits; the gates; the
  logs) AND produces the seam's training data. The seam does NOT act here; it watches and records.
- **AUDIT (required before advancing):** read `learned-seam/`. Are the human's calls consistent? Is
  the reasoning capturable and generalizable (not a per-item blacklist)? Correct bad training now.

### Run 1b — SEAM PROPOSES (correct)
- The seam (holding 1a's training) PROPOSES a verdict per piece; the human confirms or corrects.
- Corrections are the highest-value training — they mark the boundary the seam got wrong.
- **AUDIT (required):** did corrections drop vs 1a? If the seam is still wrong on SETTLED cases, stay
  in 1b, re-run, do not advance.

### Run 1c — SEAM ACTS, BLIND (grade)
- The seam acts AUTONOMOUSLY. The human spot-checks; does NOT pre-approve each call.
- **The BLIND-DISCOVERY experiment runs here:** feed material the seam has not seen — including the
  AI-engineering curriculum fed as if it were GTM — and require the seam to discover the negative
  space by reasoning. Grade against the QUARANTINED `answer-key/` (the key the human holds, the model
  does NOT).
- Still reversible — a wrong call costs a thrown-out dig.
- **PASS CONDITION:** the seam sorts blind material correctly against the key, with rare escalation to
  the bench. Only then is the seam trusted. If it carts an off-seam item or benches everything, return
  to 1b.

## PASS 2 — LIVE GTM (live, gated on 1c)
Live, irreversible (touches real leads/systems). Details deferred. Runs ONLY after 1c holds. Because
the seam already acted autonomously on reversible ground in 1c, Pass 2 is NOT the seam's first
autonomous act — the entire point of the loop. This is where operational-GTM (currently tailed
off-seam) becomes on-seam.

## BLOCKED-ON-RUN (questions the run exists to answer — not to-do items)
- gtm-starter-kit fold into the seam corpus (fold before 1a ONLY if it is answer-key material; else
  deferred — see `deposits.md`).
- GBrain vs Understand-Anything final ingest split (needs a wiki produced in the loop to test GBrain).
- the seam layer itself (it is the OUTPUT of the 1a→1c loop, not an input).
- whether conformance-by-shape holds (first tested when material flows the gates, 1a).
- whether the done-gate's substance-to-surface signal fires correctly (first tested across iterations).
- whether the seam discovers the boundary BLIND (the 1c experiment).
