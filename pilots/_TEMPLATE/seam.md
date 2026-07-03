# seam.md — TEMPLATE (Claude Code defaults pre-filled; name YOUR system in every `<...>`)

The engine defines the seam GENERICALLY (operator-supplied boundary; on/off/uncertain; necessarily
incomplete; accretes via logged human calls — see `stages/02-assay/CONTRACT.md`). This file supplies
the CONCRETE boundary for ONE Claude Code system. The Claude Code defaults below hold for any pilot;
the `<...>` slots are yours.

## The system
`<Name the system and its declared capabilities — what it does, where it runs, who operates it.>`

On-seam = material that specifies or shapes THE ONE system under build: behavioral rules destined
for its CLAUDE.md, skill procedures and trigger phrasing, agent role definitions, hook trigger→action
pairs, MCP server configs and tool surfaces, workflow transcripts demonstrating the desired behavior,
schemas and conventions the system must conform to. `<Add your system's specific edges.>`

Off-seam = generic Claude Code documentation not specific to this system's behavior; deterministic
one-shot content with no operational afterlife (the engine-level scope guard, restated as a seam
default — see CLAUDE.md "What M2W is NOT for"); material for a *different* Claude Code system; prose
*about* AI agents rather than *for* this one. `<Add your system's specific exclusions.>`

## The boundary is discovered, not authored
The seam starts incomplete. On the first run the HUMAN makes each cart/tailings/bench call and the
system records it with its reason (core `platform/LOGS.md`); the seam layer accretes into
`learned-seam/`. It is "load-bearing" once escalations to the human are rare.

## Positive tests (the assay needs both — see the assay contract)
- on-seam test: the piece names or constrains a behavior this system must perform, traceable to a
  declared capability. `<Sharpen for your system.>`
- off-seam test: positive evidence the piece belongs to an identified other system or runtime, or is
  one-shot content with no recurring trigger. `<Sharpen for your system.>`
Neither passes cleanly -> bench.

## Highest-value training data: looks-transferable-but-off-seam
Defaults for any Claude Code system (tag these distinctly in logs/rejections.md):
- a well-written skill for ANOTHER system's workflow — right format, wrong behavior;
- generic prompt-engineering advice — shares the vocabulary, not this system's law;
- a transcript of a similar-but-different workflow;
- harness config for a different runtime (Cursor rules, GPT actions, Copilot instructions) that
  superficially resembles Claude Code artifacts.
`<Add your system's own near-miss patterns.>`

## Negative-space control (for blind grading)
`<Name the off-seam material you will quarantine in answer-key/ to grade the blind run. The model
never sees it.>`
