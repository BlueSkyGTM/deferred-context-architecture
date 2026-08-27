# 2026-08-25 Founding session

The session in which Deferred Context Architecture was named and specified. Recorded as a
deliberation ledger rather than a summary: what was settled, what was rejected, and what is
still open, so a later session does not re-derive it or reopen it by accident.

## What started it

Four problems, brought by the operator, which turned out to be one problem seen from four
sides.

1. **ICM restructuring fires on the wrong signal and fires blind.** The trigger is the
   operator noticing degradation, so repair is always late. When it does fire, the skill reads
   the folder, while the information deciding which of the five forms fits lives in the
   surrounding contracts.
2. **No router exists for build work.** Task routing serves the business, where a named task
   has a known destination. Building comes from excavation, experimentation, and deliberation,
   which has no destination at the start, so the operator is the router, turn by turn.
3. **Ending a session costs most when the build is rawest.** A handoff preserves settled
   conclusions and drops live deliberation, which is what an unfinished build is made of.
4. **No model routing.** Standard guidance assumes a task is complex or simple, while real
   plans braid both, forcing every run to the top tier.

The loop underneath: poor structure raises prompting cost, prompting cost burns the window,
the window ends sooner, ending is unaffordable, so the session continues and the structure
decays further before anything fires on it.

## What was settled

| Ruling | Note |
|---|---|
| Loops are the primitive | A loop is the only thing that moves the trigger off the operator |
| The two deferrals are activation and scope | The operator's refinement. Time is a symptom; activation is the mechanism |
| Independence comes from withholding, not from model variation | The contamination is a context property, so the fix is a context property |
| Capability is per decision, cost is per token | They need not land on the same model. The strong model decides and does not type |
| A fourth rung exists below the cheapest model | Work that is not a model question. It saves most because it costs nothing |
| Tier belongs on the construct | Capability becomes a property of position rather than a decision on arrival |
| The orchestrator is dissolved, not centralised | Stripe's constraint discipline survives the inversion. The dispatcher does not |
| One push tick is required | Pull-based activation is blind at unvisited nodes, which is where decay lives |
| Evaluation criteria live one level above the stage | Otherwise a stage writes its own passing grade and the loop reports green forever |
| A woken agent proposes, never settles | It sits at level five and cannot see the ladder |
| Multi-agent swarms are declined | Sub-agents are taken for verification and cheap limbs. Worktrees and parallel fan-out are not |
| ICM stays underneath | Remove it and DCA becomes the opaque thing the operator rejected |

## What was rejected, and why

**Model swapping as the route to a sceptical evaluator.** Not wrong, but it pays twice for a
property deferred scope already provides. Retained as an option where two genuinely
independent readings are worth the money.

**A swarm woken and fed prompts.** Resident cost with no matching benefit at this scale. The
book's own text concedes that worktrees are optional for a loop running one agent at a time,
and worktrees earn their keep only at Stripe-scale parallelism.

**Vigilance as the guard against cognitive surrender.** Willpower is not a control, and it
degrades exactly when the loop runs well. Replaced by the structural version: nothing
structural moves without a ruling.

**Treating DCA and ICM as siblings in the host system.** The operator's call: siblings compete and
make a mess. Fork from the host system, amend, feed back, and it stays one system.

## What is still open

| Question | Why it matters | Status |
|---|---|---|
| Does ignition run as a cloud routine or an in-session loop | Decides whether the trigger leaves the operator's machine at all | Leaning cloud, per `../mechanics/ignition.md`. Not settled |
| What the drift threshold is | Too tight and every tick wakes something. Too loose and this reproduces the original problem | Open. Needs a first run to calibrate |
| Where the deliberation ledger lives, and its shape | It answers problem three, and the book's memory model is a checkpoint rather than a ledger | Open. Named as a need, not yet designed |
| Whether the parent or the level above it holds reconciliation authority | Sibling coherence has a procedure and no run behind it | Provisionally the parent, per `../mechanics/reconciliation.md` |
| Whether DCA becomes a standalone repository | Currently a folder on a branch of the host system, which is a fork that feeds back | Open. A subtree split promotes it later if wanted |
| Verification of product specifics | Command names, version numbers, interval floors, and expiry windows came from a secondary source | Unverified. Flagged at each point of use |

## Known defects and unfinished work

Recorded here rather than in a file of their own, so the state of this workspace lives beside
the reasoning that produced it. Appended with a date rather than rewritten.

### Defects

| id | What is wrong | Why it matters |
|---|---|---|
| `shared-tool-touched` | The host system's pointer checker had to gain a vendored-tree skip so its whole-repo check stays clean with ICM vendored inside this bundle. A shared tool widened for one workspace's benefit | The skip is categorised and prints under a verbose flag, so it is visible rather than silent. It still widens a check everything else depends on, and a second vendored tree will want the same treatment. Anyone vendoring this bundle inherits the same problem |
| `conventions-tension` | The host system's own conventions record that ICM was absorbed rather than vendored, with its naming section deliberately not carried. ICM is now vendored whole in `origins/icm-architect/` | Both calls stand for different purposes and `lineage.md` says so. A reader meeting the conventions note alone will think the vendoring is a mistake to correct |

### Unfinished

Specified and never run. Each is a first version by the house convention that depth is
earned by a second and third run.

| id | What is missing | Consequence if trusted as is |
|---|---|---|
| `reconciliation-unrun` | `mechanics/reconciliation.md` has a responsibility and a procedure and no implementation behind it. The weakest file in the workspace | Sibling divergence is the one failure mode with no tested guard. The first parallel run should be expected to rewrite the file |
| `construct-unexercised` | The frontmatter shape in `../_archive/constructs.md` is a proposal. No construct has been written, fired, or audited | Superseded 2026-08-26: the frontmatter mechanism was replaced by the binding, and the defect stands in the new form. See `../decisions/2026-08-26-the-binding-and-the-bbs.md` |
| `ignition-unscheduled` | No walk is scheduled. No fingerprint format is implemented, no threshold set, no cap configured | The unvisited-node hole that ignition exists to close is currently open. Structural decay still waits on the operator noticing |
| `tiering-unmeasured` | The four rungs are reasoned, not measured. No run has been costed at any rung | The claim that this reduces spend is untested. It is the premise of the whole architecture |

### Verification owed

| id | What is unverified | How to close it |
|---|---|---|
| `secondary-source` | Command names, version numbers, interval floors, and the expiry window for in-session loops came from a book summarising blog posts and a podcast. Not checked against current documentation | Read the current product documentation before building anything that depends on a specific. Flagged at each point of use, notably in `mechanics/ignition.md` |

### Not defects

Recorded so they are not "fixed" by a later session.

**This workspace is a folder rather than a standalone repository.** That is a fork of the
host system that feeds back, which is what the operator specified. Promoting it remains
available and is listed as an open question, not a defect. *(Superseded 2026-08-26 by the
extraction note at the end of this file.)*

## Second pass, same day: the board

The founding session specified how an agent is woken. It did not answer what decides which
work is woken next, and the operator named that as the gap that had made building unsustainable:
constant turn-by-turn routing, then a handoff that preserved conclusions and dropped the
reasoning behind them.

### What was settled

**The board.** A mutable file holding what is outstanding, in what order, and what counts as
done. Superseded 2026-08-26 by `../mechanics/the-bbs.md`; the original is `../_archive/the-board.md`.

**Mandate and method are separate artifacts.** The board says which work, in what order, and
what finishing means. The context file behind the named door says how that work is done. Two
opposite lifetimes: stable files cacheable, the volatile board read late.

**A card names its door and carries its own definition of done.** Without the first, the agent
picks its route at runtime and the dispatcher returns. Without the second, the card is marked
done by whoever came back from it.

**The core persona is the sole author of the board.** Agents write output to the path their
construct named and return the path. This closes the dead-agent case: an unmoved card beside a
missing output is legible where a lost transcript is not.

**The board is the file. The ledger is git.** A committed file already carries current state
and append-only history. A second artifact was proposed and dropped.

**A file cannot fail.** The buildable statement of what ICM lacks, replacing the looser
complaint that it has no opinion. ICM keeps everything on disk, which is right; nothing on that
disk ever gets a turn. Three parts close it: the context file is the law, the construct is the
hearing, the board is the docket.

**Independence is positional, not intellectual.** An agent's contribution is the seat it
occupies, not the weights behind it.

**Every construct is written by hand.** A model may select which one fires and may never compose
what one says. Borrowed prompt libraries were considered and rejected: they hold roles rather
than judgments, and a prompt's debugging surface is its author's understanding of it.

**Fan out only where the merge is mechanical.** Partition so combining is concatenation, or run
a relay. Width is capped by how many results can be gated in one pass, never by a vendor's
concurrency ceiling.

**A foreign model at the fetch or build rung is a cost decision only.** It buys nothing on
independence. Constructs name rungs; one mapping file names the models.

### What this pass corrected from the first

**Agents do not record their own state.** The founding pass had a woken agent appending to a
ledger on its way out. That is write contention across concurrent agents, and worse, it is a
stage stating whether it passed. Superseded by sole core authorship.

**The standalone ledger is superseded** by the board plus git history.

### What was verified rather than asserted

Prompt caching is a prefix match over tools, then system, then messages; a fork that rebuilds
any of those with a difference misses the parent's cache entirely; caches are scoped to one
model. Checked against the bundled claude-api skill reference rather than recalled. The
consequence is that fan-out is the one topology in which every worker pays full uncached input,
which explains the earlier iteration's token detonation as structural rather than unlucky.

### What is still open after this pass

**Ignition scheduling.** Unchanged and still the blocker: cloud routine against in-session
loop.

**Z.ai plan shape.** Whether flat or metered, and which of the listed models the plan actually
covers. Test calls owed before any topology assumes the answer.

**Gate width.** How many returned results the core can genuinely judge in one pass. Comes from
a measured run.

**Nothing has run.** No board exists, no construct has fired, no cost has been measured. Every
file named above is a first version.

### The reframe: what the architecture is actually about

Late in the second pass the operator identified the four-part decomposition of output quality
as upstream of the two deferrals rather than beside them, and asked for it recorded as the
heart of the method.

The decomposition: **method, materials, standard, capability**, with no fifth contributor, and
capability the smallest term for most work. Written up in `../foundations/the-four-parts.md`.

Why it was accepted rather than filed as a restatement. Every mechanic in the workspace maps
onto one of the four given a mechanism, and the mapping is exhaustive: the board picks a door
and so fixes three of them, the construct delivers all four, tiering is capability, evaluation is
standard, ignition decides whether a door is reached, reconciliation handles siblings that
assembled the four differently. `../foundations/the-two-deferrals.md` already ended on the law
that an agent
is exactly as good as what its construct encodes; the four parts are what that sentence
decomposes into, so the relationship was already implied and only needed naming.

The architecture is therefore named after its method rather than its claim. Recorded here so a
later reader does not mistake the name for the thesis.

Three questions this settled that had been recurring:

- **The expert registry.** Rejected for the last time. A registry of experts is a registry of
  costumes, since the three parts that matter are fixed by which door the work enters. What is
  worth having is a generated index of construction conditions, which is a different artifact and
  is not yet built.
- **Prompt libraries.** Same reason, now stated positively rather than as a prohibition.
- **Where expertise comes from.** It is already written. It is the context files behind the
  doors, which is to say the practice the host system already documents.

## Provenance

Method sources and what is this project's own are separated in `lineage.md`. The
loop-engineering material entered the session as a PDF supplied by the operator: HuaShu,
*Loop Engineering: The Complete Guide*, v260615, June 2026 edition, 36 pages.

## Extraction, 2026-08-26

This bundle was lifted out of the private system it was written inside and published as a
standalone public repository. That closes the open question above about whether DCA becomes
its own repo. The answer is yes, and the reason is not tidiness.

**A private method folder drifts toward its owner.** Every mechanic here was written with one
system's accounts, wings, and conventions within reach, and reaching for them is free. Nothing
in the architecture requires that content, and any file that quietly assumed it was a file
that had stopped being a method and started being a configuration. Publishing removes the
temptation by removing the access.

### What changed in the move

| Change | Why |
|---|---|
| One host system's name replaced throughout with **the host system** | The architecture installs into any workspace. The name of the one it was born in is not a property of it |
| The authority ladder generalised, and its requirement stated | The five rungs are load-bearing. Which five they are is the installer's call |
| The probe promoted to `tools/probe_models.py` | It was living outside the bundle in the host system's integrations folder, which meant `rungs.md` cited a file its own readers could not see |
| One private audit finding removed | It counted unreferenced files in a system nobody reading this can open. It taught nothing about the method |
| A duplicated paragraph in **Unfinished** deleted | Straightforward defect |

### What did not change

No claim was softened, no defect was dropped, and nothing in **Known defects and unfinished
work** was closed to make the repository look better than it is. The status is what it was
yesterday: specified, not exercised.

### What the extraction did not fix

The bundle still contains no board, no construct, and no ignition. It contains exactly one
executable file, and that file measures a vendor rather than running any part of the
architecture. Publishing changed where the work lives. It did not run any of it.
