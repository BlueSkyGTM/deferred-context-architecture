# The router

Which folders exist, and what mode each one is in. The standing map the core reads before it
can deliberate.

## The one thing it holds

Every working folder is in one of two states, and the difference decides what kind of agent gets
sent there.

| Mode | Means | The folder holds | An agent sent there |
|---|---|---|---|
| built | the work here is understood and repeatable | `CONTEXT.md`, a standing method | mills: runs the stage and produces product |
| under construction | the work here has not been shaped yet | `CONTRACT.md`, an issued mandate | builds: produces the folder, and emits a contract describing it |

That is the whole file. Two columns and a rule.

## Wings, and the grain above folders

A folder is a boundary. A **wing** is a folder holding folders, and it is a boundary too. The
mechanism does not change with the grain; only the size of the wall does.

The router therefore carries two levels. Which wings exist, and which folders inside each are
built or under construction.

| Wing | Charter | Folder | Mode |
|---|---|---|---|
| `<wing>` | `<wing>/CHARTER.md` | `<wing>/01-name/` | built |

A wing's territory and the doors out of it live in its charter, not here. The router says what
exists and what mode it is in; the charter says what may be reached and at what cost. Facts in
one, grants in the other.

**One board serves every wing.** Cards carry a wing column. Splitting the board per wing would
split its authorship, and the single-author rule is what makes an unmoved card mean something.

## A folder is named for the work, never for the product

A mill is not named after the flour. A folder called `receptionist` or `invoices` or `blog-posts`
is named after what comes out of it, and that name is wrong in a way that spreads.

It spreads because a folder named for its output cannot say what belongs in it. Everything that
touches the product has a claim, so the folder accumulates whatever is adjacent, and the boundary
that was supposed to make deferral safe stops describing anything. The same folder named for the
work it does answers the question in its own title, and what does not belong is obvious to a
reader who has never seen the tree.

The check is one question: **does this name describe an activity or an artifact?** An artifact
name is a finding, and renaming is structural, so it is filed and waits for a ruling rather than
being performed.

## Why it is separate from the board

A router holds a **fact**. A board holds a **decision**. They have different lifetimes and
different authors, and merging them produces a router that has started holding opinions.

The router changes when a folder is created or promoted, which is rare. The board changes every
time a card moves. `../mechanics/the-bbs.md` carries why that difference is load-bearing rather
than tidy: stable files can sit in a cached prefix, and a file that mutates by design must never
sit in front of content worth caching.

The router is read **in order to** deliberate. The card is what the deliberation produces.

## It should be derivable, and checked rather than trusted

Nothing in the router is an opinion. A folder holding `CONTRACT.md` and no `CONTEXT.md` is under
construction. A folder holding a promoted `CONTEXT.md` is built. That is answerable by `find`,
which means the router is a generated index, and ICM's rule about generated indexes applies:
they are rebuilt by script, never hand-edited, because a hand-curated index always drifts.

Rung zero rebuilds it and compares. A router that disagrees with the tree is the defect, not the
tree.

## Promotion is the only transition

A folder moves from under construction to built when the operator accepts the contract an agent
emitted about it. Not when the agent finishes. Not when the audits pass.

`the-two-documents.md` holds why the gap matters: until a person promotes it, the emitted
contract is an artifact rather than a standing method, and nothing downstream is allowed to
learn from it. ICM states the general form as *early outputs are the worst outputs*. A promotion
step is what keeps the first attempt from becoming the pattern.

There is no reverse transition by default. A built folder whose method has gone wrong is repaired
by editing its contract, which is ordinary work. Demoting it back to under construction means
rebuilding it, and that is a ruling rather than a maintenance task.

## What it must not become

A dependency graph. A schedule. A place to record which folder feeds which.

Order between folders lives on the card for building work and in folder numbering for milling
work, per `../origins/divergence.md`. A router that starts describing flow has begun
reimplementing the pipeline in a second place, and the two will disagree.

If the router grows past a table, something has been put in it that belongs elsewhere.

## Source

Session of 2026-08-26. The dispatch decision, choosing between sending a miller and sending a
builder, is the operator's, and it is what closed the gap between milling and building without
requiring two mechanisms.

Not yet exercised. No router exists, and the first one will show whether two modes are enough.
