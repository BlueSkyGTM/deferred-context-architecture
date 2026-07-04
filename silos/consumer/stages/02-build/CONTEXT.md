# Stage 02: Build (the reader)

Build the program that reads `task` records and reports on them, relying on the keystone drawn in
stage 01. One job.

## Inputs
| Source | File/Location | Scope | Why |
|--------|--------------|-------|-----|
| Drawn keystone | `../01-draw/output/` | full | the contract to read against |

## Process
1. Write `output/consume.py`: read `task` records as JSONL from stdin.
2. Rely on exactly the keystone's fields (`id`, `title`, `done`); reject any record that violates the
   contract, rather than guessing around it.

## Outputs
| Artifact | Location | Format |
|----------|----------|--------|
| The reader | `output/consume.py` | Python; reads JSONL from stdin, reports a summary |

## Do not
- Do not accept records that break the keystone. A silent workaround hides an integration failure.
- Do not reference the producer silo. The two align only through the keystone.
