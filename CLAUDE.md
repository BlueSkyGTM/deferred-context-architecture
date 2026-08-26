# Deferred Context Architecture

Agents that never see the whole. Two deferrals: activation, so nothing runs until traversal
reaches it, and scope, so what runs is handed a contract instead of a history.

Those two deferrals are the method. The claim underneath them is that four things make an
output good, and only four: method, materials, standard, capability. Three of them are the
operator's to write, and the fourth is the smallest lever. `foundations/the-four-parts.md`.

**Routing begins in `CONTEXT.md`.** This file says where you are. That one says where to go.

## Where you are

A method bundle, not a running system. Nothing in it executes. It is an amendment to
Interpretable Context Methodology, which is vendored whole in `amendment/icm-architect/`
under the MIT licence.

Throughout, **the host system** means whatever workspace this architecture is installed into:
your repo, your folder tree, your contracts. This bundle was extracted from one such system
and deliberately carries none of its content.

```
deferred-context-architecture/
├── README.md                 what this is, for someone who has not read anything else
├── CLAUDE.md · CONTEXT.md    this file · the task router
├── foundations/              the laws, and the silent ways this goes wrong
├── mechanics/                how it runs. The board, constructs, tiering, ignition, evaluation
├── amendment/                the ICM relationship, and ICM itself vendored
├── decisions/                what was settled, what is open, what is broken
├── rungs.md                  which model serves which rung today. The only file naming one
├── tools/                    the one executable file. It measures a vendor, not this
├── lineage.md                what was brought in, from whom, what is ours
└── NOTICE.md · LICENSE       attribution and terms
```

## The two rules

**A construct hands down, never lets an agent look up.** Everything a woken agent will ever see
is listed on its construct. If it can read the host system, scope was not deferred and the
independence that makes its judgment worth having was never manufactured.

**A construct proposes, never settles.** A woken agent sits on the lowest rung of the host system's
authority ladder and cannot see that ladder. Structural change is filed as a finding and
waits for a ruling.

## Authority

This workspace does not define its own precedence. It requires that the host system have one,
written down, and inherits it. The default shape, highest first: the operator's live ruling,
then a dated ruling in an append-only record, then the standing principles of the area the
work sits in, then method, then a session's own reasoning, lowest. A woken agent is always on
the bottom rung. `foundations/authority.md`.

## Hard lines

- ICM stays underneath. Remove it and this becomes opaque agent state, which is the thing it
  was built to avoid.
- The picture lives in human-readable folders, never in agent configuration. That property is
  the whole safety argument.
- Evaluation criteria live one level above the stage they judge. A stage never states what
  counts as good.
- A model may select which construct fires. It never composes what one says. Every construct is
  written by hand, or it is a prompt nobody can read, diff, or debug.
- Nothing scheduled runs without a spend ceiling and a genuine no-op exit.
- Specified, not exercised. Every mechanics file is a first version.
