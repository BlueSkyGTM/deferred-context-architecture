# CONTEXT.md — Root Routing

You are at the root of the M2W pipeline. The canonical read order lives in `CLAUDE.md` — start there
and follow it.

Core (domain-agnostic): CLAUDE.md and the root docs, platform/, stages/, manifest/, the holding
folders, logs/.
Instantiations (domain-specific): pilots/ — the operator's supplied domain. Core never references a
pilot; a pilot may reference core.

Holding folders (start EMPTY): vault/ carts/ tailings/ bench/ library/
Manifest (starts EMPTY): manifest/ (index.md + items/)
Observability: logs/

The law lives in platform/ and the root docs. The work lives in stages/. The state lives in the
holding folders, manifest/, and logs/. Nothing is committed until it is needed; nothing downstream of
the assay is earned until it clears a deferral point (vault/ is the pre-assay intake door — admitted
and accounted, not earned).
