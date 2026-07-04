# consumer (proof silo)

Reads `task` records (JSONL) and reports on them, relying on the shared keystone. One pillar of DCA —
a self-contained ICM workspace that draws from the shared well (`../../vault`) and builds one part.
Built independently of the producer; they align only through `../../vault/keystone-task.md`.

## Folder map

```
[silo-name]/
├── CLAUDE.md              (you are here — Layer 0)
├── CONTEXT.md             (start here for task routing — Layer 1)
├── setup/
│   └── questionnaire.md   (one-time: configure identity, voice, deliverable type)
├── reference/             (Layer 3 — the factory: voice, design, conventions)
│   └── CONTEXT.md
├── shared/
│   └── identity.md        (who/what this silo produces — set at setup)
└── stages/
    ├── 01-draw/           (draw the slice this silo needs from the well)
    ├── 02-[name]/         ([build stage])
    └── 0N-[name]/         ([final stage → deliverable in its output/])
```

## Triggers

| Keyword | Action |
|---------|--------|
| `setup` | Run `setup/questionnaire.md` once — configure the factory (identity, voice, deliverable type, default start stage). |
| `status` | Scan `stages/*/output/`. A stage with files (beyond .gitkeep) is COMPLETE, else PENDING. Render the pipeline line. |

## Routing

| Task | Go to |
|------|-------|
| Draw source from the well | `stages/01-draw/CONTEXT.md` |
| [Build task] | `stages/02-[name]/CONTEXT.md` |
| [Final task] | `stages/0N-[name]/CONTEXT.md` |

## What to load (minimal set per task — loading more dilutes quality)

| Task | Load these | Do NOT load |
|------|-----------|-------------|
| Draw | `stages/01-draw/CONTEXT.md`, `../../vault/account.md` | the raw well; other silos |
| Build | this stage's `CONTEXT.md`, `reference/`, `stages/01-draw/output/` | the whole well; unrelated stages |

## Laws (from `../../_core/CONVENTIONS.md` — do not restate, follow)

One-way refs: this silo reads only `../../vault`, `../../_core`, `../../meta-seams`. Never another
silo. Deferral: draw only what a stage needs. Single-agent, glass-box. Configure the factory, not the
product.
