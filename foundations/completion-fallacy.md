# The completion fallacy

The observation this architecture was built to answer.

## The claim

An agent that finished a task thoroughly reports that the task went well. Thoroughness is
what it can observe about its own run. Correctness is not, so it substitutes the first for
the second and reports confidence it has not earned.

Stated as the model states it to itself: *I finished the task meticulously, therefore it is
good.*

## Why the substitution happens

By the time an agent evaluates its output, its window holds the reasoning that produced that
output. It does not see the artifact. It sees the argument for the artifact, and that
argument was persuasive enough to act on, which is why the work exists in the shape it does.

Anthropic's Prithvi Rajasekaran observed the same behaviour while building long-running
applications: asked to evaluate work they produced, agents confidently praise it, including
work a human reads as plainly mediocre. He attributes it to structure rather than capability,
and reports that tuning a standalone evaluator toward scepticism is far more tractable than
making a generator critical of its own work.

The important part of that finding is what it rules out. The defect is not in the model. A
larger model reasons its way to the same conclusion with more conviction, because it built a
better argument on the way in.

## The consequence that motivated this work

An operator watching a meticulous agent produce a bad result reads the failure as a model
failure. The natural response is to instruct harder: more detail, more constraint, more
specification. That response corrupts the next run, because the added instruction is more
material for the agent to be persuaded by, and the operator has now authored the
persuasion.

Projects fail this way quietly. Nothing errors. Every stage reports success. The structure
degrades under instruction that was written in good faith to fix it.

## Where judgment has to come from instead

If the defect is a property of context rather than capability, the fix is a property of
context too. Do not ask an agent to be sceptical about what it can see. Change what it can
see.

That is the whole of `the-two-deferrals.md`, and the reason this architecture is named for
what it withholds rather than for what it runs. The rest of this file is where the capacity
to say no actually comes from, and why the cheapest source is the one the field has been
overlooking.

Judgment therefore has to come from an outsider: something that did not build the work and
carries none of the reasoning that produced it. The field manufactures that outsider by
varying the agent. Addy Osmani runs a second
sub-agent with different instructions and sometimes a different model. Rajasekaran builds a
generator and evaluator pair, borrowing the structure from generative adversarial networks.
Claude Code's stop-condition check hands the question to a separate small model that took no
part in the turn. All three vary *who is asked*.

## What this architecture does instead

It varies *what can be seen*.

The contamination is a context property. The generator is compromised because the reasoning
is in its window, not because of anything about the model that holds it. Swapping the model
removes the reasoning as a side effect of removing the agent. Deferring scope removes the
reasoning directly.

| Approach | Manufactures independence by | Costs |
|---|---|---|
| Different instructions | Asking differently | A second run, same blind spots |
| Different model | Changing the reader | A second run, plus the second model's price and latency |
| Deferred scope | Withholding the argument | A second run, nothing else |

The third row is the same model, at the same tier, reading a contract instead of a history.
Independence is structural, so it does not have to be bought.

This is not a rejection of model variation. Where two independent readings are genuinely
worth the money, vary both. The claim is narrower: model variation is a way of paying for
independence that deferred scope already provides, and paying twice for one property is how
a token budget disappears.

## The consequence for tiering

Because independence no longer depends on which model is woken, the evaluator position stops
being a premium seat. A cheap model reading a tight contract, with no history to be persuaded
by, is a real evaluator. That is what makes the ladder in `../mechanics/tiering.md` viable
rather than a compromise.

## The limit

Withholding manufactures independence. It does not manufacture competence.

An evaluator with no picture can check the work against the contract and cannot check the
contract. So the standard has to arrive with the card, already decided, from something
that did have the picture when it decided. In the host system that is a ruling: dated, recorded,
and outranking whatever the session in front of it happens to think.

The evaluator is blind on purpose. Something that could see has to have written down what it
saw.

## Source

Origin: operator, 2026-08-25, from repeated project failures attributed to models and later
traced to instruction. Rajasekaran's finding, and the Osmani and stop-condition approaches
above, are reported in HuaShu, *Loop Engineering* (June 2026 edition), sections 04 and 05.
The withholding mechanism is this architecture's own and is recorded in
`../decisions/2026-08-25-founding-session.md`.
