# Notice: provenance and attribution

What in this repository is someone else's, what is ours, and under what terms. Attribution
travels with revisions here as a standing rule, so entries state what was checked and when
rather than what is assumed.

Where a claim came from, as opposed to where a file came from, is a different question and is
answered in `lineage.md`.

## Vendored

Two artifacts, both **Interpretable Context Methodology**, both MIT, and complementary rather
than versions of one thing. The method is published as Van Clief and McDermott,
arXiv:2603.16021.

**`amendment/icm-architect/`** is the `icm-architect` skill, copyright 2026 **Jake Van Clief**.
It carries the five forms, the walk test, and the build and restructure modes.

**`amendment/icm-upstream/`** is the method repository's `_core`, copyright 2026 **Model
Workspace Protocol Contributors**, created by Jake Van Clief. Taken 2026-08-26 at commit
`02ba5d85c7871b75c7c702a2d8da6524723d53d4`, dated 2026-07-25, from
https://github.com/RinDig/Interpretable-Context-Methodology. It carries fifteen numbered
patterns, checkpoints, and stage audits.

Both are vendored **unmodified**, each with its own `LICENSE` in place, as MIT requires. Nothing
in either has been edited, and nothing has been copied out of them into the files around them.
`amendment/icm-upstream/VENDORED.md` is this repository's own note, records the comparison
between the two, and lists what was omitted from the second: the worked example workspaces, the
repository's own entry file, and its `.gitignore`.

This repository is an amendment to that method and is unreadable without it, which is why
working copies are carried rather than citations. If you want ICM on its own, take it from its
author rather than from here.

## Cited, not carried

These shaped the argument. No text from any of them is reproduced here beyond ordinary
quotation, and each is credited at the point of use in `lineage.md`.

| Source | What it contributes |
|---|---|
| Addy Osmani, *Loop Engineering*, June 2026 | The named layer above the harness, and the rule that automation fires a named skill rather than a pasted wall of instructions |
| Peter Steinberger and Boris Cherny, June 2026 | Design the loops that prompt the agent rather than prompting the agent |
| Prithvi Rajasekaran, Anthropic | Agents confidently praise their own output; a standalone sceptic is more tractable than a self-critical generator |
| Stripe Minions, reported by Steve Kaliski | A deterministic orchestrator assembles context before the model wakes |
| HuaShu, *Loop Engineering: The Complete Guide*, v260615 | The secondary source through which the four above reached the founding session |

**On that last row.** The loop-engineering material reached this work through one book
summarising blog posts, a podcast, and official documentation. Its structural claims are
consistent and useful. Its product specifics, meaning command names, version numbers, interval
floors and expiry windows, are second-hand and were not verified. Verify them against current
documentation before building anything that depends on one. Each such specific says so at its
point of use.

## Ours

Everything outside `amendment/icm-architect/` is original work, MIT licensed, copyright 2026
BlueSkyGTM. See `LICENSE`.

The specific claims that are ours rather than inherited are listed in `lineage.md` under
"This project's own", so a later reader can tell a citation from a claim.

## Vendor names

`rungs.md` names a model vendor, and `tools/probe_models.py` calls one. `tools/audit.py` calls
nothing and reads only the tree it is pointed at. None of it is an endorsement, an affiliation,
or a dependency. The architecture requires that some model serve
each rung; which one is an edit to a single file, which is the whole of what model agnosticism
means here.

No credential, key, endpoint secret, or account identifier appears anywhere in this
repository. `tools/probe_models.py` reads its key from the environment, never prints it, and
never accepts it as an argument.
