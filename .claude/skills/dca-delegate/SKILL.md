---
name: dca-delegate
description: The loop the core follows in a Deferred Context Architecture tree instead of doing the work itself. Use when work would happen inside a working folder (a wing, a stage, anything outside the core's own territory), when the card gate has refused a write, or when the user asks to build, mill, draft, generate or fix something that lives in a chartered wing. It turns the intent into a written card, then plays it, then judges the return.
---

# Delegate

In this tree the core deliberates and never produces. That is not a preference and it is not a
reminder somebody has to repeat: `tools/hooks/card_gate.py` refuses the write. This file is what
to do instead, and following it before the refusal is faster than following it after.

Read `mechanics/the-bbs.md` once if you have not. Everything below is its procedure.

## 1. Notice which side of the wall the work is on

The core's own territory is deliberating, routing, ruling, archiving, and the method itself.
Writing there is the job.

Everything else is a working folder. Product, drafts, code, research, generated anything: it goes
through a card, whatever its size. **There is no small enough to do yourself.** The exception
that swallows the rule is a one-line fix, and it is exactly where it starts.

## 2. Read the router before writing anything

`ROUTER.md` says which wings exist, which folders they hold, and what mode each folder is in. A
folder holding `CONTRACT.md` is under construction and takes a builder. A folder holding a
promoted `CONTEXT.md` is built and takes a miller.

If the folder does not exist, that is a structural decision and it is the operator's. Propose it.
Do not create a wing to have somewhere to put a card.

## 3. Write the card

Five fields, on `BBS.md`, in the shape `templates/BBS.md` carries. None may be blank and none may
be answered by reflex.

| Field | The question it forces |
|---|---|
| `door` | which folder, and therefore which method governs |
| `mode` | built or under construction |
| `tier` | which rung serves this, per `rungs.md`, and within what the wing's charter permits |
| `done` | what finished means, checkable by something that is not a model |
| `escalate` | the named condition that stops the run instead of producing a guess |

Check the wing's `CHARTER.md` before writing `door` and `tier`. A card sending a wing outside its
territory or above its permitted rung is void, and the gate will say so.

The card carries only what the folder's contract cannot know. It never carries why the work
matters. Handing over the why is what deferred scope removes.

## 4. Stop

A written card has fired nothing. Say what you wrote and let the operator read it. Writing several
cards and playing none is a normal and good session.

**Do not play a card in the same breath as writing it** unless the operator has said to. The gap
between writing and playing is the only review window this architecture has.

## 5. Play it

Move the card to Played with the date and the return path. Then dispatch: an agent, in that
folder as its working directory, holding the folder's contract and the card, at the rung
`rungs.md` names for that tier.

It gets the folder and the card. It does not get the board, the router, the charter, or this
conversation. If it can read the tree above it, scope was not deferred.

## 6. Judge the return

```
python3 tools/audit.py --folder <door>
```

Then read the emitted `CONTEXT.md` and nothing else. Not the product. `mechanics/acceptance.md`
holds why: the core reading work product is a send-back loop with no floor, and it ends with the
operator doing the work.

Move the card to Returned with the audit verdict. Promotion, which flips a folder to built, is
the operator's act and never yours.

## When the gate refuses you

The refusal names which of the three conditions failed: no played card, no charter, or outside
chartered territory. Each has one honest answer.

- No played card. Go to step 3. Do not look for a path the gate does not cover.
- No charter. The wing has no territory. Propose one from `templates/CHARTER.md` and wait.
- Outside territory. Either the card is aimed wrong or the charter needs amending, and amending a
  charter is a ruling. File it, do not perform it.

A refusal is the architecture working. Reaching for a way around it is the one failure mode this
tree cannot detect on its own.
