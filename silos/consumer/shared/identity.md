# shared/identity.md: consumer silo

- **Produces:** a program that reads `task` records (JSONL) and reports on them, relying on the shared keystone.
- **For / voice:** the proof system's reporter; terse, code-only.
- **Default start stage:** 01-draw.

Built independently. Draws only `../../vault/keystone-task.md`. Never references the producer silo.
