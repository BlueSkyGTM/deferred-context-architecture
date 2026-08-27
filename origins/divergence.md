# Divergence

What was inherited from Interpretable Context Methodology, where the two methods part, and why
this is descent rather than amendment.

Stated from ICM's own text wherever possible. A descendant that misdescribes its origin is
appropriating rather than inheriting, and the claim is easier to check when it quotes.

## What ICM does, in its own words

`icm-upstream/README.md`:

> ICM replaces framework-level orchestration with filesystem structure. Numbered folders
> represent stages. Markdown files carry the prompts and context that tell a single AI agent
> what role to play at each step. The result is a system where **one agent, reading the right
> files at the right moment, does the work that would otherwise require a multi-agent
> framework.**

Stage sequencing is folder numbering. Context scoping is folder hierarchy. State management is
files on disk. Coordination is one folder's output being another folder's input. A human can open
any folder and see what state the system is in, because state is just files.

Nothing below disputes any of that. This method is built out of it.

## Where the aims part

Read that quotation again and the divergence is in the first sentence rather than in any
mechanism. **ICM's goal is one agent doing what a framework would otherwise do.** This method's
goal is many bounded agents run cheaply and safely, with the operator out of the work entirely.

Those are different problems with different success conditions, and the instincts they produce
point in opposite directions.

**ICM consolidates.** One roof, one walker, shared reference material, simplicity as the aim.

**This defers.** Many walls, nothing seeing the whole, deferral as the aim rather than a cost
paid for it.

The proof is what happens at the limit. Consolidate an ICM workspace and it gets simpler, which
is the intended direction. Consolidate this one and **it stops working**, because a single
undivided workspace has nothing left to defer between. Two methods whose optimum configurations
are opposites are not one method.

### The axis the aims part along

Stated as what each is optimising, which is more useful than what each looks like.

**ICM optimises for a picture a person can read.** One agent, one roof, state on disk, and
simplicity as the aim.

**This optimises for a bill a person can afford to spend well.** Not a smaller bill. The
resource deferral frees is reinvested in standards, gates and judgment passes rather than
banked, which is the thesis in `../foundations/the-economy.md`.

That is the addition, and it is genuinely an addition rather than a correction: ICM does not
undertake resource management and does not claim to. Nothing above says ICM is wrong about
anything. It says the two are solving for different scarcities.

The constraint on the addition is the inheritance itself. Interpretability is not a resource
this method is permitted to spend, however much of it could be converted into throughput.
Remove ICM's folder legibility to buy cheapness and what remains is opaque agent state, which
is the thing the whole arrangement exists to avoid. The economy is bounded by the origin.

## What that makes this

A descendant. The lineage is real and stays named: the orchestration model here is Van Clief's,
who drew on older practice in turn. Judo produced Brazilian jiu-jitsu, which never stopped
naming Judo and whose practitioners still study it.

The discipline that follows: **fork the agenda, not the reading.** Four upstream patterns were
nearly reinvented in this repository because nobody was checking. `the-machinery.md` records a
verdict on every one of them, and keeping that file honest as upstream moves is the ongoing cost
of descent.

Forking also raises the attribution bar rather than lowering it. `../NOTICE.md` states what is
carried and under what terms; both copies stay unmodified.

**The second failure of descent is wanting the room.** Not reinventing a pattern, which is merely
expensive, but building a case that the origin was wrong so that the descendant can replace it
rather than depend on it. It never arrives as an argument about the text, because the text does
not support it. It arrives as a claim about what the author believes, and it is usually stated
warmly, by someone who has read the work and is trying to place it.

The tell is a citation with no line reference. A position attributed to a person is unfalsifiable
by anyone downstream, so this repository quotes and never characterises: every claim about ICM
here points at a file, and where the two methods disagree, the disagreement is between two
statements a reader can put side by side. That is why `../NOTICE.md` and `../lineage.md` name
authorship, copyright and terms, and nothing else.

## The gap that was found first

`icm-architect/references/core.md`, under Where ICM Loses, names three limits:

> Real-time multi-agent collaboration. High concurrency. Automated mid-pipeline branching:
> a human choosing stage 3a vs 3b between stages is natural; the system branching on AI
> output mid-run pushes ICM toward becoming the framework it replaced.

The first two are out of scope for a local workspace. The third is the one this method was built
against, and note what it actually says: not that branching is unnecessary, but that the only way
ICM knows to get it is to become a framework, and a framework holds its logic in code rather
than in files.

## The gap stated so something can be built against it

ICM's framing is that a workspace is not a chatbot, and that is true in a precise way: **the
interface is a folder rather than a conversation.** Nobody prompts their way to an outcome
because the structure carries the instruction.

That is not the same as headless, and ICM does not claim it is. Every stage contract carries a
human check written as something a person physically does. A person walking in is the design.
**ICM removed the prompting. It did not remove the presence.**

Which gives the gap a form. A context file is full of opinion and has no moment of execution: it
is read, and whatever the reader does next is the outcome. It cannot check, cannot object, cannot
notice it was ignored. **A file cannot fail.** This is not a complaint about state living in
transit, which is the thing ICM most emphatically fixes. Everything is on disk. Nothing on that
disk ever gets a turn.

ICM builds the courtroom. It never schedules a hearing. `../mechanics/the-bbs.md` names the three
parts that close it: the context file is the law, the binding is the hearing, and the board is
where a hearing gets scheduled.

## Ordinality: added to, not replaced

Numbered stages encode a sequence known before the work starts, which is right for milling and
wrong for building, where the sequence is what is being discovered.

**This does not replace ICM's stage ordinality. It makes ordinality per card rather than per
tree.** Numbered folders keep sequence wherever sequence is genuinely permanent, and a mill keeps
its numbers untouched. A card carries sequence where it is not permanent. Nothing is taken away;
a second place to put order is added, for the case ICM's own text says it loses.

## The second gap, and how it closed

An earlier version of this file named a second problem: `icm-architect/SKILL.md` requires
choosing among five forms at build time, the information that decides the form often lives
outside the folder being examined, and choosing wrong produces a workspace that answers questions
badly for as long as it exists.

**That gap is closed by deletion rather than by mechanism, and the earlier claim was wrong.**

This method uses one form. Of the five, the umbrella is the only one with more than one wall in
it: a pipeline is a single boundary, a record library holds instances rather than domains and so
cannot carry differing charters, a knowledge bundle has no execution, and a context map describes
an organization rather than being a place work happens. Deferral needs plurality of bounded
domains, and exactly one form supplies it.

So there is no fit decision left to get wrong. The other four forms are not defective; they have
no gap this method fits into, and someone running ICM still wants all five.

One gap remains, not two: branching without a framework, because the branch is a card.

## Why this does not become the framework ICM warned about

The objection was about where the logic lives, not about branching itself.

A card is plain text a person can read before anything runs. The condition, what it wakes, what
it may see, what it returns. No orchestration code, no registry, no runtime holding a graph.

| ICM invariant | Here |
|---|---|
| One folder, one job | Unchanged. The folder states its job; the card names which job is running |
| Small stable entry file | Unchanged. Cards live on the board, never in the entry file |
| Every contract explicit | Strengthened. A card is written before anything fires and can be read first |
| Load only what the step needs | Extended from reading to activation, and enforced by the working directory rather than requested |
| Plain text, linkable | Unchanged |
| The filesystem is the state machine | Unchanged for stage state. A card is an authored decision rather than derived state, which is a different artifact class rather than a violation |
| Every output is an edit surface | Unchanged and load-bearing twice: a finding is a file the operator edits, and so is a card before it is played |

## What is inherited and cannot be dropped

The dependency runs one way and it is also the safety argument.

Agents here are blind. The core's window holds decisions rather than work product. So nothing in
a run holds the whole picture, and the picture has to live somewhere.

**It lives in human-readable folders, which is ICM's contribution and the only reason blindness
is safe here.** A swarm holds its picture in memory nobody can read, which is the thing this
method was built to avoid. Encode the picture in agent configuration or in a stream of spent
cards and it becomes that thing. Treat it as a hard line rather than a preference.

## Source

Founding session 2026-08-25, revised through 2026-08-26. Quotations are from
`icm-architect/references/core.md`, `icm-architect/SKILL.md` and `icm-upstream/README.md`,
vendored in this folder under MIT licence. Method: Interpretable Context Methodology, Van Clief
and McDermott, arXiv:2603.16021.

Renamed from the-amendment file on 2026-08-26, when the relationship was settled as descent. Two
claims were corrected in the same pass: ordinality is added to rather than replaced, and the fit
problem closes by using one form rather than by the mechanism this file previously credited.
