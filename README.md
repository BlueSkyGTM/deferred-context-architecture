# Deferred Context Architecture

A way of running AI agents in which no agent ever sees the whole picture, and that is the
point rather than a limitation.

It is a method, not a framework. There is nothing to install and no runtime to adopt. What is
here is a set of files describing how to arrange a workspace so that agents are woken by
traversal rather than by a dispatcher, and so that what wakes is structurally incapable of
believing its own reasoning.

Throughout, **the host system** means whatever workspace you install this into: your repo,
your folder tree, your contracts. This bundle was extracted from one such system and
deliberately carries none of its content.

---

## The defect it exists for

An agent that finishes a task thoroughly reports that the task went well. Thoroughness is
something it can observe about its own work. Correctness is not, so it substitutes one for the
other and returns confidence it has not earned.

The failure is quiet. Nothing errors, every stage reports success, and the work is wrong in
ways only a reader with the wider picture could catch. Operators reading this as a model
failure respond by instructing harder, which adds more material for the agent to be persuaded
by, and the next run is worse for reasons that look like the model again.

The defect is not in the model. It is in what the model can see. By the time an agent judges
its output, its window holds the reasoning that produced that output, so it reads the argument
rather than the artifact. Ask it to check its work and it checks the argument, finds it sound,
because it is the argument it just made.

`foundations/completion-fallacy.md`

---

## What it does about it

If the defect is a property of context, the fix is a property of context. Do not ask an agent
to be sceptical about what it can see. Change what it can see.

Two deferrals do that work.

**Deferred activation.** No agent is running and waiting. The instruction to wake one lives in
the context file for the folder whose work it governs, and does nothing until a task arrives
at that file. Nothing costs anything until it is reached, so the set of specialists a system
can call is unbounded, because none of them exist until called.

**Deferred scope.** What does wake is handed its contract and its inputs, and nothing else. It
cannot read the wider system and cannot see what other agents did. That makes it a genuine
outsider to work it did not produce, which is the one condition under which its judgment is
worth having.

Independence here is manufactured by withholding, not bought by switching vendors. A second
model handed the same transcript reads the same argument and agrees for the same reason. The
variable that matters is what is in the window.

`foundations/the-two-deferrals.md`

---

## The claim underneath

The deferrals are the method. The architecture is named after them, which is slightly
misleading, because the claim they serve is smaller and more useful.

**Four things determine whether an output is any good, and there is no fifth.**

| Part | What it is | Where it lives |
|---|---|---|
| **Method** | How this kind of work is done here | The context file behind the door |
| **Materials** | The specific facts this task needs, and the ones it must not see | `hands-down` on the construct |
| **Standard** | What counts as done, and who says so | One level above the stage being judged |
| **Capability** | Raw model horsepower | One line on the construct, resolved in `rungs.md` |

Persona is not on that list. "You are a senior specialist in X" adds nothing to any of the
four, which is why libraries of ready-made agent prompts are mostly costume. The other three
parts belong to a particular practice and cannot be distributed.

Capability is also the smallest of the four for most work. A strong model with no method, no
materials and no standard produces confident garbage; a modest one with all three produces
something shippable. Three of the four are yours to write, once, in files that accumulate.
That is the whole economic argument, and it is why routing work to a cheaper model is not a
quality cut.

The consequence for anyone building on this: **expertise is assembled, not summoned. The
specialist is the position, not the occupant.**

`foundations/the-four-parts.md`

---

## How it actually runs

Three artifacts, and it is worth naming what each one is for, because the distinction is what
the architecture turns on.

| Artifact | Role | Holds |
|---|---|---|
| The context file | The law | What good work is, for this kind of work |
| The construct | The hearing | An occasion where that law is applied and can return a no |
| The board | The docket | What is outstanding, in what order, and what was decided |

**A file cannot fail.** That is the gap this fills. A context file is read, and whatever the
reader does next is the outcome. It has opinion; it has no courtroom. A construct is the
moment of execution that a file structurally lacks.

### The construct

A construct is frontmatter on a stage contract. It names what is assembled when work reaches
this point, and exactly what that thing is allowed to see.

```yaml
---
constructs:
  - when: the variation that selects this branch, stated as a condition
    wakes: what is woken, named
    tier: none | fetch | build | judgment
    hands-down:
      - exact/path/to/contract.md
      - exact/path/to/ruling.md
    returns: the artifact, named, and where it lands
    judged-by: ../CONTEXT.md#criteria
    escalates-when: the condition under which this stops and files instead
---
```

`hands-down` is the control surface of the entire architecture. It is the only channel through
which your judgment reaches a blind agent, and it is an allowlist rather than a denylist on
purpose: a denylist requires you to predict what an unknown reader might wrongly reach for.

`escalates-when` is not optional. A cheap tier will meet something its contract does not cover,
and without a named exit it will guess.

**Every construct is written by hand.** A model may select which one fires. It may never
compose what one says. A prompt composed at runtime is not an artifact: it cannot be read,
diffed, or improved, and no record of it survives the call.

`mechanics/constructs.md`, `mechanics/writing-for-an-unknown-reader.md`

### The board

A mutable file holding what is outstanding, in what order, and what counts as done. The board
carries the mandate; the context file behind the door it names carries the method.

A card carries two fields that separate a work order from a wish: **the door**, meaning the
entry point rather than only the task, and **its own definition of done**. A card with no
acceptance condition cannot be gated, so it gets marked done by whoever returns from it, which
is the completion fallacy with a card number attached.

The core persona is the sole author of the board. An agent writes its output to the path its
construct named and returns that path. The board is the file; the ledger is git.

`mechanics/the-board.md`

### The rungs

Four tiers, one of which is not a model at all.

| Rung | For |
|---|---|
| **none** | Work that is not a model question. Counting, listing, diffing, confirming a path |
| **fetch** | Retrieval that returns facts and makes no decisions |
| **build** | Executing a complete specification |
| **judgment** | Deciding. Emits little, decides much |

Constructs declare a rung. One file, `rungs.md`, says which model serves that rung today.
Changing supplier is an edit there and nowhere else, which is the whole of what model
agnosticism requires. Vendor choice is a cost decision only; it buys nothing on independence.

`mechanics/tiering.md`, `rungs.md`

---

## What it costs

Stated plainly, because the tradeoffs are real and none of them is hypothetical.

**Depth is never something an agent goes and finds.** An agent that cannot see the picture can
check work against its contract and cannot ask whether the contract was right. The quality of
the whole system is the quality of what gets handed down. If `hands-down` is thin, the output
is thin, and nothing in the run will tell you so.

**Independent specialists produce work that does not automatically match.** The uniformity you
get free from running one template repeatedly has to be paid for once depth is bought. That
bill is `mechanics/reconciliation.md`, and it is the weakest file here.

**Pull-based activation is blind where nothing arrives.** Activation that waits to be reached
never fires at an unvisited node, which is exactly where structural decay happens. One
scheduled walk closes that gap, and it carries no method of its own: it notices and it names,
and everything else is a finding that waits for a ruling.

**Fan-out is the one topology where every worker pays full uncached input.** Prompt caching is
a prefix match; a fork that rebuilds any of the prefix misses the parent's cache entirely. So
fan out only where the merge is mechanical, meaning a partition whose combination is
concatenation, or a relay. Width is capped by how many results can be gated in one pass, never
by a vendor's concurrency ceiling.

---

## What is in here

```
deferred-context-architecture/
├── CONTEXT.md              the task router. Start here after this file
├── CLAUDE.md               what this workspace is, for an agent that lands in it
│
├── foundations/            the argument
│   ├── completion-fallacy.md            why this exists at all
│   ├── the-four-parts.md                what makes an output good, and what does not
│   ├── the-two-deferrals.md             what "deferred" refers to
│   ├── constraints-over-capability.md   why the strong model decides and does not type
│   ├── authority.md                     whose call is this, and what a woken agent may not do
│   └── failure-modes.md                 the ways this goes wrong and reports fine
│
├── mechanics/              how it runs
│   ├── the-board.md                     what is outstanding, and what a card must carry
│   ├── constructs.md                    the unit. What assembles an agent
│   ├── tiering.md                       the four rungs, and the one that is not a model
│   ├── writing-for-an-unknown-reader.md contracts a second-hand model can execute
│   ├── ignition.md                      the scheduled walk, its caps, what it may never do
│   ├── evaluation.md                    who says no, and where the criteria live
│   └── reconciliation.md                two branches disagreed
│
├── amendment/
│   ├── the-amendment.md                 what ICM cannot do, and how this extends it
│   └── icm-architect/                   ICM itself, vendored whole under MIT
│
├── decisions/              what was settled, what is open, what is broken
├── rungs.md                which model serves which rung today. The only file naming one
├── lineage.md              what was brought in, from whom, and what is ours
└── tools/probe_models.py   the one executable file. Measures a vendor, not the architecture
```

---

## What is still missing

This is the section to read before deciding whether to build on any of it.

**Nothing here has been run.** The architecture is specified and documented. No board exists,
no construct has fired, no ignition has been scheduled, and no cost has been measured at any
rung. Every file in `mechanics/` is a first version by a convention that says depth is earned
by a second and third run rather than designed in advance.

Specifically, and in the order that matters:

| Gap | State | What closes it |
|---|---|---|
| **No adoption surface** | One executable file in the whole bundle, and it probes a vendor. There is no template, no schema, no worked example | A board file, a construct on one real contract, and a generated index of construction conditions |
| **The construct shape is a proposal** | The frontmatter above has never been written for real work, fired, or audited. Whether `hands-down` is sufficient in practice is a guess. The `wakes` field looks redundant now that the unit is assembled rather than summoned | Write one against a real stage and see which fields survive |
| **The judgment rung is unvalidated** | Every measurement in `rungs.md` comes from asking a model to reply with the word "ok". That proves reachability and latency. It says nothing about quality | Hand a foreign model an artifact and criteria, withhold the argument, and see whether it returns a defensible no |
| **Tiering is reasoned, not measured** | The claim that this reduces spend is the premise of the architecture and is untested. No run has been costed at any rung | One real run, costed per rung |
| **Reconciliation has no implementation** | A responsibility and a procedure and nothing behind them. Sibling divergence is the one failure mode with no tested guard | The first parallel run, which should be expected to rewrite the file |
| **Ignition is unscheduled** | No walk runs. No fingerprint format is implemented, no drift threshold set, no spend cap configured | Schedule one, cap it, and calibrate the threshold against a real tree |
| **The fetch rung is unresolved** | Not unavailable. The retrieval endpoints return a server error rather than a clean rejection, which means the request shape is wrong, not the access | Find the right shape, or accept that rung zero holds it |
| **Some product specifics are second-hand** | Interval floors, expiry windows and command names came from a book summarising blog posts and a podcast, and were not checked | Read current vendor documentation before building anything that depends on a specific. Flagged at each point of use |

Known defects and the full open-questions list live in
`decisions/2026-08-25-founding-session.md`, beside the reasoning that produced them. Read it
before trusting any mechanics file. **A documented workspace is not a working one**, and this
repository is currently the former.

---

## What it is built on

**Interpretable Context Methodology**, by Van Clief and McDermott, arXiv:2603.16021, in which
folder structure does the orchestration a framework would otherwise do in code. ICM is
vendored whole in `amendment/icm-architect/` under the MIT licence, with its own LICENSE file
travelling with it.

This is an amendment to ICM, not a replacement. **ICM defers what is read. This defers what is
woken.** Everything ICM guarantees has to keep holding, and one guarantee in particular is
load-bearing rather than merely nice: a person can open any folder and see what state the
system is in. Blindness is only safe because the picture stays in human-readable files. Start
encoding that picture in agent configuration instead and this becomes the opaque thing it was
built to avoid.

`amendment/the-amendment.md`, `lineage.md`, `NOTICE.md`

---

## Licence

The original work in this repository is MIT, copyright 2026 BlueSkyGTM. The vendored ICM
bundle under `amendment/icm-architect/` is separately MIT, copyright 2026 Jake Van Clief, and
carries its own LICENSE file. See `NOTICE.md`.
