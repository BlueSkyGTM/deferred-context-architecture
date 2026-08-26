# Installing the harness

Three files make delegation a default rather than a request in a host system. Copy them, then
prove the gate fires, because a gate that is installed and never consulted looks exactly like a
gate that is working.

## What to copy

| From | To | Committed |
|---|---|---|
| `tools/hooks/card_gate.py` | `tools/hooks/card_gate.py` | yes |
| `templates/harness/settings.json` | `.claude/settings.json`, merged | yes |
| `templates/harness/gitignore-lines` | appended to `.gitignore` | yes |
| `.claude/skills/dca-delegate/` | `.claude/skills/dca-delegate/` | yes |

**Merged, not overwritten.** If the host system already has `.claude/settings.json`, add the
`PreToolUse` entry to the array it already carries. A settings file replaced wholesale takes
every hook and permission in it with it.

**Never `.claude/settings.local.json`.** Local settings are device-local by design and are not
committed, so a gate installed there is live on one machine and silently absent on every other.
That is the failure this arrangement exists to make visible, so it must not be the way it is
installed.

## Then teach it the tree

The gate ships knowing this method's own layout. Open `tools/hooks/card_gate.py` and set
`CORE_DIRS` to the folders in the host system that belong to the core: wherever rulings,
mechanics, templates and tooling live. Everything not listed is a working folder and is gated.

Getting this wrong in the safe direction produces a refusal with a reason attached, which is a
question a person can answer in a second. Getting it wrong in the other direction gates nothing
and says nothing.

## Then prove it

```
python3 tools/audit.py --harness
```

Never fired is the expected state immediately after installing. Hooks load from directories that
already held a settings file when the session started, so a settings file created inside a live
session is usually not read until the hooks menu is opened once or the session restarts.

Once it reports a timestamp, defeat it deliberately: edit a file inside a working folder with no
played card and confirm the refusal. An untested gate is a belief.
