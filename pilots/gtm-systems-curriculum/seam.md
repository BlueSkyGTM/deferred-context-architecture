# seam.md — The Seam for This Pilot (the GTM domain boundary)

The core defines the seam GENERICALLY (an operator-supplied domain boundary; on-seam / off-seam /
uncertain; necessarily incomplete; accretes via logged human calls — see
`stages/02-assay/CONTRACT.md`). This file supplies the CONCRETE boundary for the GTM-systems pilot.

## The domain
On-seam = **GTM systems engineering, civil-engineering-shaped**: assembling proven components into
load-bearing infrastructure that others run on. Off-seam = everything else, including material that
shares a principle with the domain but does not belong to it.

## The boundary is discovered, not authored
The seam starts **necessarily incomplete**. Boundaries are found by hitting them, not written up
front. On the pilot the HUMAN makes each cart/tailings/bench call and the system records it with its
reason (see core `platform/LOGS.md`); the seam layer accretes those calls into `learned-seam/`. It
is never "done"; it is "load-bearing" once escalations to the human are rare.

## The highest-value training data: looks-transferable-but-off-seam
The most valuable cases are material that **resembles** the GTM seam because it shares a DevOps /
platform-engineering principle but sits OFF it. Examples for this domain:
- An AI-engineering / LLM-systems curriculum fed in as if it were GTM (the deliberate blind control).
- Generic DevOps or platform-engineering patterns that are not GTM infrastructure.
- Software-engineering practices that share vocabulary ("pipeline", "deployment") but not the domain.

Tag these distinctly as `looks-transferable-but-off-seam` in `logs/rejections.md`. In this domain
they are roughly half of the wasted effort the seam layer exists to prevent. (This "~50%" is a
property OF this domain, observed on the pilot — not a core claim.)

## The negative-space control (for grading Run 1c)
The quarantined `answer-key/` holds the off-seam material the model must discover blind. The model
never sees the key; the human grades 1c against it. See `dry-run.md` Run 1c and `answer-key/`.
