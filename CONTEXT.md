# Task router

What this workspace is, and which one file answers the task in front of you.

Deferred Context Architecture is a method for running agents that never see the whole. It
defers two things: activation, so nothing is instantiated until traversal reaches it, and
scope, so what is instantiated is handed a contract instead of a history. The first makes it
cheap. The second makes its judgment trustworthy.

It is an amendment to Interpretable Context Methodology, not a replacement. ICM stays
underneath. Where the two overlap, ICM wins.

## Routing

| You need | Go |
|---|---|
| Why this exists at all, and why a blind agent judges better than a second model | `foundations/completion-fallacy.md` |
| What actually makes an output good, and what a construct can carry | `foundations/the-four-parts.md` |
| What "deferred" actually refers to | `foundations/the-two-deferrals.md` |
| Why the strong model should decide and not type | `foundations/constraints-over-capability.md` |
| Whose call is this, and what a woken agent may not do | `foundations/authority.md` |
| What is outstanding, what a card must carry, who writes it | `mechanics/the-board.md` |
| How to write the thing that assembles an agent, and why it is not summoned | `mechanics/constructs.md` |
| Which model tier, and the rung that is not a model | `mechanics/tiering.md` |
| Which model actually serves which rung, today | `rungs.md` |
| Writing a contract a second-hand model can execute | `mechanics/writing-for-an-unknown-reader.md` |
| The scheduled walk, its caps, and what it may never do | `mechanics/ignition.md` |
| Who says no, and where the criteria live | `mechanics/evaluation.md` |
| Two branches disagreed | `mechanics/reconciliation.md` |
| What ICM cannot do, and how this extends it without becoming a framework | `amendment/the-amendment.md` |
| The method being amended, vendored whole | `amendment/icm-architect/SKILL.md` |
| Something has gone wrong and reports fine | `foundations/failure-modes.md` |
| Who said what, and what is ours | `lineage.md` |
| What is vendored, from whom, under what terms | `NOTICE.md` |
| Which model serves a rung, and how that was measured | `tools/probe_models.py` |
| Why a thing was settled, what is open, what is broken | `decisions/2026-08-25-founding-session.md` |

## Reading order, first time

`foundations/completion-fallacy.md` for why this exists, then
`foundations/the-four-parts.md`, which is the claim the rest of the workspace serves, then
`foundations/the-two-deferrals.md` for how those four get delivered, then
`amendment/the-amendment.md`. Those four carry the argument. Then
`mechanics/the-board.md`, where it becomes something that runs. Everything else is how it is
built or how it fails.

## On the shape of this workspace

There is no per-folder contract here, and that is deliberate rather than an omission. ICM
requires a `CONTEXT.md` for every working folder, meaning a folder where a stage runs. This
workspace is a knowledge bundle: nothing executes in it, the folders are shelves, and one
router reaching every file is smaller and truer than four routers covering four each. A folder
that exists for a kind of work which has happened twice is scaffolding, not structure.

When a stage does appear here, meaning the first ignition or the first construct that actually
runs, it gets a contract of its own and this note gets revised.

## Status

Specified, not exercised. No construct has been run, no ignition scheduled, and
`mechanics/reconciliation.md` has no implementation behind it at all. Depth is earned by a
second and third run rather than designed in advance, so treat every mechanics file as a first
version.

Known defects, unfinished pieces, and what waits on a ruling are all in
`decisions/2026-08-25-founding-session.md`, beside the reasoning that produced them. Read it
before trusting any mechanics file: a documented workspace is not a working one.
