# Evaluation

Who says no, what they are allowed to see, and where the standard they apply is kept.

## The placement question

Deferred scope manufactures an independent reader at no extra cost. That settles who
evaluates. It does not settle where the criteria live, and the answer matters more than it
looks.

If the criteria sit in the same file as the card that wakes the generator, then generator
and judge share an author. The windows differ, so this is weaker than an agent grading its
own output, but it undoes the mechanism in one specific way: a stage becomes able to write
its own passing grade, and nothing downstream can see that it did. The loop reports green
forever.

**The rule: whoever writes the card writes the acceptance, and never the party doing the work.**
A stage may state what it produces. It may not state what counts as good.

That is a rule about authorship, not about where a file sits. An earlier version stated it
positionally, as criteria living one level above the stage and reached by a relative path.
Position cannot survive a reader with no location, and the relative path it depended on resolved
only for something standing in the folder. Authorship survives, because it is a fact about who
held the pen rather than about who can see what.

Two halves, both written before the work starts: standing criteria in the folder's contract, and
this run's acceptance on the card. A stage contract that defines its own success condition is a
defect to be fixed rather than a style choice. `acceptance.md` holds the checks that enforce
it.

## What an evaluator can and cannot do

| Can | Cannot |
|---|---|
| Check the work against the contract | Check whether the contract was right |
| Confirm the artifact exists and is shaped as specified | Judge whether this artifact was the right thing to build |
| Apply a stated standard | Supply a standard it was not given |
| Report a violation | Weigh a violation against a goal it cannot see |

The right-hand column is not a shortcoming to be engineered away. It is the price of the
independence in the left-hand column, and trying to buy both by letting the evaluator see
more turns it back into an insider.

Fit judgment therefore never belongs to a woken evaluator. It belongs to a ruling, decided by
something that had the picture, and it reaches the work through the card.

## Verify by acting, not by reading

An evaluator that only reads its input judges whether the work looks right. Rajasekaran's
practice on frontend tasks was to give the evaluator the ability to open the page, click, and
inspect, which moves the basis of judgment from an impression to an observation.

The equivalent here is rung zero, and it is cheap. Before any model is asked an opinion:

- Does every pointer the artifact introduced resolve
- Does the file it claims to have written exist, at the path claimed
- Does the count it reports match the tree
- Does the check script pass

An evaluator that has run those is judging behaviour. One that has not is judging prose about
behaviour, and prose about behaviour is what the completion fallacy produces most fluently.

## Default stance

The evaluator's default is doubt. The generator already trusts the work, and a polite
evaluator adds nothing but a second signature.

This is calibration rather than theatre. An evaluator instructed to assume the work is broken
until shown otherwise, and handed a concrete list of things to check, returns findings. One
asked whether the work looks acceptable returns agreement.

## The escalation it owes

An evaluator that finds something outside its contract does not resolve it. It files, per
`escalate` on its card. Its authority is to reject and to report, never to repair,
because repairing requires knowing what should have been built, and it cannot see that.

Rejection without repair feels incomplete. It is the correct boundary: a blind agent that
starts fixing is a blind agent making structural decisions.

## Source

Rajasekaran's acting-evaluator practice is reported in HuaShu, *Loop Engineering* (June 2026
edition), section 05. The criteria-placement rule was settled in the founding session,
2026-08-25.

Revised 2026-08-26. The rule was restated as authorship rather than filesystem placement, and
`judged-by` was dropped along with the relative path it depended on.
