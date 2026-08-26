# Constructs

The unit of the architecture. A construct is an instruction, living in a context file, that
names what is assembled when a task reaches this point, and what that thing is allowed to see.

## Why it is called a construct

The word carries the boundary between this and the standard agent model, so it is worth one
paragraph rather than being left to inference.

A summons implies an entity that already exists somewhere, with agency of its own, waiting to
be called. That is the standard model: a population of configured agents, and routing that
picks among them. It is also what produces registries, personas, and every failure this
workspace catalogues.

A construct is assembled at the moment it is needed, out of what the door supplies. Method,
materials, standard and capability, per `../foundations/the-four-parts.md`. Nothing about it
pre-exists the task, so there is no population, nothing to route among, and nothing to keep in
sync.

And a construct is disposable by design. It holds for one call and is not preserved, which is
why nothing here stores agents and why `../mechanics/the-board.md` rather than the construct
carries what survives.

## What it replaces

A dispatcher. In a centralised design something above the work holds a table of agents and
decides which to call. That table has to know about every branch, it lives in a different
file from the methods it calls, and it is edited in a different pass. It drifts, and the
drift is invisible until a run takes a branch nobody updated.

A construct has no table. Each file knows its own, and knows nothing else.

## Where it lives

In the context file for the folder whose work it governs, and nowhere else. This is the
host system's existing pointer discipline applied to activation: a wing points, never copies.

The maintenance property that follows is the whole reason for the placement. When the method
in a folder changes, the construct is in the file already open, edited in the same pass. Addy
Osmani's warning about a wall of instructions pasted into a schedule nobody will ever update
describes a failure of distance. Remove the distance and the failure has nowhere to occur.

## Who writes it

**The operator writes every construct, by hand. A model may select which construct fires. It may
never compose what one says.**

This is the hardest line in the architecture and the one whose breach is least visible. A
prompt composed at runtime by a model is not an artifact: it cannot be read, diffed, or
improved, and no record of it survives the call. An earlier iteration of this architecture
failed exactly here, and the operator's account of it is the diagnosis: there was no way to
know what the models were prompting each other with. Everything downstream of that is
unfixable in principle rather than merely unfixed.

A borrowed library of agent prompts breaches the same line one step earlier. Such a library
holds **roles**, not judgments. A generic reviewer persona carries no criteria for this work,
no tier, and no escalation condition, so importing fifty of them produces fifty agents and
zero gates while feeling like considerable progress. That is the completion fallacy operating
on the architecture rather than on an output.

The host system's instinct to prefer a library over a reimplementation is right for code and
inverts for prompts. Code's debugging surface is its behaviour, and behaviour can be observed.
**A prompt's debugging surface is the author's understanding of it.** A borrowed prompt is
therefore the one thing that cannot be debugged, failing at runtime, invisibly, in the exact
manner the earlier iteration failed. Where an outside library is worth anything, it is worth
reading once for its taxonomy of roles and discarding the prose, which makes stealing the
design the cheap option rather than the expensive one.

The corollary settles where the choice is made. Handing a model a catalogue to pick from is a
dispatcher wearing a folder's clothes: the routing decision is still taken at runtime, by a
model, unrecorded. Written into the context file, the same choice moves to write time, where
the operator makes it and it stays diffable.

## Shape

A construct is frontmatter on a stage contract. The fields are few on purpose: every field is
something the woken agent will receive, and `../foundations/the-two-deferrals.md` establishes
that what is handed down is the ceiling on quality.

```yaml
---
constructs:
  - when: the variation that selects this branch, stated as a condition
    wakes: what is woken, named
    tier: none | fetch | build | judgment
    hands-down:
      - exact/path/to/contract.md
      - exact/path/to/ruling.md
    returns: the artifact, named, and where it lands
    judged-by: ../CONTEXT.md#criteria
    escalates-when: the condition under which this stops and files instead
---
```

Read the fields as answers to five questions.

| Field | Answers |
|---|---|
| when | Why this branch and not its sibling |
| wakes | What is instantiated, if anything |
| tier | Which rung, per `tiering.md` |
| hands-down | Everything the agent will ever see |
| returns | What comes back, and where it lands on disk |
| judged-by | Whose criteria, held one level up per `evaluation.md` |
| escalates-when | The named condition that stops the run rather than guessing |

`hands-down` is the control surface of the entire architecture. It is the only channel
through which the host system's judgment reaches a blind agent. An audit of a DCA workspace is
mostly an audit of these lists.

`escalates-when` is not optional. A cheap tier will meet something its contract does not
cover, and without a named exit it will guess. Routing down with no escape hatch does not
avoid the hard case, it defers it to worse odds.

## The two rules

**A construct hands down. It never lets an agent look up.** If a woken thing can read the
host system, scope was not deferred and the outsider was not manufactured. Everything it gets, it
gets from `hands-down`.

**A construct proposes. It does not settle.** Structural change returns as a finding, per
`../foundations/authority.md`. A construct that writes to structure has promoted rung five to
rung one, and nothing downstream can detect that it happened.

## What this makes of a variation

Under ICM a variation is data: sixty seconds rather than ninety, this palette rather than
that one. A parameter the single walking agent reads and adapts to.

Under DCA a variation is dispatch. It names which intelligence the branch requires and wakes
it. The pipeline stops being a template with slots and becomes a tree where each branch
carries its own specialist, instantiated only if that branch is taken.

That is the whole amendment, and `../amendment/the-amendment.md` develops it.

## Source

Operator, 2026-08-25. The frontmatter shape is this workspace's proposal and has not yet been
exercised on a real run. Treat it as a first version per the house convention that depth is
earned by a second and third run rather than designed in advance.
