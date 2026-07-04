# producer

Emits `task` records that conform to the shared keystone. Two stages: draw the keystone, then build
the emitter.

## Task routing

| Task type | Go to | Description |
|-----------|-------|-------------|
| Draw source | `stages/01-draw/CONTEXT.md` | pull the keystone from the shared well |
| Build | `stages/02-build/CONTEXT.md` | build `produce.py`, the emitter |

## Shared resources

| Resource | Location | Contains |
|----------|----------|----------|
| Identity | `shared/identity.md` | what this silo produces |
| The keystone | `../../vault/keystone-task.md` | the contract this silo emits against |
| Build laws | `../../_core/CONVENTIONS.md` | five-layer routing, the stage contract, one-way refs |
