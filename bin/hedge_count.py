#!/usr/bin/env python3
"""hedge_count.py — deterministic hedge-density metric for keystone testing.

Usage:
    python3 hedge_count.py file.md          # count one file
    python3 hedge_count.py dir/             # count every .md/.txt in a dir
    echo "some text" | python3 hedge_count.py   # stdin

The lexicon is the contract: fixed, visible, auditable. Changing it is a
protocol version bump, not a tweak. This metric owns itself — it is not
negotiated at the handshake.
"""
import re
import sys
from pathlib import Path

LEXICON = [
    "either way", "it depends", "depends on", "whichever", "both approaches",
    "both options", "both have", "both are", "some teams", "many teams",
    "most teams", "consider", "could be", "can be", "might", "may want",
    "may be", "often", "typically", "generally", "usually", "that said",
    "on the other hand", "trade-off", "tradeoff", "no right answer",
    "one-size-fits-all", "the right balance", "a balance",
]

PATTERNS = [(h, re.compile(r"\b" + re.escape(h) + r"\b")) for h in LEXICON]


def count(text: str):
    t = text.lower()
    hits = []
    for phrase, pat in PATTERNS:
        n = len(pat.findall(t))
        if n:
            hits.append((phrase, n))
    total = sum(n for _, n in hits)
    return total, hits


def report(label: str, text: str):
    total, hits = count(text)
    words = len(text.split())
    print(f"{label}: {total} hedge(s) / {words} words")
    for phrase, n in sorted(hits, key=lambda x: -x[1]):
        print(f"    {n} × {phrase!r}")
    return total


def main(argv):
    if len(argv) < 2:
        report("stdin", sys.stdin.read())
        return
    target = Path(argv[1])
    if target.is_dir():
        files = sorted(
            p for p in target.rglob("*") if p.suffix in (".md", ".txt")
        )
        grand = 0
        for p in files:
            grand += report(str(p), p.read_text(encoding="utf-8", errors="replace"))
        print(f"TOTAL: {grand} hedge(s) across {len(files)} file(s)")
    else:
        report(str(target), target.read_text(encoding="utf-8", errors="replace"))


if __name__ == "__main__":
    main(sys.argv)
