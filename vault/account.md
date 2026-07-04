# account.md — the well's catalogue (append-only)

Every piece in the well gets one row here, so the well is a routable catalogue, not a pile. Material
enters by extraction or placement; each entry is addressed here before any silo can draw it. Starts
EMPTY (nothing in the well yet) — ready infrastructure, like the logs.

Row format:

```
| id | source | addressed | descriptor |
```

- **id** — stable, well-unique address.
- **source** — where it came from (a deposit, or "placed").
- **addressed** — `yes` once it has an id + lives at `vault/<id>`; unaddressed = the only error state.
- **descriptor** — a one-line what-it-is, so a silo can select from the catalogue without opening it.

A silo's `stages/01-draw` reads this catalogue, selects its slice, and pulls only those ids. The well
is read-only from a silo; entries are never edited by a draw. See `../_core/well-contract.md`.

| id | source | addressed | descriptor |
|----|--------|-----------|------------|
| keystone-task | placed | yes | shared contract: the `task` JSONL record (id·title·done) two silos build against |
