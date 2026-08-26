# Tiering

Three rungs a card can declare, and one seat that is not a rung at all. Nothing chooses
centrally, which is the point.

## The ladder

| Rung | What it is | Use for | Costs |
|---|---|---|---|
| none | Not a model question. Shell, script, a diff | Walking a tree, checking a path resolves, comparing a fingerprint, counting files | Nothing |
| fetch | Fast retrieval. Returns facts, makes no calls | Searching, reading, gathering, listing what exists | Least |
| build | Executes a complete specification | Writing to a contract, applying a convention, producing volume from a settled decision | More |

## The seat that is not a rung

An earlier version of this file listed a fourth rung called judgment, for fit, precedence,
whether a contract was right, and reconciling siblings. Every one of those is something
`evaluation.md` forbids a woken agent to do, and `../rungs.md` records what actually serves that
position: the core, in session.

A card cannot declare the core. The core is what reads the card.

So judgment is not a tier anyone routes to. It is the seat the deliberation happens in, and the
work listed above is the core's own, done before a card is written or after a result comes back.
Keeping it on the ladder invited a card to hand its hardest question to a woken model, which is
the one thing the architecture is built to prevent.

**On the word.** This ladder is measured in **rungs**. The authority ladder in
`../foundations/authority.md` is measured in **levels**. Two ordered lists sharing one word was a
live defect until 2026-08-26.

## The rule that makes it work

**Capability is spent per decision. Cost is spent per token.**

The core is not rationed because it is expensive. It is expensive per token and cheap per
decision, so it is spent wherever a decision is genuinely being made and kept away from anything
that produces volume. A strong model writing four hundred lines of boilerplate is the failure
this ladder exists to prevent. The same model writing one card is the success.

## Rung zero earns the most

The bottom rung saves more than the others because it does not cost less, it costs nothing.
Most of what gets done to a workspace is not reasoning:

- Enumerate the tree
- Check whether an entry file exists in each folder
- Confirm every pointer in a routing table resolves
- Diff the current structural fingerprint against the last recorded one
- Count what is there, so a claim about counts can be verified

All of that was being done by the strongest available model reading directories. Moving it to
rung zero is the single largest saving in the architecture and the one with no quality
tradeoff at all, because a deterministic check is not merely cheaper than a model, it is more
reliable than one.

The house convention already requires counts to be verified against the tree rather
than remembered. Rung zero is that rule given a mechanism.

## Why the tier belongs on the card

The routing fallacy in `../foundations/constraints-over-capability.md` exists because tier was
being chosen at the wrong granularity. One call for a whole braided task forces the maximum,
because the caller does not know which strands the run will hit.

Put the tier on the card and nobody makes that call. Each strand is labelled when the card that
governs it is written. The braid does not have to be untangled by anyone, because it was never tied: each
thread was tagged at the point it was written.

Capability stops being a decision and becomes a property of position. That is the same move
`../foundations/the-binding.md` makes with activation, one level down.

## Escalation

A rung below judgment will meet something its contract does not cover. Two things can happen
and only one of them is acceptable.

It stops and files, per `escalate` on its card. Or it guesses.

Routing down without a named exit condition does not avoid the hard case. It relocates the
hard case to the least capable reader in the system, unobserved, and the completion fallacy
guarantees the result comes back reported as a success.

Every card states its exit. A card that cannot state one is a card whose tier was set too low,
or a question that belonged to the core in the first place.

## Fan-out and what it costs

Width is the thing that looks like a saving and is not. Running ten workers at once buys wall
clock and nothing else: ten concurrent calls bill ten context loads, exactly as ten sequential
ones do.

On one vendor it is worse than sequential, and the mechanism is caching. Prompt caching is a
prefix match over tools, then system, then messages, and a fork that rebuilds any of those
with a difference misses the parent's cache entirely. A woken agent carrying its own contract
is a different prefix by definition. So every worker in a fan-out pays full uncached input for
context a sequential continuation would have read back at a fraction of it. Caches are also
scoped to one model, so a worker on a second vendor shares nothing with the first under any
topology.

That last point cuts both ways and is worth stating plainly, because it is easy to read as
permission. Putting the workers on a second vendor takes their cost off the first vendor's
meter. It does not remove the cost; it relocates it, and whether it lands depends on whether
that vendor caches prefixes at all and whether the plan is flat or metered. **A concurrency
limit is a rate cap, not a budget.** Ten concurrent slots are not ten free calls.

Two costs stay on the logic layer no matter who runs the workers:

- **The fan-in.** Someone writes the work orders and someone reads the results. Ten outputs
  arriving at once is the strong tier paying strong-tier prices, which is the original
  detonation wearing a different hat. A card names a return path for this reason, and the board
  holds those paths so the core opens one deliberately rather than ten because they all came
  back.
- **The review surface.** Ten results nobody reads individually collapse into a summary of
  summaries. No vendor arrangement buys back a single unit of that, which is why the ceiling
  below is not stated in money.

**The rule: fan out only where the merge is mechanical.**

Where work partitions cleanly, each worker owns a disjoint slice and writes its own file.
Combining is concatenation, a rung-zero operation with no judgment in it. That is a partition
rather than a team, and it is safe precisely because nobody merged anything.

Where it does not partition, run a relay: one worker writes the file, the next edits that
file. Genuinely one output, every step inspectable, and sequential. Wall clock was the only
thing width was buying, so a relay gives up the only thing that was ever on offer.

What is never sound is a team that returns a single merged output. One output is not one gate,
it is no gate over a blend whose seams nobody inspected, and the merge itself was composed at
runtime by a model working from an instruction no human wrote. `reconciliation.md` states the
same prohibition from the other end.

**Width is capped by how many results can genuinely be gated in one pass, never by the
vendor's concurrency ceiling.** What that number is comes from a measured run, not from this
file.

Where genuinely cheap width is wanted on the Anthropic surface, the Batch API is the
mechanism: asynchronous, half cost. Parallel sub-agents are not.

## Vendor is a cost decision

A foreign model at the fetch or build rung is `capability is spent per decision, cost is spent
per token` with a supplier attached. Sound, and worth doing.

It buys nothing on judgment. Independence comes from withholding the argument, never from
varying the weights, and a foreign agent handed the full reasoning is exactly as captured as a
local one. Believing the swap purchased independence is how the withholding discipline gets
skipped, and then the outsider stops existing. `../foundations/completion-fallacy.md` holds
the argument.

The same applies to what corrupts the logic layer. It is not the model doing work, it is the
main window holding outputs. A foreign worker returning forty thousand tokens pollutes exactly
as much and charges a second supplier for the privilege. The protection is `returns` naming a
path.

**Write rungs, never vendor names.** A card declares `fetch` or `build`; one mapping file says
which model serves each rung today. Swapping a supplier, including a local one on the
operator's own hardware, is then an edit to that one file rather than a sweep through every
contract. Model agnosticism is not something to build. It is something to avoid breaking.

## What this does not do

It does not promise a cheap tier can hold a hard position. It promises that independence,
which `../foundations/completion-fallacy.md` shows comes from withholding rather than from
model choice, is available at every rung. A cheap model reading a tight contract with no
history to be persuaded by is a real evaluator. A cheap model asked to decide whether the
contract was right is not.

## Source

Operator and session, 2026-08-25. Rung zero derives from the Stripe deterministic orchestrator
described in `../foundations/constraints-over-capability.md`.

Revised 2026-08-26. The judgment rung was removed from the ladder because it named the core,
which no card can declare, and because the work listed under it was work `evaluation.md` forbids
a woken agent. The rung and level collision with the authority ladder was resolved in the same
pass.
