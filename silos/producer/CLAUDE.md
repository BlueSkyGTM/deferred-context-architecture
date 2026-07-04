# producer (proof silo)

Emits `task` records (JSONL) that conform to the shared keystone. One pillar of DCA: a self-contained
workspace that draws from the shared well (`../../vault`) and builds one part. Built independently of
the consumer; the two align only through `../../vault/keystone-task.md`, never by referencing each
other.

## Folder map

```
producer/
├── CLAUDE.md              (you are here: where am I)
├── CONTEXT.md             (task routing: where do I go)
├── shared/
│   └── identity.md        (what this silo produces)
└── stages/
    ├── 01-draw/           (draw the keystone from the well)
    └── 02-build/          (build produce.py: the emitter)
```

## Routing

| Task | Go to |
|------|-------|
| Draw from the well | `stages/01-draw/CONTEXT.md` |
| Build the emitter | `stages/02-build/CONTEXT.md` |

## Laws (from `../../_core/CONVENTIONS.md`)

One-way references: this silo reads only `../../vault`, `../../_core`, `../../meta-seams`, never
another silo. Deferral: draw only what a stage needs. Single-agent, glass-box.
