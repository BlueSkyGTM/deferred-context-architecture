# [Arm Name]

[One sentence: what this arm operates.] One arm of DCA, an independent operating branch: structurally
a self-contained ICM workspace that draws from the shared well (`../../vault`), plus the operating
discipline (runbook, done-when, decision log).

## Folder map

```
[arm-name]/
├── CLAUDE.md              (you are here, Layer 0)
├── CONTEXT.md             (start here for task routing, Layer 1)
├── runbook.md             (the arm cold-start: exact steps, re-runnable)
├── done-when.md           (the operator-supplied done metric; never invented)
├── decision-log.md        (three lines per decision; copied to well/exhaust on close)
├── setup/
│   └── questionnaire.md   (one-time: configure identity, voice, deliverable type)
├── reference/             (Layer 3, the factory: voice, design, conventions)
│   └── CONTEXT.md
├── shared/
│   └── identity.md        (who/what this arm produces, set at setup)
└── stages/
    ├── 01-draw/           (the contract draw: keystone reference, one-way, well only)
    ├── 02-[name]/         ([build stage])
    └── 0N-[name]/         ([final stage to deliverable in its output/])
```

## Triggers

| Keyword | Action |
|---------|--------|
| `setup` | Run `setup/questionnaire.md` once, configure the factory (identity, voice, deliverable type, default start stage). |
| `run` | Follow `runbook.md` top to bottom. Stop at any step that needs the operator. |
| `status` | Scan `stages/*/output/`. A stage with files (beyond .gitkeep) is COMPLETE, else PENDING. Check `done-when.md`. Render the pipeline line. |

## Routing

| Task | Go to |
|------|-------|
| Draw the contract + source from the well | `stages/01-draw/CONTEXT.md` |
| [Build task] | `stages/02-[name]/CONTEXT.md` |
| [Final task] | `stages/0N-[name]/CONTEXT.md` |
| Record a decision | `decision-log.md` (three lines, append-only) |

## What to load (minimal set per task: loading more dilutes quality)

| Task | Load these | Do NOT load |
|------|-----------|-------------|
| Run | `runbook.md`, `done-when.md` | other arms; any silo |
| Draw | `stages/01-draw/CONTEXT.md`, `../../vault/account.md` | the raw well; other arms; silos |
| Build | this stage's `CONTEXT.md`, `reference/`, `stages/01-draw/output/` | the whole well; unrelated stages |

## Laws (from `../../_core/CONVENTIONS.md` and `../CONTEXT.md`: do not restate, follow)

One-way refs: this arm reads only `../../vault`, `../../_core`, `../../meta-seams`. Never another
arm, never a silo. No connectors are granted. Deferral: draw only what a stage needs. Single-agent,
glass-box. No keystone enters this arm untested (`../../keystone-forge/FORGE.md`). The done-when is
the operator's; if you find yourself writing it, stop.
