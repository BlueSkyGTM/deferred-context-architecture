# dry-run.md — TEMPLATE (the default validation ladder for a Claude Code system)

Core defines the generic ladder (`DRY-RUN.md`: fidelity × consequence; reversible-first;
watch → propose → act). This file maps it onto the fixed domain — a Claude Code system validated by
behaving in a live session. Keep the shape; your sub-runs, material, and grading are yours.

## Reversible ground (the law before anything live)
- A scratch clone / disposable worktree of the target repo — never the real one.
- A disposable Claude Code session — nothing installed to user scope, no settings written outside the
  scratch ground.
The DELIVERABLE is throwable; the LEARNING is sticky — so the between-pass audits are required.

## The ladder
1. **Watch / train** — the human makes every assay call; the system logs each with its reason into
   `learned-seam/`. `<Your watch sub-run: which deposits, how many pieces.>`
2. **Propose / correct** — the seam proposes routes; the human confirms or corrects. Advance only
   when corrections drop on settled cases.
3. **Act / grade (blind)** — the built system runs in a live, disposable Claude Code session against
   prompts it has never seen, graded against the QUARANTINED `answer-key/` the human holds and the
   model does NOT. Exercise every trigger phrase, hook, and tool surface; the transcript is the
   evidence. PASS: correct behavior with rare escalation. `<Your blind experiment + pass bar.>`
4. **Live pass** — only after the blind grade holds: install into the real repo / user scope. Even
   then it is not the system's first autonomous act — that was the point of the ladder.

## Blocked-on-run items
`<List what only the run can answer — e.g. does the done-gate's substance-to-surface signal fire on
behavioral (not prose) change; does the seam discover the boundary blind.>`
