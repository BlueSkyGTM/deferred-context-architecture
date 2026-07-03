# CHANGELOG.md — Machine Change Record (append-only, newest at bottom)

Read CONTEXT.md for the format and the REVERT GUARD. Each entry says what changed, why (design
intent), how it was tested, and what breaks if it is reverted.


## 2026-07-03 — Domain fixed: M2W specializes to Claude Code powered systems
- what: Core doctrine re-scoped (CLAUDE.md, M2W.md, ARCHITECTURE.md, root CONTEXT.md, platform/ and
  stage-contract sweeps); the old law "core never names a domain" narrowed to "core never names a
  specific pilot" — the domain (Claude Code systems) is now core vocabulary; scope guard added
  (CLAUDE.md + README "What M2W is NOT for": deterministic one-shot content milling is off-seam by
  definition); vocabulary settled in platform/glossary.md ("Claude Code system" entry, "Seam"
  rewritten, retirement lineage note); pilots/_TEMPLATE pre-filled with Claude Code defaults
  (seam.md, tooling.md specialized; NEW deposits.md, iteration-workflow.md, design-schema.md stub,
  dry-run.md — closing the gap where the contract named files the template did not ship); claude CLI
  added REQUIRED and skill-creator/skill-auditor added conditional to the universal manifest
  (platform/TOOLING.md) and bin/scan-tools.sh; SKILLS.md gate→play map gains skill-creator (build)
  and skill-auditor (conformance).
- why: the engine's checks (schema-discovery, fresh-context evaluator, substance-vs-surface
  done-gate, source-pinning) are shaped for living systems that iterate, and fought one-shot content
  generation; fixing the domain lets core carry the Claude Code toolchain and seam defaults every
  pilot was re-deriving. Operator-approved pivot (2026-07-03).
- tested: `bash bin/scan-tools.sh` exits 0 with `claude (Claude Code CLI) … PRESENT` and
  `skill-creator / skill-auditor … PRESENT`; leftover-claim grep
  (`domain-agnostic|agnostic to domain|never names a domain|operator supplies the domain`) returns
  only the glossary lineage note and this entry; every remaining "domain" hit means the FIXED domain,
  never a per-pilot boundary; no "instantiation" wording remains.
- revert-risk: restoring "domain-agnostic" wording re-opens the two-senses-of-"domain" drift (the
  per-pilot boundary vs the fixed domain), contradicts the deletion-test wording now synchronized
  across CLAUDE.md / ARCHITECTURE.md / pilots/CONTEXT.md / README, and orphans the pre-filled
  template defaults plus the claude-CLI / skill-auditor scan rows. The no-auto-loop law, single-agent
  law, ICM exclusion, deferral discipline, glass-box, and logging mandates were deliberately left
  verbatim — reverting this entry does not touch them because this change never did.
