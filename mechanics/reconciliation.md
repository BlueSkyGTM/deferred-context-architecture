# Reconciliation

What depth costs, and who pays it.

## The trade

ICM's milling produces consistency as a free side effect. Every branch runs the same template
against a different parameter, so uniformity is not something anyone maintains. It is what
running one template gets you.

DCA buys depth at exactly that price. A branch that wakes its own specialist produces work
shaped by that specialist rather than by a shared template, and deferred scope means no
specialist can see what its siblings did.

So three siblings can each be excellent and mutually inconsistent, and none of them can
detect it. Each reports success truthfully. The inconsistency exists only in a view none of
them has.

This is the second failure mode of deferred scope, alongside fit, and it appears the moment
more than one branch of a variation is taken in the same run.

## Who reconciles

The core, reading the board. Not the siblings, and not a file.

This needs saying plainly because an earlier version gave the job to "a constructing file", which
cannot see anything, and the alternative reading is worse: a woken agent able to see all of its
siblings would have the picture, and deferred scope exists to prevent exactly that. The only
party that can compare branches is the one that wrote the cards for them.

That makes reconciliation a named responsibility rather than something that happens by
attention. State it in the contract of the folder whose cards opened the branches:

- Which siblings this parent may open
- What must agree across them, named specifically, not as a wish for coherence
- What the parent does when they do not agree

The middle item is the work. "The outputs should be consistent" is not a criterion anything
can apply. "All three use the same term for the buyer, the same date format, and cite the
same ruling for pricing" is.

## Reconcile against the contract, never by merging outputs

The tempting fix is to hand all sibling outputs to one reader and ask for a coherent whole.
That reader is now an insider holding every argument at once, and the completion fallacy
returns at full strength: it will find the merged result good, because it built the reasoning
for the merge.

The sound version is narrower and cheaper.

1. Rung zero first. Compare the siblings on the named points mechanically wherever the point
   is mechanical: same term, same format, same cited ruling, same schema.
2. Where a real conflict is found, the core does not choose. It files, because a disagreement
   between two branches usually means the variation was cut wrong or the contract they shared
   was underspecified, and both are structural questions.
3. A ruling settles it, and the settlement is written back into the contract so the next run
   cannot reproduce it.

Step three is what stops reconciliation becoming a recurring tax. A conflict resolved only in
the output returns every run. A conflict resolved in the contract is gone.

That prohibition has a preventive form one level up. `tiering.md` restricts fan-out to cases
where the merge is mechanical, which is the same rule applied before the siblings exist rather
than after: partition the work so combining is concatenation, or run a relay so there is only
ever one artifact. Reconciliation is what remains when neither was available.

Sibling state is not held by the siblings. Each card carries its own acceptance condition and
the core moves it, per `the-bbs.md`, so reconciling means reading recorded outcomes rather than
interrogating agents that have already exited.

## The signal worth watching

Repeated sibling conflict on the same point is not a coordination problem. It is a structural
one, and the structure is telling you where.

Two branches that keep disagreeing about the same thing are usually one branch that was split
too early, or two branches that should have shared a reference file they were never given. In
both cases the fix is in what the cards carried or in where the variation was cut, never in
asking the agents to try harder.

## The limit worth stating

This is the least exercised part of the architecture. Fit and unvisited nodes have clear
mechanisms; reconciliation has a responsibility and a procedure, and no run behind it yet.

Expect the first real parallel run to change this file. Per the house convention, depth
here is earned by a second and third run rather than designed in advance, and what is written
above is a first version.

## Source

The sibling-coherence problem was raised in the founding session, 2026-08-25, and is recorded
in `../decisions/2026-08-25-founding-session.md`. No implementation has yet exercised it.

Revised 2026-08-26. Reconciliation was attributed to a file that cannot see, and is now the
core's, reading recorded outcomes.
