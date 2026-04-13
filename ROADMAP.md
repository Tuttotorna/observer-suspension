# Observer Suspension - Roadmap

## Current status

The project is conceptually coherent but still too soft to produce external impact.

What exists now:
- core idea
- O1 protocol
- first examples
- epistemic direction

What is still missing:
- measurable criterion
- reproducible test set
- comparable outputs
- explicit connection to structural diagnostics

---

## Objective

Turn observer suspension from a conceptual framework into a minimal testable protocol.

The project must answer this:

"Does removing observer-centered assumptions produce a representation that is structurally more invariant, portable, or decomposed than the original one?"

If the answer cannot be tested, the framework remains philosophical only.

---

## Immediate priorities

### Step 1 - Freeze the protocol
Define O1 as a fixed minimal protocol with stable fields and exact purpose.

Output of this step:
- one canonical protocol definition
- no ambiguity about what O1 does
- no narrative language inside the protocol

### Step 2 - Build a minimal evaluation set
Create a small dataset of observer-loaded human statements.

Each sample should contain:
- original statement
- hidden observer assumption
- O1 reformulation
- structural note

Goal:
produce a small but clean corpus that can be reused.

### Step 3 - Define a gain criterion
A reformulation is not useful just because it sounds more abstract.

Need a minimal criterion for improvement, such as:
- lower dependence on privileged frame
- higher relational explicitness
- better portability across observers
- reduced narrative compression

This does not need to be perfect yet.
It must only be explicit.

### Step 4 - Add hard examples
Test the protocol on cases where ordinary language hides strong observer bias.

Priority domains:
- motion
- time
- causality
- perception
- identity

### Step 5 - Connect with OMNIA
Observer Suspension should not remain isolated.

Possible role:
a pre-structural decomposition layer that removes observer privilege before structural measurement.

If this bridge is not built, the repo risks remaining an isolated idea.

---

## Minimal deliverables

The repository should soon contain:

- `docs/O1_PROTOCOL.md`
- `data/o1_miniset.jsonl`
- `docs/O1_GAIN_CRITERIA.md`
- `examples/O1_examples.md`

This is enough to move from concept to protocol.

---

## Failure condition

The project fails if it stays at the level of elegant reformulation without a way to compare original vs transformed statements.

In that case it becomes philosophy, not method.

---

## Success condition

The project succeeds if it can show, even on a very small scale, that:

1. observer-centered language contains hidden structural assumptions
2. O1 exposes them explicitly
3. the transformed formulation is measurably less frame-dependent

That is enough for version zero.

---

## Strategic note

This repository does not need size.
It needs hardness.

A small protocol with 20 good samples and one explicit gain rule is worth more than 200 vague lines of epistemology.