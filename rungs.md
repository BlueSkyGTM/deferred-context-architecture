# Rungs

The one file that names models. Constructs declare a rung; this says what serves that rung
today. Changing supplier is an edit here and nowhere else, which is the whole of what model
agnosticism requires.

Method is `mechanics/tiering.md`. This is the instance, and the two are kept apart on purpose.

## What serves each rung

Measured 2026-08-26 with `tools/probe_models.py` from a local machine.

| Rung | Served by | Answered in | Tokens |
|---|---|---|---|
| none | Shell, Python, the host system's own checks | Instant | Free |
| fetch | Rung zero. No model surface found yet | | |
| build | `glm-4.6` | 0.84s to 1.08s | 14 |
| build, cheap | `glm-4.5-air` | 1.55s | 13 |
| build, cheapest | `glm-4.5-flash` | 0.61s | 21 |
| judgment | Claude, in session | | Not separately measured |
| judgment, alternate | `glm-5` | 1.22s to 7.78s | 22 |
| judgment, alternate | `glm-5.2` | 1.24s | 22 |

Model names are case insensitive on this surface: `GLM-5` and `glm-5` both answer. Lower case
is used above because it is what the vendor's own documentation uses and one form beats two.

## The surface, which is the thing that was actually wrong

Z.ai sells two products against the same key. The open platform is pay-as-you-go and bills a
balance. The coding plan is Anthropic-shaped and carries its own quota.

| | Open platform | Coding plan |
|---|---|---|
| Base | `https://api.z.ai/api/paas/v4` | `https://api.z.ai/api/anthropic` |
| Path | `/chat/completions` | `/v1/messages` |
| Auth | `Authorization: Bearer` | `x-api-key` plus `anthropic-version` |
| Reaches | Two free-tier Flash models | Everything above |

The first probe hit the open platform and found eight of ten models refusing for want of
balance. That measured an empty wallet, not a plan. **Every model in the table above is on the
coding plan and always was.** Probe with `--surface anthropic`.

## The fetch rung, still open

Web-Reader, Search-Prime and Search-Prime-Claude return HTTP 500, "Internal Network Failure",
on the coding plan, having returned a balance refusal on the open platform. A 500 rather than a
404 is the tell: these are search and retrieval products with their own request shape, and
sending them a chat body produces a server error rather than a clean rejection.

So the fetch rung is unresolved rather than unavailable, and the honest state is that the
endpoint has not been found. **Rung zero holds it meanwhile**, which is not a hardship: finding
which files touch a thing, listing what exists, confirming a path and counting are not model
questions, and shell answers them free and identically every time. Live web retrieval is the
part that genuinely needs a model, and nothing built so far depends on it.

## The latency question, now closed

An earlier run recorded `GLM-4.7-Flash` at 20.59 seconds against `GLM-4.5-Flash` at 0.78, and
this file filed it as a question rather than a property. That was right.

On the coding plan every model answers between 0.6 and 1.6 seconds, and `glm-5` returned 7.78s
on one call and 1.22s on the next. The variance is cold start and queueing, not a property of
any model. Nothing should be routed or avoided on the strength of a single timing.

## What has not been measured

**Whether any of these can hold a judgment position.** Every number above comes from asking a
model to reply with the word "ok". That measures reachability and latency and says nothing
about quality. Listing `glm-5` at the judgment rung records that it is reachable, not that it
is trusted there.

The test that would settle it is the manufactured outsider working: hand it an artifact and
criteria, withhold the argument, and see whether it returns a defensible no.
`mechanics/evaluation.md` describes the position. Nothing has yet occupied it.

## Changing this file

Contracts name rungs. Nothing anywhere else names a model. When a supplier changes, a plan is
funded, or a local model comes up on the operator's hardware, the edit is the table above and
nothing follows it.

Re-run the probe and date the result. A rung mapping that was true once and is never
re-measured is the drift `foundations/failure-modes.md` describes.
