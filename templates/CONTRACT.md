# <folder name> - <what should come to exist here>

Issued. The operator wrote this before anything ran. An agent working here reads it and does not
edit it. What the agent produces is a `CONTEXT.md`, written beside its output, describing what
is now here.

One outcome: <the thing that should exist when this is done, stated as a result rather than a
procedure>.

## Available

| Source | Path | Scope | Why |
|---|---|---|---|
| Reference | `<path>` | `<section, or full file>` | <what it settles> |
| Working | `<path>` | `<section, or full file>` | <what it supplies> |

Every path resolves from this folder. Nothing outside this folder is reachable, and nothing
outside it should be named.

## Shape

1. <step>
2. <step>
3. <step>

Constraints live in the reference files above, not restated here.

## Audit

Run these before writing anything to `output/`. If one fails, revise rather than save.

| Check | Pass condition |
|---|---|
| <name> | <what passing looks like, checkable without an opinion> |

## Escalate

<named condition> -> stop, write `output/BLOCKED.md` saying what is missing, and exit. Do not
infer, do not substitute, do not proceed on a guess.

## Emit

Last act: write `CONTEXT.md` in this folder describing what is now here, in the shape of
`templates/CONTEXT.md`. It is an artifact until a person promotes it, so write it for the next
reader rather than as a report on your run.
