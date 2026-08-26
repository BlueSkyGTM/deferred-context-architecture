# The BBS

Where the core is forced to think, and the one interface this method adds to the one it amends.

## What it is

A file holding cards. A card is a work order: which folder, which mode, which model, what counts
as done, and what should stop the work rather than be guessed.

That description makes it sound like a queue. It is not, and the difference is the whole point.

## Why it is an engine and not a list

A card cannot be written without deciding five things. The fields are the questions.

| Field | What had to be settled to fill it |
|---|---|
| `door` | which folder, and therefore which method governs the work |
| `mode` | built or under construction, so miller or builder |
| `tier` | which rung serves this, and so which model, per `tiering.md` |
| `done` | what finished means, stated so something other than a model can check it |
| `escalate` | the named condition that stops the run instead of producing a guess |

None of them can be left blank and none can be answered by reflex. `../mechanics/the-router.md`
supplies the fact behind `mode`. `../rungs.md` supplies the menu behind `tier`. The decision is
made here, once, before anything runs, and the card is what the deliberation leaves behind:
dated, diffable, and readable before it commits anything.

**A file cannot fail.** It is read, and whatever the reader does next is the outcome. It cannot
check, object, or notice that it was ignored. That is what ICM leaves open, and it is not a
complaint about state living in transit, which ICM most emphatically fixes. Everything is on
disk. Nothing on that disk ever gets a turn. The BBS is where a turn is scheduled.

## The reasoning it triggers is the core's

A card that explained itself to the agent would be handing over the *why*, which is exactly what
deferred scope strips. So the deliberation the BBS forces belongs to one party only.

| Moment | Who reasons | About what |
|---|---|---|
| Before | the core | what is needed, which folder, which mode, which model, what done means |
| During | nobody deliberates | the agent works, and the folder's contract governs how |
| After | the agent | whether what it made matches what was asked, written as a contract someone else could use |

**The agent's duties begin on arrival at the folder, not at the board.** It never contends with
whether the card was well formed. Card quality is the core's problem, and an agent auditing its
own mandate is level five auditing level one.

The board itself never travels. If a woken agent could read it, it would see sibling work,
priorities and the whole outstanding queue, which is the picture. Only the card crosses.

## What a card may not carry

The folder's contract is scoped to the folder. The card must not become a second instruction
surface competing with it, or the two drift and the one at a distance wins by recency.

**A card carries only what the standing contract cannot know.** This run's acceptance, this
client's specifics, this job's exit condition. Anything the folder could have known stays in the
folder.

Hand-holding is allowed and sometimes necessary, particularly for building. It means more
method, more inputs, tighter acceptance. It never means more reasoning about why the work
matters.

## Written, then played

A written card is inert. No model is committed, no spend has occurred, nothing is running.
Playing it is a separate act that assembles the binding and commits the cost.

That gap is the operator's review window, and it is what makes "nothing fires that the operator
could not have read first" a mechanism rather than a hope. Ten cards can be written in one
sitting and none played.

| State | Means | What the state is for |
|---|---|---|
| written | the deliberation is done, nothing has fired | a person can read it, edit it, or bin it |
| played | model committed, agent in the folder | spend is named here, not discovered afterwards |
| returned | output exists and the audits have run | a mechanical verdict, not an opinion |
| accepted | the emitted contract has been promoted | the folder flips to built |

The card's text is fixed at writing. The core chooses which card and when, never what it says.

## One author

**The core writes the board. Nothing else writes to it.**

An agent writes its output to the path its card named and returns that path. The core moves the
card. This is not tidiness. Several agents writing one file is contention for no gain, and worse,
an agent recording its own status is a stage stating whether it passed, which `evaluation.md`
rules out.

The death case then closes itself. An agent that never comes back leaves a card still marked
played beside an output path that either exists or does not, and the core sees that on its next
read. Ten dead workers become ten cards that never moved. Ten dead transcripts become nothing.

## The board is the file. The ledger is git.

A ledger and a board want opposite things: append-only history against current mutable state.
Two artifacts are not needed, because a committed file carries both. The file is the state. Its
history is the ledger, dated, immutable, with a reason on every entry.

This is also what a handoff was failing to do. Prose compresses reasoning first, because
reasoning is the most compressible thing in it, so conclusions survive and the why does not. A
card is never long enough to be worth compressing, and a trail can be walked backwards where a
summary cannot.

## Router and board are not the same artifact

They sit on opposite sides of one act.

| | Holds | Changes | Derivable |
|---|---|---|---|
| Router | a fact: which folders exist and what mode each is in | rarely | yes, by script |
| Board | a decision: which work, in what order, judged how | constantly | never |

The router is what the core reads **in order to** deliberate. The card is what the deliberation
produces. Merge them and you have a router that has started holding opinions, which is a board
with the reasoning removed.

## Where the line with ICM falls

Worth stating plainly, because it is the reason this file exists.

ICM owns the folders, the contracts, the layers, the handoffs through output folders, the
audits, and one home per fact. All of it inside a folder. Between folders, ICM has numbering and
convention, and nothing travels that gap carrying rules of its own.

**This method owns the gap.** What moves between folders now carries a mandate, an acceptance
condition, a model commitment and a boundary, all authored in advance and readable before
anything fires. Making implicit connective tissue explicit and authored is the contribution.
Everything inside the folder is inherited.

## Two pictures, and how far to take them

A bulletin board explains why a mandate arrives stripped of its history. Whoever posted the
notice wanted something and said what and roughly why, and the rest of their life is not part of
the duty.

A card that does nothing until it is played explains why activation is a property rather than a
policy, and why the cost is paid at a nameable moment.

Neither goes further than that. They belong in prose that explains the mechanism to a person.
They are not the mechanism.

## Source

Sessions of 2026-08-25 and 2026-08-26. `../_archive/the-board.md` is the version this replaces,
and the note on it says what changed. The reframing from docket to engine, and the observation
that the deliberation belongs to the core rather than to the agent, are the operator's.

Nothing here has been exercised. No board exists, no card has been written, and the first real
one will change this file.
