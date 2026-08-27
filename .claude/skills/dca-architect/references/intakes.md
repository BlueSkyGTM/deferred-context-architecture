# The two intakes

Two questionnaires that look similar and do opposite things. One configures a host system once.
The other produces work, every session, and configures nothing.

Both inherit ICM's questionnaire design, Pattern 8 in
`origins/icm-upstream/_core/CONVENTIONS.md`. Read it rather than reinventing it.

## Shared rules, inherited whole

- **Flat.** No branching. A questionnaire that branches is a program, and it will be wrong about
  the branch it did not anticipate.
- **One pass.** Ask everything, then act. Do not interleave questions with work.
- **Derive rather than ask.** Anything answerable by looking at the tree is not a question. Every
  question you ask that the filesystem could have answered spends the operator's attention on
  something a script would have got right.
- **Sensible defaults.** Offer one and let it be accepted by silence.
- **Examples over descriptions.** "Territory: `billing/`, everything under it" beats "the set of
  folders this wing has authority over". This is the questionnaire form of what
  `mechanics/writing-for-an-unknown-reader.md` says about readers with no surroundings.
- **The placeholder sweep, with teeth.** ICM completes setup only when no `{{` patterns remain.
  Here it is stronger: **a card carrying an unfilled placeholder is not playable**, and the gate
  refuses the write rather than a person noticing. Never hand over a deck with `<` in it.

## `setup`

**Asked once, ever.** It configures the host system: where the tree lives, what the wings are
called, which rungs are available, what the ceilings are, where findings go.

Scope is system level. It does not ask about a job, a folder, or a piece of work. If a question
would have a different answer next week, it belongs in `intake` instead.

Its output is the tree's own furniture: charters, a router, a board with no cards on it, and the
folders that will hold contracts.

After setup, the operator grants the charters, and only then is the harness installed. Adoption
creates the territory the gate enforces, so a live gate during setup refuses the very files that
would authorise it.

## `intake`

**Asked once per session.** New, and it is the reason a session can produce more than one or two
cards without the operator writing each one from a blank page.

One conversational pass over what needs doing, producing a **written deck**: several cards, all
in the Written state, none played. Nothing has fired, no model is committed, no spend has
occurred. The deck is entirely reviewable, editable and binnable before any of it costs anything.

That is the whole reason it is safe to produce cards in bulk. `mechanics/the-bbs.md` holds the
separation it rests on: the card's text is fixed at writing, and playing is a separate act the
operator controls.

### What it asks

Only what the tree cannot answer.

- What needs to happen, in the operator's own words, one item at a time
- For each: which folder it lands in, if the operator knows. If not, propose one from the router
  and let it be corrected
- What finished looks like, stated so something other than a model could check it
- What should stop the work rather than be guessed at

`mode` is derived from the router. `wing` is derived from the folder. `tier` is proposed from the
work and checked against the charter's capability table, and a tier the charter withholds is not
offered.

### What it must not do

- **Play anything.** The deck is written and stops there.
- **Ask why the work matters.** That is the operator's context and no card carries it.
- **Ask what the folder already says.** A card carries only what the standing contract cannot
  know: this run's acceptance, this job's specifics, this exit condition.
- **Produce a card it knows is unplayable.** A blank field, a placeholder, a door outside
  territory, or a tier outside capability is a card that will be refused, so fix it before
  handing it over or say plainly that it could not be completed.

## Which one is running

If the tree has no board, it is `setup`. If it has one, it is `intake`. Do not ask.
