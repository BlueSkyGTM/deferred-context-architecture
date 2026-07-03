# CONTEXT.md — pilots/ (the pilot CONTRACT, not pilots)

This repo is the engine, and its domain is fixed: it builds **Claude Code powered systems**. A
**pilot** is one such system commissioned for building — a skill suite, an agent, a hook set, MCP
wiring, a CLAUDE.md-governed repo, or a combination. Pilots are system-specific, so they live in
**their own projects** — not in this engine repo. What ships here is `_TEMPLATE/`: the CONTRACT a
pilot must satisfy, pre-filled with Claude Code defaults. A pilot project copies the template,
renames it to its system, and fills the remaining `<...>` slots.

## The one law of this layer (ICM one-way references)
- A pilot MAY reference core (its contracts, schemas, gates, glossary).
- The core MUST NEVER reference a specific pilot. Deletion test: this engine stands with NO pilot
  present — a standing factory for Claude Code systems, waiting for its next commission. That is the
  normal state of this repo.

## The extension points a pilot fills (declared by core; defaults shipped in `_TEMPLATE/`)
| Core declares (interface) | Pilot supplies (in its own project) |
|---|---|
| Seam contract (`stages/02-assay/CONTRACT.md`) | the ONE system's boundary + near-miss edges (defaults: `_TEMPLATE/seam.md`) |
| Deposit/extractor contract (`stages/01-excavation/CONTRACT.md`) | where material lives + which extractor matches (defaults: `_TEMPLATE/deposits.md`) |
| Universal tool policy + scan (`platform/TOOLING.md`) | the SYSTEM-specific tools (the Claude Code toolchain is universal, core) |
| Iteration-workflow interface (`stages/04-iteration/`) | the concrete build chain (default: `_TEMPLATE/iteration-workflow.md`) |
| Validation ladder (`DRY-RUN.md`) | the system's reversible run + grading (default shape: `_TEMPLATE/dry-run.md`) |
| Logs / manifest / gates | (used as-is; nothing to supply) |

The template's pre-filled content is INTERFACE plus defaults, not earned judgment: `design-schema.md`
stays a stub until schema-discovery cuts it; `answer-key/` and `learned-seam/` are named by the
contract but produced per pilot — earned, not given.

Read `_TEMPLATE/CONTEXT.md` for the full contract and the required shapes. There is intentionally no
concrete pilot in this repo; the engine is what you are looking at.
