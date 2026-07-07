# CONTEXT.md: silos/ (the pillars)

Each silo is one **pillar**: a self-contained ICM workspace that draws from the shared well
(`../vault`) and builds one kind of deliverable. Silos are independent, built in any order, in
parallel, none waiting on another.

**This layer is FROZEN as the proof record (restructure order executed 2026-07-06).** `producer`
and `consumer` are the two pillars of DCA's first operating history (`PROOF.md`), preserved exactly
as they ran so `../bin/join-check.py` re-verifies them forever. New operating work goes in
`../arms/` — see `../arms/CONTEXT.md`.

## Spin up a new silo
1. Copy `../_core/templates/silo/` to `silos/<name>/`.
2. Run `setup` in it (`setup/questionnaire.md`), configure the factory once: identity, voice,
   deliverable type, build stages. "Configure the factory, not the product."
3. Run its stages: `01-draw` pulls its slice from the well, later stages build. The deliverable lands
   in the final stage's `output/`.

## The one law of this layer (one-way references)
A silo reads only `../vault` (the well), `../_core`, and `../meta-seams`. **Never another silo. Never
does the well reach into a silo.** No cycles. This independence is the whole point: it is why you can
build silo B while silo A is half-done, and why finishing one never blocks another.

Deletion test: remove `silos/` and the well + `_core` still stand, a standing rig with a fillable
well, waiting for its first pillar.
