# _core/well-contract.md: the shared well (vault/) and the well-to-silo handoff

The **well** is the one shared vault every silo draws from. It is the only shared holding place in
DCA. Many silos, one well.

## How material enters the well (one door)

Raw material enters `vault/` exactly two ways:

1. **Extraction**, pulled from a located deposit (a repo, docs, a transcript, a page) into `vault/`.
2. **Placement**, you drop it in directly.

Either way, a piece is not usable until it is **addressed and accounted**: it has a stable id and a
row in `vault/account.md` (the catalogue). Unaddressed material is invisible to silos, a raw pile
with no catalogue forces whole-well loading, which defeats deferral. Address what you place, or let
an extraction pass address it.

`vault/` is the **only** entrance. Nothing is hand-placed into a silo's `output/` to fake a draw,
that would skip the catalogue and break glass-box. All material routes through the well.

## The catalogue: `vault/account.md`

One row per piece: `id | source | addressed | descriptor`. This is the shared manifest of what the
well holds. Silos read it to decide what to draw; they never scan the raw well blind.

## The well to silo handoff (deferred draw)

A silo's `stages/01-draw` is the only bridge from the shared well into a silo:

1. Read `vault/account.md`.
2. Select the slice this silo's deliverable needs (its own call, a silo may apply its own selection
   rules; the well makes none for it).
3. Pull ONLY those pieces into `stages/01-draw/output/`, and write `draw-manifest.md` recording
   what was drawn and why (glass-box; the silo's own manifest, roots sense: draw a manifest from the
   well, then build the workspace).

The well never references a silo (one-way). It does not know who drew what; it just holds and
catalogues. That ignorance is what lets silos be built in any order, in parallel, without collision.
