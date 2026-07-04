#!/usr/bin/env python3
"""join-check.py — verify that independently-built silos fit at the join.

The gap DCA named: composition (parts don't corrupt each other) is guaranteed by one-way refs, but
INTEGRATION (parts fit) was unverified. This check closes it. It draws the keystone from the well
(the single source of truth), then confirms every interoperating silo honors it and the round-trip
runs. Neither silo references the other; they align solely through the shared keystone.

Run: python bin/join-check.py
"""
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
KEYSTONE = ROOT / "vault" / "keystone-task.md"
PRODUCER = ROOT / "silos" / "producer" / "stages" / "02-build" / "output" / "produce.py"
CONSUMER = ROOT / "silos" / "consumer" / "stages" / "02-build" / "output" / "consume.py"


def keystone_fields() -> set[str]:
    """Parse the required field names from the keystone table in the well (single source of truth)."""
    fields = set()
    for line in KEYSTONE.read_text(encoding="utf-8").splitlines():
        m = re.match(r"\|\s*`(\w+)`\s*\|\s*(integer|string|boolean)\s*\|", line)
        if m:
            fields.add(m.group(1))
    return fields


def main() -> int:
    fields = keystone_fields()
    print(f"keystone fields (from the well): {sorted(fields)}")
    if not fields:
        print("FAIL: could not read the keystone contract from the well")
        return 1

    # 1. run the producer (built drawing only the keystone)
    prod = subprocess.run([sys.executable, str(PRODUCER)], capture_output=True, text=True)
    if prod.returncode != 0:
        print("FAIL: producer errored\n" + prod.stderr)
        return 1

    # 2. each emitted record must honor the keystone exactly
    import json
    for i, line in enumerate(l for l in prod.stdout.splitlines() if l.strip()):
        got = set(json.loads(line))
        if got != fields:
            print(f"FAIL: producer row {i} has fields {sorted(got)}, keystone requires {sorted(fields)}")
            return 1
    print("producer output conforms to the keystone")

    # 3. the join: feed producer output to the independently-built consumer
    cons = subprocess.run([sys.executable, str(CONSUMER)], input=prod.stdout, capture_output=True, text=True)
    if cons.returncode != 0:
        print("FAIL: consumer rejected the producer's output at the join\n" + cons.stderr)
        return 1

    print(f"consumer accepted the producer's output: {cons.stdout.strip()!r}")
    print("PASS: two independent silos, one shared keystone, parts fit at the join.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
