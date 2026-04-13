# O1 Gain Criteria - Minimal Evaluation Rule v0

## Purpose

O1 is useful only if the decentered reformulation is structurally better than the original statement in an explicit way.

This document defines a minimal gain rule.

It is not a final metric.
It is a first hard criterion for comparing:

- original statement
- O1 reformulation

---

## Core question

Does the O1 reformulation reduce observer privilege while preserving the original target?

If yes, it produces gain.
If not, it is only paraphrase.

---

## Gain dimensions

A reformulation may improve along four dimensions.

### G1 - Reduced privileged frame dependence

Definition:
The reformulation relies less on one hidden observer frame treated as absolute.

Signal of gain:
The chosen frame becomes explicit, conditional, or replaceable.

Example:
"The object is still"
- hidden absolute frame

"The object remains at constant position relative to the chosen reference frame"
- frame dependence made explicit

### G2 - Increased relational explicitness

Definition:
The reformulation replaces intrinsic-looking properties with explicit relations.

Signal of gain:
The statement now shows dependencies between observer, frame, object, process, or condition.

Example:
"The road goes uphill"
becomes
"Along this traversal direction, elevation increases relative to the local gravitational frame"

### G3 - Reduced narrative compression

Definition:
The reformulation exposes structure that the original sentence compresses into a simple human narrative.

Signal of gain:
Simple verbs like rises, decides, passes, causes, feels, is, same are replaced by explicit structural relations where appropriate.

Example:
"A causes B"
becomes
"Within this model, changes in A systematically precede and constrain changes in B"

### G4 - Preserved referential continuity

Definition:
The reformulation must still refer to the same target as the original statement.

Signal of gain:
The sentence becomes structurally clearer without changing what it is about.

This is not optional.
Without referential continuity, the transformation fails.

---

## Minimal scoring rule

Each O1 reformulation is evaluated with four binary checks.

Score each dimension as:

- 1 = satisfied
- 0 = not satisfied

### Check 1 - Frame dependence reduced
Does the reformulation make the observer frame less hidden or less absolute?

### Check 2 - Relation made explicit
Does the reformulation replace intrinsic appearance with explicit relation or dependency?

### Check 3 - Compression reduced
Does the reformulation expose structure hidden by ordinary human phrasing?

### Check 4 - Target preserved
Does the reformulation still point to the same original referent or event?

---

## O1 Gain Score

Define:

O1_GAIN = C1 + C2 + C3 + C4

Range:
- 0 = failure
- 1 = negligible
- 2 = weak
- 3 = acceptable
- 4 = strong

---

## Acceptance threshold

A reformulation is minimally acceptable only if:

- C4 = 1
- total O1_GAIN >= 3

Reason:
A decentered reformulation that changes target is invalid.
A reformulation with weak structural gain is not worth keeping.

---

## Rejection conditions

Reject the O1 output if one or more of the following occurs:

- target changes
- reformulation becomes vaguer than original
- observer privilege is only renamed, not reduced
- abstraction increases but structure does not
- metaphysical content is added
- rhetorical sophistication replaces structural clarity

---

## Interpretation rule

High O1 gain does not mean "truer in absolute terms."

It means only this:
the reformulation is structurally less dependent on hidden observer privilege.

That is the only claim allowed here.

---

## Example evaluation

### Original
"The sun rises"

### Reformulation
"The sun's apparent position changes relative to an Earth-bound observer due to Earth's rotation."

### Evaluation
- C1 = 1
- C2 = 1
- C3 = 1
- C4 = 1

O1_GAIN = 4

Why:
- frame is explicit
- relation is explicit
- narrative compression is reduced
- original target is preserved

---

## Counterexample

### Original
"The object is still"

### Bad reformulation
"Reality is relative and stillness is an illusion"

### Evaluation
- C1 = 0
- C2 = 0
- C3 = 0
- C4 = 0

O1_GAIN = 0

Why:
- no explicit frame
- no usable relation
- no structural clarification
- target has been replaced by abstraction

---

## Strategic value

This gain rule is intentionally minimal.

Its role is:
- force explicit comparison
- prevent philosophical drift
- filter weak O1 records
- prepare later quantitative refinement

A small hard rule is better than a large vague theory.