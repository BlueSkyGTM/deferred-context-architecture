# 2026-08-26 The binding and the BBS

The session in which the architecture acquired an actor. Recorded as a deliberation ledger
rather than a summary, and written to supersede rather than to replace: every ruling from
2026-08-25 that stopped being true is named below, so a later session does not restore it by
accident.

## What started it

A question about whether the board's function was understood, which turned into a triage of the
documentation, which found something worse than a wording problem.

`../_archive/the-board.md` states the governing sentence of the whole bundle: a file cannot
fail, because it has no moment of execution. Five files then handed files exactly those verbs.
A context file that wakes what it needs. A folder's context file that takes over. A constructing
file that sees the branches it opened, and chooses, and files.

The count behind it: **"core persona" appeared nine times in 2,441 lines and never as an actor.**
`../_archive/constructs.md`, 141 lines defining the unit of the architecture, never said who
reads a construct and performs the wake.

## What was settled

**The actor is a binding, not a party.** Contract, model, tools and card, joined when work
begins and discarded when it ends. Nothing to store, index, or keep in sync.
`../foundations/the-binding.md` carries it.

**The core acts at layer two, and its action is selection.** It opens the folder's contract and
picks the model. It composes nothing. This resolved several passes of disagreement about where a
construct begins and the core's duty ends, and it preserves the hardest line in the architecture:
a model may select which model runs, and may never write what the work is told to do.

**The BBS is the engine, not a docket.** Its five fields are questions the core cannot skip, so
the act of writing a card is the deliberation and the card is what it leaves behind. This is the
interface that separates this method from the one it amends: ICM owns everything inside a
folder, and this owns the gap between folders.

**Writing a card and playing it are separate acts.** A written card is inert. The gap is the
operator's review window, and it turns "nothing fires that the operator could not have read
first" into a mechanism.

**Two modes, one machinery.** A folder is built or under construction, `ROUTER.md` holds which,
and the core sends a miller or a builder accordingly. That closed the gap between milling and
building without a second mechanism, and it makes an empty folder holding one contract a
legitimate unit of work.

**Two documents, opposite directions.** `CONTRACT.md` in, `CONTEXT.md` out, never the same file.
An agent that overwrites its own instructions makes the next run build on the previous run's
self-report.

**The completion condition is an emitted contract.** A purely mechanical check proves completion
rather than quality. A quality review by the core produces a send-back loop that converges on the
operator doing the work; that was tested rather than reasoned about. Making the agent describe
what it built, in the form the workspace uses, forces it to contend with its own output, and
what it buys is review cost.

**Withholding runs both ways.** The agent is blind to the picture. The core is blind to the work.
The second half was missing from the first pass, and it is what keeps the core's judgment clean
over a long session.

**Scope is geography.** The agent is sent to a folder as its working directory. A contract asking
a reader to stay put can be declined; a boundary cannot.

**Archive, never delete.** Inherited from ICM, now recorded as a hard line.

## What this supersedes from 2026-08-25

| Ruling then | Now |
|---|---|
| Tier belongs on the construct | Constructs are dissolved. Tier is on the card, resolved in `../rungs.md` |
| Evaluation criteria live one level above the stage | Restated as authorship. Whoever writes the card writes the acceptance, never the party doing the work. The positional version depended on a relative path that cannot resolve for a reader with no location |
| The board replaces ICM's stage ordinality | Wrong, and a worse claim. Ordinality becomes per card rather than per tree. Numbered folders keep sequence wherever it is permanent |
| Activation is triggered by arrival | There is no traversal. Activation is triggered by authorship: a card exists, so something can run |
| A woken agent sits on rung five | Levels measure authority, rungs measure capability. Two ladders shared one word until today |
| The judgment rung | Removed from the ladder. It named the core, which no card can declare, and the work listed under it is work `../mechanics/evaluation.md` forbids a woken agent |
| `hands-down` as the control surface | The working directory is the control surface. A list can be reached past; a boundary cannot |
| A construct hands down, never lets an agent look up | Same rule, re-addressed. A construct is a list and can neither permit nor forbid. The core assembles the payload |

## What was verified rather than asserted

**Upstream ICM is not a newer version of the vendored skill.** The `icm-architect` skill does not
exist in the method repository, which lives at
https://github.com/RinDig/Interpretable-Context-Methodology. That repository carries fifteen
numbered patterns, checkpoints and stage audits; the skill carries the five forms, the walk test
and the build and restructure modes. Neither contains the other, the copyright strings differ, and
`../amendment/icm-upstream/VENDORED.md` records the comparison.

Following the plan literally would have replaced the skill with the repository and orphaned five
citations, including the fit argument in `../amendment/the-amendment.md` which depends on the
five forms. Both are now vendored, side by side.

**Four upstream patterns were being reinvented here.** Selective section routing, checkpoints,
stage audits, and docs over outputs. The third is most of the mechanical half of acceptance and
was about to be written from scratch.

**The bundle's own pointers did not all resolve.** `tools/audit.py` found five on its first run
against this tree: three unanchored paths that a person could read but a script could not, and
two stale. Fixed in the same pass. That is the first time anything in this repository was
checked rather than reviewed.

## What is still open

**Nothing has run.** No card has been written, no binding assembled, no folder built, no ignition
scheduled. `tools/audit.py` has been exercised against this repository and against a synthetic
folder, and never against real returned work.

**No model has been tried at any rung.** Every number in `../rungs.md` comes from asking a model
to reply with the word "ok", which measures reachability and latency and says nothing about
quality. The test that would settle it is one folder, three runs on identical input, and a diff
of the three emitted contracts. Until then the emitted-contract mechanism is a design rather
than a finding.

**Gate width.** How many returns the core can judge in one pass. Unchanged, and still comes from
a measured run.

**Ignition scheduling.** Unchanged. Cloud routine against in-session loop, still the blocker for
the one thing in the architecture that pushes.

**The scout.** A wake that returns cards rather than product is the answer to building work whose
shape is not yet known. Not built. Until it is, the operator writes every card for unscoped work,
which is founding problem two in better clothes and is an accepted cost rather than an oversight.

**Reconciliation.** Still the least exercised part, now correctly attributed to the core and still
with no implementation behind it.

## Source

Operator and session, 2026-08-26. The reframing of the board from docket to engine, the
observation that its deliberation belongs to the core rather than to the agent, the two-document
split, and the completion condition are all the operator's. The triage that found the missing
actor, and the check that upstream is a different artifact from the skill, are this session's.
