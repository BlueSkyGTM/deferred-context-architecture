# CONTEXT.md: vault/ (THE WELL)

The one shared well every silo draws from. Starts EMPTY and is correct when empty. Full contract:
`../_core/well-contract.md`.

Role: the shared source pool. Raw material enters ONE of two ways, **extracted** (pulled from a
located deposit) or **placed** (you drop it in), and is usable only once **addressed and accounted**
(a stable id + a row in `account.md`). Unaddressed material is the only error state; a raw pile with
no catalogue forces whole-well loading and defeats deferral.

The well is the ONLY entrance to DCA. Nothing is hand-placed into a silo to fake a draw. Silos read
the well (via `stages/01-draw`); the well never references a silo, that ignorance is what lets silos
be built in any order, in parallel, without collision.

Nothing is loaded from here speculatively (deferral): a silo follows the catalogue to the thin slice
it needs, never absorbs the pile. See `../_core/deferral.md`.
