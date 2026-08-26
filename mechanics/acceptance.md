# Acceptance

How work is judged finished without the core reading it, and why the obvious alternatives both
fail.

## The two failures this replaces

**A purely mechanical check proves completion, not quality.** The file exists, the script exits
zero, the count matches. None of that says the work was any good. Stop here and the card gets
marked done by whoever came back from it, which is the completion fallacy with a card number
attached.

**A quality review by the core produces a loop with no floor.** The core reads the output, forms
an opinion, sends it back, reads the next version. Taste is not a pass condition, so nothing
terminates the loop except the operator giving up and doing the work. This was tested rather than
reasoned about, and it is `../foundations/failure-modes.md` number nine.

Both failures come from asking one artifact to answer two questions. Separate them and both
become tractable.

## The shape

The agent's last act is to write a document describing what it produced, in the form the
workspace uses. Then three checks run, none of which is an opinion.

| Check | Who runs it | Catches |
|---|---|---|
| The stage audit | the agent, before writing to `output/` | the obvious, cheaply, while it can still fix it |
| The diff | rung zero | a result that does not match what was asked |
| Tree resolution | rung zero | claims that do not correspond to anything on disk |

The core reads three exit codes and one short document. It never reads the product.

## 1. The stage audit

ICM's own pattern, inherited whole from `../amendment/icm-upstream/_core/CONVENTIONS.md`: a
table of checks with pass conditions, run by the agent after the work and before saving, with
revision if anything fails.

Self-auditing is normally the thing this workspace refuses, so the boundary matters. This audit
checks against **stated conditions the agent did not write**, which is a different act from
deciding whether the work was good. It is cheap, it catches the obvious, and it never has the
last word.

## 2. The diff

The issued `CONTRACT.md` said what should come to exist. The emitted `CONTEXT.md` says what does.
Compare them.

Inputs that appear in one and not the other, outputs at different paths, an audit in the
contract that the emitted document does not carry: each is a signal that the agent built
something other than what was asked. This is mechanical, and it is the only mechanical purchase
anyone has on fit.

It is not complete. A coherent build of the wrong thing can still describe itself in terms that
line up. `../foundations/failure-modes.md` number ten is that case, and the remaining guard is
not a check at all: it is that the acceptance condition was written by someone who could see the
picture.

## 3. Tree resolution

Every claim the emitted document makes about the filesystem is checkable against the filesystem.

- does every path it names resolve
- does every output it claims exist, at the path claimed
- does every count it reports match the tree
- does every path it names sit inside the folder the agent was given

The last one is the wall, checked rather than trusted. A build whose declared inputs reach
outside its working directory either had a boundary that leaked or is describing work it did not
do. The one legitimate exception is a declared relay handoff, where one card's output is the
next card's input by design, per `tiering.md`.

`../tools/audit.py` implements this and returns an exit code, so what reaches the core is a
number rather than a paragraph.

## Who writes the standard

**Whoever writes the card writes the acceptance, and never the party doing the work.**

That is the rule, and it is about authorship rather than filesystem placement. An earlier version
of this workspace stated it positionally, as criteria living one level above the stage, reached
by a relative path. Position cannot survive a reader that has no location. Authorship can.

Two halves, both written before the work starts:

- **Standing**, in the folder's contract: what good work of this kind looks like here
- **This run**, on the card: what finished means for this particular job

A stage may state what it produces. It may not state what counts as good.

## Where a person still has to look

The audits reduce what the operator reads. They do not remove them from the loop, and an
architecture sold as an empty console is a promise that will not survive its first month.

What is left for a person is small and specific: read the emitted contract, decide whether it
describes the right thing, promote it or do not. That is a different job from reviewing output,
it is done in the operator's own words, and it accumulates. But it is a job.

## Source

Session of 2026-08-26. The completion condition and the observation that quality review produces
a feedback loop requiring heavy operator input are the operator's, from testing rather than from
argument. The stage audit is ICM's, inherited unchanged.

Nothing here has been exercised. No audit has run against a real return.
