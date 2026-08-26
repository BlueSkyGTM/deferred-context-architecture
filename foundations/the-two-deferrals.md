# The two deferrals

Deferred Context Architecture defers two different things. They share a name, they solve
different problems, and they fail in different ways. Reading them as one thing is how the
architecture gets built wrong.

## Deferred activation

Nothing is instantiated until traversal reaches it.

There is no dispatcher holding a population of agents. There is no swarm woken at the start
of a run and fed work. A context file carries the instruction that wakes what it needs, and
that instruction does nothing at all until a task arrives at that file.

The cost model is the point. A resident agent costs a context window whether or not it is
used. A construct costs nothing until it fires. The set of agents the host system can call is
therefore unbounded, because none of them exist. They are definitions, not processes.

What it buys:

| Effect | Because |
|---|---|
| Zero standing cost | Nothing runs that the task did not reach |
| Maintenance that cannot drift | The construct is edited in the same file, in the same pass, as the method it wakes |
| No central registry | Nothing has to know about everything, so nothing has to be kept in sync with everything |

The third row is the one that survives contact with time. A central orchestrator has to be
edited in a different file from the method it dispatches, so the two drift, and the drift is
invisible until a run takes a branch nobody updated.

**Failure mode: the unvisited node.** A construct that only fires on traversal never fires
where nothing traverses. Structural decay is defined by absence of traffic, so the mechanism
is blindest exactly where the problem lives. This is not a small caveat. It is the reason
`../mechanics/ignition.md` exists.

## Deferred scope

What is woken never sees the whole.

An agent is handed its contract, its inputs, and nothing else. It cannot read the host system. It
cannot see its siblings. It does not know what the run is ultimately for.

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

Deferred scope means the constructing file is the only channel through which judgment reaches
the agent. Therefore:

> **A DCA agent is exactly as good as what its construct encodes. Depth is in what is handed
> down, never in what the agent can go find.**

What that sentence decomposes into is `the-four-parts.md`: method, materials, standard and
capability, which are the only four things a construct can carry and the only four that make
the difference. These two deferrals are how those four get delivered. They are not what
makes the work good.

Withhold too much and the completion fallacy returns wearing a different coat: not an agent
persuaded by its own reasoning, but an agent faithfully executing a contract that was never
adequate. The failure looks identical from outside. Everything reports green.

## Why not "time and scope"

An earlier draft named the first deferral *time*. Time is a symptom. The mechanism is not
that activation happens later, it is that activation is triggered by arrival rather than by a
schedule. Late is what it looks like from outside. Activation is what it is.

## Source

Operator, 2026-08-25. The activation and scope split was named in the founding session and is
recorded in `../decisions/2026-08-25-founding-session.md`.
