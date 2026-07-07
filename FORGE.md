# KEYSTONE-FORGE — creation + validation, one function
*Lives at keystone-forge/ in the DCA repo. This is how contracts are authored
and how they are proven before use. Law: no keystone enters production untested.*

---

## Part 1 — What a keystone is (and is not)

The small shared thing parts build against so they fit without referencing each
other. A formal contract between the parts that share a join. **Not acted out**
(not a persona). **Not a tool** (inert; it is read, conformed-to, and checked —
it never executes). Plural and tiny — one per join, never one master contract.

A keystone stabilizes to the exact degree it converts judgment into **rules**
(executed identically every run). Instructions shaped as **goals** re-sample
each run and wobble. (Empirical basis: Run 001, below.)

## Part 2 — Creation template

Every keystone is one file in `well/keystones/`, this shape, ≤60 lines:

```
name:        [short, lowercase]
seat:        [what join or function it serves; gradient position if paired]
tested:      [UNTESTED | run-id + date + result]
version:     [n, bump on any edit]

PATTERN      one paragraph: the domain-agnostic decision-pattern this encodes.

RULES        numbered, each one checkable by reading the output:
             1. ...
             2. ...
             (rules are the stabilizing surface — maximize what lives here)

GUARDS       - the figure/source is never named in output
             - this keystone checks conformance only, never quality
             - [seat-specific fences]

PROVENANCE   which claims in PATTERN are primary-sourced vs community lore.
```

## Part 3 — Test protocol (the stability rig)

Before first production use, every keystone runs this. It is a controlled
ablation measuring contract robustness — whether the contract resists the
model's averaging pull, independent of correctness.

**Setup.** One constant task (~180-word output, same source facts, same
generating request). One variable: the keystone, passed as system prompt.
**N = 10 independent generations** (fresh context each — API calls, never one
session). Include a null/baseline contract if comparing.

**Metrics.**
1. *Hedge density* — deterministic count (bin/hedge_count.py). Owns itself; not
   negotiable.
2. *Falsifiable* (0–2), *Fork-cut* (0–2), *Voice* (0–2) — operator-scored,
   blind (mapping hidden until all scored).
3. *Attributability* — operator guesses the contract per output; chance = 1/k.

**Pass conditions.**
- Stabilizes: hedge mean low AND spread tight (min–max ≤1). Trust for volume.
- Biases only: good mean, wide spread. Use with regenerate-and-pick.
- Converged with baseline: the average won. Do not deploy; rewrite goals→rules
  or retire.

**Standing cautions.** Results are model-relative (record generator + date;
re-run when the substrate changes). Stability ≠ quality — the most stable
contract in Run 001 was also the most same-y. No contract manufactures
falsifiability; a risk-bearing claim requires an operator willing to be wrong.

## Part 4 — Run 001 (the record)

2026-07-04 · generator claude-sonnet-4-6 · 4 contracts × 10 · blind-scored.

| Contract (type)            | Hedges mean (min–max) | Fork | Voice | Verdict |
|----------------------------|----------------------|------|-------|---------|
| conformance (Clay-style)   | 1.5 (0–3)            | low  | 0.x   | converged — the average won |
| scarcity rules (stance)    | 0.0 (0–0)            | 0.9  | mid   | stabilized; same-y at volume |
| awareness goals (excav.)   | 1.0 (0–2)            | 1.9  | 1.7   | biases; alive; regenerate-and-pick |
| measurement rules          | 0.1 (0–1)            | high | mid   | stabilized |

Findings carried forward: rules stabilize, goals wobble; stability and
aliveness trade; falsifiability ≈ 0 across all four (no contract was a someone).

## Part 5 — Usage in this repo vs the DRA clone

Here (DCA): the forge is demonstration + validation only. Keystones may be
authored and tested; none deploy into arms in this repo. In the DRA OS clone:
tested keystones deploy per arm, one join at a time, first arm proven before
the second exists.
