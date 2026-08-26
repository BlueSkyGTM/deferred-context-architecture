# Ignition

The one thing in this architecture that pushes. Everything after it pulls.

## The hole it closes

Deferred activation wakes a construct when traversal reaches it. That is correct for
task-driven work and blind in one specific place: structural decay is defined by nothing
arriving.

A folder rots because no task has named it. A construct that only fires on traversal therefore
never fires in the folders that most need it. The mechanism is blindest exactly where the
disease is, and the failure is silent, because an unvisited node produces no output to
inspect.

Left unaddressed, the trigger for structural repair is the operator noticing degradation.
That is the condition this architecture was built to remove, so a purely pull-based design
would have reproduced the original problem with more machinery.

## What ignition is

A scheduled walk that carries no method.

It runs at rung zero: shell and diff, no model. Its entire job is to compare the host system's
current structural fingerprint against the last recorded one and notice what moved or what
has gone untouched past a threshold. It does not interpret, it does not restructure, and it
does not decide anything.

When it finds something, it writes a card naming the folder and stops. Nothing else happens
until a person reads that card and plays it.

Writing a card is the whole of what ignition may produce, and the reason is that nothing else
would run. There is no traversal in this architecture, so a folder that has been named but never
carded is a folder nobody visits. An earlier version of this file had the folder's own context
file taking over from there, which is a file being asked to act.

**One ignition, everything after it lazy.** That is the shape that keeps the topology intact
while closing the hole.

## What a fingerprint holds

Structure only, never content. Content is what makes a sweep expensive, and reading it would
put the walk back on a model.

- The tree: folders and files, with modification times
- Presence: does each working folder carry a contract
- Resolution: does every pointer in a routing table open
- Counts, so a later claim about counts can be checked
- Last-touched age per folder, which is the drift signal itself

Everything on that list is answerable with `find`, `git`, and a comparison. None of it needs a
sentence written about it.

## Where it runs

Scheduling has two shapes and they are not interchangeable. The choice follows from what the
loop needs to see.

| Property | Cloud routine | In-session loop |
|---|---|---|
| Runs with the machine off | Yes | No |
| Needs an open session | No | Yes |
| Sees local files | No, works from a fresh clone | Yes |
| Minimum interval | About an hour | About a minute |
| Survives the session ending | Yes | No, and it expires after about a week |

Ignition wants the first column. It reads a repository rather than local process state, and
hourly is far more often than structural drift requires. Tying it to an open session would
put the trigger back on the operator, which is the thing being removed.

The in-session shape has a different job, covered in `../foundations/authority.md` and the
deliberation ledger: it is for capturing live reasoning while a session is running, which by
definition cannot be observed from outside.

Version numbers, interval floors, and expiry windows in this table come from a secondary
source. Verify them against current documentation before building on them.

## Caps are load-bearing

This architecture is adopted to reduce spend. The loop-engineering literature's fourth cost
is that loops are how bills detonate: an agent hatches helpers, retries, and runs round after
round, and what was written as logic comes out as a count of runs multiplied by a unit price.

Both are true, and the resolution is narrow. **A loop saves money only when the tick is
mostly deterministic and mostly a no-op.** An ignition that wakes a judgment-tier model every
hour to consider the host system is strictly worse than the manual trigger it replaced.

So the caps are not hygiene. They are the condition under which the premise holds:

- A per-run ceiling and a daily ceiling, set before the first scheduled run
- A retry limit, so a spinning bug cannot consume a night
- A no-op exit that costs nothing when the fingerprint is unchanged, which will be most runs

## What ignition may never do

It may not restructure. It may not write to any contract. It may not decide which of the five
ICM forms fits. It may not play the card it wrote.

It notices, it names, and it stops. Everything else is a finding that waits for a ruling, per
`../foundations/authority.md`. An ignition with write authority is an unattended level-five
agent editing the structure the whole host system routes through, which is the worst available
configuration of this architecture.

## Source

The unvisited-node problem and the one-ignition shape were identified in the founding session,
2026-08-25. Scheduling properties and the cost warning are from HuaShu, *Loop Engineering*
(June 2026 edition), sections 06 and 07.
