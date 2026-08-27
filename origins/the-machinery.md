# The machinery

Every piece of ICM's apparatus, with a verdict. Three verdicts only: **inherited** unchanged,
**amended** with the reason, or **does not apply** with the reason.

Nothing goes unlisted. A pattern with no verdict here is a defect, because an unlisted pattern is
one nobody decided about, and the two methods drift apart quietly rather than deliberately.

Sources are `icm-upstream/_core/CONVENTIONS.md` for the numbered patterns and
`icm-architect/` for the forms, the invariants and the walk test.

## The numbered patterns

| Pattern | Verdict |
|---|---|
| 1, Stage Contracts | **Inherited.** Inputs, Process, Outputs is the shape of an emitted `CONTEXT.md` here |
| 2, Handoffs via `output/` | **Amended.** See below |
| 3, One-Way Cross-References | **Inherited, and strengthened.** The wall makes a back-reference unreachable rather than merely discouraged |
| 4, Selective Section Routing | **Inherited.** Naming a section rather than a file keeps a payload narrow, which matters more here because the payload is the only thing an agent gets |
| 5, Canonical Sources | **Inherited.** One home per fact. An emitted contract is the only home for facts about its folder, not a second one |
| 6, CONTEXT.md is routing, 25 to 80 lines | **Amended.** See below |
| 7, Tool Prerequisites | **Inherited** unchanged |
| 8, Questionnaire Design | **Inherited**, and extended by a second intake. See below |
| 9, Bundled Skills | **Inherited**, including its exclusion: never bundle skills that are about Claude Code itself. That is why the workflow skill here is installed rather than bundled |
| 10, Specs Are Contracts | **Inherited.** What and when, not how, with freedom inside the quality floor. It is the clearest existing statement of what an issued `CONTRACT.md` is |
| 11, Checkpoints | **Amended.** See below |
| 12, Stage Audits | **Inherited.** It is the agent-side check in `../mechanics/acceptance.md` |
| 13, Value Validation | **Does not apply by default.** It is a content-workspace device. A wing whose product is content may adopt it; nothing here depends on it |
| 14, Docs Over Outputs | **Inherited**, and it is the argument for the promotion gate |
| 15, Shared Constants | **Inherited** for wings that produce code. Pattern 5 applied to values |

### Pattern 2, amended

ICM's handoff points up and over into the previous stage's output folder, which crosses a folder
boundary. Here the working directory is the wall, so that path is a breach by default.

It stays legal in exactly one case: a **declared relay**, where one card's output is the next
card's input by design, per `../mechanics/tiering.md`. Declared, because the difference between a
relay and a leak is whether someone wrote it down. `../tools/audit.py --relay` is where that
declaration is honoured.

### Pattern 6, amended

The 25-to-80-line routing rule governs the **emitted** `CONTEXT.md`, which is a stage contract
and is bound by it.

It does not govern an issued `CONTRACT.md`. That is a different artifact carrying an outcome
statement and audits, and holding it to a routing-only rule would strip the two things it exists
to say. `../mechanics/the-two-documents.md` holds the distinction.

### Pattern 11, amended

A checkpoint pauses mid-run so a human can steer. **A woken agent has no channel to a human
mid-run.** It is in a folder, alone, and the only thing it can do when it meets what its contract
does not cover is stop.

So a checkpoint keeps its full meaning for the core and for a stage a person runs, and for a
woken agent it becomes `escalate`: stop, write what is missing, exit. Not a pause, because
nothing is listening.

### Pattern 8, extended

Inherited whole for `setup`: flat, one pass, system level only, derive rather than ask, sensible
defaults, examples over descriptions, asked once and never again.

A second intake is added rather than replacing it. **`intake` asks once per session** and
produces a written deck of cards rather than configuring the workspace. One substitution in the
rules, everything else identical.

Its placeholder sweep is inherited with teeth added: ICM completes setup only when zero `{{`
patterns remain. Here, **a card carrying an unfilled placeholder is not playable**, which rung
zero enforces rather than a person noticing.

## The five layers, restated

Inherited in substance, restated because ICM's version assumes one reader and there are two.

| Layer | ICM | Here |
|---|---|---|
| 0, entry file | where am I | the core's. An agent never sees it |
| 1, root router | where do I go | the core's. An agent never sees it |
| 2, stage contract | what do I do, the control point | **splits in two**: an issued `CONTRACT.md` and an emitted `CONTEXT.md` |
| 3, reference | what rules apply | reachable only inside the folder, or where a charter names the path |
| 4, working artifacts | what am I working with | unchanged |

The core reads zero and one and never two. An agent reads two and below and never zero or one.
That is the whole of what two readers changes, and it changes nothing about the layers
themselves.

## Triggers, naming, placeholders, guardrails

| Item | Verdict |
|---|---|
| `setup` trigger | **Inherited** |
| `status` trigger | **Inherited, extended.** It scans `output/` folders for stage state as upstream specifies, and also reads the board for card state |
| Naming, `lowercase-with-hyphens`, `NN-` prefixes | **Inherited, and this settled a conflict.** The vendored skill says `NN_kebab` with an underscore; upstream says `01-`. They disagree. This method follows upstream as the current source, and `templates/CONTEXT.md` was corrected on 2026-08-26 |
| Placeholders `{{SCREAMING_SNAKE}}` | **Inherited** whole |
| Guardrails: contracts under 80 lines, references under 200 | **Inherited**, scoped to what a binding might carry. A front door, an argument and a dated ledger are none of those, per `icm-upstream/VENDORED.md` |
| Guardrail: no em dashes | **Inherited.** The repository already contained zero before it was written down |
| Generated indexes never hand-edited | **Inherited**, and it is why `ROUTER.md` is rebuilt and compared rather than curated |

## From the skill rather than the repository

| Item | Verdict |
|---|---|
| Ten invariants | **Inherited.** The per-invariant reading is in `divergence.md` |
| Five forms | **Reduced to one.** The umbrella is the only form with more than one wall in it, and deferral needs plurality of bounded domains. The other four are not defective; they have no gap this method fits into. `divergence.md` argues it |
| The walk test | **Inherited for the core, insufficient alone.** It validates that a reader can navigate to the work. An agent here does not navigate, it arrives, so the companion test is `../mechanics/writing-for-an-unknown-reader.md`: can a reader that has never seen the host system produce the named output from the folder and the card alone |
| Build and restructure modes | **Inherited** as the shape of `dca-architect`, minus the form-selection step, which no longer exists |
| Factory and product, L3 against L4 | **Inherited, and the word is reserved.** *Factory* means ICM's stable reference layer and nothing else here. A wing is a wing, not a factory. One vocabulary collision was already cleaned up in this repository and a second is not wanted |

## The one thing an umbrella adds that needs guarding

ICM's umbrella exists so several pipelines can share brand, voice and tools. That shared layer is
a **hole in the wall**: if every wing reads a shared voice file, then every agent can reach
outside its folder.

The rule that closes it without losing the point of the form: **a wing may reach outside itself
only where its charter names the path.** The audit checks that nothing else outside is named. The
hole becomes a door with a frame around it, and the umbrella keeps doing what it is for.

## Keeping this file honest

Upstream moves. This file is the record of what was decided about it, so it goes stale silently
unless someone re-reads.

Re-check on any re-vendor, and record the date. Four patterns here were nearly reinvented before
anyone read the current version, which is the cost of descent when the reading stops.

## Source

Session of 2026-08-26, against `icm-upstream` at commit `02ba5d8` and the vendored
`icm-architect` skill. Not yet exercised: no verdict here has been tested by a run.
