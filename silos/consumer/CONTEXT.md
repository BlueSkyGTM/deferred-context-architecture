# [Silo Name]

[One sentence: what this silo covers.] Set up once (`setup`), then run any time.

## Task routing

| Task type | Go to | Description |
|-----------|-------|-------------|
| Draw source | `stages/01-draw/CONTEXT.md` | Pull the slice this silo needs from the shared well. |
| [Build] | `stages/02-[name]/CONTEXT.md` | [what this stage does] |
| [Final] | `stages/0N-[name]/CONTEXT.md` | [→ deliverable] |

## Shared resources

| Resource | Location | Contains |
|----------|----------|----------|
| Identity | `shared/identity.md` | Who/what this silo produces (set at setup). |
| Factory config | `reference/CONTEXT.md` | Voice, design, conventions — the Layer-3 factory. |
| Writing bar | `../../meta-seams/writing.md` | The shared prose standard every silo clears. |
| The well | `../../vault/account.md` | Catalogue of raw material available to draw. |
| Build laws | `../../_core/CONVENTIONS.md` | Five-layer routing, stage contract, one-way refs. |
