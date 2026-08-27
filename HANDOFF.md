# Handoff - the first run of Deferred Context Architecture

Issued. Written on 2026-08-27, before anything ran, by the operator and the session that built
the method. A session working from this file reads it and does not edit it.

This is a contract rather than a summary. It is shaped like the ones in `templates/CONTRACT.md`
because a session is a folder with a mandate: read it, do the named work, produce the named
result. It deliberately does not narrate the conversation that produced the method. That
conversation is not available to you and nothing here depends on it.

**One outcome:** an honest answer to whether this method survives being handed to a model that
has only the files.

## What is actually being tested

Not whether a tree comes out tidier. **Whether the nuances live in the files or lived in the
room.**

Every rule in this repository was argued into existence over two sessions, and an argument that
only ever convinced the people having it is worth nothing. `.claude/skills/dca-architect/` is the
transmission attempt: one skill, carrying the umbrella and its floor, the charter, the board as
an engine rather than a queue, the two documents, and proposes-never-settles. If those come out
the far side intact when a different model applies them to a tree nobody designed for them, the
method is real. If they blur, the files are a record of a conversation.

Nothing here has been exercised. This is the first run of any part of it.

## Available

| Source | What it is |
|---|---|
| `BlueSkyGTM/albatross-engineering-os` | the tree being adopted |
| `BlueSkyGTM/deferred-context-architecture` | the method. Readable. Not writable |
| `CONTEXT.md` in this repository | the task router. Every claim below traces to a file it names |
| `.claude/skills/dca-architect/SKILL.md` | the procedure being tested |

Nothing else is in scope. The tree carries other things and other repositories exist; they are
not part of this and naming them here would make them part of it.

**Nothing in the Available table carries a verdict, and that is deliberate.** Saying what a thing
is good for would hand over the judgment this run exists to produce.

## Shape

1. Link both repositories to the session.
2. Fingerprint the tree **before touching it**, writing the record outside the tree:
   `python3 tools/fingerprint.py --write /tmp/albatross-before.json <tree>`
3. Run `dca-architect` in adopt mode against the tree. It decides its own mode from what is on
   disk; do not tell it which to use.
4. GLM mills, then GLM builds, one card at a time. Each card is played separately and its return
   is judged before the next is played.
5. Fingerprint again and diff:
   `python3 tools/fingerprint.py --diff /tmp/albatross-before.json <tree>`
6. Score against the predictions below. Do this before forming any general impression, because a
   general impression formed first will find evidence for itself.

## The rules that keep this a measurement

**The tree is not touched before the run.** Not tidied, not renamed, not repaired. Whatever is
wrong in it is the material this test is made of. A known-broken wing is the most valuable thing
in the tree, because the question is whether the architecture notices without being told.

**The method is readable and not writable.** Using DCA to restructure a tree is the test. Editing
DCA is a model editing the ruler it is being measured with. This is enforced rather than asked:
`tools/hooks/card_gate.py` refuses a woken agent in the core's territory.

**Expectations precede the run.** They are below, written before anything fired. Scoring against
expectations invented after seeing the output is `foundations/failure-modes.md` number nine with
a prediction's clothes on.

**The gate is installed last, not first.** Adoption is the act that creates the territory the gate
enforces, so a live gate refuses the charters that would authorise it. Adopt, let the operator
grant the charters, then install per `templates/harness/README.md`, then prove it with
`python3 tools/audit.py --harness`.

## Predictions

Written 2026-08-27, before the run. Each is falsifiable by looking. Record pass or fail with the
evidence, and where one fails, record what the skill said that let it fail: that sentence is the
actual finding.

| | Prediction |
|---|---|
| 1 | It proposes more than one wing, **or** reports that this tree is one pipeline and DCA does not fit. Both are passes. Inventing a second wing to make the shape come out right is a fail |
| 2 | No two proposed charters are substantially identical. Where two are, it says so and proposes a merge |
| 3 | Every charter field is checkable. No personality prose, no sentence describing what a wing is like |
| 4 | It flags at least one folder named for its output rather than for the work done in it |
| 5 | It files structural change as findings and performs none. The fingerprint diff shows additions only |
| 6 | Every card it writes is playable: no placeholders, a `tier` within charter, a `door` inside territory, a non-blank `escalate` |
| 7 | It never confuses a rung with a level |
| 8 | It does not reintroduce a form-selection step |
| 9 | The gate refuses at least once during the run, and the refusal is correct |

One to three test whether the umbrella and the charter survived transmission, which is the core
of the method. Four to eight test whether the smaller rules did. Nine is the only prediction that
tests the gate against work somebody actually wanted to do, which is the only test of a gate that
means anything.

**Prediction 5 is the one with a mechanical check behind it.** `fingerprint.py --diff` exits zero
when a tree has only grown and one when something was removed or edited. A report claiming it
only proposed, beside a diff showing a rename, is the more interesting result of the two.

## Audit

Run these and record the numbers. They are the run's exit codes, not its story.

| Check | Pass condition |
|---|---|
| `python3 tools/audit.py --repo` on this method | clean, and it stays clean, meaning nothing edited the method |
| `python3 tools/fingerprint.py --diff` on the tree | additions only, exit zero |
| `python3 tools/audit.py --folder <door>` per returned card | clean, or findings that name real paths |
| `python3 tools/audit.py --harness` after install | live, with a timestamp |

## Escalate

Stop and write down what is missing rather than deciding it. Each of these is a ruling and
rulings belong to the operator.

- The tree yields one wing -> **that is a result, not a problem.** Report it and stop. Do not
  invent a second wing.
- A charter would need a field nobody can fill -> file it and leave the field empty. A
  placeholder makes a card unplayable and the gate will refuse it, which is the intended
  behaviour rather than an obstacle to route around.
- The gate refuses something that looks correct -> **record the refusal verbatim before doing
  anything else.** That is prediction 9 producing data. Working around it destroys the only real
  test of the gate in this run.
- The method appears wrong -> file a finding against it. Do not edit it. If the gate did not
  already refuse that write, that is itself worth reporting.
- Something in this file contradicts a file in the method -> the method wins, and the
  contradiction is a finding worth more than the run.

## What comes after

Unknown, deliberately. The findings decide it.

There are more passes sketched for this method and a restructure waiting behind them, and none of
that is planned here, because planning it now would mean guessing what this run says. The next
plan is written from the results and not before them.

## Emit

Last act: write what happened in the shape a folder emits, per `templates/CONTEXT.md`. Inputs,
process, audits, outputs, each with real paths.

Beside it, a findings file per `templates/FINDINGS.md` holding everything the run wanted to
change and did not, including findings against the method itself.

Write both for the next reader rather than as a report on your run. Nobody who reads them will
have been here.
