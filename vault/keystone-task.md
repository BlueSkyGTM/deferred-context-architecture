# keystone-task: the shared contract between silos (a well artifact)

A **keystone** is a shared contract that lives in the well. Multiple silos draw it and build against
it; because they all honor the same keystone, their parts fit, without any silo referencing another
(one-way discipline preserved). This is the join mechanism DCA was missing.

## The contract

A **task** is one JSON object, one per line (JSONL), with EXACTLY these fields:

| field | type | meaning |
|-------|------|---------|
| `id` | integer | stable, unique per task |
| `title` | string | non-empty |
| `done` | boolean | completion state |

No extra fields. No missing fields. A part that emits tasks MUST match this exactly; a part that
consumes tasks MAY rely on exactly these fields being present.

## Conformance
A silo's build stage validates its own output against this keystone (drawn from the well, one-way).
If both the producing silo and the consuming silo conform to this keystone, their parts interoperate
by construction, neither needs to know the other exists.
