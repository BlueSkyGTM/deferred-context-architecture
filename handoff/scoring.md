# Scoring the run

How to read what comes back without deciding it in advance, and what to do with each kind of
failure. The predictions are in `../HANDOFF.md`; this is the procedure for answering them.

## Score before you form an impression

Go prediction by prediction, with the evidence, **before** writing any general assessment of how
the run went. An impression formed first will find evidence for itself, and by the time it does,
every prediction has quietly become a lookup for something already decided.

This is not a style preference. It is the same failure the whole method is built against, run on
the test instead of on the work.

## Three outcomes, not two

| Verdict | When |
|---|---|
| **passed** | the prediction held, and it could have failed |
| **failed** | it did not hold |
| **not tested** | nothing in the run could have falsified it |

**Not tested is a real answer and recording it as a pass is the most likely way this run lies to
you.** A prediction about consolidation is not tested if only one wing was proposed. A prediction
about the gate is not tested if the gate was never live. `known-limits.md` names the checks that
are structurally blind, and each of those can produce a silence that reads like a pass.

## When a prediction fails, find out which of two things happened

Every failure has one of two causes and they need opposite repairs. **Getting this wrong is worse
than not diagnosing it at all**, because the fix goes to the wrong layer and the failure returns
wearing different clothes.

**The skill was silent.** Nothing in `.claude/skills/dca-architect/` said the thing, so the model
had no way to know it. The repair is prose: add the rule, in the file that owns it, and the
architect picks it up.

**The skill said it and the model did not do it.** The rule exists, in plain language, and was
not followed. **The repair is not more prose.** Rewriting the sentence more emphatically is the
move that feels like progress and changes nothing, because the layer that failed is the one that
can decline. This method already names the three layers and only the last is a default:

| Layer | Enforced by | Strength |
|---|---|---|
| an instruction in a context file | the model choosing to comply | a request |
| a skill | the model deciding it applies | a method |
| a hook or a tool check | the harness | a default |

A rule that was stated and ignored is a rule that needs to move down that table: into
`../tools/audit.py` as a check with an exit code, or into `../tools/hooks/card_gate.py` as a
refusal.

**So record, for every failure, the exact sentence in the skill that should have prevented it, or
the fact that no such sentence exists.** That sentence, quoted, is the actual finding. The
failure itself is only the symptom.

## What counts as evidence

- A file, with its path, and the lines in it that show the behaviour.
- An exit code from `../tools/audit.py` or `../tools/fingerprint.py`.
- A gate refusal, **quoted verbatim**, including its reason.

What does not count: that the output reads well, that the structure looks sensible, that the
model explained its reasoning convincingly. `../foundations/completion-fallacy.md` is the file on
why. A confident report of success is the default output of a model that has finished, and it is
the thing this entire architecture exists to stop trusting.

## Do not repair the skill during the run

A skill edited halfway through means the second half was tested against a different instrument
from the first, and neither half is now comparable to anything.

Write the repair down. Apply it after the run is scored, and note in the scoring which
predictions were answered by which version. If a defect is severe enough that continuing is
pointless, stop the run and say so; a short run with a clean result beats a long one with a
moving standard.

## Findings against the method are the most valuable output

More valuable than the tree that comes out. The tree can be rebuilt in an afternoon; a defect in
the method survives every future run until somebody notices it.

File them per `../templates/FINDINGS.md`, as facts about the files rather than as complaints.
**Do not fix them.** A woken agent proposes and does not settle, and this run is no exception:
`../foundations/authority.md` puts structural change behind a ruling, and a change to the method
is the most structural change there is.

## Where the result goes

Two artifacts, per `../HANDOFF.md`:

- An emitted `CONTEXT.md` in the shape of `../templates/CONTEXT.md`: inputs, process, audits,
  outputs, with real paths.
- A findings file per `../templates/FINDINGS.md`, holding everything the run wanted to change and
  did not, including findings against the method.

Then a dated entry in `../decisions/`, which is where this repository puts what a session settled,
what it left open, and what it got wrong. Read one of the existing entries first; they are the
shape, and they are all written to be read by someone who was not there.

## The result that would be most useful

Not a clean sweep. A run where every prediction passes tells you the predictions were too easy,
and predictions written by the party that built the thing usually are.

The most useful outcome is a failure with its cause located precisely enough to fix in one edit,
in the layer where the failure actually happened.
