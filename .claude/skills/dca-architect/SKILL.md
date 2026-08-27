---
name: dca-architect
description: Lay Deferred Context Architecture over a folder tree, or build one from nothing. Use when someone wants a workspace where many bounded agents can be run cheaply and safely, wants an existing repo or folder tree adopted into wings with charters, a router and a board, asks to "make this a DCA", "adopt this tree", "structure this for agents that cannot see the whole", or wants a first deck of cards written for work that has never been delegated. Proposes structure and files findings; it never restructures and never grants a charter.
---

# DCA Architect

Build the tree, then get out of it. This skill produces the things a woken agent arrives into:
folders with bounded contracts, wings with charters that say what those folders may reach, a
router that says what exists, and a board where work is deliberated before anything fires.

It never does the work those folders are for. `.claude/skills/dca-delegate/SKILL.md` is what runs
afterwards, one card at a time.

**Read `CONTEXT.md` at the root of this method before proposing anything.** The files it routes
to are the authority; this skill is the procedure for applying them. Where the two disagree, the
method wins and the disagreement is worth reporting.

## What is being built, in one paragraph

A tree of bounded domains. Each domain is a **wing**, a folder holding folders, governed by a
**charter** that states what it owns, what it may reach outside itself, which rungs it may use
and what it must refer upward. Inside a wing are **folders**, each holding one job, each either
built or under construction. Work reaches a folder only through a **card** written on the board,
and the card is what makes the deliberation visible before it costs anything.

Nothing sees the whole. That is the point rather than a limitation, and every rule below exists
to keep it true.

## The one form, and its floor

ICM has five workspace forms. This method uses **one: the umbrella.** It is the only form with
more than one wall in it, and deferral needs a plurality of bounded domains. There is no form
selection step. Do not reintroduce one, and do not offer the other four as options; they are not
defective, they simply have no gap this method fits into. `origins/divergence.md` argues it.

The floor follows and is the thing most easily lost:

> **An umbrella with one pipeline is just a pipeline.**

If a tree yields exactly one wing, DCA has nothing to do there. **Say so and stop.** That is a
correct outcome, not a failure of the exercise, and reporting it honestly is worth more than
inventing a second wing so the shape comes out right. Inventing wings to reach a quota produces
two charters that are secretly the same charter, which the consolidation test then has to undo.

## Modes

Decide from what is on disk. Do not ask which mode to run.

| Mode | When | Produces |
|---|---|---|
| **build** | the tree is empty or nearly so | wings, charters, a router, a board, folders with issued contracts, a first deck |
| **adopt** | a tree already exists | proposed wings and charters over what is there, a router, a board, and findings |

### Adopt proposes. It never settles.

This is the rule most likely to be broken, because a tree being adopted is usually a tree with
obvious problems in it, and fixing them feels like the job.

In adopt mode you may **create** the method's own artifacts: charters marked proposed, a router,
a board, a findings file. You may **not** move a folder, rename anything, delete anything, merge
two folders, or edit any file that was there before you arrived. Every one of those is a
structural change, structural change is a ruling, and a ruling belongs to the operator.

Write what you would have done into `FINDINGS.md` and let it wait. `foundations/authority.md`
holds why: a woken agent sits at the bottom of the ladder and cannot see it.

## The order of work

### 1. Read the tree before deciding anything

What folders exist, what each contains, which ones carry a contract already, what has not been
touched in a long time. Do not read deeply into content yet. Structure first, because the
structure is what is being proposed and content will bias it toward whatever is loudest.

### 2. Find the wings

A wing is a **bounded domain of work**, not a category of output and not a stage in a sequence.
The test that separates them: could this part of the tree have a different answer from its
neighbours to *what may this reach, what may it spend, what must it refer upward?* If two parts
would answer identically on all three, they are one wing.

Name each wing for what is done there. Then apply the naming check to every folder as well.

### 3. Apply the naming check

**Does this name describe an activity or an artifact?** A folder named for its output cannot say
what belongs in it, so it accumulates whatever is adjacent and the boundary stops describing
anything. A mill is not named after the flour.

An artifact name is a **finding**. Renaming is structural. File it.

### 4. Draft a charter per wing

Copy `templates/CHARTER.md` and fill every field. In adopt mode, head each one **Proposed** with
the date, because a charter is granted by the operator and not by you.

Every field must be checkable. **Prose with no pass condition does not belong in a charter** and
fails its own audit: it is an operations config, not a description of a personality. If you catch
yourself writing what a wing is *like*, delete the sentence.

- **Territory**: the folders it owns. Everything else is unreachable.
- **Doors**: paths outside the territory it may reach, each with a reason. **Absence is
  prohibition.** A wing with no doors is the safest state and the default. Every door is a hole
  somebody decided to cut.
- **Capability**: which rungs, per `rungs.md`. Risk decides this, not convenience. A wing that
  can break something live should not have the cheapest model at the build rung.
- **Ceiling**: spend per card, spend per session, cards in flight.
- **Refers upward**: standing conditions that stop the work, on every job, always.

### 5. Run the consolidation test

Put the charters side by side. **Two wings whose charters come out substantially identical are one
wing.** Say so and merge the proposal. Merging is cheaper than maintaining a distinction that is
not real.

The guard on this test: only an **exercised** charter counts, meaning one amended at least once in
response to something real. Every charter you write is unexercised, so at this stage the test can
only catch charters that are identical on their face. Note that limit rather than overclaiming.

Run it the other direction too: a wing with no work anyone can name is the same finding wearing
the opposite symptom.

### 6. Mark every folder built or under construction

Derivable, so derive it rather than asking. A folder holding a promoted `CONTEXT.md` is **built**
and takes a miller. A folder holding an issued `CONTRACT.md` and no promoted context is **under
construction** and takes a builder. A folder holding neither is a finding: it is doing work
nobody has written down.

### 7. Write the router

`templates/ROUTER.md`. Wings and their charters, then folders and their modes. It holds facts
only. No order, no dependencies, no flow: order lives on a card for building work and in folder
numbering for milling work. A router that starts describing flow has reimplemented the pipeline in
a second place and the two will disagree.

### 8. Write the board, and play nothing

`templates/BBS.md`. Cards go in **Written**. Playing is the operator's act and is not yours.

Five fields, and none can be filled by reflex, because filling them **is** the deliberation:

| Field | What must be settled to fill it |
|---|---|
| `door` | which folder, and therefore which method governs |
| `mode` | built or under construction |
| `tier` | which rung serves this, within what the charter permits |
| `done` | what finished means, checkable by something that is not a model |
| `escalate` | the named condition that stops the run instead of producing a guess |

A card carries **only what the folder's contract cannot know**. Anything the folder could have
said stays in the folder, or the two drift and the one at a distance wins by recency.

**No card explains why the work matters.** Handing over the why removes the independence the
whole arrangement exists to manufacture.

### 9. Write the contracts

For each folder under construction, an issued `CONTRACT.md` from `templates/CONTRACT.md`: what
should exist when this is done stated as an outcome rather than a procedure, what it may use and
where, the audits the result must pass, what to do when the mandate does not cover the case.

The emitted `CONTEXT.md` is not yours to write. **An agent writes it as its last act and the
operator promotes it.** Never write both, and never write a contract into the file an agent will
emit; the two are opposite directions and merging them means run two builds on run one's account
of itself.

### 10. Do not install the harness

Adoption is the act that **creates** the territory the gate enforces, so a live gate refuses the
charters that would authorise it. The order is fixed and installing the gate is the last step:

1. Adopt: propose charters, router, board, findings.
2. The operator reads and **grants** the charters.
3. Then `templates/harness/README.md`, then `python3 tools/audit.py --harness` to prove it live.

Tell the operator this rather than doing it.

## Writing for a reader with no location

Everything produced here is read by something that arrives rather than navigates. It has no
memory of this session, no view of the tree above its folder, and no way to ask.

- Name what may be seen, never what may not. Predicting what an unfamiliar reader would wrongly
  reach for is a losing game; listing what is available is not.
- Never write "as elsewhere in this repo", "the usual pattern", or "match the existing style". It
  has no surroundings.
- Label an example as illustrative, or make it exact and mean it. An example beside an
  instruction reads as the instruction.
- Every path resolves from the folder the agent is put in, not from where you were standing.

`mechanics/writing-for-an-unknown-reader.md` is the full version.

## Vocabulary that must not blur

| Word | Means | Never |
|---|---|---|
| **rung** | capability, per `rungs.md`: none, fetch, build | an authority level |
| **level** | authority, per `foundations/authority.md`, five of them | a capability |
| **wing** | a folder of folders under one charter | a factory. That word is ICM's, one grain down |
| **binding** | contract, model, tools and card joined at play time | a stored agent or a persona |
| **card** | one work order on the board | a prompt, or a place to explain yourself |

A bare number belongs to a rung or a level and never to both.

## Before you hand anything over

- [ ] More than one wing, or an explicit report that this tree is one pipeline and DCA does not fit
- [ ] No two charters substantially identical, or a merge proposed where they are
- [ ] Every charter field checkable, no personality prose
- [ ] Every folder named for work rather than output, or a finding filed
- [ ] Every folder marked built or under construction, derived from what is on disk
- [ ] No placeholder left anywhere: a card carrying `<` cannot be played, and the gate refuses it
- [ ] Every card's `door` inside its wing's territory and `tier` within its charter's capability
- [ ] Every card has a non-blank `escalate`
- [ ] Nothing outside the method's own artifacts was created, moved, renamed or edited
- [ ] Findings filed for everything you wanted to fix and did not
- [ ] `python3 tools/audit.py --repo <tree>` clean
- [ ] No em dashes

## The two intakes

`references/intakes.md` carries both in full. In short: `setup` configures a host system once and
is never asked again. `intake` asks once per session and produces a written deck of cards rather
than configuring anything, which works only because writing and playing are separate acts.

## What this skill must never do

- Select a workspace form. There is one.
- Restructure, rename, move or delete anything in adopt mode.
- Grant a charter. It proposes; the operator grants.
- Play a card, or write into a working folder.
- Write an emitted `CONTEXT.md`, which is an agent's last act.
- Compose an instruction at runtime for a model to follow. Every card and every contract is
  written by hand and readable before it fires. A model may select which model runs; it may never
  write what the work is told to do.
