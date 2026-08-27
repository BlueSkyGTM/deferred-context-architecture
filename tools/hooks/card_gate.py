#!/usr/bin/env python3
"""The gate. A PreToolUse hook that refuses a write into a working folder unless a card is
played for it and the path sits inside the wing's chartered territory.

`../../foundations/the-binding.md` says the core selects and never authors, and
`../../mechanics/the-bbs.md` says a card is written before anything fires. Neither statement is
worth much while the only thing enforcing them is the core's willingness to comply. Three layers
were available and only one of them is a default:

    a CLAUDE.md instruction   enforced by the model choosing to comply    a request
    a skill                   enforced by the model deciding it applies    a method
    a hook                    enforced by the harness                      a default

This is the third. It is the only part of this architecture that a model cannot talk its way
past, which is why it holds the one rule that most wants breaking: **do not do the work
yourself.**

## What it allows

Writes to the core's own territory, because deliberating, routing, ruling and archiving are the
core's job and always were. The board, the router, `decisions/`, `_archive/`, `foundations/`,
`mechanics/`, `templates/`, `tools/`, `origins/`, `skills/`, `.claude/`, and any file sitting at
the root of the tree.

Writes anywhere outside the tree, because this gate speaks for one tree and has no board for
anything else.

## What it refuses

A write into a working folder with no played card naming that folder. That is the core doing the
work instead of sending it, which is the failure the whole method exists to prevent, and it is
the one that feels most like progress while it happens.

A write outside the wing's chartered territory, even with a valid played card. Territory is a
grant, absence is prohibition, and `../../templates/CHARTER.md` says acting outside a charter is
void rather than discouraged. Void has to mean something a person cannot override by wanting to.

A card sending a wing to a rung its charter withholds. `templates/BBS.md` has always said a card
may not do this and nothing enforced it, which is where territory was before this file existed.
Spend ceilings are still unenforced, because the gate sees a write rather than a bill.

**A write by a woken agent into the core's territory.** The board, the router, the rulings and
the method are handed down and never reached up into. Geography is supposed to make that
unreachable, and where an agent shares a working directory with its caller it is not, so the
same signal that identifies the agent is what refuses it here.

**A write by the core into a folder its own card opened.** Playing a card is not permission to do
the work, it is permission for the agent the card wakes. The payload carries `agent_id` only when
a hook fires inside a woken agent, so the two parties are distinguishable and the core is refused
in the one place it most wants not to be: after it has done the deliberation, with a valid card
in hand, one edit away from finishing the job itself.

That check has a live edge. It reads a woken agent as something the harness woke, so a binding
assembled some other way, in a separate process the harness never sees, is refused here rather
than allowed. The refusal says so. Erring that way is deliberate: a gate that guessed in the
other direction would let anything through by claiming to be an agent.

A card carrying an unfilled placeholder authorises nothing. That is upstream's placeholder sweep
with teeth: ICM completes setup only when no `{{` patterns remain, and here an unfilled card is
simply not playable. It is also what keeps the example card in `templates/BBS.md` from granting
anything.

## Failing open, on purpose

A crash here allows the write and says so loudly. A gate that fails closed turns any bug in
itself into a tree nobody can edit, and the operator's only recovery is to delete the gate, which
is a worse end state than the one it was guarding against.

The cost of that choice is a gate that could die silently, so it does not get to be silent. Every
run the harness starts stamps `.claude/gate-last-fired`, and `tools/audit.py --harness` reports
what that stamp says. Never fired reports as not live, which is the signal on a machine where the
hook was never approved.

**A run piped in by hand leaves no stamp.** Only the harness supplies a `session_id`, so only the
harness can write the file that claims the gate is live. Otherwise testing the gate would be the
thing that made it look installed, and the one check for silent death would certify itself.

Standard library only, project-relative paths only. A gate that needs an install is a gate that
is not installed somewhere.
"""

import json
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

# The core's own territory. Writing here is the core doing its own job rather than avoiding
# delegation, so none of it is gated. `handoff/` is on the list because a handoff is a mandate
# the operator issues, which makes it the same class of artifact as a ruling in `decisions/`,
# not a folder where work happens.
CORE_DIRS = {
    ".claude", ".git", ".github",
    "_archive", "decisions", "foundations", "handoff", "mechanics",
    "origins", "skills", "templates", "tools",
}

BOARD = "BBS.md"
CHARTER = "CHARTER.md"
STAMP = Path(".claude") / "gate-last-fired"

PATH_KEYS = ("file_path", "notebook_path", "path")
FIELD = re.compile(r"^\s*([a-z_]+):\s*(.+?)\s*$")
BACKTICKED = re.compile(r"`([^`\n]+)`")


def unfilled(value):
    """A placeholder authorises nothing. Upstream sweeps for these before declaring setup done."""
    return "<" in value or "{{" in value


def section(text, heading):
    """The lines under one `## heading`, up to the next heading of the same level."""
    out = []
    inside = False
    for line in text.splitlines():
        if line.startswith("## "):
            inside = line[3:].strip().lower() == heading.lower()
            continue
        if inside:
            out.append(line)
    return out


def played_cards(root):
    """Every played card, as a dict of its filled fields. A fenced block per card.

    Fields carrying a placeholder are dropped rather than the card, so a half-filled card opens
    nothing while still being visible to a person reading the board.
    """
    board = root / BOARD
    if not board.exists():
        return []
    text = board.read_text(encoding="utf-8", errors="replace")
    cards = []
    current = {}
    for line in section(text, "Played"):
        if line.strip().startswith("```"):
            if current:
                cards.append(current)
                current = {}
            continue
        match = FIELD.match(line)
        if not match:
            continue
        key, value = match.group(1), match.group(2).strip().strip("`")
        if not unfilled(value):
            current[key] = value.rstrip("/")
    if current:
        cards.append(current)
    return cards


def permitted_rungs(charter):
    """The rungs a charter's Capability table marks allowed."""
    text = charter.read_text(encoding="utf-8", errors="replace")
    allowed = set()
    for line in section(text, "Capability"):
        cells = [cell.strip().strip("`*") for cell in line.strip().strip("|").split("|")]
        if len(cells) < 2 or cells[0].lower() in ("rung", "---", ""):
            continue
        if set(cells[0]) <= set("-: "):
            continue
        if cells[1].lower() in ("yes", "y", "true"):
            allowed.add(cells[0].lower())
    return allowed


def charter_for(target, root):
    """The nearest charter at or above a path, and the territory it grants.

    Returns (charter_path, [territory]) or (None, []) when no wing claims the path.
    """
    current = target.parent
    while True:
        candidate = current / CHARTER
        if candidate.exists():
            text = candidate.read_text(encoding="utf-8", errors="replace")
            territory = []
            for line in section(text, "Territory"):
                for match in BACKTICKED.findall(line):
                    match = match.strip().rstrip("/")
                    if match and not unfilled(match):
                        territory.append(match)
            return candidate, territory
        if current == root or root not in current.parents:
            return None, []
        current = current.parent


def inside(child, parent):
    return child == parent or parent in child.parents


def stamp(payload, root, verdict, detail):
    """Prove the gate ran on this device. A silent gate and a dead gate look identical.

    Only a run the harness started is recorded, which is what `session_id` in the payload marks.
    A hand-piped test that stamped the file would be evidence of nothing except that somebody
    tested it, and the check for a dead gate would pass by being run.
    """
    if not payload.get("session_id"):
        return
    try:
        path = root / STAMP
        path.parent.mkdir(parents=True, exist_ok=True)
        now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        writer = payload.get("agent_type") or ("agent" if payload.get("agent_id") else "core")
        path.write_text("{} {} {} {}\n".format(now, writer, verdict, detail[:80]),
                        encoding="utf-8")
    except OSError:
        pass


def deny(reason):
    json.dump({"hookSpecificOutput": {
        "hookEventName": "PreToolUse",
        "permissionDecision": "deny",
        "permissionDecisionReason": reason,
    }}, sys.stdout)
    sys.stdout.write("\n")


def decide(payload, root):
    """(verdict, detail). Verdict is `allow` or `deny`; detail is shown when it is `deny`."""
    tool_input = payload.get("tool_input") or {}
    raw = ""
    for key in PATH_KEYS:
        if tool_input.get(key):
            raw = str(tool_input[key])
            break
    if not raw:
        return "allow", "no path in tool input"

    target = Path(raw)
    if not target.is_absolute():
        target = (Path.cwd() / target)
    target = target.resolve()

    if not inside(target, root):
        return "allow", "outside this tree"

    rel = target.relative_to(root)
    core_side = len(rel.parts) == 1 or rel.parts[0] in CORE_DIRS
    if core_side:
        if payload.get("agent_id"):
            return "deny", (
                "`{}` is the core's own territory and a woken agent may not write it. Structural "
                "change is filed as a finding and waits for a ruling: write what is missing to the "
                "path your card named and return, per the folder's escalate condition.".format(
                    rel.as_posix())
            )
        return "allow", "core territory"

    opened = [
        card for card in played_cards(root)
        for path in (card.get("door"), card.get("returns"))
        if path and inside(target, (root / path).resolve())
    ]
    if not opened:
        return "deny", (
            "No played card opens `{}`. This is a working folder, and the core does not do the "
            "work: write a card naming that folder on {}, play it, and let the binding write. "
            "If this folder is the core's own, add it to CORE_DIRS in tools/hooks/card_gate.py "
            "and say why in the commit.".format(rel.as_posix(), BOARD)
        )

    charter, territory = charter_for(target, root)
    if charter is None:
        return "deny", (
            "`{}` sits under no charter. A wing without one has no territory, and absence is "
            "prohibition: grant it a {} from templates/CHARTER.md first.".format(
                rel.as_posix(), CHARTER)
        )
    granted = [t for t in territory if inside(target, (root / t).resolve())]
    if not granted:
        return "deny", (
            "`{}` falls outside the territory granted by `{}`, so the write is void whatever the "
            "card says. Amend the charter, or send the work to a wing that owns this path.".format(
                rel.as_posix(), charter.relative_to(root).as_posix())
        )

    allowed = permitted_rungs(charter)
    tiers = {card.get("tier", "").lower() for card in opened if card.get("tier")}
    if allowed and tiers and not (tiers & allowed):
        return "deny", (
            "The card opening `{}` runs at {}, and `{}` permits only {}. A wing cannot be sent "
            "to a rung its charter withholds, whatever the card says.".format(
                rel.as_posix(), " or ".join(sorted(tiers)),
                charter.relative_to(root).as_posix(), ", ".join(sorted(allowed)))
        )

    if not payload.get("agent_id"):
        return "deny", (
            "A card is played for `{}`, and this write is not coming from the agent it woke. "
            "Playing a card commits the work to a binding, not to the core: dispatch it with that "
            "folder as the working directory and let it write. If a binding really is running "
            "here and the harness cannot see it as one, that is worth recording before working "
            "around it.".format(rel.as_posix())
        )

    return "allow", "card played, inside territory, rung permitted, written by {}".format(
        payload.get("agent_type") or "a woken agent")


def main():
    root = Path(os.environ.get("CLAUDE_PROJECT_DIR") or Path.cwd()).resolve()
    try:
        payload = json.load(sys.stdin)
    except (json.JSONDecodeError, ValueError):
        stamp({"session_id": "unreadable"}, root, "error", "unreadable stdin")
        json.dump({"systemMessage": "card gate: unreadable hook input, write allowed"},
                  sys.stdout)
        return 0

    try:
        verdict, detail = decide(payload, root)
    except Exception as error:  # noqa: BLE001 - failing open is the documented choice
        stamp(payload, root, "error", type(error).__name__)
        json.dump({"systemMessage":
                   "card gate: failed open ({}), write allowed".format(error)}, sys.stdout)
        return 0

    stamp(payload, root, verdict, detail)
    if verdict == "deny":
        deny(detail)
    return 0


if __name__ == "__main__":
    sys.exit(main())
