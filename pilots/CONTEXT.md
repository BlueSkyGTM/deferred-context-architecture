# CONTEXT.md — pilots/ (Instantiations, NOT Core)

The core (root docs, `platform/`, `stages/`, the holding folders, `logs/`) is **domain-agnostic**:
the operator supplies the domain. A **pilot** is one supplied domain — a concrete instantiation that
fills the extension points the core declares. The GTM-systems-curriculum pilot lives here; another
operator with another domain would add a sibling folder and the core would not change.

## The one law of this layer (ICM one-way references)

- A pilot **MAY** reference core (its contracts, schemas, gates, glossary).
- The core **MUST NEVER** reference a pilot. If a core file names "GTM", "curriculum",
  "wiki→course", a specific extractor, GBrain, or any domain content, that is a leak — flag it to
  `logs/failures.md` and move it here.
- **Deletion test:** remove `pilots/` entirely and the core must still stand and run (against a
  different pilot). If removing a pilot breaks the core, the boundary was violated.

## The extension points a pilot fills (declared by core)

| Core declares (interface) | Pilot supplies (instantiation) |
|---|---|
| Seam contract (`stages/02-assay/CONTRACT.md`) | `seam.md` — the domain boundary + its near-miss edges |
| Deposit/extractor contract (`stages/01-excavation/CONTRACT.md`) | `deposits.md` — where material lives + which extractor matches |
| Tool-surface policy (`platform/TOOLING.md`) | `tooling.md` — the concrete tools chosen for this domain |
| Iteration-workflow interface (`stages/04-iteration/`) | `iteration-workflow.md` — the concrete build chain |
| Evaluator policy (`stages/04-iteration/evaluator-rubric.md`) | the domain's conformance/source-fidelity rule |
| Validation ladder (`DRY-RUN.md`) | `dry-run.md` — the domain's reversible run + grading |
| Answer key + learned-seam outputs | `answer-key/`, `learned-seam/` |

Read `gtm-systems-curriculum/CONTEXT.md` for the one pilot that currently exists.
