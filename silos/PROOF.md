# PROOF.md — DCA's first operating history

Architecture is not proof. This is the run record that makes DCA more than an elegant structure.

## The claim tested
Two silos, built independently (one-way refs — neither references the other), each drawing only a
shared **keystone** from the well, produce parts that **fit** at the join.

## The setup
- **Well:** `vault/keystone-task.md` — the keystone (a `task` JSONL contract: `id·title·done`),
  catalogued in `vault/account.md`.
- **Silo `producer`:** drew the keystone, built `stages/02-build/output/produce.py` — emits tasks.
- **Silo `consumer`:** drew the keystone, built `stages/02-build/output/consume.py` — reads tasks,
  relying on exactly the keystone fields. Never saw the producer.
- **Join check:** `bin/join-check.py` — reads the keystone from the well (single source of truth),
  confirms the producer's output conforms, then runs producer → consumer end to end.

## The result (reproduce: `python bin/join-check.py`)
```
keystone fields (from the well): ['done', 'id', 'title']
producer output conforms to the keystone
consumer accepted the producer's output: '3 tasks, 2 done'
falsification holds: 2 violating records injected, all rejected
PASS: two independent silos, one shared keystone, parts fit at the join -- and the check can fail.
```
The falsification is ENCODED in the check, not testimonial: `join-check.py` itself injects records
that violate the keystone (extra field, missing field) and requires the consumer to reject each
before it will print PASS. A check that cannot fail proves nothing; this one demonstrates its own
ability to fail on every run.

## What this proves — and what it does not
- **Proves:** DCA composition + integration works. Independent silos align through a well keystone
  without referencing each other; the fit is mechanically verified, not assumed. This is the join
  mechanism the architecture review named as the missing piece.
- **Does not prove:** that any silo's output is *good*. Quality is still human taste + the staking
  rule. This is a does-it-compose / does-it-fit win, not a does-it-land win. Those stay orthogonal.

## Deletion test still holds
Remove `silos/` (these two proof pillars included) and the well + `_core` still stand — the rig is
intact, the proof was a run on it, not part of it.
