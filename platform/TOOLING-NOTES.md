# platform/TOOLING-NOTES.md — Machine-Specific Install & Troubleshooting (NOT law)

Per-machine operational notes for tools in the universal manifest. The LAW — admission rules,
fences, manifests, the scan protocol — stays in `platform/TOOLING.md`; this file only records the
gotchas that cost real time to rediscover. Nothing here changes policy.

**gbrain note (embeddings need the key at MCP-server start):** gbrain embeds via OpenAI
(`text-embedding-3-large`). The gbrain MCP server (`gbrain serve`) captures its environment at START,
so if `OPENAI_API_KEY` wasn't present when Claude Code launched it, embeddings silently produce 0
coverage (pages exist, search returns nothing). Fix: ensure `OPENAI_API_KEY` is a persistent env var
(Windows User scope / shell profile), then RESTART the host so the server relaunches with it; then
backfill embeddings. Also: PGLite is single-connection, so the `gbrain` CLI (and `/sync-gbrain`) cannot
run while the MCP server holds the brain open — use the gbrain MCP tools, or stop the server first.
And: `gbrain serve` exposes the API but does NOT process the job queue — submitted jobs (embed, sync)
sit `waiting` until a worker runs. Run `gbrain autopilot --install` (a per-machine background daemon)
to actually process embeds/syncs. Until the daemon runs, embeddings stay at 0 even with the key set.

**gbrain install (clone, NOT the registry) + onboarding a second machine:** gbrain's CLI is a Bun
program published from `github.com/garrytan/gbrain` — it is NOT the unrelated `gbrain` on the public
npm registry (that is a different package; `npm i -g gbrain` installs the wrong thing). Install:
ensure `bun` is present, then `git clone https://github.com/garrytan/gbrain && cd gbrain && bun
install`, then put it on PATH with `npm link` (or `bun link`). If the CLI errors right after linking,
run `bun run build` in the clone. To point a SECOND machine at an EXISTING brain (e.g. a shared
hosted-Postgres brain), do NOT `migrate` or `--force` anything — install as above, then `gbrain init
--url '<the brain's connection string>'`, which CONNECTS to the existing brain without copying or
wiping. Then register the MCP at user scope (`claude mcp add --scope user gbrain -- <abs-path>/gbrain
serve`) and restart the host so `mcp__gbrain__*` tools load. NEVER commit the connection string — it
carries the DB password; fetch it per-machine from the provider (e.g. Supabase → Connect → Session
pooler) and keep it out of git. (PGLite is single-machine/local; a hosted-Postgres brain is what
enables multi-machine sharing — many connections, no single-connection lock.)
