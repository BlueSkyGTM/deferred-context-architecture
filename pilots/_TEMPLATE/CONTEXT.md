# CONTEXT.md — _TEMPLATE (the pilot contract — copy this into your system's project)

This repo is the engine; its domain is fixed (Claude Code powered systems). A **pilot** is ONE such
system commissioned for building, and pilots are system-specific, so they live in **their own
projects**, not here. This `_TEMPLATE/` is the CONTRACT: the extension points your pilot must fill,
pre-filled with Claude Code defaults where a default is safe. Copy it into your project, rename it to
your system, keep what fits, and fill each `<...>` slot. The engine never references your pilot; your
pilot references the engine.

## The one law (ICM one-way references)
- Your pilot MAY reference core (its contracts, schemas, gates, glossary).
- Core MUST NEVER reference your pilot. Deletion test: the engine must stand with no pilot present.

## Extension points your pilot must supply
| You provide | Fills the core interface | Shipped default |
|---|---|---|
| `seam.md` | the assay's seam (`stages/02-assay/CONTRACT.md`) — your system's on-seam/off-seam edges | Claude Code system defaults pre-filled; name YOUR system's edges |
| `deposits.md` | the excavation inputs (`stages/01-excavation/CONTRACT.md`) — your sources + extractor matching | typical deposit types pre-filled; register rows are yours |
| `tooling.md` | your SYSTEM-specific tools (the universal tools, incl. the Claude Code toolchain, are core; see `platform/TOOLING.md`) | guidance pre-filled |
| `iteration-workflow.md` | the concrete build chain (`stages/04-iteration/iteration-workflow.md`) | the default Claude Code build chain; override per system |
| `dry-run.md` | your validation ladder (`DRY-RUN.md`) — the reversible first run + grading | the default ladder shape; your sub-runs are yours |
| `design-schema.md` | the quality cookie-cutter (cut during schema-discovery iteration 1) | stub only — earned, never pre-filled |
| `answer-key/` | the quarantined grading key for blind-discovery (the model never reads it) | not shipped — per pilot |
| `learned-seam/` | where the seam's training accretes (the OUTPUT of your first run) | not shipped — per pilot |

The defaults are interface, not earned judgment. Anything a deferral point owns (the schema, the
learned seam, the answer key) stays empty until the run that produces it.

## Required shapes (so the handoffs match the engine)
- **seam.md** — on-seam definition; off-seam patterns; the highest-value `looks-transferable-but-off-seam`
  cases. The assay needs BOTH a positive on-seam test and a positive off-seam test (see the assay
  contract); supply both.
- **deposits.md** — a register row per source: `deposit_id | source | type | bounded_space | extractor
  | status`, and a deposit-type → extractor table whose left column matches your `type:` enum exactly.
- **tooling.md** — a manifest table the core Tool scan reads:
  `| tool | role/stage slot | required | detect (shell test) | install (shell cmd) |`. Flag anything
  whose install you can't state safely as `MISSING-ASK` (never guess an install).
- **design-schema.md** — declare its path here; the schema-discovery iteration writes it.

Read `pilots/CONTEXT.md` for how this layer relates to the engine.
