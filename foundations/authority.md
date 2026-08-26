# Authority

Verification asks whether the work is right. Authority asks whose call it was. A system with
the first and not the second produces well-checked work that overrides decisions it was never
entitled to touch.

## The gap in loop engineering

The published loop-engineering material has a developed safety model and all of it is
verification: an independent evaluator, a stop condition judged by a fresh model, hard-coded
gates the agent cannot skip, a human review point. Every one of those answers the same
question, which is whether the output is any good.

None of them answers what happens when a well-verified output contradicts a standing
decision. The literature has no precedence model at all.

That is survivable when a loop's blast radius is a pull request that a human reads. It is not
survivable when the loop acts on the structure the whole host system routes through, because the
loop is then able to be correct and out of order at the same time, and nothing in it can
detect the difference.

## What this architecture requires instead

DCA inherits precedence from the host system it runs in rather than inventing its own. It
requires that such a ladder exist and be written down. The shape it was extracted from,
highest first, is a workable default:

1. The operator's ruling, live in the session
2. A dated ruling in an append-only record
3. The standing principles of the area the work sits in
4. Method: the contracts themselves
5. A session's own reasoning, lowest

Substitute your own levels. What must survive substitution is that there are five of them, that
they are ordered, that the order is written where a person can read it, and that the bottom
level is where a woken agent sits.

A woken agent sits at level five. It is the least authoritative thing in the building, and
deferred scope means it cannot see levels one through four unless they were handed to it.

**On the word.** This ladder is measured in **levels**. The capability ladder in
`../mechanics/tiering.md` is measured in **rungs**. Two ordered lists in one bundle sharing one
word was a live defect until 2026-08-26, and a contract author hitting a bare number should
never have to work out which ladder is meant.

Two consequences, and they are the load-bearing ones:

**A woken agent proposes. It does not settle.** Structural change is filed as a finding and
waits for a ruling. This is not caution about model quality. It is that level five cannot
promote itself, and an agent that cannot see the ladder cannot know it is standing at the
bottom of one.

A folder under construction is not an exception. The operator authorised that structure by
creating the folder and writing its contract, before anything ran. An agent fills a space that
was already sanctioned; it never decides that a space should exist.

**A ruling is how sight reaches the blind.** `completion-fallacy.md` establishes that
withholding buys independence and not competence, so the standard has to arrive already
decided from something that had the picture. A ruling is exactly that: a compressed piece of
the bigger picture, dated, recorded, small enough to hand to an agent that will never see the
rest.

Rulings are therefore not bureaucracy in this architecture. They are the supply line.

## Why this also answers cognitive surrender

The loop-engineering literature names the risk that an operator stops having an opinion once
the loop runs smoothly, and prescribes vigilance: read the output regularly, keep the
capacity to say this is wrong.

Vigilance is not a control. It degrades exactly when the loop is running well, which is when
it is least examined.

The structural version costs no willpower: nothing structural moves without a ruling, so the
operator's judgment is not something to remember to apply. It is in the path. This mirrors
the host system's existing rule that nothing is offered ahead of a finding, which is the same move
made one wing over.

## Where the picture is held

By design nobody holds it. The woken agents are blind. The main window holds decisions rather
than work product. The picture is in the structure.

That is the bet, and it is only safe under one condition: **the structure is human-readable
files, not opaque agent state.** A swarm holds its picture in memory nobody can read. This
architecture holds it in folders the operator can walk with their own eyes.

Lose that property, start encoding the picture in agent configuration rather than in the
file tree, and DCA becomes the thing it was built to avoid. Treat it as a hard line rather than
a preference.

## Source

The ladder is the host system's own, generalised here. The gap in the loop-engineering
literature is an observation from the founding session, recorded in
`../decisions/2026-08-25-founding-session.md`.
