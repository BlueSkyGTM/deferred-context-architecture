# account.md — Vault-Level Index (the routable account, append-only)

Every piece excavation hauls gets one row here, so vault/ is a routable account, not a pile. Stage 01
appends; stage 02 (assay) reads. Starts EMPTY (nothing hauled yet). Exists as ready infrastructure,
like the logs.

# Row format is owned by stages/01-excavation/CONTRACT.md (Outputs). Stage 01 appends one row per
# hauled piece; stage 02 (assay) reads only `consumed: false` rows and flips them true when it routes
# the piece — this is what lets a LATER loop ignore already-routed material without a run counter
# (progress marked by production, not numbering; see platform/GATES.md §4).

