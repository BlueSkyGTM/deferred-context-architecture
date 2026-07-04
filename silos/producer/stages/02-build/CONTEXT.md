# Stage 02: Build (the emitter)

Build the program that emits `task` records matching the keystone drawn in stage 01. One job.

## Inputs
| Source | File/Location | Scope | Why |
|--------|--------------|-------|-----|
| Drawn keystone | `../01-draw/output/` | full | the contract to emit against |

## Process
1. Write `output/produce.py`: emit `task` records as JSONL, one per line.
2. Every record carries exactly the keystone's fields (`id`, `title`, `done`): no extra, none missing.

## Outputs
| Artifact | Location | Format |
|----------|----------|--------|
| The emitter | `output/produce.py` | Python; prints JSONL to stdout |

## Do not
- Do not add fields the keystone does not define, or drop ones it requires.
- Do not reference the consumer silo. The two align only through the keystone.
