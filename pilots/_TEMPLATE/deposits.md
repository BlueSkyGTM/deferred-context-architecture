# deposits.md — TEMPLATE (your sources + extractor matching; typical types pre-filled)

The excavation contract (`stages/01-excavation/CONTRACT.md`) takes located deposits and a bounded
space from the pilot. This file is that register. The deposit-type → extractor table below is the
typical set for building a Claude Code system; keep what applies, add what your system needs. The
left column of the table must match your register's `type:` enum exactly.

## Deposit register (one row per source; fill in)
| deposit_id | source | type | bounded_space | extractor | status |
|---|---|---|---|---|---|
| `<d-001>` | `<path or URL>` | `<type from the table below>` | `<what counts as "the whole deposit">` | `<from the table below>` | `<located / excavated>` |

## Deposit-type → extractor table (defaults for a Claude Code system build)
| type | what it is | extractor |
|---|---|---|
| existing-repo | the codebase the system will govern or extend | direct file read (glob; no install) |
| docs | Claude Code docs pages, schema references, API refs | trafilatura (web) / markitdown (pdf, office) |
| transcript | session transcripts demonstrating the target workflow | direct read / markitdown |
| skill-library | existing skills/agents/hooks mined for patterns | direct file read |
| video | walkthroughs / demos of the desired behavior | youtube-transcript |

Extractor availability is the Tool scan's job (`platform/TOOLING.md`); only the extractors your
deposit types actually need are required for a run.
