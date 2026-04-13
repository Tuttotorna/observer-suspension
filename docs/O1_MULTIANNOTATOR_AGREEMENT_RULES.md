# O1 Multi-Annotator Agreement Rules v0

## Purpose

This document defines how agreement between annotators is classified in the O1 multi-annotator setting.

Its role is not to decide who is right in an absolute sense.
Its role is to classify how stable O1 remains when the same input is annotated by different hands.

Without agreement rules, multi-annotator analysis remains descriptive only.
With agreement rules, it becomes a structured part of the protocol.

---

## Core principle

Two annotators do not need to produce identical wording.

What matters is whether they preserve:

- the same input target
- acceptable O1 structure
- similar gain profile
- similar verdict outcome

Agreement is therefore measured structurally, not stylistically.

---

## Agreement dimensions

Multi-annotator agreement is evaluated along these dimensions:

1. shared input identity
2. verdict convergence
3. gain gap
4. structural acceptability
5. location of failure, if failure exists

These dimensions are enough for version zero.

---

## Agreement classes

### A0 - Strong convergence

Definition:
Both annotators produce acceptable annotations with the same verdict and the same gain.

Conditions:
- verdict pattern = accepted / accepted
- gain gap = 0

Interpretation:
The protocol remains highly stable across annotators for this input.

Meaning:
Different hands converge not only on acceptability but also on measured structural gain.

---

### A1 - Acceptable convergence

Definition:
Both annotators produce acceptable annotations with the same verdict and a small gain difference.

Conditions:
- verdict pattern = accepted / accepted
- gain gap = 1

Interpretation:
The protocol remains stable across annotators, with only a mild precision difference.

Meaning:
This is still good convergence.
It suggests the input admits a common structural reading even when phrasing differs.

---

### A2 - Weak convergence

Definition:
Both annotators produce acceptable annotations, but the gain difference is larger.

Conditions:
- verdict pattern = accepted / accepted
- gain gap > 1

Interpretation:
The protocol still converges on acceptability, but structural sharpness differs more substantially.

Meaning:
This is not failure, but it indicates that annotator dependence is increasing.

---

### A3 - Verdict split

Definition:
One annotator produces an acceptable annotation and the other produces a rejected one.

Conditions:
- verdict pattern = accepted / rejected

Interpretation:
The input reveals a true protocol boundary under annotator variation.

Meaning:
This is the most important form of instability in version zero.
It shows where one annotation remains structurally valid while another collapses into abstraction or failure.

---

### A4 - Rejected convergence

Definition:
Both annotators produce rejected annotations.

Conditions:
- verdict pattern = rejected / rejected

Interpretation:
The input may be especially difficult, the protocol may be underspecified, or both annotators may be failing in similar ways.

Meaning:
This is not convergence in a positive sense.
It is only convergence on failure.

This class is not present in the current seed dataset, but must remain available.

---

## Gain gap interpretation

The gain gap is defined as:

gain_gap = absolute difference between the two O1_GAIN scores

Interpretation:

- 0 = same measured structural gain
- 1 = mild precision difference
- 2 or more = larger structural difference
- 4 = maximal split in the current binary scoring regime

Gain gap does not replace verdict.
It refines verdict.

---

## Priority rule

When classifying agreement, verdict comes before gain.

Use this order:

1. If verdict pattern is accepted / rejected -> classify as A3
2. If verdict pattern is rejected / rejected -> classify as A4
3. If verdict pattern is accepted / accepted:
   - gain gap = 0 -> A0
   - gain gap = 1 -> A1
   - gain gap > 1 -> A2

This ordering prevents gain similarity from hiding verdict instability.

---

## Current observed pattern in the seed dataset

The current seed dataset shows:

- 3 cases of acceptable convergence
- 1 case of verdict split

This means O1 currently shows:

- stability on most seed inputs
- boundary exposure on at least one input

That is a meaningful methodological signal.

---

## Interpretation rule

Agreement classes do not tell us whether an annotation is metaphysically true.

They tell us only how stable the protocol remains under annotator variation.

That is the only allowed claim here.

---

## Good use

Use agreement classes to:

- compare annotators on the same input
- identify stable inputs
- identify protocol boundaries
- guide future inter-annotator studies
- monitor whether the protocol becomes more stable over time

---

## Bad use

Do not use agreement classes to:

- rank annotators as people
- infer intelligence
- infer truth of the external world
- replace record-level validation
- hide disagreement behind averaged scores

Agreement analysis complements validation.
It does not replace it.

---

## Minimal conclusion

A protocol becomes stronger when it remains usable across annotators.

O1 multi-annotator agreement classes are the first minimal layer for measuring that stability.