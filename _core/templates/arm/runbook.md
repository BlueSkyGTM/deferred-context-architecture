# runbook.md: [arm name] (re-runnable cold)

The exact steps to run this arm from a cold start, no session memory assumed. If a step needs
judgment, it names whose (operator) and where the answer gets written. Filled at setup; updated
whenever a run reveals a missing step.

## Preconditions
- [ ] `done-when.md` is filled (an arm without a done-when does not run)
- [ ] The keystone(s) this arm draws are marked `tested:` (see `../../keystone-forge/FORGE.md` — no keystone enters an arm untested)
- [ ] [tool / material preconditions]

## Steps
1. Draw: run `stages/01-draw` — pull only what this run needs from the well (`../../vault/account.md`).
2. [build steps, one line each, in order]
3. Close: check the output against `done-when.md`; log the run's decisions in `decision-log.md`;
   on arm close, copy the decision log to `../../vault/exhaust/`.

## Failure handling
- [what to do when a step fails; where the failure is recorded]
