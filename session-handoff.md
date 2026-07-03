# session-handoff.md — Clock-Out Note (cross-session continuity)

Updated at the end of every working session. The next session reads this FIRST. Keeps the agent from
losing the thread across long runs.

## Format
```
## <ISO-8601 timestamp> — session N
- verified: <what is confirmed working>
- changed: <what changed this session>
- broken: <what is known broken / blocked>
- next: <the single next-best step>
```

## Current state

## 2026-07-03 — session 1 (post-reset)
- verified: `bash bin/scan-tools.sh` exits 0 (claude CLI + skill-creator/skill-auditor PRESENT);
  leftover-claim grep clean (only the glossary lineage note remains); template contract closure holds
  (every file named in `pilots/_TEMPLATE/CONTEXT.md` now ships, except answer-key/ and learned-seam/
  which are per-pilot by design).
- changed: the engine specialized — domain fixed to Claude Code powered systems (see
  `changelog/CHANGELOG.md` 2026-07-03, marked tested). Doctrine re-scoped across core; scope guard
  added ("What M2W is NOT for"); `pilots/_TEMPLATE/` pre-filled with Claude Code defaults + four new
  files; Claude Code toolchain added to the universal tool scan.
- broken: nothing known.
- next: commission the first pilot — copy `pilots/_TEMPLATE/` into a system's own project, name the
  system, and run the seam's training run (watch → propose → act).
