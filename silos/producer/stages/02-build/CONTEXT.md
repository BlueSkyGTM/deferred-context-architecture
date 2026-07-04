# Stage 02 — [Build] (rename per this silo's setup; one stage, one job)

Template build stage. A silo names its real build stages at `setup` and writes each to this shape.
Reads the drawn material (Layer 4) + the factory (Layer 3); produces the next artifact. One job only.

## Inputs
| Source | File/Location | Scope | Why |
|--------|--------------|-------|-----|
| Drawn material | `../01-draw/output/` | this run | what to build from |
| Factory | `../../reference/CONTEXT.md` | as named | voice, design, conventions |
| Writing bar | `../../../../meta-seams/writing.md` | full | the prose standard |

## Process
1. Build the artifact from the drawn material — source-pinned: contains only what the draw supports,
   nothing invented outside it.
2. **Staking rule (enforced per unit, not hoped for):** each unit declares the ONE thing it is staked
   on. Everything not serving that is **cut, not shrunk.** Even coverage is the defect — a unit that
   tries to matter everywhere matters nowhere. Rank the claims; keep the top; cut the rest.
3. Clear the prose against the writing bar.

## Outputs
| Artifact | Location | Format |
|----------|----------|--------|
| [Built artifact] | `output/` | [format] |

## Do not
- Do not invent facts the drawn material does not support (source-pinning).
- Do not shrink a weak unit to keep it — cut it. Perfection is subtraction, not padding.
