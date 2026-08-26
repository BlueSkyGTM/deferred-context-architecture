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

## What it deliberately does not do

It does not parse claims about counts out of prose. A tool that guesses which numbers in a
sentence were meant as assertions produces findings nobody trusts, and an untrusted check is
worse than no check. Where a count matters, state it as a check with a pass condition in the
contract's Audit table, where a person wrote what passing means.

It does not judge anything. If it ever needs to, it has stopped being rung zero.

Standard library only. A check that needs an install is a check someone skips.
"""

import argparse
import re
import sys
from pathlib import Path

SKIP_DIRS = {".git", "_archive", "templates",
             "amendment/icm-architect", "amendment/icm-upstream"}

# Names this method uses as nouns rather than as pointers. "Write a CONTEXT.md" names a kind of
# file, not a file. Treating them as pointers produced findings nobody would act on, and an
# untrusted check is worse than no check.
GENERIC_NAMES = {"CONTRACT.md", "CONTEXT.md", "CLAUDE.md", "AGENTS.md", "SKILL.md",
                 "BLOCKED.md", "ROUTER.md", "BBS.md"}
PATH_SUFFIXES = {".md", ".py", ".txt", ".json", ".yaml", ".yml", ".html", ".sh"}

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
            findings.append("issued `{}` as available, emitted contract does not use it".format(path))
        for path in sorted(used - asked):
            findings.append("emitted contract uses `{}`, which was never issued".format(path))

    return findings


def main():
    parser = argparse.ArgumentParser(description="Rung zero checks against a tree.")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--repo", nargs="?", const=".", metavar="ROOT",
                       help="check that every pointer in the bundle resolves")
    group.add_argument("--folder", metavar="PATH",
                       help="audit one worked folder's contracts against what is there")
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
