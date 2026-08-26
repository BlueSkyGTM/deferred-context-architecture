# The binding

What actually wakes, what assembles it, and why there is nothing to store.

## The thing that was missing

This workspace spent its first pass describing an architecture with no actor in it. Files were
said to wake, to take over, to see the branches they opened, to let an agent look up or refuse
to. `../mechanics/the-bbs.md` carries the sentence that makes all of those impossible: a file
cannot fail, because it has no moment of execution. Something has to hold the moment.

That something is not a party. It is a **binding**: a contract, a model, a set of tools, and a
card, joined at the moment work begins and gone when it ends.

```
contract  x  model  x  tools  x  card   ->   one agent, one job, one return
```

Nothing about it pre-exists the work. There is no population to route among, no registry to
keep in sync, no configured agent sitting somewhere costing a context window. The set of
specialists the host system can call is unbounded because none of them exist.

## The core acts, and its action is selection

The old confusion was whether the core persona touches the folder contract at all. It does. It
opens the contract, reads what kind of work lives there, and picks the model that serves it.

**It selects. It never authors.**

The instructions were written by hand, in advance, by the operator: the method in the folder's
contract, the mandate on the card. The core adds capability and nothing else. That is the whole
of its involvement at the folder, and it is why the hardest line in this architecture survives
contact with a model that appears to be composing something.

A model may choose which model runs. It may never write what the work is told to do.

## Why a prompt composed at runtime is not an artifact

The line above is the one whose breach is least visible, so it is worth stating what it buys.

A prompt written at runtime cannot be read, diffed, or improved, and no record of it survives
the call. An earlier iteration of this architecture failed exactly there, and the operator's
account of it is the diagnosis: there was no way to know what the models were prompting each
other with. Everything downstream of that is unfixable in principle rather than merely unfixed.

A borrowed library of agent prompts breaches the same line one step earlier. Such a library
holds **roles**, not judgments. A generic reviewer persona carries no criteria for this work, no
rung, and no escalation condition, so importing fifty of them produces fifty agents and zero
gates while feeling like progress. That is the completion fallacy operating on the architecture
rather than on an output.

The instinct to prefer a library over a reimplementation is right for code and inverts for
prompts. Code's debugging surface is its behaviour, and behaviour can be observed. **A prompt's
debugging surface is its author's understanding of it.** A borrowed prompt is therefore the one
thing that cannot be debugged, failing at runtime, invisibly.

Handing a model a catalogue to pick from fails the same way. The routing decision is still taken
at runtime, by a model, unrecorded, which is a dispatcher wearing a folder's clothes.

## Written, then played

A card is written and then, separately, played. Between the two it is inert: no model committed,
no spend, nothing running. That gap is the operator's review window, and it is what turns
"nothing fires that the operator could not have read first" from a hope into a mechanism.

Ten cards can be written and none played. A card written today can be played next week.

The card's text is fixed at writing. Playing it selects the model and commits the spend. The
core chooses which card and when, never what it says.

## The two modes

The same binding runs both kinds of work. Only the folder's state differs, and
`../mechanics/the-router.md` holds that state.

| | Miller | Builder |
|---|---|---|
| Folder | built | under construction |
| Reads | `CONTEXT.md`, the standing method | `CONTRACT.md`, an issued mandate |
| Produces | product into `output/` | the folder itself, plus an emitted contract |
| Order comes from | folder numbering | the contract, which may route onward |

This is why an empty folder holding one contract is a legitimate unit of work. A build site and
a mill stage run identical machinery, and neither needs a mechanism the other lacks.

## Scope is geography

The agent is sent to the folder as its working directory. What it can reach is what is there.

That is a stronger guarantee than a contract asking it to stay put, because a request can be
declined and a boundary cannot. `../mechanics/writing-for-an-unknown-reader.md` states the
general form: naming what may be seen beats naming what may not, since the second requires
predicting what an unfamiliar reader would wrongly reach for.

## Withholding runs both ways

The agent is blind to the picture, so it cannot argue from the whole.

The core is blind to the work, so it cannot argue from the doing. It reads a path and an audit
result, never work product. This is the half the first pass missed, and it is the half that
keeps judgment clean over a long session: a reader that walks and works accumulates the
reasoning behind everything it produced, and then grades what it argued itself into.

Independence at both ends, from one mechanism pointed in opposite directions, at no extra cost.
`completion-fallacy.md` develops why withholding is what manufactures it.

## The two rules, addressed to the party that can obey them

**The core hands down. It never lets an agent look up.** A card is a list and cannot permit
or forbid anything. The party that can breach this is the one assembling the payload.

**A woken agent proposes. It does not settle.** Structural change returns as a finding and waits
for a ruling, per `authority.md`. A folder that is under construction is not an exception: the
operator authorised that structure by creating the folder and writing its contract, in advance.
An agent fills a space already sanctioned. It never decides that a space should exist.

## What this replaces

Constructs as frontmatter living in a stage contract, which is archived at
`../_archive/constructs.md`. That shape tried to persist something whose whole nature is to be
transient, and it required every folder to declare in advance what work would arrive at it.

The argument that survived the move is the one above about hand-written prompts. The mechanism
did not.

## Source

Session of 2026-08-26, continuing `../decisions/2026-08-25-founding-session.md`. The correction
that the core selects a model rather than composing a role is the operator's, and it resolved
several passes of disagreement about where a construct begins. Nothing here has been exercised:
no binding has been assembled, and the first real one will change this file.
