# The economy

What this architecture manages, and what it does with what it saves.

The other foundations answer why a blind agent judges better and what makes an output good.
This one answers a question they leave open: why any of it is affordable, and why the saving is
the point rather than the consolation.

## The thesis

**Deferral converts spend into quality.**

Not into savings. A method whose claim was "the same work for less money" would be an
optimisation, and optimisations are optional. This one reallocates: every resource a
conventional run burns on context nobody needed is still spent, on more passes, more gates,
more standards written before the work, and more attempts at the parts that are hard. The bill
does not have to fall for the method to have worked. What has to change is what the bill bought.

That is the difference between austerity and reinvestment, and it is the whole argument. An
operator who takes the saving as a discount has run this method and got an optimisation. An
operator who spends it back on the three parts they own has run it as intended.

## One quantity, six meters

Everything this architecture manages is the same resource under different names: **model
attention that has to be paid for**. Naming the six separately is useful because they are
metered separately and run out separately, but they are not six problems.

| Meter | What runs out | What deferral does about it |
|---|---|---|
| Tokens | Money, per unit of attention | Deferred scope: a folder is smaller than a system |
| Context | Capacity, per call | The picture lives in folders, so nothing has to hold it |
| Usage windows | Throughput, per interval | The head and the rungs are both swappable, in one file |
| Agent cost | Money, per standing specialist | Deferred activation: an unplayed card costs nothing |
| Swarm concurrency | Money and coordination, to hold live state | A folder of markdown holds state at rest, for free |
| Quality checks | Money, per review pass | The gate and the audits are deterministic, so they are free |

Two of those rows are a different move from the other four, and the distinction matters more
than the tally. Tokens, context, windows and checks are resources this method **manages**.
Agent cost and swarm concurrency are resources it **deletes**: a standing specialist is
replaced by a card that does not exist until played, and a live swarm is replaced by files that
cost nothing to hold and cost only at the moment of reading. Managing a cost and abolishing the
need for it are both wins, and conflating them hides the better half.

## The meter money cannot clear

Usage windows deserve separating out, because they behave unlike the rest and they are what
forces architecture rather than budgeting.

Tokens and context are money problems. Spend more and they relax. A usage window is
throughput entitlement, and inside the window money does not help: there is no amount payable
that returns the capacity before it resets. The only responses are to wait, to route the work
to a rung that is not capped, or to change what is serving the position.

That is why the head is a capability slot like any other, and why swapping it is not an
infrastructure decision that happened to arrive alongside a method decision. A resource that
money cannot relieve is the only kind that changes the shape of a system rather than its
budget. `../rungs.md` is the file that absorbs it, for the head as much as for the rungs
beneath.

## Why the saving is available at all

`the-four-parts.md` establishes that capability is the smallest of the four contributors for
most work, and that three of the four are the operator's to write once, in files that
accumulate. `constraints-over-capability.md` establishes the split that makes the saving
bankable: capability is spent per decision, cost is spent per token, and the two do not have to
land on the same model.

Deferred scope is what makes those claims cash. An agent that cannot see the host system is
not paying for the host system. It is paying for one folder, which is the only thing its
contract asks about anyway. The saving is not a discount negotiated with a vendor. It is the
difference between what the work needed and what a conventional run would have loaded.

Deferred activation supplies the other half. A specialist that does not exist until a card is
played costs nothing to keep, so the set of specialists is unbounded. Breadth stops being a
budget line.

## What the saving buys

Reinvestment is not a sentiment. It has addresses, and each one is a place a conventional run
declines to spend because the money is already gone.

| Spend it on | Which part it buys | Why it was previously unaffordable |
|---|---|---|
| A standard written before the work, by someone not doing it | Standard | A second author is a second bill |
| More gates, and gates on more paths | Standard | Deterministic checks cost nothing but were never budgeted |
| A judgment pass over a finished artifact, argument withheld | Standard | An independent reader is a whole extra run |
| More attempts at the hard part, discarded freely | Method | Retry is only cheap when the retried scope is small |
| Method written down rather than re-derived per session | Method | Writing it once competes with shipping today |
| Materials chosen deliberately rather than loaded wholesale | Materials | Choosing costs thought; loading everything costs only money |

Read down that table and every row buys one of the three parts the operator owns. That is the
mechanism by which resource management becomes quality: the resource is fungible into exactly
the parts that dominate the outcome, and capability, the part it is usually spent on, is the
one that matters least.

## What this claim does not cover

Three limits, stated here so the thesis is not read as covering more than it does.

**A cheap check is not a quality check.** The gate is deterministic, free, and enforced by the
harness rather than requested in prose. What it enforces is policy: that a card was played,
that the path sits inside a chartered territory, that the rung is permitted. It does not
enforce whether the work was any good, and `../handoff/known-limits.md` says so in its own
table. Counting the gate as quality assurance claims the one thing it was never built to do.

**The gate's coverage is a matcher, not a boundary.** It fires on the harness tool calls it is
registered for. A write that reaches disk by another route is not refused, and is not recorded
as unrefused either. That is a documented limit rather than a defect, and it bounds how much of
the quality argument the gate can carry.

**The reinvestment is a claim about where the saving can go, not evidence that it went there.**
Nothing in this bundle spends the saving on the operator's behalf, and nothing measures whether
it was spent. An operator who banks it has not violated the method. They have just bought an
optimisation instead of the thing.

## Against the origin

`../origins/divergence.md` records that ICM consolidates toward one roof while this defers
toward many, and that the aims part in the first sentence rather than in any mechanism. This
file gives that divergence its axis.

**ICM optimises for a picture a person can read.** One agent, one roof, state on disk,
simplicity as the aim.

**This optimises for a bill a person can afford to spend well**, while keeping enough of that
legibility to stay auditable.

The two are in designed tension, and the hard line that holds it is already written: remove
ICM's folder legibility and this becomes opaque agent state, which is the thing it was built to
avoid. Resource management is what this method adds. Interpretability is the constraint it is
not permitted to spend.

## Source

Operator and session, 2026-08-27, drawn in conversation while reviewing what a live vendor
environment actually metered. The six meters are the operator's enumeration. The collapse onto
one quantity, the manage-versus-delete split, and the caveats are this session's, and rank
lowest by `authority.md` until ruled on.

The premise was already latent in the bundle and stated nowhere in `foundations/`:
`../tools/probe_models.py` opens by saying that capability is spent per decision and cost per
token, and that none of it has been measured. That sentence is this file's thesis written in a
docstring.

Not yet exercised. No run has been costed at any rung, so the reinvestment claim is reasoned
rather than measured, and it belongs in the same column as everything else in
`../README.md` under what is still missing.
