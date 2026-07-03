# iteration-workflow.md — TEMPLATE (the default Claude Code build chain; override per system)

This is the concrete build chain the core interface requires
(`stages/04-iteration/iteration-workflow.md`). It is the DEFAULT for any Claude Code system; a pilot
keeps it, trims it, or replaces it — but whatever chain it runs must satisfy the core interface
(manifest in, just-in-time; MVP-first; conformance by shape; source-pinning; done-gate stop) and must
end in a live dry-run: the system's ground truth is behavior, not prose.

## The default chain
1. **Scaffold** — the target system's repo skeleton and directory layout (`.claude/`, skills, hooks,
   `.mcp.json` slots), from the manifest's schema items. Source-pinned: every scaffold decision traces
   to a manifest item.
2. **Law files** — the system's own CLAUDE.md / governing docs, cut against `design-schema.md`.
   (PRINCIPLES #3 note: the product's CLAUDE.md is produced here, downstream — never confused with the
   engine's own CLAUDE.md.)
3. **Capabilities** — skills (SKILL.md per the current skill schema and skill-creator conventions),
   agent definitions, hooks (settings.json entries), MCP wiring. MVP-first: the smallest set of
   capabilities that makes the system live.
4. **Live dry-run** — open the built system in a real Claude Code session on reversible ground (a
   scratch clone / disposable session — see `dry-run.md`); exercise each trigger phrase, hook, and
   tool; capture the transcript as evidence. This is the stage's ground truth — the system is
   validated by behaving, not by its prose reading well.
5. **Audit / conformance** — skill-auditor pass on every skill; schema conformance (frontmatter,
   descriptions, hook JSON validity, MCP config shape); the sequential fresh-context evaluator
   (Accept/Revise/Block; worker ≠ checker; no subagents — `stages/04-iteration/evaluator-rubric.md`).
   Prose surfaces also clear `meta-seams/writing.md`.
6. **Done-gate** — substance-vs-surface, read against the live dry-run: when another pass stops
   changing observed behavior and starts rewording prose, ship (`stages/04-iteration/done-gate.md`).

## What the pilot still declares
- The deliverable `kind` (e.g. `skill-suite | agent | governed-repo`) in the deliverable frontmatter.
- The design schema path (`design-schema.md` here; written by schema-discovery iteration 1).
- The concrete source-fidelity check the evaluator enforces (e.g. "every behavioral rule traces to a
  manifest item").
