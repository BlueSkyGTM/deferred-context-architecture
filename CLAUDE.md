# Deferred Context Architecture

Agents that never see the whole. Two deferrals: activation, so nothing runs until a card is
written for it, and scope, so what runs is put somewhere bounded and handed a contract instead
of a history.

Those two deferrals are the method. The claim underneath them is that four things make an
output good, and only four: method, materials, standard, capability. Three of them are the
operator's to write, and the fourth is the smallest lever. `foundations/the-four-parts.md`.

**Routing begins in `CONTEXT.md`.** This file says where you are. That one says where to go.

## Where you are

A method bundle with one enforced rule in it. Four files execute. `tools/probe_models.py`
measures a vendor, `tools/audit.py` checks a tree against what its files claim, and
`tools/fingerprint.py` records what a tree structurally is so a later state can be compared to
it. None of those three runs any part of the architecture. `tools/hooks/card_gate.py` does: it is a harness hook that refuses a write into a
working folder unless a card is played for it, which is the one place a rule here is a default
rather than a request. Everything else is prose.

It descends from Interpretable Context Methodology, which is vendored twice in `origins/` under
the MIT licence: the `icm-architect` skill, and the method repository's core. ICM consolidates
toward one roof; this defers toward many. `origins/divergence.md` says where the aims part.

Throughout, **the host system** means whatever workspace this architecture is installed into:
your repo, your folder tree, your contracts. This bundle was extracted from one such system
and deliberately carries none of its content.

```
deferred-context-architecture/
├── README.md                 what this is, for someone who has not read anything else
├── CLAUDE.md · CONTEXT.md    this file · the task router
├── foundations/              the laws, and the silent ways this goes wrong
├── mechanics/                how it runs. The BBS, the router, the two documents, acceptance
├── templates/                the copyable starting points
├── origins/                  where this came from, the pattern verdicts, ICM vendored twice
├── decisions/                what was settled, what is open, what is broken
├── rungs.md                  which model serves which rung today. The only file naming one
├── tools/                    four executable files. One probes a vendor, two read a tree
│   └── hooks/                and one refuses the write, which is the gate
├── .claude/                  the gate's registration, and the two skills. Architect, delegate
├── HANDOFF.md · handoff/     the first run, what was predicted of it, and its references
├── _archive/                 superseded, kept with a note saying what replaced it
├── lineage.md                what was brought in, from whom, what is ours
└── NOTICE.md · LICENSE       attribution and terms
```

## The two rules

**The core hands down, and never lets an agent look up.** What a woken agent can reach is the
folder it was put in. If it can read the host system, scope was not deferred and the
independence that makes its judgment worth having was never manufactured. These rules address
the core because a card is a list and can neither permit nor forbid anything.

**A woken agent proposes, never settles.** It sits at the lowest level of the host system's
authority ladder and cannot see that ladder. Structural change is filed as a finding and waits
for a ruling.

## Authority

This workspace does not define its own precedence. It requires that the host system have one,
written down, and inherits it. The default shape, highest first: the operator's live ruling,
then a dated ruling in an append-only record, then the standing principles of the area the
work sits in, then method, then a session's own reasoning, lowest. A woken agent is always on
the bottom level. `foundations/authority.md`.

Two ladders, two words. **Rungs** measure capability, in `mechanics/tiering.md`. **Levels**
measure authority, in `foundations/authority.md`. A bare number belongs to one or the other and
never to both.

## Hard lines

- ICM's folder legibility stays underneath. Remove it and this becomes opaque agent state,
  which is the thing it was built to avoid.
- The picture lives in human-readable folders, never in agent configuration or in a stream of
  spent cards. That property is the whole safety argument.
- Acceptance is written before the work by someone who is not doing it. A stage never states
  what counts as good.
- A model may select which model runs. It never writes what the work is told to do. Every
  contract and every card is written by hand, or it is a prompt nobody can read, diff, or debug.
- Nothing fires that the operator could not have read first. A written card is inert until it
  is played.
- Nothing scheduled runs without a spend ceiling and a genuine no-op exit.
- Delegation is enforced by the harness rather than asked for in prose. A rule that lives only in
  this file is a request to the layer that can decline it.
- One form only, the umbrella. Deferral needs more than one wall, and no other form has one.
- A wing reaches outside itself only where its charter names the path. Absence is prohibition.
- Superseded files are archived with a dated note, never deleted.
- Specified, not exercised. Every mechanics file is a first version.
