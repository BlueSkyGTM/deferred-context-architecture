# CONTEXT.md — meta-seams/

**Meta-seams** are cross-domain influences on *how* a deliverable is built — distinct from a pilot's
**seam**, which sorts *what material* belongs to one domain.

- A **seam** answers *"is this material on-seam for my domain?"* — per-pilot, sorts material at the assay.
- A **meta-seam** answers *"does the output meet this cross-cutting standard?"* — all domains, shapes the output.

A pilot (or a build pass) **opts in** to a meta-seam; the engine does not require one. Optional and
separable: remove `meta-seams/` and the engine still stands (deletion test holds). A meta-seam is an
**influence**, not law and not ingest material — so it lives here, not in `platform/` (law) or
`vault/` (ingest).

Current meta-seams:
- **`writing.md`** — clear, effective, persuasive prose. Distilled principles (copyright-safe); the
  verbatim source corpus is private at `BlueSkyGTM/writing-corpus`. Apply it as the writing bar for
  any deliverable's prose.

To wire one into a build, have the pilot's iteration workflow reference it as a standard the
conformance check holds the output to. (Not yet referenced from core law by default — opt-in.)
