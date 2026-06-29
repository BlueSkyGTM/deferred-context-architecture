# CONTEXT.md — answer-key/ (QUARANTINED — the model must never read this)

The grading key for Run 1c blind-discovery (see `../dry-run.md`). It holds the off-seam material the
seam must discover by reasoning, plus the correct verdict for each piece. The HUMAN holds it; the
model does NOT. If the model reads this folder, Run 1c is invalidated — the seam would appear to have
sorted material it never had to reason about.

## Quarantine rules
- Nothing here is ever loaded into the model's context during a run. It is the human's reference.
- It is NOT a deposit and NOT in `vault/`. It never flows the pipeline. It sits outside the line.
- Keep it physically separate from any path the excavation extractor is pointed at.

## Entry format (one file per graded item, filled by the human before Run 1c)
```
- item_id:        <stable id>
- material:       <the piece, or a pointer the human controls — NOT a vault address>
- correct_verdict: <cart | tailings | bench>
- why:            <the reason — this is what the seam is graded against>
- category:       <on-seam | off-seam | looks-transferable-but-off-seam>
```

Status: _empty — the human populates this before Run 1c._ Includes at minimum the deliberate blind
control: an AI-engineering / LLM-systems curriculum fed as if it were GTM (correct_verdict: tailings,
category: looks-transferable-but-off-seam).
