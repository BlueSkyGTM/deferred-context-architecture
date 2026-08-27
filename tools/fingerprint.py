#!/usr/bin/env python3
"""Rung zero. What a tree structurally is, recorded so a later state can be compared to it.

`../mechanics/ignition.md` specifies this list and nothing beyond it: the tree with modification
times, whether each working folder carries a contract, whether every pointer in a routing table
opens, counts, and last-touched age per folder. Everything on that list is answerable with
`find`, `git` and a comparison, and none of it needs a sentence written about it.

    python3 tools/fingerprint.py --write before.json <tree>
    python3 tools/fingerprint.py --diff before.json after.json
    python3 tools/fingerprint.py --diff before.json <tree>     # against the tree as it is now

## Why structure only, never content

Content is what makes a sweep expensive, and reading it would put the walk on a model. A
fingerprint that read files would cost money every time it ran, which breaks the one condition
that makes a scheduled loop cheaper than the manual trigger it replaced: the tick has to be
mostly deterministic and mostly a no-op.

## What it is for

Two jobs, and they are the same mechanism pointed at different questions.

**Drift.** Structural decay is defined by nothing arriving. A folder rots because no card has
named it, and activation that begins with authorship never begins at all in the folders that
most need it. Last-touched age per folder is the signal, and it is the only one that catches a
failure whose entire symptom is absence.

**Adoption.** When something is laid over an existing tree, the claim that it proposed rather
than performed is checkable rather than trusted. A diff that shows only added method artifacts
is a proposal. A diff that shows moves, renames or edits to files that were already there is a
restructure, whatever the report says about itself.

## Where to put the output

Not inside the tree. A fingerprint written into the tree it describes becomes part of what it
describes, and every diff afterwards opens with the record of itself. `--write` refuses rather
than filtering by filename, because filtering would silently skip a file somebody meant to track.

## What it deliberately does not do

It does not judge. A folder untouched for a year might be finished or might be abandoned, and
nothing here can tell which. It reports the age and stops.

It does not read `.git`, because a fingerprint of a working tree should describe the working
tree. Two trees at the same commit with different uncommitted state are different trees.

Standard library only, and no network. A check that needs an install is a check someone skips.
"""

import argparse
import hashlib
import json
import sys
import time
from pathlib import Path

SKIP = {".git", ".venv", "venv", "node_modules", "__pycache__", ".mypy_cache",
        ".pytest_cache", ".ruff_cache", "dist", "build", ".DS_Store"}

CONTRACTS = ("CONTRACT.md", "CONTEXT.md")
ROUTING = ("ROUTER.md", "CONTEXT.md", "BBS.md", "CLAUDE.md")

LINK = None  # compiled lazily; the audit module owns pointer syntax and this only counts


def walk(root):
    """Every file under root that is not in a skipped directory."""
    for path in sorted(root.rglob("*")):
        parts = set(path.relative_to(root).parts)
        if parts & SKIP:
            continue
        if path.is_file():
            yield path


def shape(text):
    """A stable hash of a file's bytes. Identity, not content: nothing here reads meaning."""
    return hashlib.sha256(text).hexdigest()[:16]


def unresolved_pointers(md_file, root):
    """How many relative paths a routing file names that do not open.

    Deliberately a count rather than a list. `audit.py --repo` is where a person goes for which
    pointer broke; this only needs to know whether the number moved.
    """
    global LINK
    if LINK is None:
        import re
        LINK = re.compile(r"\[[^\]]*\]\(([^)#][^)]*)\)|`([^`\n]*/[^`\n]*)`")
    text = md_file.read_text(encoding="utf-8", errors="replace")
    broken = 0
    for group in LINK.findall(text):
        raw = (group[0] or group[1]).split("#", 1)[0].strip().rstrip("/")
        if not raw or raw.startswith(("http://", "https://", "$")) or "<" in raw:
            continue
        if (md_file.parent / raw).exists() or (root / raw).exists():
            continue
        broken += 1
    return broken


def fingerprint(root):
    now = time.time()
    files = {}
    for path in walk(root):
        rel = path.relative_to(root).as_posix()
        try:
            stat = path.stat()
            files[rel] = {
                "bytes": stat.st_size,
                "mtime": int(stat.st_mtime),
                "hash": shape(path.read_bytes()),
            }
        except OSError as error:
            files[rel] = {"unreadable": type(error).__name__}

    folders = {}
    for path in sorted(root.rglob("*")):
        if not path.is_dir():
            continue
        parts = set(path.relative_to(root).parts)
        if parts & SKIP:
            continue
        rel = path.relative_to(root).as_posix()
        contained = [p for p in path.iterdir() if p.is_file()]
        newest = max((p.stat().st_mtime for p in contained), default=path.stat().st_mtime)
        folders[rel] = {
            "files": len(contained),
            "carries": [name for name in CONTRACTS if (path / name).exists()],
            "charter": (path / "CHARTER.md").exists(),
            "untouched_days": round((now - newest) / 86400, 1),
        }

    routing = {}
    for name in ROUTING:
        for path in sorted(root.rglob(name)):
            parts = set(path.relative_to(root).parts)
            if parts & SKIP:
                continue
            rel = path.relative_to(root).as_posix()
            routing[rel] = unresolved_pointers(path, root)

    return {
        "root": root.name,
        "taken": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(now)),
        "counts": {"files": len(files), "folders": len(folders),
                   "routing_files": len(routing),
                   "unresolved_pointers": sum(routing.values())},
        "files": files,
        "folders": folders,
        "routing": routing,
    }


def load(source):
    """A saved fingerprint, or a live tree fingerprinted now."""
    path = Path(source)
    if path.is_dir():
        return fingerprint(path.resolve())
    return json.loads(path.read_text(encoding="utf-8"))


def diff(before, after):
    """What moved. Added, removed and changed, with the ones that matter named first."""
    old, new = before["files"], after["files"]
    added = sorted(set(new) - set(old))
    removed = sorted(set(old) - set(new))
    changed = sorted(p for p in set(old) & set(new)
                     if old[p].get("hash") != new[p].get("hash"))

    # Folders are compared separately because an empty one holds no file to notice it by, and
    # renaming a folder is precisely the restructure this is here to catch.
    old_dirs, new_dirs = before.get("folders", {}), after.get("folders", {})
    dirs_added = sorted(set(new_dirs) - set(old_dirs))
    dirs_removed = sorted(set(old_dirs) - set(new_dirs))

    lines = []
    # Removed and changed come first: a proposal only adds, so these are the ones that decide
    # whether something restructured a tree it said it would only read.
    for path in dirs_removed:
        lines.append("removed  {}/ (folder)".format(path))
    for path in removed:
        lines.append("removed  {}".format(path))
    for path in changed:
        lines.append("changed  {} ({} -> {} bytes)".format(
            path, old[path].get("bytes"), new[path].get("bytes")))
    for path in dirs_added:
        lines.append("added    {}/ (folder)".format(path))
    for path in added:
        lines.append("added    {}".format(path))

    added, removed = added + dirs_added, removed + dirs_removed

    before_broken = before["counts"]["unresolved_pointers"]
    after_broken = after["counts"]["unresolved_pointers"]
    if after_broken != before_broken:
        lines.append("pointers unresolved {} -> {}".format(before_broken, after_broken))

    return lines, {"added": len(added), "removed": len(removed), "changed": len(changed)}


def main():
    parser = argparse.ArgumentParser(description="Structural fingerprint of a tree.")
    parser.add_argument("--write", metavar="OUT", help="write a fingerprint to this file")
    parser.add_argument("--diff", nargs=2, metavar=("BEFORE", "AFTER"),
                        help="compare two fingerprints, or a fingerprint against a live tree")
    parser.add_argument("tree", nargs="?", default=".", help="the tree to fingerprint")
    args = parser.parse_args()

    if args.diff:
        before, after = (load(source) for source in args.diff)
        lines, totals = diff(before, after)
        if not lines:
            print("no structural change")
            return 0
        for line in lines:
            print("  {}".format(line))
        print("{} added, {} removed, {} changed".format(
            totals["added"], totals["removed"], totals["changed"]))
        # Removed or changed means something edited a tree rather than adding to it, which is a
        # different verdict from growth and gets a different exit code.
        return 1 if (totals["removed"] or totals["changed"]) else 0

    root = Path(args.tree).resolve()
    if not root.is_dir():
        print("not a directory: {}".format(root), file=sys.stderr)
        return 2
    if args.write:
        out = Path(args.write).resolve()
        # A fingerprint written inside the tree becomes part of what it describes, and then
        # every later diff opens with the record of itself. Refuse rather than filter, because
        # filtering by filename would silently skip a file somebody meant to track.
        if root == out.parent or root in out.parents:
            print("refusing to write inside the tree being fingerprinted: {}\n"
                  "the file would appear in its own diff. Write it somewhere outside {}".format(
                      out, root), file=sys.stderr)
            return 2
    result = fingerprint(root)
    if args.write:
        Path(args.write).write_text(json.dumps(result, indent=2, sort_keys=True) + "\n",
                                    encoding="utf-8")
        print("wrote {} ({} files, {} folders)".format(
            args.write, result["counts"]["files"], result["counts"]["folders"]))
    else:
        print(json.dumps(result["counts"], indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    sys.exit(main())
