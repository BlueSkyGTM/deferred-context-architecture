# Task router

What this workspace is, and which one file answers the task in front of you.

Deferred Context Architecture is a method for running agents that never see the whole. It defers
two things: activation, so nothing is instantiated until a card is written for it, and scope, so
what is instantiated is bounded by a folder rather than trusted with a system. The first makes it
cheap and reviewable. The second makes its judgment trustworthy.

It descends from Interpretable Context Methodology rather than amending it. ICM stays
underneath. Where the two overlap, ICM wins.

## Routing

| You need | Go |
|---|---|
| Why this exists at all, and why a blind agent judges better than a second model | `foundations/completion-fallacy.md` |
| What actually makes an output good, and what a construct can carry | `foundations/the-four-parts.md` |
| What "deferred" actually refers to | `foundations/the-two-deferrals.md` |
| Why the strong model should decide and not type | `foundations/constraints-over-capability.md` |
| Whose call is this, and what a woken agent may not do | `foundations/authority.md` |
| What is outstanding, what a card must carry, and where the core is forced to think | `mechanics/the-bbs.md` |
| Which wings exist, which folders are built, and who decides | `mechanics/the-router.md` |
| What a wing owns, may reach, may spend, and must refer upward | `templates/CHARTER.md` |
| What assembles an agent, and why there is nothing to store | `foundations/the-binding.md` |
| What goes into a folder being built and what comes out of it | `mechanics/the-two-documents.md` |
| How work is judged finished without the core reading it | `mechanics/acceptance.md` |
| Which model tier, and the rung that is not a model | `mechanics/tiering.md` |
| Which model actually serves which rung, today | `rungs.md` |
| Writing a contract a second-hand model can execute | `mechanics/writing-for-an-unknown-reader.md` |
| The scheduled walk, its caps, and what it may never do | `mechanics/ignition.md` |
| Who says no, and who is allowed to have written the standard | `mechanics/evaluation.md` |
| Two branches disagreed | `mechanics/reconciliation.md` |
| What was inherited, where the aims part, and why this is descent | `origins/divergence.md` |
| Every upstream pattern, with a verdict on what happened to it here | `origins/the-machinery.md` |
| The method descended from, as a skill | `origins/icm-architect/SKILL.md` |
| The method descended from, as its current conventions | `origins/icm-upstream/_core/CONVENTIONS.md` |
| Why both are vendored and how they differ | `origins/icm-upstream/VENDORED.md` |
| Something has gone wrong and reports fine | `foundations/failure-modes.md` |
| Who said what, and what is ours | `lineage.md` |
| What is vendored, from whom, under what terms | `NOTICE.md` |
| Why the core cannot do the work itself, and what it does when refused | `.claude/skills/dca-delegate/SKILL.md` |
| The rule that is a default rather than a request, and how it fails open | `tools/hooks/card_gate.py` |
| Installing that gate into a host system, and proving it is live | `templates/harness/README.md` |
| Which model serves a rung, and how that was measured | `tools/probe_models.py` |
| The mechanical half of acceptance, as something that runs | `tools/audit.py` |
| A copyable starting point for a card, a contract, or a router | `templates/` |
| What was superseded, and what replaced it | `_archive/` |
| Why a thing was settled, what is open, what is broken | `decisions/2026-08-25-founding-session.md` |

## Reading order, first time

`foundations/completion-fallacy.md` for why this exists, then
`foundations/the-four-parts.md`, which is the claim the rest of the workspace serves, then
`foundations/the-two-deferrals.md` for how those four get delivered, then
`foundations/the-binding.md` for what actually wakes, then `origins/divergence.md`. Those
five carry the argument. Then `mechanics/the-bbs.md`, where it becomes something that runs. Everything else is how it is
built or how it fails.

## On the shape of this workspace

There is no per-folder contract here, and that is deliberate rather than an omission. ICM
requires a `CONTEXT.md` for every working folder, meaning a folder where a stage runs. This
workspace is a knowledge bundle: nothing executes in it, the folders are shelves, and one
router reaching every file is smaller and truer than four routers covering four each. A folder
that exists for a kind of work which has happened twice is scaffolding, not structure.

When a stage does appear here, meaning the first ignition or the first binding that actually
runs, it gets a contract of its own and this note gets revised.

`tools/hooks/card_gate.py` is not that stage. It is a check, like `tools/audit.py`, and it holds
no work of its own. What it does mean is that this bundle is no longer only prose: one of its
rules is now enforced by the harness on any device where the gate is live, and
`python3 tools/audit.py --harness` is how a device answers whether it is.

## Status

Specified, not exercised. No card has been written, no binding assembled, no ignition scheduled,
and `mechanics/reconciliation.md` has no implementation behind it at all. Depth is earned by a
second and third run rather than designed in advance, so treat every mechanics file as a first
version.

Known defects, unfinished pieces, and what waits on a ruling are all in
`decisions/2026-08-25-founding-session.md`, beside the reasoning that produced them. Read it
before trusting any mechanics file: a documented workspace is not a working one.
