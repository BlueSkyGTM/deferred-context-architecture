# Failure modes

The ways this architecture goes wrong. Each one is silent, which is what they have in common
and why they are listed rather than trusted to be noticed.

## 1. The starved binding

**Symptom.** Work comes back locally correct and globally wrong, reported as a success.

**Cause.** The binding did not carry enough. Deferred scope means it is the only channel through
which judgment reaches the agent, so a thin one produces a competent agent executing an
inadequate contract.

**Why it hides.** The agent met its contract. The evaluator checked against the same contract.
Both are telling the truth.

**Guard.** Audit what the binding carried, not the output. When a finding is wrong, the first
question is what the card and the folder failed to supply, never what the model failed to
understand.

## 2. The unvisited node

**Symptom.** A folder decays for months while everything reports healthy.

**Cause.** Nothing fires where no card is written, and decay is defined by absence of attention.
This is worse than it was when a walker existed: there is no traversal left to stumble over a
rotting folder by accident.

**Why it hides.** An unvisited node produces no output, and a system that reports on outputs
has nothing to report.

**Guard.** `mechanics/ignition.md`. The fingerprint tracks last-touched age precisely because
silence is the signal.

## 3. The self-graded stage

**Symptom.** A stage passes every run, indefinitely.

**Cause.** Its criteria were written by whoever does the work, so it defines the standard it is
measured against.

**Why it hides.** Green is the expected colour, and nothing distinguishes a stage that keeps
passing from a stage that cannot fail.

**Guard.** Acceptance is authored by someone who is not doing the work, and written before it
starts. A stage contract stating its own success condition is a defect, per
`mechanics/evaluation.md`.

## 4. Divergent siblings

**Symptom.** Individually strong outputs that do not fit together.

**Cause.** Depth was bought and uniformity was spent. No branch can see its siblings.

**Why it hides.** Every branch reports success truthfully. The inconsistency exists only in a
view none of them holds.

**Guard.** `mechanics/reconciliation.md`. Name what must agree, check it at rung zero, and
write the settlement back into the contract rather than into the output.

## 5. The promoted agent

**Symptom.** Structure changes and no ruling explains it.

**Cause.** A woken agent was given write authority over structure, so level five acted at level
one. A card holds no authority of its own; the binding assembled around it does.

**Why it hides.** The change was well executed and passed its evaluator. Nothing in the output
records that it was never authorised.

**Guard.** A woken agent proposes. Findings wait for rulings. `foundations/authority.md` treats
this as a hard line rather than a preference.

## 6. Token detonation

**Symptom.** Spend rises after adopting an architecture chosen to cut spend.

**Cause.** Ticks that wake a model rather than resolving at rung zero, retries with no ceiling,
or an ignition scheduled far more often than drift occurs.

**Why it hides.** Each individual run looks reasonable. What multiplies is the count.

**Guard.** Caps set before the first scheduled run, a genuine no-op exit, and rung zero doing
the walking. `mechanics/ignition.md` treats these as load-bearing rather than hygiene.

## 7. Comprehension rot

**Symptom.** The operator opens a folder they own and reads it like a stranger's.

**Cause.** By design nobody holds the whole picture. Agents are blind, the main window holds
decisions, and the structure carries the rest. If the operator stops reading the structure,
no reader is left.

**Why it hides.** It sounds no alarm while things work. It is discovered at the moment
understanding is most needed, which is the moment it is already gone.

**Guard.** The picture stays in human-readable folders and never migrates into agent
configuration. Findings are files the operator reads before anything acts. Where those two
hold, the map stays legible; where they slip, this failure arrives before any of the others
are visible.

## 8. Rival maps

**Symptom.** Two files describe the host system's shape and disagree.

**Cause.** This method's documentation drifting from the ICM structure it descends from, or a
second entry
file appearing beside the first.

**Why it hides.** Each file is internally consistent and both are believed.

**Guard.** One home per fact, a link beats a copy. This workspace points into
`origins/icm-architect/` rather than restating it, and the host system keeps exactly one entry
file.

## 9. The quality loop

**Symptom.** Every job takes several rounds, each round needs the operator, and the operator
ends up doing the work they delegated.

**Cause.** The core was asked to judge the quality of returned work product. It reads the output,
forms an opinion, sends it back, reads the next version, and the loop has no natural floor
because taste is not a pass condition.

**Why it hides.** Each individual round looks like diligence. The cost is spread across rounds
and shows up as a vague sense that delegation is not saving anything.

**Guard.** The core never reads work product. It reads a path and a mechanical verdict, and the
one thing it does read is the contract the agent emitted about its own work, which is short.
`../mechanics/acceptance.md` holds the argument and the three checks that replace the loop.

## 10. The coherent misfit

**Symptom.** A build passes every check, emits a clean contract, and is the wrong thing.

**Cause.** A capable agent given an inadequate mandate builds something coherent. Coherence is
what the emitted contract tests, so a wrong build describes itself accurately and passes.

**Why it hides.** This is the starved binding wearing the evidence of its own success. Every
mechanical check is green and the artifact reads well, because it is well made.

**Guard.** Diff the emitted contract against the issued one. Inputs or outputs that do not match
what was asked are the signal, and it is mechanical. Beyond that the guard is not a check at
all: fit is judged by whoever wrote the card, which is why acceptance is authored by someone who
can see the picture and never by the party doing the work.

## The trait they share

None of these announces itself. Every one of them presents as a healthy system: green
evaluators, successful runs, clean output. That is not incidental. It follows from the
completion fallacy, which guarantees that a component reporting on itself reports well.

So the guards are structural rather than observational. Nothing here relies on the operator
noticing.
