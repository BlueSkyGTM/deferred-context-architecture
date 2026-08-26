# Lineage

What was brought in, from whom, and what is this project's own. Recorded so a later session can
tell a citation from a claim.

## Brought in

| Source | What it contributes | Where it is used |
|---|---|---|
| Interpretable Context Methodology, Van Clief and McDermott, arXiv:2603.16021, MIT | The whole substrate: folders as architecture, contracts per folder, the five forms, the five-layer hierarchy, the walk test | `amendment/icm-architect/`, vendored entire |
| Addy Osmani, Loop Engineering, June 2026 | The named layer above the harness. Five moves, six parts. The rule that automation fires a named skill rather than a pasted wall of instructions | `mechanics/ignition.md`, `mechanics/constructs.md` |
| Peter Steinberger and Boris Cherny, June 2026 | The position shift: design the loops that prompt the agent rather than prompting it | Context for the whole workspace |
| Prithvi Rajasekaran, Anthropic | Agents confidently praise their own output. Tuning a standalone sceptic is more tractable than making a generator self-critical. An evaluator should act rather than read | `foundations/completion-fallacy.md`, `mechanics/evaluation.md` |
| Stripe Minions, reported by Steve Kaliski | A deterministic orchestrator assembles context before the model wakes. Reliability comes from the quality of the constraints rather than the size of the model | `foundations/constraints-over-capability.md` |
| HuaShu, Loop Engineering: The Complete Guide, v260615 | The secondary source through which the four items above reached this session, with the four costs and the scheduling comparison | Throughout, cited per file |

## This host system's own

Claims below were derived in the founding session and are not in any source above.

| Claim | Where |
|---|---|
| The completion fallacy as the motivating defect, and instruction as its amplifier | `foundations/completion-fallacy.md` |
| Deferral has two axes, activation and scope, with different failure modes | `foundations/the-two-deferrals.md` |
| Independence is manufactured by withholding the argument rather than by varying the model | `completion-fallacy.md` |
| Capability is spent per decision, cost per token, and the two need not land on the same model | `foundations/constraints-over-capability.md` |
| A fourth rung below the cheapest model: work that is not a model question | `mechanics/tiering.md` |
| Tier belongs on the construct, so capability is a property of position rather than a decision | `mechanics/tiering.md` |
| The orchestrator inverted: dissolved into the host system, pull rather than push | `mechanics/constructs.md` |
| Pull-based activation is blind at unvisited nodes, so one push tick is required | `mechanics/ignition.md` |
| Evaluation criteria belong one level above the stage | `mechanics/evaluation.md` |
| Depth costs uniformity, and the parent owes reconciliation | `mechanics/reconciliation.md` |
| Loop engineering has a verification model and no precedence model | `foundations/authority.md` |
| ICM defers what is read, DCA defers what is woken | `amendment/the-amendment.md` |
| A variation becomes dispatch rather than data | `amendment/the-amendment.md` |
| Blindness is safe only because the picture stays in human-readable folders | `foundations/authority.md`, `amendment/the-amendment.md` |

## A note on the secondary source

The loop-engineering material reached this session through one book summarising blog posts, a
podcast, and official documentation. Its structural claims are consistent and useful. Its
product specifics, meaning command names, version numbers, interval floors, and expiry
windows, are secondhand and were not verified during the founding session.

Verify those against current documentation before building anything that depends on them.
Where this workspace repeats such a specific, it says so at the point of use.

## Licence

`amendment/icm-architect/` is vendored under the MIT licence, copyright 2026 Jake Van Clief.
Its LICENSE file travels with it. It is a working copy taken so that the amendment can be
developed against a stable version and fed back as one system, per the founding session.

The host system this was extracted from made an earlier and different call about the same
source: ICM's CONTEXT.md audit checklist was absorbed rather than vendored, and its naming
section was deliberately not carried, because that system already owned naming and the two
rules disagreed. Both calls stand, for different purposes. That one keeps a checklist without
importing a rival naming rule. This one takes a full working copy in order to amend the method
itself.
