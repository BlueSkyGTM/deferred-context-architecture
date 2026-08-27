# Board

Cards, in four states. The core writes this file and nothing else does.

A written card has not fired. Playing it commits a model and a spend, and is a separate act.

## Written

```
id:       <JOB-001>
wing:     <wing name>
door:     <path/to/folder>
mode:     <built | under construction>
tier:     <none | fetch | build>
done:     <checkable condition> · <checkable condition>
escalate: <named condition> -> stop and write <path>, do not infer
```

## Played

```
id:       <JOB-000>
door:     <path/to/folder>
tier:     <rung>
played:   <YYYY-MM-DD>
returns:  <path the output will land at>
```

## Returned

- `<JOB-000>` · `<output path>` · audit `<pass | fail>` · `<YYYY-MM-DD>`

## Accepted

- `<JOB-000>` · `<YYYY-MM-DD>` · contract promoted, folder now built

## Rules

- One card, one wing, one folder, one return path.
- `door` sits inside the wing's chartered territory, or the card is void and the gate refuses it.
- `tier` is one the wing's charter permits. A wing that may not reach a rung cannot be sent
  there by a card, and the gate refuses the write rather than trusting the rule.
- `done` is checkable by something that is not a model. If it needs an opinion, it is not done.
- `escalate` is never blank. A rung below the core will meet what its contract does not cover,
  and without a named exit it guesses.
- A card carries only what the folder's contract cannot know. Anything the folder could have
  said stays in the folder.
- No card explains why the work matters. That is the operator's context, and handing it over
  removes the independence the whole arrangement exists to manufacture.
