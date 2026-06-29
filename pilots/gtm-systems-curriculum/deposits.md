# deposits.md — Located Deposits + Extractor Matching (this pilot)

The core's excavation contract (`stages/01-excavation/CONTRACT.md`) takes a "located deposit" and a
"bounded space to cover" as inputs and is agnostic about what they are. This file supplies the
CONCRETE deposits for the GTM-curriculum pilot and the rule for matching each to an extractor.

## Deposit register (fill before Run 1a)
Each deposit is one located source to mine. Record, per deposit:

```
- deposit_id:     <stable id>
- source:         <url / path / channel>
- type:           <docs-site | article | video | pdf-or-office | other>
- bounded_space:  <what counts as "the whole deposit" — the coverage target>
- extractor:      <the matched extractor from tooling.md>
- status:         <located | extracted | empty>
```

Status: _no deposits registered yet._ This register is a BLOCKED-ON-RUN input: the human supplies the
located GTM deposits before Run 1a (see `dry-run.md`).

## Extractor-matching rule (deposit type → extractor)
| Deposit type | Extractor (from tooling.md) |
|---|---|
| documentation website | docs-site skill |
| web article | article-extractor |
| video | youtube-transcript |
| PDF / Office | markitdown |

If a deposit's type matches none of the above, do NOT guess an extractor — bench the deposit and log
to `logs/failures.md` (core: you do not think, you execute).

## gtm-starter-kit
Referenced as candidate corpus material. Decide its role BEFORE Run 1a: fold it into the seam corpus
ONLY if it is answer-key material you will grade Run 1c against (then it belongs in `answer-key/`,
quarantined from the model); otherwise keep it deferred. Until decided, it is not a deposit.
