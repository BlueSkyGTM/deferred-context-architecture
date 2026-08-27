#!/usr/bin/env python3
"""Rung zero. Check what a tree actually contains against what its files claim.

`mechanics/acceptance.md` argues that judging returned work has exactly two bad answers. A
purely mechanical check proves completion rather than quality. A quality review by the core
produces a send-back loop that converges on the operator doing the work. The way out is to make
the agent describe what it built, and then check the description mechanically. This is that
check.

Nothing here has an opinion. Every question it asks has a yes or no answer that a shell could
have reached, which is the whole point of the bottom rung: a deterministic check is not merely
cheaper than a model, it is more reliable than one.

    python3 tools/audit.py --repo                 # every pointer in this bundle resolves
    python3 tools/audit.py --folder path/to/dir   # audit one worked folder
    python3 tools/audit.py --folder path --relay  # allow declared handoffs outside the folder
    python3 tools/audit.py --harness              # is the gate installed and live on this device

Exit code is the verdict, so what reaches the core is a number rather than a paragraph.
Zero is clean, one is findings, two is a usage error.

## What --repo checks

Every relative path named in a markdown file resolves to something that exists. That is ICM's
"does every pointer in a routing table open", applied to prose as well as tables, and it is the
check that catches a rename nobody finished.

Three kinds of folder are skipped. Vendored ones, because their paths are relative to the
repository they came from and `NOTICE.md` says they are carried unmodified. `_archive/`, because
an archived file names the neighbours it had when it was live and the note on it already says
what replaced them. And `templates/`, because a template names paths that do not exist yet;
that is what makes it a template.

Some names are used as nouns rather than as pointers. "Write a `CONTEXT.md`" names a kind of
file. Those are listed in `GENERIC_NAMES` and not resolved, because treating them as pointers
produced findings nobody would act on.

A few files are device-local by design and are absent from a clean tree on purpose. They are
listed in `DEVICE_LOCAL`, and whether they exist is `--harness`'s question rather than this one's.

Repository slugs and branch names are shaped like relative paths and are not paths. They are
listed in `EXTERNAL_NAMES` rather than detected, because a rule general enough to catch them all
would also skip a genuinely broken pointer to a directory.

## What --folder checks

Three things, in the order they matter:

1. **Boundary.** No path named in a contract escapes the folder. A build whose declared inputs
   reach outside its working directory either had a wall that leaked or is describing work it
   did not do. `--relay` permits it, because `mechanics/tiering.md` allows one card's output to
   be the next card's input by design, and that case should be declared rather than tolerated.

2. **Outputs exist.** Every artifact the emitted `CONTEXT.md` claims to have produced is at the
   path it claims. An agent reporting a file it did not write is the completion fallacy in its
   most checkable form.

3. **Issued against emitted.** `CONTRACT.md` said what should come to exist. `CONTEXT.md` says
   what does. Inputs and outputs that appear in one and not the other are the only mechanical
   purchase anyone has on fit, and it is partial: a coherent build of the wrong thing can still
   line up. `foundations/failure-modes.md` number ten is that case.

## What --harness checks

Whether the gate in `tools/hooks/card_gate.py` is actually in force **on this device**, which is
a different question from whether it is in the repository. Four facts, none of them opinions:
the project settings file exists and carries the hook, the script exists and is executable, the
device-local settings file is not being used to install it, and the timestamp the gate stamps on
every run.

The last one is the one that matters. A gate can be committed, correct, and never once consulted,
because a settings file created inside a running session may not be loaded by it. Never fired is
reported as not live, which is the state a fresh clone is in until something loads it.

The remedy is smaller than it looks and is in the finding: rewriting the settings file in place,
with identical bytes, registers as a direct edit and the watcher picks it up mid-session. That
was measured here rather than assumed, on the session that installed the gate.

## What it deliberately does not do

It does not parse claims about counts out of prose. A tool that guesses which numbers in a
sentence were meant as assertions produces findings nobody trusts, and an untrusted check is
worse than no check. Where a count matters, state it as a check with a pass condition in the
contract's Audit table, where a person wrote what passing means.

It does not judge anything. If it ever needs to, it has stopped being rung zero.

Standard library only. A check that needs an install is a check someone skips.
"""

import argparse
import json
import os
import re
import sys
from pathlib import Path

SKIP_DIRS = {".git", "_archive", "templates",
             "origins/icm-architect", "origins/icm-upstream"}

# Names this method uses as nouns rather than as pointers. "Write a CONTEXT.md" names a kind of
# file, not a file. Treating them as pointers produced findings nobody would act on, and an
# untrusted check is worse than no check.
GENERIC_NAMES = {"CONTRACT.md", "CONTEXT.md", "CLAUDE.md", "AGENTS.md", "SKILL.md",
                 "BLOCKED.md", "ROUTER.md", "BBS.md", "CHARTER.md", "FINDINGS.md"}
PATH_SUFFIXES = {".md", ".py", ".txt", ".json", ".yaml", ".yml", ".html", ".sh"}

# Files that are device-local by design and are absent from a clean tree on purpose. Prose has to
# be able to name them, so naming one is not a broken pointer. `--harness` is what checks these,
# because whether they exist is a fact about the machine rather than about the method.
DEVICE_LOCAL = {".claude/gate-last-fired", ".claude/settings.local.json"}

# Names of things that are not on this filesystem at all. A repository slug is `owner/name` and a
# git branch is `prefix/name`, both shaped exactly like a relative path and neither one being a
# path. Listed rather than detected: a rule that skipped every slash-separated token without a
# suffix would also skip a genuinely broken pointer to a directory, and losing a real finding
# costs more than adding a line here.
EXTERNAL_NAMES = {"BlueSkyGTM/deferred-context-architecture",
                  "BlueSkyGTM/albatross-engineering-os",
                  "TheMattBerman/first-1000-kit",
                  "claude/board-function-understanding-czri9y"}

MD_LINK = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
BACKTICKED = re.compile(r"`([^`\n]+)`")
TABLE_ROW = re.compile(r"^\|(.+)\|\s*$")


def is_path_candidate(text):
    """A backticked string worth resolving, as opposed to a field name or a shell word."""
    text = text.strip()
    if not text or " " in text or "<" in text or ">" in text:
        return False
    if text.startswith(("http://", "https://", "#", "$")):
        return False
    if "/" in text:
        return True
    return Path(text).suffix in PATH_SUFFIXES


def named_paths(md_file):
    """Every relative path a markdown file names, as (raw, resolved) pairs."""
    text = md_file.read_text(encoding="utf-8", errors="replace")
    raw = set()
    for match in MD_LINK.findall(text):
        raw.add(match)
    for match in BACKTICKED.findall(text):
        if is_path_candidate(match):
            raw.add(match)

    found = []
    for item in raw:
        cleaned = item.split("#", 1)[0].strip().rstrip("/")
        if not cleaned or not is_path_candidate(cleaned):
            continue
        if cleaned.startswith(("http://", "https://", "/")):
            continue
        found.append((cleaned, (md_file.parent / cleaned).resolve()))
    return found


def skipped(path, root):
    rel = path.relative_to(root).as_posix()
    return any(rel == s or rel.startswith(s + "/") for s in SKIP_DIRS)


def audit_repo(root):
    findings = []
    checked = 0
    for md_file in sorted(root.rglob("*.md")):
        if skipped(md_file, root):
            continue
        for raw, resolved in named_paths(md_file):
            if Path(raw).name in GENERIC_NAMES and "/" not in raw:
                continue
            if raw in DEVICE_LOCAL or raw in EXTERNAL_NAMES:
                continue
            checked += 1
            # Prose in this bundle names some paths from the repository root rather than from
            # the file they sit in. Both are legible to a person, so both count as resolved.
            if resolved.exists() or (root / raw).exists():
                continue
            rel = md_file.relative_to(root).as_posix()
            findings.append("{}: names `{}`, which does not resolve".format(rel, raw))
    return findings, checked


def table_paths(text, heading):
    """Paths sitting in backticks inside the table under a given heading."""
    lines = text.splitlines()
    out = []
    inside = False
    for line in lines:
        if line.startswith("#"):
            inside = heading.lower() in line.lower()
            continue
        if not inside:
            continue
        row = TABLE_ROW.match(line)
        if not row:
            continue
        for cell in row.group(1).split("|"):
            for match in BACKTICKED.findall(cell):
                if is_path_candidate(match):
                    out.append(match.split("#", 1)[0].strip().rstrip("/"))
    return out


def audit_folder(folder, allow_relay):
    findings = []
    issued = folder / "CONTRACT.md"
    emitted = folder / "CONTEXT.md"

    if not issued.exists() and not emitted.exists():
        return ["{}: holds neither CONTRACT.md nor CONTEXT.md".format(folder)]

    for contract in (issued, emitted):
        if not contract.exists():
            continue
        name = contract.name
        for raw, resolved in named_paths(contract):
            if not resolved.exists():
                findings.append("{}: names `{}`, which does not resolve".format(name, raw))
            if raw.startswith("..") and not allow_relay:
                findings.append(
                    "{}: `{}` reaches outside the folder. Declare a relay or fix the wall".format(
                        name, raw
                    )
                )

    if emitted.exists():
        text = emitted.read_text(encoding="utf-8", errors="replace")
        claimed = table_paths(text, "Outputs")
        if not claimed:
            findings.append("CONTEXT.md: claims no outputs, so nothing can be verified")
        for path in claimed:
            if not (folder / path).exists():
                findings.append("CONTEXT.md: claims output `{}`, which is not there".format(path))

    if issued.exists() and emitted.exists():
        issued_text = issued.read_text(encoding="utf-8", errors="replace")
        emitted_text = emitted.read_text(encoding="utf-8", errors="replace")
        asked = set(table_paths(issued_text, "Available"))
        used = set(table_paths(emitted_text, "Inputs"))
        for path in sorted(asked - used):
            findings.append(
                "issued `{}` as available, emitted contract does not use it".format(path))
        for path in sorted(used - asked):
            findings.append("emitted contract uses `{}`, which was never issued".format(path))

    return findings


HOOK_MATCHER = "Write|Edit|NotebookEdit"
GATE = Path("tools/hooks/card_gate.py")
SETTINGS = Path(".claude/settings.json")
LOCAL_SETTINGS = Path(".claude/settings.local.json")
STAMP = Path(".claude/gate-last-fired")


def audit_harness(root):
    """Is the gate in force on this device. Reports facts; findings are what is not true."""
    findings = []
    facts = []

    gate = root / GATE
    if not gate.exists():
        findings.append("{} is missing, so nothing is enforcing delegation".format(GATE))
    else:
        facts.append("gate script present")
        if not os.access(gate, os.X_OK):
            findings.append("{} is not executable".format(GATE))

    settings = root / SETTINGS
    if not settings.exists():
        findings.append("{} is missing, so the hook is not registered".format(SETTINGS))
    else:
        try:
            data = json.loads(settings.read_text(encoding="utf-8"))
        except json.JSONDecodeError as error:
            data = {}
            findings.append("{} is not valid JSON ({}), which silently disables every "
                            "setting in it".format(SETTINGS, error))
        commands = [
            hook.get("command", "")
            for entry in data.get("hooks", {}).get("PreToolUse", [])
            if entry.get("matcher") == HOOK_MATCHER
            for hook in entry.get("hooks", [])
        ]
        if any(GATE.name in command for command in commands):
            facts.append("hook registered on {}".format(HOOK_MATCHER))
        else:
            findings.append("{} carries no PreToolUse hook matching {} that runs {}".format(
                SETTINGS, HOOK_MATCHER, GATE.name))

    if (root / LOCAL_SETTINGS).exists():
        text = (root / LOCAL_SETTINGS).read_text(encoding="utf-8", errors="replace")
        if GATE.name in text:
            findings.append("{} installs the gate. Local settings do not travel with a clone, "
                            "so the gate would be live here and absent everywhere else".format(
                                LOCAL_SETTINGS))

    stamp = root / STAMP
    if not stamp.exists():
        findings.append("the gate has never fired on this device, so it is not live yet. "
                        "Rewrite {} in place, byte for byte, and the settings watcher picks it "
                        "up mid-session. Then edit any file and run this again".format(SETTINGS))
    else:
        facts.append("last fired {}".format(
            stamp.read_text(encoding="utf-8", errors="replace").strip()))

    return findings, facts


def main():
    parser = argparse.ArgumentParser(description="Rung zero checks against a tree.")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--repo", nargs="?", const=".", metavar="ROOT",
                       help="check that every pointer in the bundle resolves")
    group.add_argument("--folder", metavar="PATH",
                       help="audit one worked folder's contracts against what is there")
    group.add_argument("--harness", nargs="?", const=".", metavar="ROOT",
                       help="check that the card gate is installed and live on this device")
    parser.add_argument("--relay", action="store_true",
                        help="permit declared handoffs that reach outside the folder")
    args = parser.parse_args()

    if args.repo is not None:
        root = Path(args.repo).resolve()
        if not root.is_dir():
            print("not a directory: {}".format(root), file=sys.stderr)
            return 2
        findings, checked = audit_repo(root)
        print("checked {} pointers across {}".format(checked, root))
    elif args.harness is not None:
        root = Path(args.harness).resolve()
        if not root.is_dir():
            print("not a directory: {}".format(root), file=sys.stderr)
            return 2
        findings, facts = audit_harness(root)
        print("harness at {}".format(root))
        for fact in facts:
            print("  {}".format(fact))
    else:
        folder = Path(args.folder).resolve()
        if not folder.is_dir():
            print("not a directory: {}".format(folder), file=sys.stderr)
            return 2
        findings = audit_folder(folder, args.relay)
        print("audited {}".format(folder))

    if not findings:
        print("clean")
        return 0
    for finding in findings:
        print("  {}".format(finding))
    print("{} finding(s)".format(len(findings)))
    return 1


if __name__ == "__main__":
    sys.exit(main())
