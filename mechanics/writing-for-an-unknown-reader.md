# Writing for an unknown reader

An ICM contract is written for a reader you know: your agent, whose habits you have learned,
with you standing there when it goes wrong. A DCA contract is read by a model you did not
pick, from a vendor you did not test, carrying quirks you cannot predict, while you are not
watching.

Everything below follows from that one change.

## The change that matters most: allowlist, not denylist

ICM's stage template carries a line worth reading closely:

> Do NOT load: anything an eager agent would wrongly pull in.

That is a denylist, and a denylist only works when you can enumerate what a reader might
wrongly reach for. You can enumerate that for a reader you know. You cannot for one you do
not, and the failure is silent, because nothing reports having read something it should not
have.

`hands-down` is an allowlist. It names everything the construct will ever see, and the absence
of a path is the prohibition. Nothing has to be predicted, because nothing is reachable.

**ICM tells the reader what not to take. DCA decides what it gets.** That is deferred scope
restated as a writing rule, and it is the single largest difference between contracts written
for the two methods.

## What an unknown reader does that a known one does not

Stated as classes rather than vendors, because the list has to outlive whichever model is
cheap this quarter.

| It does this | Because | So write it this way |
|---|---|---|
| Returns prose where a structure was wanted | Chattiness is a house style, not an error | State the format exactly. Better, have it return a path: a preamble cannot corrupt a file |
| Obeys the most recent instruction over the most important one | Recency is a strong prior in most models | Put a hard limit beside the instruction it limits, never three steps later |
| Fills a gap from training rather than stopping | Stopping is rarely rewarded | Name the exit. `escalates-when` is not optional for exactly this reason |
| Infers convention from surrounding files | Every other context it has seen had surroundings | Never write "as elsewhere in this repo", "the usual pattern", or "match the existing style". It has no surroundings |
| Treats an example as a template to copy literally | An example next to an instruction reads as the instruction | Label an example illustrative, or make it exact and mean it |
| Reports success by default | `completion-fallacy.md` | Acceptance must be checkable by something that is not the construct |

## The rules that follow

1. **Every path resolves from a stated anchor.** No "the file in the parent folder."
2. **No pronoun whose antecedent is outside `hands-down`.** If "that ruling" is not in the
   list, the sentence is unreadable and the reader will guess.
3. **State the output format. Do not describe it.** "A markdown table with these three column
   headings, in this order" beats "a well-structured summary."
4. **Prefer a returned path to returned content.** It also keeps the main window a record
   rather than a workspace, per `the-board.md`.
5. **Say what to do when the contract does not cover the case, inside the contract.**
6. **Nothing is implied by position, naming, or convention.** A reader that cannot see the
   folder cannot read its shape.
7. **Where acceptance can be mechanical, make it mechanical.** Rung zero has no quirks, and it
   is the only reader in the system that behaves identically every time.

## The cold-construct test

ICM validates with the walk test: can an agent with no memory navigate the workspace. That
test is still necessary and it is no longer sufficient, because a DCA construct does not
navigate. It arrives.

So the test changes shape. Take the `hands-down` list and nothing else:

- Can a reader that has never seen the host system produce the named output from exactly that?
- Can something other than that reader determine whether it passed?

If the first fails, the fix is in `hands-down`. If the second fails, the fix is in the
acceptance condition or in `judged-by`. **In neither case is the fix a better-worded
instruction**, which is the reflex this whole architecture exists to interrupt.

## What this does not license

Verbosity. A contract that swells to pre-empt every conceivable quirk stops loading inside the
healthy band, and ICM's token discipline still binds: entry file plus contract plus inputs,
roughly two to eight thousand tokens.

Read the rules again and notice that almost all of them are substitutions rather than
additions. Allowlist for denylist. Exact for described. A path for content. A named exit for a
hope. The contract gets more precise, not longer, and precision is usually shorter.

## Source

Operator, 2026-08-25, second pass: ICM contracts assume a predictable reader, and constructs
gear up second-hand agents whose quirks are unknown, so the contract has to account for it.
The behaviour classes above are stated from the architecture's own failure modes rather than
from measurement. No construct has yet been run against a foreign model, so treat the table as
a first version and correct it from the first real run.
