# _core/deferral.md: the Deferred-Context discipline (the D in DCA)

DCA is **Deferred Context Architecture.** The governing discipline is one line:

**Pull context from the well only when a stage actually needs it. Nothing speculative.**

A stage does not load material because it exists; it loads material because its Inputs table names
it. The well holds everything raw and addressed until a silo's stage reaches for a specific slice.
This is why a silo, and the ICM workspace inside it, stops **inventing on the spot**: it is always
fed real drawn assets, never left to fabricate from an empty context.

Deferral is a contamination defense, not a delay tactic. A context that admits only what a stage
needs cannot be polluted by material it should not see. It is why:

- a silo can stop cleanly at any stage (nothing downstream is committed),
- the well can be huge without drowning any one silo (each draws a thin slice),
- and many silos share one well without interfering (each pulls only its own slice, on demand).

The rule in practice: at `stages/01-draw`, read the well's catalogue (`vault/account.md`), select
the slice this silo needs, and pull ONLY that into the silo's own `output/`. Never copy the whole
well. Never pre-load "in case." If a later stage needs more, it draws more, then.
