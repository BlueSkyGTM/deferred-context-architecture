# CONTEXT.md — Pilot: GTM-Systems Curriculum

The first instantiation of the M2W core. Chosen because it is **reversible** (no live leads, nothing
that cannot be taken back), which makes it safe ground to train and grade the seam before any live
work. This folder supplies every domain-specific decision; the core stays agnostic.

Read order for this pilot:
1. `pilot.md`            — what this pilot is, why it was chosen, the reversibility asterisk.
2. `seam.md`             — the domain boundary (what is on-seam vs off-seam) + the near-miss edges.
3. `deposits.md`         — where the raw material lives and which extractor matches each deposit type.
4. `tooling.md`          — the concrete tools chosen for this domain (the gstack fence applied).
5. `iteration-workflow.md` — the concrete build chain (sources → wiki → graph → course).
6. `dry-run.md`          — the validation ladder for this pilot (the 1a→1c curriculum loop).
7. `answer-key/`         — the quarantined corpus used to grade Run 1c (the model never sees it).
8. `learned-seam/`       — where the seam's training (assay calls + reasons) accretes.

This pilot references core; core never references it (see `pilots/CONTEXT.md`). If the core ever
needs something this pilot has, that is an extension point the core should declare generically — not
a reference back into here.
