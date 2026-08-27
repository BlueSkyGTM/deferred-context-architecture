> **Archived 2026-08-26. Replaced by `../mechanics/the-bbs.md`.**
>
> The arguments in this file survived and were carried forward: a file cannot fail, the split
> between mandate and method, sole authorship by the core, and git as the ledger. What did not
> survive is the framing. This file calls the board a docket, meaning a passive list of what is
> outstanding, and files it as one mechanic among seven.
>
> It is neither. Posting a card is the only moment in the architecture where the core is forced
> to decide which folder, which mode, which model, what counts as done and what should stop the
> work. The artifact is the record of that deliberation, and it is the interface that separates
> this method from the one it amends. A docket does not do that.
>
> Also wrong here: the claim that the board replaces ICM's stage ordinality. It does not.
> Numbered folders still carry sequence where sequence is permanent. The card carries it where
> it is not.

# The board

Where the work is, what comes next, and what counts as done. The one file in a DCA workspace
that the operator writes and everything else reads.

## Why a file could not already do this

Every context file in the host system is full of opinion. Not one of them has ever been in the
room when the opinion mattered.

A file has no moment of execution. It is read, and whatever the reader does next is the
outcome. It cannot check, cannot object, cannot notice that it was ignored. **A file cannot
fail.** That is the thing ICM does not supply, and it is not a complaint about ephemerality:
ICM keeps everything on disk, which is exactly right, and still nothing on that disk ever
gets a turn.

Three parts close it, and each is a different kind of artifact.

| Part | Is | Holds |
|---|---|---|
| The context file | The law | What good work is, for this kind of work |
| The construct | The hearing | An occasion where that law is applied and can return a no |
| The board | The docket | What is outstanding, in what order, and what was decided |

A law has opinion. It does not have a courtroom. A woken agent is not a legislator, it is a
court date, and everything it enforces was written by the operator before it woke.

What an agent contributes is therefore not intelligence but **position**. The core persona
cannot judge its own output, because it holds the argument that produced it. An agent handed
the artifact and the criteria and denied the argument occupies a seat the core structurally
cannot occupy. `../foundations/completion-fallacy.md` develops that as the manufactured
outsider; the board is what gives it something to sit in judgment of.

## The split

**The board carries the mandate. The context file carries the method.**

A card says which work, in what order, and what finishing means. The file behind the door it
names says how that kind of work is done here, and which playbooks exist to do it with.

The two halves have opposite lifetimes, and that is what makes the arrangement cheap to run
repeatedly. Context files are stable and can sit inside a cached prefix. The board mutates
every time a card moves. **Read the board late.** A file that changes by design must never sit
in front of content worth caching, since a prefix match invalidates everything after the first
changed byte. `tiering.md` holds the measured version of that.

## What a card carries

Two fields separate a work order from a wish.

**The door.** Not only the task, the entry point. "Write the migration" leaves the agent to pick
its own route, and a route chosen at runtime by a model is the dispatcher that `constructs.md`
dissolved, walking back in wearing a card number. The operator picks the door when writing the
card. The context file behind it takes over from there.

**Its own definition of done.** "Write the migration" is a wish. "Write the migration for
this table, done when it exists at the named path and the rollback runs clean" is a mandate.
A card with no acceptance condition cannot be gated, so it gets marked done by whoever returns
from it, which is the completion fallacy with a card number attached.

Criteria split in two and both halves are written before the work starts. Generic standards
for that kind of work live in the context file. Task-specific acceptance lives on the card.

## One author

**The core persona writes the board. Nothing else writes to it.**

An agent writes its output to the path its construct named and returns that path. The core moves
the card. This is not tidiness: several agents writing one file is write contention for no
gain, and an agent that records its own status is a stage stating whether it passed, which
`evaluation.md` rules out.

The death case then closes itself. An agent that never comes back leaves a card still marked
in progress beside an output path that either exists or does not, and the core sees that on
its next read. Ten dead workers become ten cards that never moved. Ten dead transcripts become
nothing at all.

## The board is the file. The ledger is git.

A ledger and a board want opposite things: append-only history against current mutable state.
Two artifacts are not needed, because a committed file already carries both. The file is the
state. Its history is the ledger, dated, immutable, with a reason on every entry.

This is also what a handoff was failing to do. Prose compresses reasoning first, because
reasoning is the most compressible thing in it, so conclusions survive the compression and the
why does not. A card line is never long enough to be worth compressing, and a trail can be
walked backwards where a summary cannot.

## What it replaces in ICM, and what it leaves alone

ICM's numbered stages encode a sequence known before the work starts. `01_research` and then
`02_script` is right for milling, where the sequence genuinely is known and repeats. It is
wrong for building, where the sequence is the thing being discovered.

**The board replaces ICM's stage ordinality. It does not touch ICM's folder legibility.** The
folders, the contracts, the scoped loading and one-home-per-fact all stand unchanged. What
changes is the answer to what comes next: the top card rather than the next ordinal. That is
the difference between a pipeline and a work queue, and it is the whole of what rotating
priorities require.

## What it removes

The motive for fan-out. Work that cannot be seen invites finishing all of it at once, and ten
workers in flight is a coping mechanism for not knowing what is left. A board makes the
outstanding work visible, and visible work can be taken one card at a time. `tiering.md` holds
why width was never the saving it appeared to be.

## What it does not remove

The operator. Routing turn by turn stops; writing cards and reading verdicts starts. That is a
better job, done in the operator's own words, at the operator's own pace, in advance, and it
accumulates instead of evaporating. But it is a job. An architecture sold as an empty console
is the promise that made ICM disappointing rather than merely bounded.

## Source

Session of 2026-08-25, continuing the founding session in
`../decisions/2026-08-25-founding-session.md`. The scrum framing and the mandate/method split
are the operator's. Nothing here has been exercised: no board exists yet, and the first real
one will change this file.
