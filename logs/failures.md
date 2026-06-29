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

## 2026-06-29T19:40:59Z
- stage: full-run simulation (sim/full-run branch + Codex cold-agent narration)
- what: Simulated a complete run (4 pieces: 2 cart, 1 tailings, 1 bench -> 2 manifested -> 1 sealed deliverable). The chain COMPLETED, but only by inventing inter-stage contracts the specs do not define. Codex (cold) and the live trace agreed on the gaps.
- expected: a cold agent runs the chain WITHOUT guessing (guessing is forbidden); every stage handoff is fully specified.
- found (confirmed inter-stage chain-breaks):
    - BLOCKER: assay produced no structured cart record carrying seam_match, but stage 03 frontmatter requires it (had to invent a cart-record format).
    - BLOCKER: design schema is "cut from logs" but no path/format for where it lives (invented pilots/<name>/design-schema.md).
    - BLOCKER: gate-check outcome enum (LOGS.md) lacked accept|revise|block that the evaluator requires (contradiction).
    - HIGH: bench escalation content named but no file format/location.
    - HIGH: shipped deliverable had no frontmatter schema / seal semantics (and no rule for sealing the consumed manifest items); no defined working location for the in-flight deliverable.
    - MEDIUM: deposit `type:` enum did not match the extractor-table labels (pilot deposits.md).
    - MEDIUM: stable-id convention undefined (vault/manifest ids).
    - BY DESIGN (not a bug): on a first run the agent cannot autonomously make seam calls (human must) and tools are unwired, so a fully autonomous cold run correctly STOPS at the assay. The seam is trained, not assumed.
- readily-inferred (safe to leave implicit): tailings/bench/cart routing given a seam; only-carts-proceed; slug id; source/bounded_space defaults for operator-supplied items.
- action: all confirmed chain-breaks FIXED this session (stage 02 cart-record + bench-note format; stage 03 inherits cart record; LOGS enum; stage 04 schema path + deliverable frontmatter + seal semantics + working location; excavation id convention; pilot deposit-label alignment). Sim artifacts preserved on branch sim/full-run (not merged).

