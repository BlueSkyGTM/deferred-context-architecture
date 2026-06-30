# CONTEXT.md — manifest/ (the cargo list + the transported items)

The destination yard. Stage 03 (Transport/Manifest) reads on-seam material from `carts/`, catalogues
it, stamps frontmatter (`stages/03-manifest/frontmatter-schema.md`), and lands it here. This folder
is the structured-input layer the system's name starts from (Manifest → Workspace). Starts EMPTY.

## Layout (where the manifest physically lives)
```
manifest/
├── CONTEXT.md     (this file)
├── index.md       (THE manifest: the itemized, addressed cargo list — one row per item)
└── items/         (the transported pieces, each an .md file with frontmatter; starts empty)
```

- `index.md` is the cargo list. Stage 03 appends one row per catalogued item. It is the queryable
  account: glob `items/` and read frontmatter to count/sort; `index.md` is the human-readable roll-up.
- `items/<id>.md` is one manifested piece: frontmatter (countable fields) + body (human-readable
  directions). The `id` is the item's stable address, inherited from excavation (reused verbatim, not
  re-minted).

## index.md row format
The row fields are the catalogued item's frontmatter — owned by `stages/03-manifest/frontmatter-schema.md`
(stage 03 appends one row per item per that schema). This file does not restate the schema.

## Invariant (from stage 03)
**Nothing uncatalogued, nothing un-typed.** Every item in `items/` has a row in `index.md` AND every
required frontmatter field present. A piece missing a required field is NOT on the manifest — bench it
or log to `logs/failures.md` and stop. Do not invent a field value to make it pass.

## What reads this
Stage 04 (Iteration) pulls from the manifest just-in-time (it does NOT load all of `items/` into
context — that would defeat the contamination defense). It reads `index.md` to find what it needs,
then pulls only the slice it is building from.
