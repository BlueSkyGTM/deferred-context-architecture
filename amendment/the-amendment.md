# The amendment

What Interpretable Context Methodology cannot do, stated in its own words, and how Deferred
Context Architecture extends it without competing with it.

Stated from ICM's own text wherever possible, because an amendment that misdescribes what it
amends is a rival rather than a supplement.

## What ICM is very good at

Interpretable Context Methodology makes folder structure do the work a framework would do in
code. Stage sequencing is folder numbering. Context scoping is folder hierarchy. State
management is files on disk. Coordination is one folder's output being another folder's
input. One agent walks the building and the question decides which shelf it walks to.

Its results are real: a human can open any folder and see what state the system is in,
because state is just files. Nothing is opaque, nothing needs a developer to interpret, and
the whole pipeline can be understood by reading the contracts top to bottom without running
anything.

Nothing below disputes any of that. DCA depends on all of it.

## The limit, in ICM's own words

`icm-architect/references/core.md`, under Where ICM Loses, names three:

> Real-time multi-agent collaboration. High concurrency. Automated mid-pipeline branching:
> a human choosing stage 3a vs 3b between stages is natural; the system branching on AI
> output mid-run pushes ICM toward becoming the framework it replaced.

The first two are genuinely out of scope for the host system. Nobody is serving many users or
running tight agent-to-agent message loops.

The third is the one that matters, and note what it actually says. It does not claim
branching is unnecessary. It claims branching costs opacity, because the only way ICM knows to
get it is to become a framework, and a framework holds its logic in code rather than in
files.

## The limit, stated so it can be built against

ICM's own framing is that a workspace is not a chatbot, and that is true in a precise way:
**the interface is a folder rather than a conversation.** Nobody prompts their way to an
outcome, because the structure carries the instruction.

That is not the same claim as headless, and ICM does not make the second one. Invariant four
makes every output an edit surface, and every stage contract carries a mandatory human check
written as something a person physically does. A person walking in is the design, not an
oversight in it. **ICM removed the prompting. It did not remove the presence.**

Which gives the limit a form something can be built against. A context file is full of
opinion, and it has no moment of execution: it is read, and whatever the reader does next is
the outcome. It cannot check, cannot object, cannot notice that it was ignored. **A file
cannot fail.** Note that this is not a complaint about state living in transit, which is the
one thing ICM most emphatically fixes. Everything is on disk. Nothing on that disk ever gets a
turn.

ICM builds the courtroom. It never schedules a hearing.
`../mechanics/the-bbs.md` names the three parts that close it: the context file is the law, the
binding is the hearing, and the board is where the hearing gets scheduled.

There is a second edge, visible once building is separated from milling. Numbered stages encode a
sequence known before the work starts, which is right for milling and wrong for building, where
the sequence is the thing being discovered.

**This does not replace ICM's stage ordinality. It makes ordinality per card rather than per
tree.** Numbered folders still carry sequence wherever sequence is genuinely permanent, and a
mill keeps its numbers untouched. A card carries sequence where it is not. Nothing is taken away
from ICM; a second place to put order is added, for the case ICM's own text says it loses. The
first version of this file claimed replacement, which was both wrong and a worse claim.

## The shape of the gap

ICM's own invariants show why branching is the missing piece rather than an optional extra.

Invariant seven says an agent loads only what its step needs, and core.md calls this
prevention rather than compression. That is deferred scope already, applied to reading. ICM
has the discipline and applies it to one verb.

The consequence is a ceiling. One librarian walks the building, so depth is bounded by what a
single walker can hold across the whole walk. A stage names a place where work happens and
then relies on whoever arrives to be adequate to it. The structure guarantees the right work
happens in the right order. It cannot make that work deep.

This is what the operator calls milling: repeatable processes with slight variations, run
faithfully. Excellent for videos, graphics, reports, anything where the shape is settled and
only the parameters move. It does not carry depth, because depth is not something a sequence
can hold.

## The second problem ICM cannot see

`icm-architect/SKILL.md` requires choosing among five forms at build time: pipeline,
umbrella, record library, knowledge bundle, context map. Choosing wrong produces a workspace
that answers questions badly for as long as it exists, and the host system then routes through the
wrong shape.

That decision depends on what the folder is for: how work enters it, what calls it, what it
must answer. A skill invoked on a folder reads the folder. The information that decides the
form frequently is not in the folder, it is in the surrounding contracts and in the operator's
head.

So the fit decision is made with less than it needs, and the completion fallacy makes the
result look settled. The workspace is built meticulously to the wrong form and reports
success.

## Where the amendment goes

Two gaps, one mechanism. Branching without a framework, because the branch is a file rather
than code. Fit decided with context rather than despite it, because activation and context
become the same artifact.

## The one-line version

**ICM defers what is read. DCA defers what is woken.**

Same discipline, one verb further. Every ICM invariant survives unchanged; the extension adds
a second thing a context file is allowed to carry.

## The mechanism

Under ICM a variation is data. Sixty seconds rather than ninety, this palette rather than
that one, this client rather than the last one. The single walking agent reads the parameter
and adapts.

Under DCA a variation is dispatch. It names which intelligence the branch requires, and wakes
it, and hands it exactly what it may see.

The pipeline stops being a template with slots and becomes a tree in which every branch
carries its own specialist, instantiated only if that branch is taken. Milling keeps its
pattern of variations. The variations acquire depth, because each one can now construct
something that has depth in it.

## Why this does not become the framework ICM warned about

ICM's objection to mid-pipeline branching is that the system branching on model output pushes
ICM toward the framework it replaced. The objection is about where the logic lives, not about
branching itself.

The branch is a card. The condition, what it wakes, what it may see, and what it returns are
plain text in a file a person can read before anything runs. There is no orchestration code, no
registry, no runtime holding a graph.

Check it against ICM's own invariants:

| ICM invariant | Here |
|---|---|
| One folder, one job | Unchanged. The folder states its job; the card names which job is being run |
| Small stable entry file | Unchanged. Cards live on the board, never in the entry file |
| Every contract explicit | Strengthened. A card is written before anything fires and can be read first |
| Load only what the step needs | Extended from reading to activation, and enforced by the working directory rather than requested |
| Plain text, linkable | Unchanged. Markdown, the format ICM already specifies |
| The filesystem is the state machine | Unchanged for stage state. A card is an authored decision rather than derived state, which is a different artifact class, not a violation |
| Every output is an edit surface | Unchanged, and load-bearing twice over: a finding is a file the operator edits, and so is a card before it is played |

Nothing in that table is a concession. The branch is a file, so the structure remains the
documentation and the operator can still walk the building with their own eyes.

## What it fixes in ICM's fit problem

The fit problem above describes a skill invoked on a folder deciding the form from what the
folder contains, while the information that settles the form lives in the surrounding
contracts.

Here there is no path to the agent that does not pass through a folder and a card. An agent is
never called with go and structure this folder. It arrives inside a folder that already states
what it is for, holding a card that states what finished means.

Decontextualisation is not reduced. It is made unreachable, because activation and context
are the same artifact.

That is a structural fix rather than a better prompt, which is the distinction the whole
architecture is built on.

## What ICM keeps that DCA depends on

The dependency runs one way and it is worth being explicit, because it is also the safety
argument.

DCA agents are blind. The main window holds decisions rather than work product. So nothing in
a DCA run holds the whole picture, and the picture has to be held somewhere.

ICM holds it, in human-readable folders. That is the only reason blindness is safe here. A
swarm holds its picture in memory nobody can read, which is why the operator rejected swarms
before this architecture existed. DCA is not exempt from that objection. It escapes it only
by keeping ICM underneath.

**Remove ICM and DCA becomes the thing it was built to avoid.** The amendment is not a
replacement and cannot survive being treated as one.

## The relationship, stated for the routing table

Where the two overlap, ICM wins. DCA fills a hole ICM leaves open and named itself. It is
never wired into ICM's internals: a contract says when to call which, and the two stay
independently debuggable.

That is the host system's standing rule for additions, applied here without exception.

## Source

Founding session, 2026-08-25. Quotations are from `icm-architect/references/core.md` and
`icm-architect/SKILL.md`, vendored in this folder under MIT licence, copyright 2026 Jake Van
Clief. Method: Interpretable Context Methodology, Van Clief and McDermott, arXiv:2603.16021.

Revised 2026-08-26. The ordinality claim was corrected from replacement to per-card ordering, the
invariant table was re-checked against the mechanism as it now stands, and
`icm-upstream/` was added beside the skill because the two are complementary artifacts rather
than versions of one thing. `icm-upstream/VENDORED.md` records that check.
