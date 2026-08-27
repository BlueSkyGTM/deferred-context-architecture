# Vendored: ICM upstream core

This folder is a partial copy of the Interpretable Context Methodology repository, taken so the
amendment can be developed against the current conventions rather than against a snapshot.

| | |
|---|---|
| Source | `https://github.com/RinDig/Interpretable-Context-Methodology` |
| Commit | `02ba5d85c7871b75c7c702a2d8da6524723d53d4` |
| Dated | 2026-07-25 |
| Taken | 2026-08-26 |
| Licence | MIT, copyright 2026 Model Workspace Protocol Contributors. Created by Jake Van Clief |
| Method | Van Clief and McDermott, arXiv:2603.16021 |

Nothing here has been edited. The `LICENSE` file travels with it, as MIT requires.

## This is not a newer version of `../icm-architect/`

The two are complementary artifacts, not old and new copies of one thing. That was checked
rather than assumed, and it is worth stating because a later session will otherwise try to
replace one with the other.

| | `icm-architect/` | `icm-upstream/` |
|---|---|---|
| What it is | the `icm-architect` skill | the method repository |
| Copyright string | Jake Van Clief | Model Workspace Protocol Contributors |
| Carries the five forms | yes | no |
| Carries the walk test | yes | no |
| Carries build and restructure modes | yes | no |
| Carries the numbered patterns | no | yes, fifteen of them |
| Carries checkpoints and stage audits | no | yes |
| Carries worked example workspaces | no | yes, omitted here |

The skill teaches how to design a workspace. The repository specifies the conventions a
workspace must follow and shows finished ones. This bundle's argument quotes both, and removing
either breaks citations in `../the-amendment.md`.

## What was omitted, and why

- **`workspaces/`.** Four worked examples: course-deck-production, script-to-animation,
  voice-driven-animation, workspace-builder. They are content rather than method, and this
  bundle deliberately carries no host system's content. Read them at the source.
- **The repository's own `CLAUDE.md`.** A second entry file inside this bundle would be two
  hand-maintained maps of different territories sitting in one tree, which is ICM's own
  duplicated-entry-file anti-pattern and this workspace's `../../foundations/failure-modes.md`
  number eight, rival maps.
- **`.gitignore`.** Not method.

## What this bundle takes from it

Four patterns are load-bearing here and were being reinvented before this copy arrived.

| Pattern | Where it lands |
|---|---|
| 4, Selective Section Routing | inputs name sections rather than whole files, so a payload stays narrow |
| 11, Checkpoints | the table form for a human steer, replacing a prose instruction |
| 12, Stage Audits | Check and Pass Condition, which is most of the mechanical half of acceptance |
| 14, Docs Over Outputs | early outputs are the worst outputs, which is why an emitted contract is an artifact until a person promotes it |

Two conventions are inherited wholesale: files that supersede others are archived rather than
deleted, and stage contracts stay under eighty lines with reference files under two hundred.

The line limits govern **what a binding might carry**, which is what they were written for: a
contract an agent reads, and the reference material behind it. They do not govern the front door,
an argument, or a dated ledger. `../../README.md` is written for a person who has read nothing
else, `the-amendment.md` is an argument that has to quote what it amends, and
`../../decisions/` grows by design and is never loaded into a run. Those three are over the
limit deliberately, and stating that here is cheaper than trimming files the rule was not
aimed at.
