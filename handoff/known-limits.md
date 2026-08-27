# Known limits

What is untested, what each instrument cannot see, and which parts of this method are a first
version. None of it says what the run will find. All of it is needed to tell a real pass from a
test that could not have failed.

Withholding this would not be neutrality. A tester who does not know that a check is blind will
record its silence as a pass.

## The state of the method as a whole

**Nothing here has ever been run.** Not one card written for real work, not one binding
assembled, not one folder built, no ignition scheduled, no cost measured at any rung. Every file
in `../mechanics/` is a first version by a convention this method states about itself: depth is
earned by a second and third run rather than designed in advance.

The two skills, the gate and the three tools have been exercised only against scratch trees built
to test them. That is a shape test. It proves the pieces fit together and proves nothing about
whether they survive real work.

## Rungs, and the two facts that change how the run is conducted

### Judgment is not a rung, so the model under test cannot judge its own returns

`../mechanics/tiering.md` used to list a fourth rung called judgment and removed it. Fit,
precedence, whether a contract was right, reconciling siblings: every one of those is something
`../mechanics/evaluation.md` forbids a woken agent to do. A card cannot declare the core, because
the core is what reads the card.

**A run where the model that produced the work also decides whether the work was good has voided
its own result.** `../rungs.md` lists an alternate at the judgment position and is explicit that
this records reachability, not trust. Nothing has ever occupied that seat.

The judging in this run is the operator's, against the predictions, plus what the audits return
as exit codes.

### The fetch rung has no model behind it

`../rungs.md`: the retrieval endpoints return HTTP 500 rather than a clean rejection, which means
the request shape is wrong rather than the access. The rung is **unresolved, not unavailable**,
and rung zero holds it meanwhile.

Consequence for this run: a card written at `tier: fetch` has nothing to run it. Rung zero can
often do the job anyway, since listing what exists, confirming a path and counting are not model
questions. But if the architect writes a deck at `fetch` and the run reports them as completed by
a model, something is wrong with the report rather than with the rung.

### Every number in `../rungs.md` measures reachability and latency only

They come from asking a model to reply with the word "ok". Nothing in that table is a claim about
quality at any rung, and the build-rung entry is no exception.

## What the gate enforces, and what it cannot

`../tools/hooks/card_gate.py`. Fourteen defeat cases behave; that is the whole of its testing.

| Enforced | Not enforced |
|---|---|
| A working folder needs a played card naming it | **Spend.** The gate sees a write, never a bill. Charter ceilings are unenforced |
| The path sits inside the wing's chartered territory | Anything a card claims about `done` |
| The card's `tier` is within the charter's Capability | Whether the work was any good |
| The core cannot write inside a folder its own card opened | Writes that never go through a tool call |
| A woken agent cannot write the core's territory or the board | |

**A woken agent means one the harness woke.** The payload carries `agent_id` only inside a
subagent, so a binding assembled in a separate process the harness cannot see is **refused rather
than allowed**, and the refusal says so. That is deliberate: a gate guessing the other way would
let anything through by claiming to be an agent. It is also the most likely source of a confusing
refusal during this run, so read the refusal text before working around it.

**The gate is not live until the settings file is loaded.** A settings file created inside a
running session may not be read by it. The remedy needs no restart: rewrite `.claude/settings.json`
in place, byte for byte, and the watcher picks it up. `python3 tools/audit.py --harness` is how a
device answers whether the gate is actually live, and never-fired reports as not live.

**`CORE_DIRS` in the gate is a hand-maintained grant, and correctly so.** It declares which
folders belong to the core, which is not a fact about the tree but a decision about it. A host
system whose core folders are named differently must edit that list;
`../templates/harness/README.md` says so at install. Getting it wrong in the safe direction
produces a refusal with a reason attached. Getting it wrong the other way gates nothing and says
nothing.

## What each tool cannot see

### `../tools/audit.py`

Pointer resolution and folder contracts. It does not parse claims about counts out of prose,
deliberately: a tool that guesses which numbers in a sentence were assertions produces findings
nobody trusts.

It carries three explicit exception lists rather than heuristics, and each one is a place a real
defect could hide: `GENERIC_NAMES` for type names used as nouns, `DEVICE_LOCAL` for files absent
from a clean tree by design, `EXTERNAL_NAMES` for repository slugs, which are shaped like
relative paths and are not. Explicit lists were chosen because a rule general enough to catch
them all would also skip a genuinely broken pointer.

`--folder` compares an issued contract against an emitted one, and that check is **partial by
construction**. A capable agent given a poor mandate builds something coherent and describes it
accurately, and the two documents line up. `../foundations/failure-modes.md` number ten is that
case, and nothing mechanical catches it.

### `../tools/fingerprint.py`

Structure only, never content, because reading content would put the walk on a model.

- A file moved with identical bytes reports as **removed here, added there**, not as a move.
  Reading that as two separate events overstates what happened; reading it as a move understates
  it if the content also changed. Check the hashes.
- It refuses to write inside the tree it is fingerprinting, because a record that is part of what
  it describes opens every later diff with itself.
- It reports the age of a folder and never what the age means. Untouched for a year might be
  finished or might be abandoned, and nothing here can tell which.
- It does not read `.git`. Two trees at the same commit with different uncommitted state are
  different trees, which is the correct answer for a working tree.

### `../tools/probe_models.py`

Measures whether a model answers and how fast. Nothing else.

## Parts of the method with nothing behind them

**Reconciliation.** `../mechanics/reconciliation.md` is a responsibility and a procedure with no
implementation. Sibling divergence is the one failure mode with no tested guard. If this run
produces two proposals that disagree, that file will not help.

**Ignition.** Nothing is scheduled. `../mechanics/ignition.md` specifies the walk and its caps;
`../tools/fingerprint.py` is the first piece of it that exists.

**The scout.** A wake that returns cards rather than product is the answer to work whose shape is
not yet known, and it is not built. Until it is, the operator writes every card for unscoped
work. This is an accepted cost, not an oversight.

**The consolidation test cannot fully run yet.** Two wings whose **exercised** charters come out
substantially identical are one wing, and only an exercised charter counts, meaning one amended
at least once in response to something real. Every charter the architect writes is unexercised,
so at this stage the test catches only charters identical on their face. **Prediction 2 is
therefore scoreable as passed, failed, or not tested, and the third is a real answer.**

## The one thing that would invalidate the whole run

The method being edited during it. `../CONTEXT.md` and everything it routes to is the standard
the result is measured against, and a standard that moves during the measurement measures
nothing. The gate refuses a woken agent in the core's territory; that is a wall, not a
suggestion, and a refusal there is worth reporting rather than routing around.
