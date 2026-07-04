#!/usr/bin/env python3
"""producer silo, emits `task` records as JSONL, conforming to vault/keystone-task.md.
Built drawing ONLY the keystone; knows nothing about any consumer."""
import json

TASKS = [
    {"id": 1, "title": "fill the well", "done": True},
    {"id": 2, "title": "stand up the silos", "done": True},
    {"id": 3, "title": "verify the join", "done": False},
]

if __name__ == "__main__":
    for t in TASKS:
        print(json.dumps(t))
