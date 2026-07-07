# CONTEXT.md: arms/ (the operating branches)

Each arm is one **independent operating branch**: structurally a silo (a self-contained ICM workspace
drawing from the shared well, `../vault`), plus the operating discipline that makes it runnable cold
and closeable clean. Arms are where DCA *operates*; `../silos/` is the frozen proof record and is not
extended. Restructure order executed 2026-07-06 (see `../RESTRUCTURE-STANDBY.md`).

## The four required pieces (an arm without all four is not an arm)

1. **Contract draw** — `stages/01-draw` pulls the keystone(s) and source slice this arm builds
   against: keystone reference, one-way, well only.
2. **Runbook** — `runbook.md`, the exact steps re-runnable from a cold start.
3. **Done-when** — `done-when.md`, the operator-supplied metric. A session never invents or edits it.
4. **Decision log** — `decision-log.md`, three lines per decision, copied to `../vault/exhaust/`
   when the arm closes.

## Spin up a new arm

1. Copy `../_core/templates/arm/` to `arms/<name>/`.
2. Operator fills `done-when.md` (the arm does not run without it).
3. Run `setup` in it (`setup/questionnaire.md`), configure the factory once.
4. Operate by `runbook.md`: draw, build, close against the done-when.

## The laws of this layer

- **One-way references.** An arm reads only `../vault` (the well), `../_core`, and `../meta-seams`.
  Never another arm. Never a silo. Never does the well reach into an arm. No cycles.
- **No connectors.** No connector permissions are granted to arms (operator decision, 2026-07-06).
  If an arm needs one, the operator grants it explicitly, in-session, recorded in the arm's
  decision log.
- **No keystone enters an arm untested.** Contracts are authored and validated in
  `../keystone-forge/` first (see FORGE.md). In THIS repo keystones never deploy into arms at all —
  deployment happens only in the DRA clone (`../RESTRUCTURE-STANDBY.md`, sequencing).
- **The operator's three touchpoints (stake / cut / sign) stay the operator's.** If a session finds
  itself performing one on the operator's behalf: stop.

Deletion test: remove `arms/` and the well + `_core` + the proof still stand.
