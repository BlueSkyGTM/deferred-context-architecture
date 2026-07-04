# reference/ — the factory (Layer 3)

The stable context this silo builds against: voice, design, conventions, domain knowledge. Configured
once at `setup`, unchanged across runs. This is internalized as *constraints and patterns* (write
like this, use these conventions), not processed as input — that is Layer 4 (`stages/*/output/`).

| Resource | Where | Contains |
|----------|-------|----------|
| Shared writing bar | `../../meta-seams/writing.md` | The prose standard every silo clears. Always applies. |
| [Silo voice] | `<file here>` | [voice beyond the shared bar] |
| [Design/format] | `<file here>` | [structure, house style for this deliverable] |
| [Domain skill] | `../skills/<name>/SKILL.md` | [bundled domain knowledge, if any] |

Keep it thin. A reference file the build stage does not name in its Inputs table is a file that
dilutes attention. Add only what a stage will actually load.
