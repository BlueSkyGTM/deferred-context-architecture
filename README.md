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

## The thesis

**This architecture manages resources, and converts what it saves into quality.**

Everything it manages is one quantity wearing six labels: model attention that has to be paid
for. Tokens meter its price, context its capacity, usage windows its throughput, standing
agents and live swarms its concurrency, and deterministic checks are the part of it you get
for nothing. Deferral is the single mechanism against all six. Never let a unit of work see
more than it needs.

The saving is not the point. A method whose claim was "the same work for less money" would be
an optimisation, and optimisations are optional. This one reallocates. Everything a
conventional run burns on context nobody needed is still spent: on standards written before
the work by someone not doing it, on more gates, on a judgment pass over the finished artifact
with the argument withheld, on more attempts at the hard part. The bill does not have to fall
for the method to have worked. What has to change is what the bill bought.

That is why it is affordable to be thorough here. Every one of those purchases buys method,
materials or standard, which are three of the four things that decide whether an output is any
good. The fourth, capability, is the one a conventional run spends the money on, and it is the
one that matters least.

Two of the six are not managed but abolished. A standing specialist is replaced by a card that
does not exist until it is played, and a live swarm is replaced by files that cost nothing to
hold and cost only at the moment of reading. Managing a cost and removing the need for it are
both wins, and the second is the larger one.

**And one of the six is not a money problem at all.** A usage window is throughput entitlement:
inside it, no amount payable returns the capacity before it resets. That is why the model
serving any position, the head included, is a slot resolved in one file rather than an
assumption baked into the architecture. A resource money cannot relieve is the only kind that
changes the shape of a system rather than its budget.

`foundations/the-economy.md`

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

**Deferred activation.** No agent is running and waiting. Work is named on a card, and a written
card is inert: no model committed, no spend, nothing running, until someone plays it. Nothing
costs anything until then, so the set of specialists a system can call is unbounded, because
none of them exist until called. The gap between writing a card and playing it is where a person
can still read it.

**Deferred scope.** What does wake is put in a folder and handed a card. What it can reach is
what is in that folder. It cannot read the wider system and cannot see what other agents did.
That makes it a genuine outsider to work it did not produce, which is the one condition under
which its judgment is worth having. Enforcing that by boundary rather than by instruction
matters: a request to stay put can be declined, and a working directory cannot.

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
| **Materials** | The specific facts this task needs, and the ones it must not see | The folder the agent is put in |
| **Standard** | What counts as done, and who says so | Written before the work by someone who is not doing it |
| **Capability** | Raw model horsepower | One line on the card, resolved in `rungs.md` |

Persona is not on that list. "You are a senior specialist in X" adds nothing to any of the
four, which is why libraries of ready-made agent prompts are mostly costume. The other three
parts belong to a particular practice and cannot be distributed.

Capability is also the smallest of the four for most work. A strong model with no method, no
materials and no standard produces confident garbage; a modest one with all three produces
something shippable. Three of the four are yours to write, once, in files that accumulate.
That is why routing work to a cheaper model is not a quality cut, and it is what makes the
thesis above cash: the resource deferral frees is fungible into exactly the three parts that
dominate the outcome.

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
| The binding | The hearing | An occasion where that law is applied and can return a no |
| The board | Where a hearing gets scheduled | What is outstanding, judged how, and what was decided |

**A file cannot fail.** That is the gap this fills. A context file is read, and whatever the
reader does next is the outcome. It has opinion; it has no courtroom. The binding is the moment
of execution that a file structurally lacks.

### The card

A card is a work order. It is written, and then, separately, played.

```
wing:     storefront                whose charter governs, and therefore what is permitted
door:     stages/03-build/          the folder, which is also the boundary
mode:     built                     so a miller goes, not a builder
tier:     build                     which rung, resolved in rungs.md
done:     output/pricing.html exists · npm run check passes · no TODO strings
escalate: brand colours not in the design system -> stop and file, do not infer
```

Five of those fields are questions, and none can be filled without a decision. That is the point: **the act of writing
a card is where the core is forced to think**, and the card is what the deliberation leaves
behind, dated and diffable and readable before it commits anything.

`escalate` is not optional. A cheap tier will meet something its contract does not cover, and
without a named exit it will guess.

**Every card and every contract is written by hand.** A model may select which model runs. It
may never write what the work is told to do. A prompt composed at runtime is not an artifact: it
cannot be read, diffed, or improved, and no record of it survives the call.

`mechanics/the-bbs.md`, `foundations/the-binding.md`

### Miller or builder

The same machinery runs both kinds of work, and one file decides which.

A folder that is **built** holds a standing `CONTEXT.md` and gets a miller: the stage runs and
produces product. A folder **under construction** holds an issued `CONTRACT.md` and gets a
builder: it produces the folder itself, and its last act is to emit the contract a future run
would be handed.

That emitted contract is the completion condition, and it is the answer to a problem with no
good alternatives. A purely mechanical check proves completion rather than quality. A quality
review by the core produces a send-back loop that converges on the operator doing the work.
Making the agent describe what it built, in the form the workspace uses, forces it to contend
with its own output, and incoherence shows up in twenty lines instead of four hundred.

`mechanics/the-router.md`, `mechanics/the-two-documents.md`, `mechanics/acceptance.md`

### Wings, and what a charter grants

A folder is a boundary. A **wing** is a folder holding folders, and it is a boundary too. Only
the size of the wall changes.

Each wing carries a `CHARTER.md`: the territory it owns, the paths outside itself it may reach,
which rungs it is permitted, what it may spend, and what it must refer upward. Every field is
checkable, and prose with no pass condition fails its own audit, because a charter is an
operations config rather than a description of a personality.

**Absence is prohibition.** A wing reaches outside itself only where its charter names the path.
That rule is what keeps the shared layer from quietly becoming a hole: this method uses one of
ICM's five workspace forms, the umbrella, because it is the only one with more than one wall in
it, and an umbrella's whole purpose is a shared layer several pipelines can read.

Two wings whose exercised charters come out substantially identical are one wing. A wing with no
card played against it in a long stretch is the same finding wearing the opposite symptom.

`templates/CHARTER.md`, `mechanics/the-router.md`

### The gate

Everything above is prose, and prose is read by the party with an interest in not following it.
One rule is not: `tools/hooks/card_gate.py` is a harness hook that refuses a write into a working
folder unless a played card names that folder and the path sits inside the wing's chartered
territory.

Three layers were available and only the last is a default.

| Layer | Enforced by | Strength |
|---|---|---|
| an instruction in a context file | the model choosing to comply | a request |
| a skill | the model deciding it applies | a method |
| a hook | the harness | a default |

It fails open and says so, because a gate that failed closed would turn any bug in itself into a
tree nobody can edit. The price of that is a gate that could die quietly, so every run the
harness starts stamps a file, and `python3 tools/audit.py --harness` reports whether the gate is
actually live on this device. Never fired reports as not live.

`templates/harness/README.md`, `decisions/2026-08-26-the-gate.md`

### The rungs

Three tiers a card can name, one of which is not a model at all.

| Rung | For |
|---|---|
| **none** | Work that is not a model question. Counting, listing, diffing, confirming a path |
| **fetch** | Retrieval that returns facts and makes no decisions |
| **build** | Executing a complete specification |

Deciding is not on that list, and that is deliberate. Fit, precedence and whether a contract was
right are the core's own work, done before a card is written or after a result comes back. A
card cannot declare the core, because the core is what reads the card.

Cards declare a rung. One file, `rungs.md`, says which model serves that rung today.
Changing supplier is an edit there and nowhere else, which is the whole of what model
agnosticism requires. Vendor choice is a cost decision only; it buys nothing on independence.

`mechanics/tiering.md`, `rungs.md`

---

## What it costs

Stated plainly, because the tradeoffs are real and none of them is hypothetical.

**Depth is never something an agent goes and finds.** An agent that cannot see the picture can
check work against its contract and cannot ask whether the contract was right. The quality of
the whole system is the quality of what gets handed down. If the folder and the card are thin,
the output is thin, and nothing in the run will tell you so.

**Independent specialists produce work that does not automatically match.** The uniformity you
get free from running one template repeatedly has to be paid for once depth is bought. That
bill is `mechanics/reconciliation.md`, and it is the weakest file here.

**Nothing fires where no card is written.** That is worse than it sounds, because there is no
traversal left to stumble over a rotting folder by accident. One scheduled walk closes the gap,
and it carries no method of its own: it notices, it writes a card, and it stops. Playing that
card is somebody else's decision.

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
│   ├── the-economy.md                   what is managed, and what the saving buys
│   ├── the-binding.md                   what actually wakes, and why nothing is stored
│   ├── constraints-over-capability.md   why the strong model decides and does not type
│   ├── authority.md                     whose call is this, and what a woken agent may not do
│   └── failure-modes.md                 the ways this goes wrong and reports fine
│
├── mechanics/              how it runs
│   ├── the-bbs.md                       where the core is forced to think
│   ├── the-router.md                    which folders are built, which are being built
│   ├── the-two-documents.md             issued contract in, emitted contract out
│   ├── acceptance.md                    judging finished work without reading it
│   ├── tiering.md                       the rungs, and the one that is not a model
│   ├── writing-for-an-unknown-reader.md contracts a second-hand model can execute
│   ├── ignition.md                      the scheduled walk, its caps, what it may never do
│   ├── evaluation.md                    who says no, and who wrote the standard
│   └── reconciliation.md                two branches disagreed
│
├── templates/              copyable starting points: card, contract, charter, router, findings
│   └── harness/                         installing the gate into a host system
│
├── origins/
│   ├── divergence.md                    what was inherited, and where the aims part
│   ├── the-machinery.md                 every upstream pattern, with a verdict
│   ├── icm-architect/                   the ICM skill, vendored under MIT
│   └── icm-upstream/                    ICM's current conventions, vendored under MIT
│
├── decisions/              what was settled, what is open, what is broken
├── _archive/               superseded files, each with a note naming its replacement
├── rungs.md                which model serves which rung today. The only file naming one
├── lineage.md              what was brought in, from whom, and what is ours
├── tools/                  four executable files. One probes a vendor, two read a tree
│   ├── fingerprint.py                   what a tree structurally is, for comparing later
│   └── hooks/card_gate.py               and one refuses the write, which is the gate
├── HANDOFF.md              the first run, and what was predicted of it beforehand
├── handoff/                its references: known limits, how to score, how to continue
└── .claude/                the gate's registration, and two skills: architect and delegate
```

---

## What is still missing

This is the section to read before deciding whether to build on any of it.

**Nothing here has been run.** The architecture is specified and documented. No card has been
written, no binding assembled, no ignition scheduled, and no cost measured at any rung. Every file in `mechanics/` is a first version by a convention that says depth is earned
by a second and third run rather than designed in advance.

Specifically, and in the order that matters:

| Gap | State | What closes it |
|---|---|---|
| **No adoption surface** | `templates/` and `tools/audit.py` now exist. Nothing in either has been used against real work | Write one card against one real folder and play it |
| **The card shape is a proposal** | The five fields have never been written for real work, played, or audited. Whether a folder plus a card carries enough is a guess | Write one against a real stage and see which fields survive |
| **No model has been tried at any rung** | Every measurement in `rungs.md` comes from asking a model to reply with the word "ok". That proves reachability and latency. It says nothing about quality | Run one folder three times on identical input and diff the emitted contracts |
| **Tiering is reasoned, not measured** | The claim that this reduces spend is the premise of the architecture and is untested. No run has been costed at any rung, so the reinvestment thesis is reasoned rather than demonstrated | One real run, costed per rung, with the saving traced to what it bought |
| **Nothing has been transmitted to another model** | `.claude/skills/dca-architect/` is the attempt. Whether the umbrella, the charter and proposes-never-settles survive being handed to a model that has only the files is untested, and it is the question the whole method rests on | `HANDOFF.md`, and the run it mandates |
| **The gate has never refused real work** | It is installed, and eight defeat attempts in a sandbox behaved. No wing exists, so it has never stood between the core and work it actually wanted to do. Its enforcement stops at spend: territory, the charter's rung ceiling, and which party is writing are all checked, but the gate sees a write rather than a bill | One chartered wing, and one honest attempt to work around it |
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
folder structure does the orchestration a framework would otherwise do in code. ICM is vendored
twice under `origins/`, both under the MIT licence with their own LICENSE files: the
`icm-architect` skill, which teaches how to design a workspace, and the method repository's
core, which specifies the conventions one must follow.

**This descends from ICM rather than amending it.** ICM's stated goal is one agent doing what a
framework would otherwise do. This method's goal is many bounded agents, and the instincts run
opposite: ICM consolidates toward one roof, this defers toward many. Consolidate an ICM workspace
and it gets simpler. Consolidate this one and it stops working, because there is nothing left to
defer between.

The axis underneath that split is the thesis above. **ICM optimises for a picture a person can
read. This optimises for a bill a person can afford to spend well**, while keeping enough of that
legibility to stay auditable. Resource management is what this method adds; interpretability is
the constraint it is not permitted to spend.

What is inherited is everything inside a folder, and it is load-bearing rather than borrowed:
blindness is only safe because the picture stays in human-readable files. What is added is the
gap between folders. `origins/divergence.md` and `origins/the-machinery.md` carry the detail,
pattern by pattern. Everything ICM guarantees has to keep holding, and one guarantee in particular is
load-bearing rather than merely nice: a person can open any folder and see what state the
system is in. Blindness is only safe because the picture stays in human-readable files. Start
encoding that picture in agent configuration instead and this becomes the opaque thing it was
built to avoid.

`origins/divergence.md`, `lineage.md`, `NOTICE.md`

---

## Licence

The original work in this repository is MIT, copyright 2026 BlueSkyGTM. The vendored ICM
bundle under `origins/icm-architect/` is separately MIT, copyright 2026 Jake Van Clief, and
carries its own LICENSE file. See `NOTICE.md`.
