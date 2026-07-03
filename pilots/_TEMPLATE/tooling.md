# tooling.md — TEMPLATE (your SYSTEM-specific tools only; the Claude Code toolchain is core)

The UNIVERSAL tools (harness, the claude CLI itself, skill-creator/skill-auditor, cross-model review,
retrieval, the evaluator method, the standing skills) are pilot-independent and live in the engine:
`platform/TOOLING.md` (universal manifest). Do NOT re-declare them here. This file declares the tools
that are specific to YOUR system — typically: the governed repo's own toolchain (test runner, linter —
needed to validate that hooks fire correctly), any MCP servers the system wires (authenticated ones
are always `MISSING-ASK`), and any extra extractors your deposit types need.

The core Tool scan (`platform/TOOLING.md` → "Tool scan protocol") reads this table, detects each,
installs the safe/known-missing ones, and FLAGS the rest `MISSING-ASK` (never guesses an install).

## System tool manifest (fill in; delete the example rows)
| tool | role / stage slot | required | detect (shell test) | install (shell cmd) |
|---|---|---|---|---|
| `<the governed repo's test runner>` | iteration: validate hook/skill behavior | if the system has hooks/tests | `<detect>` | `<install, or MISSING-ASK>` |
| `<an MCP server the system wires>` | iteration: the system's tool surface | if the system uses it | `<detect>` | `MISSING-ASK (auth is machine-specific)` |

## Pilot-woken gstack plays (optional)
The core gate→play map in `platform/SKILLS.md` is the universal DEFAULT, and it is OPEN. If your
system warrants gstack plays that are dormant in the core map, declare them here — which play, at
which deferral point, and the system surface that warrants it. They wake under the SAME invariants
(single-agent; conformance-not-quality; nothing at the assay; no subagents at conformance; the loop
boundary stays session-continuity). Delete the example rows.

| gstack play | deferral point | warranted because (the system surface) |
|---|---|---|
| `/qa` | iteration — conformance | the system has a web surface |
| `/skillify` | iteration — build | the system codifies a proven browse flow into a skill |

Only the parallel/multi-agent plays (`/pair-agent`, Conductor, sub-agents) can NEVER be woken — they
violate the single-agent law (PRINCIPLES #5).

## Rules
- `required` extractors are conditional on the deposit types in your `deposits.md` — only the ones a
  run actually needs are required for that run (engine policy: wire the subset a run needs).
- If you cannot state a safe install command, write `MISSING-ASK` — do not guess.
- The scan writes the per-machine result to your pilot's `tool-status.md` (regenerated each scan).
