# shared/identity.md — producer silo

- **Produces:** a program that emits `task` records (JSONL) conforming to the shared keystone.
- **For / voice:** the proof system's data source; terse, code-only.
- **Default start stage:** 01-draw.

Built independently. Draws only `../../vault/keystone-task.md`. Never references the consumer silo.
