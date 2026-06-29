# tooling.md — Concrete Tool Choices for This Pilot

The core declares a tool-surface POLICY (the gstack fence, ponytail-as-a-coding-rule, the
single-agent law that fences out parallel/multi-agent surfaces — see `platform/TOOLING.md`). This
file makes the CONCRETE choices for the GTM-curriculum domain. Tools are wired in a later pass, after
human review; for now these are declared selections, not installed wiring (`TODO(tools)`).

## Excavation extractors (matched to this pilot's deposit types — see deposits.md)
- docs-site skill (from awesome-claude-skills) — documentation websites
- article-extractor — web articles
- youtube-transcript — video
- markitdown — PDF / Office → markdown

## Assay
Human calls on the curriculum loop (`dry-run.md`). The seam brain is the OUTPUT of the loop, wired
after Run 1c — not an input.

## Iteration (back half) — see iteration-workflow.md
- Karpathy LLM wiki — compile manifest → linked articles + ordered index. Principles native,
  STRUCTURE NOT FORKED.
- Understand-Anything `/understand-knowledge` — graph + capstone (human comprehension + course build).
- the evaluator — Accept / Revise / Block, with source-fidelity ("no facts not in the material").

## Retrieval
- GBrain — BLACKBOX machine retrieval for the pipeline. **Canonical lives in READABLE files**
  (logs, learned-seam, session-handoff); GBrain is the projection, never the only home of a seam
  decision. NOTE: GBrain is not yet configured in this environment; until it is, the readable files
  ARE the system and GBrain is simply absent (the deletion test still passes).

## Standing skills (state/memory harness — these are core-generic but their outputs land here)
- context-compressor, memory-manager — write durable decisions to readable files first, then index
  into GBrain. See core `platform/SKILLS.md`.

## ponytail scoping (applied)
ponytail's minimalism ladder is tuned for code and UNDER-builds pedagogy. Run `/ponytail off` during
the curriculum back-half build (it would skip "redundant" lessons and write minimal explanations,
fighting the spaced reinforcement and worked examples a course needs). Keep it ON for coding/tooling
work. NOTE: verify `/ponytail` exists in the environment before relying on it (it was named in the
chat-authored spec but is not in the current gstack skill list).

## Parked / dropped (decided for this pilot)
- GBrain vs Understand-Anything: DIFFERENT LAYERS (blackbox machine retrieval vs human
  comprehension) — both kept. Final ingest details settle once Run 1c produces a wiki to point GBrain
  at.
- Dropped: headroom-desktop (no role; markitdown taken on its own), loop-engineering (parallel,
  violates single-agent), awesome-claude-skills wholesale (shopped for the one extractor), tapestry
  (overlaps the wiki layer).
