# setup/questionnaire.md — configure this silo once (the factory, not the product)

Run this ONCE when a silo is first stood up. It configures the Layer-3 factory: the stable
preferences every future run of this silo inherits. It does NOT produce a deliverable — that is what
running the stages does, later, per run.

Fill each answer into the files named, then delete the `<...>` prompts.

## 1 — Identity → writes `shared/identity.md`
- What does this silo produce? `<one deliverable type — e.g. a book, a course, a report, a system>`
- Who is it for / who authors it? `<audience + author voice>`
- Default start stage? `<usually 01-draw>`

## 2 — Voice & conventions → writes `reference/CONTEXT.md` (+ files it points to)
- Voice rules beyond the shared bar (`../../meta-seams/writing.md`)? `<silo-specific voice>`
- Design/format conventions for the deliverable? `<format, structure, house style>`
- Any domain skills to bundle under `skills/`? `<name them, or none>`

## 3 — The build stages → names `stages/02…0N`
- What are this silo's build stages, in order, one job each? `<name them>`
- Rename the `02-[name] … 0N-[name]` folders to match, and write each stage's `CONTEXT.md` to the
  contract shape in `../../_core/CONVENTIONS.md`.

## 4 — The staking rule (carried by every build stage)
- Name the ONE thing each deliverable unit is staked on. Everything not serving that is **cut, not
  shrunk.** Even coverage is the enemy; a unit that tries to matter everywhere matters nowhere.
  Write this into each build stage's Process so it is enforced per unit, not hoped for.
