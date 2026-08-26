# Lineage

What was brought in, from whom, and what is this project's own. Recorded so a later session can
tell a citation from a claim.

## Brought in

| Source | What it contributes | Where it is used |
|---|---|---|
| Interpretable Context Methodology, the `icm-architect` skill, Jake Van Clief, MIT | The five forms, the walk test, build and restructure modes, the five-layer hierarchy | `origins/icm-architect/`, vendored entire |
| Interpretable Context Methodology, the method repository, MIT | Fifteen numbered patterns. Selective section routing, checkpoints, stage audits, and docs over outputs are load-bearing here | `origins/icm-upstream/`, core vendored |
| Addy Osmani, Loop Engineering, June 2026 | The named layer above the harness. Five moves, six parts. The rule that automation fires a named skill rather than a pasted wall of instructions | `mechanics/ignition.md`, `foundations/the-binding.md` |
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
| Independence is manufactured by withholding the argument rather than by varying the model | `foundations/completion-fallacy.md` |
| Capability is spent per decision, cost per token, and the two need not land on the same model | `foundations/constraints-over-capability.md` |
| A fourth rung below the cheapest model: work that is not a model question | `mechanics/tiering.md` |
| Tier is declared when a card is written, so capability is a property of position rather than a decision on arrival | `mechanics/tiering.md` |
| The orchestrator inverted: dissolved into the host system, and what wakes is assembled rather than dispatched | `foundations/the-binding.md` |
| Nothing fires where no card is written, so one push tick is required and its only output is a card | `mechanics/ignition.md` |
| What wakes is a binding, assembled at the moment work begins and discarded after, so there is nothing to store or index | `foundations/the-binding.md` |
| The core acts at the folder contract, and its action is selection of a model rather than authorship of a role | `foundations/the-binding.md` |
| Withholding runs both ways: the core is blind to work product, which is what keeps its judgment clean across a long session | `foundations/the-binding.md`, `mechanics/acceptance.md` |
| The board is where the core is forced to deliberate, and the card is the residue. This is the interface, and the line against ICM | `mechanics/the-bbs.md` |
| A build ends by emitting the contract a future run would be handed, which beats both a mechanical check and a quality review | `mechanics/the-two-documents.md`, `mechanics/acceptance.md` |
| Issued and emitted contracts are separate files in opposite directions, so a run never builds on the previous run's self-report | `mechanics/the-two-documents.md` |
| Scope is enforced by working directory rather than by instruction, because a request can be declined and a boundary cannot | `foundations/the-binding.md` |
| Acceptance is authored by someone who is not doing the work, and written before it starts | `mechanics/evaluation.md`, `mechanics/acceptance.md` |
| Depth costs uniformity, and the parent owes reconciliation | `mechanics/reconciliation.md` |
| Loop engineering has a verification model and no precedence model | `foundations/authority.md` |
| ICM defers what is read, DCA defers what is woken | `origins/divergence.md` |
| A variation becomes dispatch rather than data | `origins/divergence.md` |
| Blindness is safe only because the picture stays in human-readable folders | `foundations/authority.md`, `origins/divergence.md` |

## A note on the secondary source

The loop-engineering material reached this session through one book summarising blog posts, a
podcast, and official documentation. Its structural claims are consistent and useful. Its
product specifics, meaning command names, version numbers, interval floors, and expiry
windows, are secondhand and were not verified during the founding session.

Verify those against current documentation before building anything that depends on them.
Where this workspace repeats such a specific, it says so at the point of use.

## Licence

Two artifacts are vendored under `origins/`, both MIT, and they are complementary rather than
versions of one thing. `icm-architect/` is the skill, copyright 2026 Jake Van Clief.
`icm-upstream/` is the method repository's core, copyright 2026 Model Workspace Protocol
Contributors, taken at commit `02ba5d8` on 2026-08-26. Each LICENSE file travels with its copy,
and `origins/icm-upstream/VENDORED.md` records how the two differ and what was omitted. Working
copies are carried so this method can be developed against, and checked against, a stable
version of what it descends from.

The host system this was extracted from made an earlier and different call about the same
source: ICM's CONTEXT.md audit checklist was absorbed rather than vendored, and its naming
section was deliberately not carried, because that system already owned naming and the two
rules disagreed. Both calls stand, for different purposes. That one keeps a checklist without
importing a rival naming rule. This one takes a full working copy in order to amend the method
itself.
