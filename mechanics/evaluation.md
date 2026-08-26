# Evaluation

Who says no, what they are allowed to see, and where the standard they apply is kept.

## The placement question

Deferred scope manufactures an independent reader at no extra cost. That settles who
evaluates. It does not settle where the criteria live, and the answer matters more than it
looks.

If the criteria sit in the same file as the construct that wakes the generator, then generator
and judge share an author. The windows differ, so this is weaker than an agent grading its
own output, but it undoes the mechanism in one specific way: a stage becomes able to write
its own passing grade, and nothing downstream can see that it did. The loop reports green
forever.

**The rule: criteria belong to the contract one level above the stage, never to the stage
itself.** A stage may state what it produces. It may not state what counts as good.

In practice `judged-by` on a construct points upward, and a stage contract that defines its own
success condition is a defect to be fixed rather than a style choice.

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

Fit judgment therefore never belongs to a woken evaluator. It belongs to a ruling, decided
by something that had the picture, handed down through `hands-down`.

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
`escalates-when` in `constructs.md`. Its authority is to reject and to report, never to repair,
because repairing requires knowing what should have been built, and it cannot see that.

Rejection without repair feels incomplete. It is the correct boundary: a blind agent that
starts fixing is a blind agent making structural decisions.

## Source

Rajasekaran's acting-evaluator practice is reported in HuaShu, *Loop Engineering* (June 2026
edition), section 05. The criteria-placement rule was settled in the founding session,
2026-08-25.
