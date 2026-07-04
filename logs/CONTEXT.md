# CONTEXT.md: logs/ (observability, glass-box)

- `failures.md`, what broke or stopped, append-only. When a stage cannot proceed, write it here and
  stop; never guess past it.

Glass-box: if something went wrong, it is a row here, not a memory. A silo may keep its own run notes
in its `stages/*/output/`; this shared log is for machine-level failures.
