# decision-log.md: [arm name] (append-only, three lines per decision)

Every decision made while operating this arm gets exactly three lines. On arm close, this file is
COPIED to `../../vault/exhaust/` (the well's record of closed arms); the original stays here.

Format per entry:

```
## [date] — [decision in one line]
- why: [the reason, one line]
- reverses: [what undoing it would cost, one line]
```
