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

## 2026-07-03 — Hygiene pass (post-pivot adversarial audit)
- what: (1) machine-specific gbrain install/troubleshooting (~30 lines) extracted from
  platform/TOOLING.md into NEW platform/TOOLING-NOTES.md (companion, not law; pointer left in place;
  platform/CONTEXT.md names it); (2) BUILD-INSTRUCTIONS.md marked COMPLETE (status banner; CLAUDE.md
  read-order item 6 marked historical); (3) SETUP.md slimmed — restated read-order/tool-scan prose
  cut to pointers; kickoff prompt and the vault one-door rule kept verbatim, RUN mode made primary;
  (4) glossary gains fresh-context evaluator / contamination defense / five-layer routing pointer
  entries; (5) local-only: deprecated .claude/skills/save-memory removed (superseded by save).
- why: an adversarial cold-read audit judged the repo designed-not-accumulated (~92% load-bearing)
  with three hygiene debts: policy mixed with machine scaffolding, a completed pass still in the
  mandatory read order, and a 62%-restated SETUP.md. Audit verdicts also recorded: naming stays
  (mining vocab, "pilot", M2W); the CLAUDE.md↔README scope-guard duplication is deliberate (READMEs
  are standalone).
- tested: `bash bin/scan-tools.sh` exits 0 (manifest rows untouched); grep for the gbrain
  machine-note strings hits only TOOLING-NOTES.md; read-order and BUILD-INSTRUCTIONS self-reference
  agree. Does NOT alter anything in the 2026-07-03 pivot entry above.
- revert-risk: re-inlining the machine notes re-mixes law with scaffolding; un-marking
  BUILD-INSTRUCTIONS puts a completed pass back in the mandatory read path; restoring SETUP.md's
  restatements re-creates the drift surface the canonical-source law forbids.

## 2026-07-03 — Restructure: M2W → DCA (Deferred Context Architecture); mono-pipeline → well + silos
- what: The single mono-pipeline was replaced by a multi-silo architecture over one shared well.
  NEW: `_core/` (CONVENTIONS.md = native 5-layer routing + stage-contract pattern + one-way/glass-box
  laws; deferral.md; well-contract.md; tooling.md + tooling-notes.md; templates/silo/ = a faithful
  blank ICM workspace with 01-draw drawing from the well and a build-stage template carrying the
  staking rule); `silos/CONTEXT.md`; `vault/` recontextualized as THE WELL (account.md is its
  catalogue); root `CLAUDE.md` and `README.md` rewritten thin as the DCA law. RETIRED (deleted):
  top-level `stages/`, `pilots/`, holding folders `carts/ tailings/ bench/ manifest/ library/`,
  heavy `platform/` law (GATES/SKILLS/LOGS/glossary/PRINCIPLES/MWP/CONTEXT + TOOLING → distilled into
  `_core/`), `M2W.md ARCHITECTURE.md DRY-RUN.md SETUP.md BUILD-INSTRUCTIONS.md` root CONTEXT.md, and
  the assay-only log streams (gate-checks, rejections). `bin/scan-tools.sh` now scans `silos/*` not
  `pilots/*`; `.gitignore` updated.
- why: the mono-pipeline hoards (defer-and-preserve, never delete) and only ever builds one thing.
  The pattern that actually worked (the scriptorium: 7 books, any order) is many independent silos
  over one shared well, each a native ICM workspace drawing the slice it needs on demand — which is
  why the ICM inside a silo stops inventing on the spot (always fed real assets). Operator-directed
  redirection (2026-07-03).
- SUPERSEDES (not a silent revert — surfaced per the REVERT GUARD): the "Domain fixed: Claude Code
  systems" pivot entry above. Its `pilots/_TEMPLATE` and Claude-Code framing are retired in favor of
  the silo model; the operator chose DCA over that framing. The claude-CLI tool-scan row it added is
  KEPT (carried into `_core/tooling.md`). No part of it was undone without being named here.
- tested: `bash bin/scan-tools.sh` exits 0; one-way grep finds no `silos/<name>` reference in
  `_core/`, `vault/`, or root docs; deletion test holds (remove `silos/` → well + `_core` still
  stand); the restructure is a net deletion (fewer lines of law than the retired `platform/` + root
  docs).
- revert-risk: restoring the mono-pipeline re-introduces the hoarding architecture (never-delete,
  single-deliverable) the scriptorium pattern was chosen over, and orphans `_core/` + the silo
  template + the well-catalogue recontextualization. The deferral discipline, single-agent, glass-box,
  and one-way-reference laws were carried forward (distilled into `_core/`), not dropped.

## 2026-07-03 — Proof build: DCA composes (first operating history) + the keystone mechanism
- what: A minimal two-silo system proving DCA end to end. NEW: `vault/keystone-task.md` (a **keystone**
  — a shared contract in the well two silos build against) + its `account.md` row; `silos/producer`
  and `silos/consumer` (real silos copied from the template, each drawing only the keystone, built
  independently — one-way, neither references the other); `bin/join-check.py` (integration check:
  reads the keystone from the well, verifies producer conformance, runs producer → consumer); a
  falsifiable-check probe (extra/missing field → rejected); `silos/PROOF.md` (the run record).
- why: the architecture review named DCA's gap — composition without verified integration — and the
  session's own verdict (architecture is not proof) demanded a real run, not admiration. The keystone
  closes the gap: interoperating silos align through a shared well contract without referencing each
  other; fit is mechanically checked at the join.
- tested: `python bin/join-check.py` → PASS (`3 tasks, 2 done`); negative probes (extra field, missing
  field) → REJECTED exit 1; positive probe → exit 0. The check is falsifiable, not a rubber stamp.
  Deletion test still holds (remove `silos/` → well + `_core` stand). `bash bin/scan-tools.sh` exits 0.
- revert-risk: removing the proof erases DCA's only operating history and the keystone mechanism —
  the one demonstrated answer to the integration gap. The proof silos are examples, not core; they may
  be deleted without touching the rig, but the keystone concept they validated is the load-bearing
  finding.
- follow-up (NOT done — earned, not given): the keystone is proven but not yet written into the law
  (`_core/`). Promote it to a first-class DCA concept only after a second, non-trivial keystone holds.

## 2026-07-06 — Restructure order executed: arms layer + keystone-forge; silos frozen as proof
- what: The RESTRUCTURE-STANDBY.md order was issued in-session and executed. NEW: `arms/` (the
  operating layer; `arms/CONTEXT.md` = the four required pieces + one-way/no-connector laws);
  `_core/templates/arm/` (the silo template + `runbook.md`, `done-when.md`, `decision-log.md`);
  `arms/arm-01/` (first arm, scaffolded empty, done-when filled by the operator);
  `keystone-forge/FORGE.md` (moved from root — creation + validation of keystones, Run 001 record);
  `bin/hedge_count.py` (moved from root, beside join-check.py, per FORGE.md's own pointer);
  `vault/exhaust/` (the well's record of closed arms' decision logs — records, not drawable
  material, no account.md rows). CHANGED: RESTRUCTURE-STANDBY.md status FROZEN → EXECUTED with the
  four operator inputs recorded; silos/CONTEXT.md marked frozen-as-proof; CLAUDE.md shape/read-order
  updated; README gains the "Arms: The Operating Layer" section. UNTOUCHED: `vault/keystone-task.md`,
  `bin/join-check.py`, all silo internals — silos/ stays exactly as it ran so the hardcoded
  join-check paths keep working (this is why silos/ was frozen rather than renamed).
- why: operator-issued restructure order (2026-07-06). Operator inputs, not invented: silos stay as
  frozen proof + new arms/ layer; no silo→arm conversions; first arm done-when = join-check PASS +
  all four pieces present; connectors = none. Keystones deploy only in the DRA clone, never here
  (standby sequencing, kept as standing law).
- tested: `python3 bin/join-check.py` → PASS (proof layer intact post-restructure);
  `bash bin/scan-tools.sh` → exit 0; `python3 bin/hedge_count.py README.md` runs from its new home;
  one-way grep — nothing in `_core/`, `vault/`, or `silos/` references `arms/arm-01`; nothing in
  `arms/` references a silo or another arm; arm-01 contains all four required pieces (done-when met).
- revert-risk: removing `arms/` orphans the executed order and the arm template but does not touch
  the proof (deletion test: well + `_core` + silos still stand). Un-freezing `silos/` for new work
  re-couples the proof record to live changes and risks breaking the immutable join-check's
  hardcoded paths. Moving FORGE.md or hedge_count.py back to root breaks FORGE.md's internal
  `bin/hedge_count.py` pointer and the standby doc's `keystone-forge/` location law.
