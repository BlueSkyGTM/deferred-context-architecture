# Continuing this work

What exists, where it lives, the conventions that will be broken by accident, and how to leave
the repository in a state the session after you can pick up. Read this before writing anything
into the method, not after.

## Get your bearings in this order

1. `../CONTEXT.md`, the task router. It names every file and what question each answers. Nothing
   below replaces it.
2. `../CLAUDE.md`, which states the two rules and the hard lines.
3. The most recent file in `../decisions/`. Each entry says what a session settled, what it left
   open and what it got wrong, and they are written for a reader who was not there.

`../README.md` is the front door for someone who has read nothing else, including a *what is
still missing* table that is kept current.

## What has been built, and in what order

| Pass | What it settled | Commit |
|---|---|---|
| Founding | the two deferrals, the four parts, authority, failure modes | `930f3f0` |
| The binding | the actor: contract, model, tools and card joined at play time. The BBS as an engine. The two documents, and `../tools/audit.py` | `5634231` |
| The fork | descent rather than amendment. One form, the umbrella. Every upstream pattern given a verdict | `a2a64b7` |
| The gate | delegation as a harness default rather than a request | `c019bd1` |
| Both walls | the core refused inside its own card's folder, an agent refused in the core's territory | `8bdaf57` |
| The architect | `dca-architect`, the findings template, `../tools/fingerprint.py`, the handoff | `920463d` |

`git log` is the ledger. The board is state and its history is the record, which is why no
separate ledger file exists.

## The two skills, and when each fires

**`dca-architect`** lays the method over a tree or builds one from nothing. It proposes and files
findings; it never restructures, never grants a charter, never plays a card.

**`dca-delegate`** is the loop the core follows instead of doing the work: read the router, write
the card, stop, play it, judge the return. It fires when work would happen inside a working
folder, and it is what to read when the gate refuses a write.

Both live in `../.claude/skills/`, which is where a project skill actually loads. A top-level
`skills/` folder would need an install step to do anything.

## Conventions that get broken by accident

- **No em dashes anywhere.** The repository contained zero before the rule was written down.
  The check has to build the character rather than contain it, or the file that hunts for it
  becomes a hit: `grep -rl "$(printf '\u2014')" --include=*.md .`. Expect matches only under the
  two vendored folders in `../origins/`, which are carried unmodified.
- **Superseded files are archived, never deleted.** Move to `../_archive/` with a dated note at
  the top saying what replaced it and why.
- **Every session leaves a dated entry in `../decisions/`.** What was settled, what was verified
  rather than asserted, what is still open, and a source note naming whose idea was whose.
- **A rung is capability, a level is authority.** Never let a bare number belong to both.
- **One form, the umbrella.** There is no form selection anywhere in this method, and
  reintroducing one is the likeliest regression because the vendored skill opens with it.
- **The vendored copies are never edited.** `../origins/icm-architect/` and
  `../origins/icm-upstream/` are carried unmodified under MIT, and `../NOTICE.md` says so.
- **Attribution names authorship and terms, and nothing else.** This repository quotes and never
  characterises: no position is attributed to a person, because a citation without a line
  reference is unfalsifiable by anyone downstream. `../origins/divergence.md` records why, under
  the second failure of descent.
- **Guardrails on length**: contracts under 80 lines, references under 200.

## The verification loop, run before every commit

```
python3 tools/audit.py --repo        # every pointer resolves. Clean, or the rename is unfinished
python3 tools/audit.py --harness     # is the gate actually live on this device
grep -rl "$(printf '\u2014')" --include=*.md .   # em dashes. Vendored folders are the only hits
```

`--repo` is the one that catches a rename nobody finished, and it has caught every one so far. If
you add a file that names something outside the filesystem, the exception lists in
`../tools/audit.py` are where that goes, with a stated reason, rather than a new heuristic.

## Adding to the method without breaking it

**One home per fact.** Upstream Pattern 5, inherited. If something is already stated in a file,
route to it rather than restating it, or the two will drift and nobody will know which is
current.

**A new rule needs a layer.** Prose in a file is a request. Before writing one, ask whether it
can be a check in `../tools/audit.py` or a refusal in `../tools/hooks/card_gate.py`. If it can,
put it there and let the prose explain it rather than carry it. `scoring.md` has the table.

**Findings before fixes.** Structural change waits for a ruling, per
`../foundations/authority.md`, and that applies to a session working on the method as much as to
a woken agent.

**Say what has not been exercised.** Every mechanics file ends with a source note that says so.
That convention is why this repository can be trusted about its own state, and dropping it for
one file costs more than it saves.

## Upstream moves, and this goes stale silently

`../origins/the-machinery.md` gives every ICM pattern a verdict: inherited, amended with the
reason, or does not apply with the reason. Four patterns were nearly reinvented here because
nobody was checking.

Re-read it on any re-vendor and record the date. That file is the ongoing cost of descent, and it
is the one that decays without anything failing.

## What is deliberately not planned

What comes after the first run. There is a restructure waiting and further passes sketched, and
none of it is written down, because planning it now would mean guessing what the run says.

**Write the next plan from the results.** If you find yourself building the thing after next
before this run has returned, that is the instinct this method exists to interrupt.
