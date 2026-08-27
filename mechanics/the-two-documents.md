# The two documents

What goes into a folder under construction, what comes out of it, and why they are never the
same file.

## The pair

```
CONTRACT.md   issued    operator writes it   what should come to exist here
     |
     v  an agent builds
CONTEXT.md    emitted   the agent writes it  what is here now
```

Opposite directions, different authors, different lifetimes. The issued one is a mandate and is
finished before the work starts. The emitted one is a description and cannot exist until the
work is done.

## Why they cannot be one file

If the agent writes its result over the file that instructed it, the next run reads the previous
run's self-report as its mandate.

That is a silent compounding failure. Run two builds on run one's account of itself rather than
on what was asked. Run three builds on run two's account of that. Nothing errors, each run is
locally faithful, and the drift is invisible because the original mandate no longer exists to
compare against.

Keeping them separate also preserves the thing that makes acceptance cheap: the two can be
diffed. `acceptance.md` uses that diff as the only mechanical check for fit anyone has.

## The emitted contract is the deliverable

This is the part that does real work, so it is worth being precise about what it buys.

A build is finished when the agent can describe what it made in the form the workspace uses.
Not a summary, not a report: the actual contract a future run of that folder would be handed.
Inputs, process, audits, outputs.

Writing that forces the agent to contend with its own output against the shape of the workspace.
A folder built without understanding produces a contract that does not hang together, and
incoherence surfaces in twenty lines rather than in four hundred lines of product.

What it buys is **review cost**. The operator reads a contract instead of an artifact, and
`../foundations/failure-modes.md` number nine is why that matters: the alternative is the core
reading work product, forming an opinion, and sending it back, which is a loop with no floor.

What it does not buy is fit. A capable agent given a poor mandate builds something coherent and
describes it accurately. That is failure mode ten, and the diff against the issued contract is
the only mechanical thing that catches it.

## Promotion

An emitted contract is an **artifact** until a person promotes it. It sits with the run's
output. It is not the folder's method, nothing routes to it, and no later run reads it.

Promotion is the operator accepting it: the file becomes the folder's standing `CONTEXT.md`, and
`the-router.md` flips that folder to built.

The gate is not ceremony. ICM's rule is that reference docs are the authority for how to build
and previous outputs are artifacts rather than templates, because early outputs are the worst
outputs and a system that learns from them never improves. An unpromoted contract is an early
output. Promotion is a person saying this one is good enough to be copied from.

## What each file contains

**`CONTRACT.md`**, written by the operator before anything runs:

- what should exist here when this is done, stated as an outcome rather than a procedure
- what it may use, and where those things are
- the audits the result has to pass
- what to do when the mandate does not cover the case
- where to route next, if this is one of several chained builds

**`CONTEXT.md`**, written by the agent as its last act, in the shape a mill stage uses:

- Inputs, with the section or scope named rather than only the file
- Process, numbered and short
- Checkpoints, where a person steers
- Audit, as checks with pass conditions
- Outputs, named with their paths

The second shape is ICM's and is not ours to redesign. `../origins/icm-upstream/` carries the
current version of it.

## The rule that generalises

Neither document describes the other's job. The contract does not describe what will be there;
it states what must be. The emitted context does not argue that the work was good; it states
what is there.

**Descriptions are checkable. Verdicts are not.** That is why the emitted document is written as
a description, and why rung zero can audit it: every path it names either resolves or does not.
An agent asserting that its work was good would give us nothing to check.

## Source

Session of 2026-08-26. The completion condition, meaning that a build ends by producing the
contract a future run would need, is the operator's, and it came from having tested the two
alternatives: a purely mechanical check proves completion rather than quality, and a quality
review by the core produces a loop that consumes the operator.

Not yet exercised. No contract has been issued and none emitted.
