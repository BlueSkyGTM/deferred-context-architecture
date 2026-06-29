# failures.md — What Broke or Stopped (append-only)

# Entry format (see platform/LOGS.md):
# ## <ISO-8601 timestamp>
# - stage: <stage or "skeleton-verify">
# - what: <what broke or stopped>
# - expected: <what the spec said>
# - found: <what was actually there>
# - action: <stopped / benched / flagged>

## 2026-06-29T19:03:11Z
- stage: audit (cross-model: Claude Opus 4.8 + Codex, read-only)
- what: Pre-refactor audit of the chat-authored specs. Findings being resolved in the engine/pilot separation pass.
- expected: A domain-AGNOSTIC core (operator supplies the domain) with the GTM-curriculum pilot cleanly separable; no internal contradictions.
- found (severity-ranked):
    - BLOCKER: GTM/curriculum/wiki->course specifics hard-wired into core law/platform/stage files (ARCHITECTURE §2.2/§6, DRY-RUN, TOOLING, SKILLS, glossary, capstone-build, evaluator-rubric, SETUP, session-handoff, LOGS).
    - BLOCKER: stage 04 defines iteration AS sources->wiki->graph->course (curriculum is the engine); must become a generic iteration-workflow interface.
    - BLOCKER: seam definition contaminated by domain ("civil-engineering-shaped", DevOps near-misses, ~50% claim) in ARCHITECTURE §2.2 + glossary.
    - BLOCKER: single-agent law (PRINCIPLES #5) contradicted by M2W.md "Parallelism is a runtime setting" and evaluator-rubric.md worker!=checker / "second-agent/gstack review".
    - BLOCKER: the manifest has NO physical location/schema (no manifest/ folder); the system is named for it.
    - BLOCKER: design-schema bootstrap null on pass 1 (schema "cut from logs of proven-good work" but pilot is the first run).
    - HIGH: DRY-RUN 1c depends on missing artifacts (quarantined seam corpus/answer key, gtm-starter-kit, learned-seam files) with no paths/schemas/ownership.
    - HIGH: excavation vault-account index underspecified; deposit/extractor matching rule undefined.
    - HIGH: vault/CONTEXT.md says vault material is "earned" — contradicts vault as the raw pre-assay intake door.
    - HIGH: circular read-order (README vs BUILD-INSTRUCTIONS vs SETUP vs CONTEXT.md disagree on what to read first).
    - HIGH: stage-04 CONTEXT routing omits capstone-build.md + evaluator-rubric.md.
    - MEDIUM: assay off-seam (tailings) evidence rule not operationalized; only on-seam matching defined.
    - MEDIUM: frontmatter labels assigned/lifecycle fields (id/stage/assay/sealed) as "observed".
    - MEDIUM: ECP defined but never operationalized.
    - MEDIUM: done-gate "mechanical" still needs a classifier + iteration-log path.
    - LOW: glossary "Seam" + ARCHITECTURE §2.2 have broken sentences (chat edit corruption).
- action: flagged; resolving in the engine/pilot separation refactor (this session). Core->never references pilot; pilot->references core (one-way, per ICM).

