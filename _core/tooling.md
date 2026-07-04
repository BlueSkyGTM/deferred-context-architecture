# _core/tooling.md: the tool scan (universal tools; silos add their own)

Two manifests, read by `bin/scan-tools.sh`:
- the **universal manifest** below, tools every silo may use (intake extractors, the harness, the
  Claude Code CLI, retrieval). Lives in core.
- a **silo manifest** (`silos/<name>/tooling.md`, optional), tools specific to one silo's deliverable.
  Scanned into that silo's own `tool-status.md` when present.

`tool-status.md` is per-machine and gitignored, a fresh clone has no stale status; the first scan is
what tells you what to install. Nothing is installed by guess: unknown/auth/clone installs are flagged
`MISSING-ASK` for the human.

## Universal manifest (keep `bin/scan-tools.sh` detects in sync with this)

| tool | role | required | detect | install |
|---|---|---|---|---|
| gstack skills | harness + standing skills | yes | `[ -d ~/.claude/skills/gstack ]` | MISSING-ASK (ships with the Claude Code env) |
| claude (Claude Code CLI) | the runtime a silo builds/runs in | yes | `command -v claude` | MISSING-ASK (install per official docs; auth is machine-specific) |
| evaluator | the fresh-context conformance pass (rubric, no external tool) | yes | n/a | n/a |
| codex | cross-model review | optional | `command -v codex` | `npm i -g @openai/codex` |
| markitdown | intake: pdf/office to markdown | if that deposit type | `python -c "import markitdown"` | `pip install markitdown` |
| youtube-transcript | intake: video to transcript | if that deposit type | `python -c "import youtube_transcript_api"` | `pip install youtube-transcript-api` |
| article-extractor | intake: web article to markdown | if that deposit type | `python -c "import trafilatura"` | MISSING-ASK (candidate `pip install trafilatura`) |
| gbrain | retrieval projection (optional; readable files stay canonical) | optional | `command -v gbrain && [ -f ~/.gbrain/config.json ]` | see `tooling-notes.md` |
| LLMLingua | compress the CONTEXT fed to the model (never the deliverable) | optional | `python -c "import llmlingua"` | `pip install llmlingua` |

## Scan protocol
1. For each row, run `detect`. Record PRESENT / MISSING.
2. A MISSING **required** tool blocks a run of the affected stage, stop and report.
3. A MISSING tool whose install is unknown / needs auth / needs a clone to `MISSING-ASK`, never guessed.
4. Write results to `tool-status.md` (universal) and `silos/<name>/tool-status.md` (per silo). Glass-box.

Machine-specific install/troubleshooting (gbrain especially): `_core/tooling-notes.md`.
