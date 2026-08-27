# Constraints over capability

Where reliability actually comes from, and the routing mistake that follows from getting it
wrong.

## The Stripe result

Stripe's Minions system merges more than 1,300 pull requests a week with no line written by
hand. The counterintuitive part is what it is built on: a fork of an open-source tool, not a
stronger model. Their stated claim is that reliability comes from the quality of the
constraints rather than the size of the model.

The move that produces it: before the model wakes, a deterministic orchestrator assembles the
context. It scans links, pulls tickets, finds documents, searches the code. By the time the
agent takes the stage the materials are already on the table. Deterministic gates and model
steps then alternate, and the agent cannot skip a gate.

The principle underneath, stated so it can be applied: **anything deterministic logic can
solve never goes to a probabilistic model.**

## The routing fallacy this corrects

Standard guidance says to use the strong model for planning and complexity, and a cheaper one
for execution against a plan, provided the plan is simple. The guidance assumes capability
requirement is a property of the task.

It is a property of each step, and the steps are braided rather than phased. A single plan
contains genuine judgment (which structure fits, what the authority ladder implies, whether
an addition competes with an engine) interleaved with mechanical work (enumerate the tree,
check the paths resolve, apply the naming convention, write the stub files).

So the requirement is a maximum, not an average. One hard sentence in four hundred lines pins
the entire run to the top tier, and the operator pays peak rates against a task whose mean is
nowhere near peak.

Splitting by hand fails for a reason that looks fatal: deciding which parts are simple is
itself a judgment call, so the expensive model is needed for the triage and the saving
appears to eat itself.

## Why it does not eat itself

**Capability is spent per decision. Cost is spent per token. The two do not have to land on
the same model.**

A routing decision is high judgment and near zero output. A build-out is low judgment and
enormous output. Keep the expensive model emitting decisions and let cheap tiers emit volume,
and every step still runs at the capability it needs while the bill collapses. The goal is
not to avoid the strong model. It is to stop it from typing.

That split is the mechanism the economy runs on. `the-economy.md` takes it one step further:
the collapse in the bill is not the return. What the freed resource is spent on afterwards is,
and it buys standards, gates and judgment passes rather than a discount.

## The tier this adds

The braid is not two strands. It is three, and the third is the one that saves the most,
because it costs nothing rather than less:

1. Genuine judgment
2. Mechanical work a cheap model can do
3. Work that is not a model question at all

Walking a directory, diffing a fingerprint, checking that a file exists, confirming a pointer
resolves: these were being done by the strongest available model reading directories, which
is the most expensive possible way to run `ls`.

The full ladder and how a card names its tier are in `../mechanics/tiering.md`.

## The relationship to deferred activation

Stripe centralises the orchestrator. This architecture dissolves it. The constraint
discipline is identical and the topology is inverted, which matters for one reason: a central
orchestrator has to pick a tier before it knows which strands the run will hit, so it picks
the maximum. A card at the point of use names the tier of the one strand it governs,
and no central choice is ever made.

The Stripe insight survives the inversion. Only the dispatcher does not.

## Source

Steve Kaliski on the *How I AI* podcast, as reported in HuaShu, *Loop Engineering* (June 2026
edition), section 06. The three-tier reading and the inversion are this architecture's own.
