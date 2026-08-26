# The four parts

What makes any output good, decomposed. There are four contributors and there is no fifth.

| Part | What it is | Who writes it |
|---|---|---|
| Method | How this kind of work is done here | The operator, once, and it accumulates |
| Materials | The specific facts this task needs, and the ones it must not see | The operator, per card |
| Standard | What counts as good, and who says so | The operator, and never the party doing the work |
| Capability | Raw model horsepower | Declared when the card is written, never chosen at runtime |

Where each one lives depends on which mode the folder is in, per `../mechanics/the-router.md`.
The parts do not change. Their addresses do.

| Part | Miller | Builder |
|---|---|---|
| Method | the standing `CONTEXT.md` in the folder | `CONTRACT.md`, plus any steps the card adds |
| Materials | the folder's contents, bounded by the working directory | the same |
| Standard | the contract's audit, plus the card's `done` | the emitted contract has to pass those audits |
| Capability | `tier` on the card | the same |

Two things are worth reading off that table. Capability has one home in both modes, because a
folder has no horsepower requirement and a task does. And materials are never a list the agent
reads: they are the place it was put.

The addresses moved on 2026-08-26 and the parts did not. Three of the four were previously
spread across a context file, a construct and a card, tied together by relative paths. They now
arrive through one binding.

## What is not on the list

Persona. There is no fifth part reading "you are a senior strategist with twenty years of
experience." It adds nothing to method, because it is not a method. Nothing to materials,
because it carries no facts. Nothing to standard, because it names no criterion. Nothing to
capability, because it does not change the weights.

It is a costume, and a costume is the only part of an expert that can be copied without
understanding anything. That is precisely why libraries of agent prompts consist almost
entirely of costumes: the other three parts are specific to a practice and cannot be
distributed.

## The ratio, which is the whole economic argument

**Capability is the smallest of the four for most work.**

A strong model with no method, no materials and no standard produces confident garbage: fast,
thorough, wrong, and reported green. A middling model with all three produces something
shippable.

This is the only reason tiering works. If capability were the dominant term, routing down
would be a quality cut with a discount attached and the ladder in `../mechanics/tiering.md`
would be false economy. It is not the dominant term. Three of the four are the operator's to
supply, and supplying them well is worth more than the gap between two model tiers.

It is also why the opposite reflex is so expensive. **Reaching for the strongest available
model is reaching for the smallest lever**, and it feels like the responsible move because it
is the only one of the four that can be bought.

## Expertise is assembled, not constructed

Nobody is made an expert. A capable-enough model is handed a method, materials and a standard,
and the combination performs. **The specialist is the position, not the occupant.**

`completion-fallacy.md` makes the same claim about independence: it comes from withholding the
argument rather than from the weights, so it is positional. Competence turns out to work the
same way. Neither is a property of the thing that wakes.

Three consequences follow immediately, and each of them settles a question that keeps
returning:

- **There is nothing to store.** A registry of experts is a registry of costumes. What is
  worth deriving is an index of construction conditions, which is a different artifact.
- **A menu of experts is a menu of doors.** The door fixes method, materials and standard;
  the fourth is declared on the construct at that same door. There is no second list.
- **"Make it an expert in X" is not a buildable instruction.** "Write down how X is done here"
  is, and it is the same work, done once, in a form that survives the session.

## Why this is the heart, and the deferrals are the method

`the-two-deferrals.md` ends on the law that a DCA agent is exactly as good as what its construct
encodes, and that depth is in what is handed down. This file is what that sentence decomposes
into. The four parts name what "what is handed down" actually consists of.

Both deferrals turn out to be two properties of one artifact:

> **A job's existence is deferred activation. A job's `inputs` list is deferred scope.**

Nothing else in the workspace defers anything. Material stores, the router addresses, the
product returns, and the job carries the whole mechanism. That is worth knowing mostly as a
warning: everything that can go wrong structurally goes wrong on the job, so that is where the
checks belong.

Read in that order, every mechanic in this workspace is one of the four given a mechanism.

| Mechanic | Serves |
|---|---|
| `../mechanics/the-bbs.md` | Which door, and so method, materials and standard together |
| `the-binding.md` | The delivery vehicle for all four |
| `../mechanics/the-router.md` | Which mode, and so which set of addresses applies |
| `../mechanics/tiering.md` | Capability, and the argument that it is the smallest lever |
| `../mechanics/acceptance.md` | Standard, and how it is checked without a review loop |
| `../mechanics/evaluation.md` | Standard, and why it is authored by someone who is not doing the work |
| `../mechanics/ignition.md` | Whether a card is ever written |
| `../mechanics/reconciliation.md` | Siblings that assembled the same four differently |

Deferred activation is what makes it affordable to have many doors. Deferred scope is what
keeps materials deliberate, since an agent that can read the host system is one whose materials
were never chosen. Both are how the four parts get delivered. Neither is what makes the work
good.

The architecture takes its name from the method rather than the heart, which is normal and
worth stating once so a later reader does not mistake the name for the claim.

## Using it

Four questions, in front of any task:

1. Is the method written down, or is it in my head?
2. Which facts does this need exactly, and which must it not be allowed to see?
3. What counts as done, who says so, and is that written somewhere the work cannot reach?
4. What is the cheapest rung that can hold this, given the first three are supplied?

A task that cannot answer one through three does not need a better model. It needs a file.

## Where each part fails

| Part missing | Looks like |
|---|---|
| Method | Plausible work in the wrong shape. Conventions reinvented each run, no two runs matching |
| Materials | Confident invention. Gaps filled from training rather than from the account |
| Standard | Everything passes. The completion fallacy at full strength |
| Capability | Visible failure, and the only one of the four that announces itself |

That last row is why the other three go unnoticed for months. Under-capability is loud, so it
gets fixed, repeatedly, by reaching for a larger model. The other three are silent, and
`failure-modes.md` collects the silent ones.

## Source

Operator and session, 2026-08-25, second pass. The decomposition was drawn in conversation and
the operator identified it as upstream of the two deferrals rather than beside them. Not yet
exercised: no run has tested whether the four are separable in practice as cleanly as they
separate on paper.

Revised 2026-08-26. The four parts were cross-referenced against the proposed layers and against
the two deferrals and came through unchanged. Only their addresses moved, they now differ by
mode, and the deferrals were found to collapse onto a single artifact. Of everything settled on
the 25th, this file is the only one that needed no argument rewritten, which is worth recording:
it is a claim about outputs rather than about architecture, and architecture claims are the ones
better architecture invalidates.
