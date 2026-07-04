#!/usr/bin/env python3
"""consumer silo — reads `task` records (JSONL) from stdin and reports, per vault/keystone-task.md.
Built drawing ONLY the keystone; knows nothing about any producer.
Relies on exactly the keystone fields: id, title, done."""
import sys
import json

REQUIRED = {"id", "title", "done"}

def main() -> int:
    total = done = 0
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        task = json.loads(line)
        # rely on the keystone contract: exactly id, title, done
        if set(task) != REQUIRED:
            print(f"CONTRACT VIOLATION: got fields {sorted(task)}, keystone requires {sorted(REQUIRED)}", file=sys.stderr)
            return 1
        total += 1
        done += 1 if task["done"] else 0
    print(f"{total} tasks, {done} done")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
