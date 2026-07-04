# Stage 01 — Draw (the only bridge from the shared well into this silo)

Pull the slice of the well this silo needs — and only that. Deferred: draw what this run needs, not
the whole well. See `../../../../_core/well-contract.md` and `../../../../_core/deferral.md`.

## Inputs
| Source | File/Location | Scope | Why |
|--------|--------------|-------|-----|
| Well catalogue | `../../../../vault/account.md` | full | decide what exists to draw |
| The well | `../../../../vault/<id>` | only selected ids | the raw material this silo pulls |

## Process
1. Read the well catalogue (`vault/account.md`). Do NOT scan the raw well blind.
2. Select the slice this silo's deliverable needs (this silo's own call; the well makes none for it).
3. Copy ONLY the selected pieces into `output/`. Never copy the whole well.
4. Write `output/draw-manifest.md` — one row per drawn piece: `id | source | why-drawn`. This is the
   silo's own manifest (glass-box): what it drew from the well, and why.

## Outputs
| Artifact | Location | Format |
|----------|----------|--------|
| Drawn material | `output/` | the selected pieces, verbatim |
| Draw manifest | `output/draw-manifest.md` | table: id · source · why-drawn |

## Do not
- Do not pull material no later stage will use (deferral — draw thin).
- Do not edit the well. The well is shared and read-only from a silo.
- Do not reference another silo. Silos are independent.
