# [Arm Name]

[One sentence: what this arm covers.] Set up once (`setup`), then operated by runbook, against a
done-when the operator supplies.

## Task routing

| Task type | Go to | Description |
|-----------|-------|-------------|
| Run the arm | `runbook.md` | The cold-start steps, top to bottom. |
| Draw contract + source | `stages/01-draw/CONTEXT.md` | Pull the keystone + slice this arm needs from the shared well. |
| [Build] | `stages/02-[name]/CONTEXT.md` | [what this stage does] |
| [Final] | `stages/0N-[name]/CONTEXT.md` | [to deliverable] |
| Record a decision | `decision-log.md` | Three lines per decision, append-only. |

## Shared resources

| Resource | Location | Contains |
|----------|----------|----------|
| Done metric | `done-when.md` | The operator-supplied done condition for the current objective. |
| Identity | `shared/identity.md` | Who/what this arm produces (set at setup). |
| Factory config | `reference/CONTEXT.md` | Voice, design, conventions, the Layer-3 factory. |
| Writing bar | `../../meta-seams/writing.md` | The shared prose standard every arm clears. |
| The well | `../../vault/account.md` | Catalogue of raw material available to draw. |
| Build laws | `../../_core/CONVENTIONS.md` | Five-layer routing, stage contract, one-way refs. |
| Keystone law | `../../keystone-forge/FORGE.md` | No keystone enters an arm untested. |
