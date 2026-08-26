# The two deferrals

Deferred Context Architecture defers two different things. They share a name, they solve
different problems, and they fail in different ways. Reading them as one thing is how the
architecture gets built wrong.

## Deferred activation

Nothing is instantiated until a card is written for it, and nothing runs until that card is
played.

There is no dispatcher holding a population of agents. There is no swarm woken at the start of
a run and fed work. A card names the work, and until someone plays it the card is inert: no
model committed, no spend, nothing running.

The cost model is the point. A resident agent costs a context window whether or not it is used.
A binding costs nothing until it is assembled. The set of agents the host system can call is
therefore unbounded, because none of them exist. They are definitions, not processes.

What it buys:

| Effect | Because |
|---|---|
| Zero standing cost | Nothing runs that no card named |
| A review window that costs nothing | A written card has not fired, so it can be read, edited, or thrown away before it commits anything |
| No central registry | Nothing has to know about everything, so nothing has to be kept in sync with everything |

The third row is the one that survives contact with time. A central orchestrator has to be
edited in a different file from the method it dispatches, so the two drift, and the drift is
invisible until a run takes a branch nobody updated.

**Failure mode: the unvisited node.** Nothing fires where no card is written. Structural decay
is defined by absence of attention, so the mechanism is blindest exactly where the problem
lives, and it is blinder here than in a system that at least gets walked: there is no traversal
left to stumble over a rotting folder. This is not a small caveat. It is the reason
`../mechanics/ignition.md` exists, and the reason ignition's only output is a card.

## Deferred scope

What is woken never sees the whole.

An agent is sent to a folder and handed a card. What it can reach is what is in that folder. It
cannot read the host system, cannot see its siblings, and does not know what the run is
ultimately for.

Enforcing this by geography rather than by instruction matters. A contract asking a reader to
stay put can be declined. A working directory cannot.

This is not a limitation accepted for cost reasons. It is the mechanism that produces a
trustworthy judgment, and it follows directly from `completion-fallacy.md`: an agent is soft
on work whose reasoning is in its window. Withhold the reasoning and the softness has nothing
to attach to. The evaluator is an outsider because it was never let inside.

What it buys:

| Effect | Because |
|---|---|
| A genuine outsider, at no extra cost | Independence comes from the withholding, not from a second model |
| Composability with tiering | Nothing about the mechanism cares which model is woken, so cheap models can hold real positions |
| A main window that stays a ledger | Work product never enters it, so what accumulates is decisions |

**Failure mode: fit.** An agent that cannot see the picture can verify against its contract
and cannot ask whether the contract was right. It will produce work that is locally correct
and globally wrong, and it will report success, because by its own contract it succeeded.

## The law that follows

Deferred scope means the binding is the only channel through which judgment reaches the agent.
Therefore:

> **A woken agent is exactly as good as what its binding carries. Depth is in what is handed
> down, never in what the agent can go find.**

What that sentence decomposes into is `the-four-parts.md`: method, materials, standard and
capability, which are the only four things a binding can carry and the only four that make the
difference. These two deferrals are how those four get delivered. They are not what
makes the work good.

Withhold too much and the completion fallacy returns wearing a different coat: not an agent
persuaded by its own reasoning, but an agent faithfully executing a contract that was never
adequate. The failure looks identical from outside. Everything reports green.

## Why not "time and scope"

An earlier draft named the first deferral *time*. Time is a symptom. The mechanism is not that
activation happens later, it is what activation is triggered by. Late is what it looks like from
outside. Activation is what it is.

That argument outlived the answer it was written for. The first pass said activation is
triggered by arrival rather than by a schedule, which assumed a walker who could arrive
somewhere. There is no walker. Activation is triggered by **authorship**: a card exists, so
something can run; no card, and nothing does.

Moving the trigger from a runtime event to an authored artifact is what makes the guarantee
checkable. An arrival happens whether or not anyone meant it. A card had to be written by
someone, and it can be read before it fires.

**A card's existence is deferred activation. A card's working directory is deferred scope.**

## Source

Operator, 2026-08-25. The activation and scope split was named in the founding session and is
recorded in `../decisions/2026-08-25-founding-session.md`.

Revised 2026-08-26. Activation was defined as traversal reaching a construct, which assumed a
walker this architecture no longer has. It is authorship instead, and both deferrals turn out to
be two properties of one artifact. The unvisited node got worse rather than better in the move,
and that is stated above rather than left for a reader to notice.
