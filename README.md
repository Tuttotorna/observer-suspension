# Observer Suspension

A minimal research protocol for detecting and reducing hidden observer privilege in ordinary descriptions.

This repository does not propose a final theory of reality.
It does not attempt to replace science, language, or human cognition.

Its scope is narrower and harder:

**Given a statement shaped by ordinary human description, can we expose the hidden observer-centered assumptions inside it and produce a structurally less frame-dependent reformulation?**

That is the only core task of this repository.

---

## Why this exists

Human language is efficient, but it is not neutral.

Many ordinary statements appear simple only because they hide structural assumptions such as:

- a privileged observer frame
- a stable point of view treated as natural
- object properties treated as intrinsic rather than relational
- temporal flow treated as directly given
- causal narration treated as if it were the structure itself
- perception treated as neutral access

These assumptions are often useful for local survival and communication.
They are not therefore structurally universal.

This repository exists to test a simple possibility:

**some descriptions look natural only because observer privilege has been silently built into them.**

If that privilege is made explicit and reduced, different structure may become visible.

---

## Core question

The repository is organized around one question:

**What changes when the privileged human observer is no longer treated as the default center of description?**

Not everything changes.
Not everything should change.
The task is not to destroy ordinary language.

The task is to identify where ordinary language compresses frame-dependent structure into apparently absolute statements.

---

## Scope

Observer Suspension is a minimal structural framework.

It does not claim:

- a universal ontology
- a complete theory of time
- a complete theory of causality
- a final model of perception
- a replacement for ordinary language
- an automatic truth criterion

It only defines a protocol for structural decomposition of observer-loaded statements.

---

## Current status

This repository has moved beyond pure concept and now contains a minimal technical spine:

- a frozen first protocol: `docs/O1_PROTOCOL.md`
- a minimal dataset: `data/o1_miniset.jsonl`
- a minimal gain rule: `docs/O1_GAIN_CRITERIA.md`
- evaluated examples: `examples/O1_examples.md`
- a roadmap: `ROADMAP.md`
- a minimal dataset validator: `tools/validate_o1_dataset.py`

This is still an early-stage framework.
But it is no longer just a manifesto.

---

## Repository structure

README.md
ROADMAP.md
docs/
  O1_PROTOCOL.md
  O1_GAIN_CRITERIA.md
data/
  o1_miniset.jsonl
examples/
  O1_examples.md
tools/
  validate_o1_dataset.py

---

## Protocol O1

The first protocol in this repository is:

## O1 - Suspension of the privileged observer

O1 takes an ordinary statement and decomposes it into five fixed fields:

1. **Standard formulation**  
   The original sentence, unchanged.

2. **Hidden observer assumption**  
   The observer-centered condition that makes the sentence appear natural.

3. **Structural distortion**  
   What the hidden assumption compresses, absolutizes, or falsely stabilizes.

4. **Decentered reformulation**  
   A version with lower dependence on privileged observer framing.

5. **Emergent structure**  
   The relation or dependency that becomes visible after decentering.

O1 is not a theory generator.
O1 is not a truth machine.
O1 is not a rhetorical exercise.

It is only a minimal protocol for exposing hidden observer privilege inside statements.

---

## Minimal example

### Standard formulation
The sun rises

### Hidden observer assumption
Assumes a stable Earth-bound observer frame treated as primary.

### Structural distortion
Relative apparent motion is compressed into an absolute event attributed to the sun.

### Decentered reformulation
The sun's apparent position changes relative to an Earth-bound observer due to Earth's rotation.

### Emergent structure
Observed solar motion depends on observer frame and planetary rotation, not on an intrinsic rising event.

---

## What counts as gain

A reformulation is not useful just because it sounds more abstract.

The repository defines a minimal gain rule in `docs/O1_GAIN_CRITERIA.md`.

A valid O1 reformulation should improve along explicit structural dimensions such as:

- reduced hidden frame dependence
- increased relational explicitness
- reduced narrative compression
- preserved referential continuity

This produces an `O1_GAIN` score from 0 to 4.

Minimum acceptance condition:

- referential continuity must be preserved
- total gain must be at least 3

Without this rule, O1 would collapse into elegant paraphrase.
With this rule, O1 becomes minimally testable.

---

## Validation

The repository includes a minimal validator for the JSONL dataset.

Current validator:

- `tools/validate_o1_dataset.py`

It checks that each dataset record:

- is valid JSON
- contains all required fields
- does not leave required fields empty

Run it from the repository root:

python tools/validate_o1_dataset.py

This does not prove theoretical correctness.
It only ensures that the dataset has the minimum structural integrity required for reuse.

---

## First domains

The current protocol is applied to observer-loaded statements in domains such as:

- motion
- time
- causality
- perception
- identity
- space
- agency
- temperature
- sound
- value
- orientation

These domains are not final.
They are just the first places where hidden observer privilege appears clearly enough to be tested.

---

## Example domains of compression

The framework starts from a simple observation:

ordinary sentences often hide structure by making relational configurations look intrinsic.

Examples:

- The object is still
- Time passes
- I see a tree
- A causes B
- The room is silent
- The picture is upside down

These sentences are not useless.
They are locally efficient.

But they may hide:

- reference-frame dependence
- observer threshold dependence
- continuity criteria
- perceptual mediation
- model-dependent causality
- directional conventions presented as absolute

Observer Suspension does not reject these statements.
It decomposes them.

---

## What this repository is not

This project is not:

- a metaphysical doctrine
- anti-scientific critique
- relativism
- linguistic decoration
- phenomenology without criteria
- an ontology of everything

It does not say that all descriptions are equally valid.
It does not say that nothing is real.
It does not say that structure depends only on the observer.

It says something narrower:

**many ordinary descriptions silently privilege one observer frame, and this privilege can sometimes be exposed and reduced in a reproducible way.**

---

## Success condition

This repository succeeds only if it can show, even at small scale, that:

1. observer-centered statements contain hidden structural assumptions
2. O1 can expose these assumptions explicitly
3. the reformulated statements are less frame-dependent under a fixed gain rule
4. this produces non-trivial structural clarification

Anything weaker than that is not enough.

---

## Failure condition

This repository fails if it remains at one of these levels:

- elegant epistemic language without protocol
- abstract reformulations without comparison
- vague philosophy without dataset
- rhetorical depth without measurable gain
- observer critique without structural output

If that happens, the project should be treated as a limited conceptual note and nothing more.

---

## Immediate research direction

The current direction is simple and concrete:

### 1. Harden O1
Expand the dataset with harder cases while preserving protocol rigidity.

### 2. Stress-test gain
Identify borderline examples where reformulation becomes vague, target-shifting, or falsely abstract.

### 3. Compare domains
Check whether observer privilege behaves differently across motion, time, causality, perception, and identity.

### 4. Prepare bridge to stronger structural systems
Observer Suspension may later serve as a pre-structural decomposition layer before deeper structural diagnostics.

That bridge is not yet the claim of this repository.
It is only a possible next step.

---

## Why the project matters

If even a small subset of ordinary descriptions turns out to depend heavily on hidden observer privilege, then some apparently basic concepts may be less structurally primary than they appear.

That would matter because it would suggest that:

- some descriptions are anthropically compressed
- some "obvious" properties are actually frame-dependent
- some conceptual primitives may be downstream products of observer-centered language

This is worth testing.
Not assuming.
Testing.

---

## Minimal reading order

For the shortest useful path through the repository:

1. README.md
2. docs/O1_PROTOCOL.md
3. docs/O1_GAIN_CRITERIA.md
4. examples/O1_examples.md
5. data/o1_miniset.jsonl
6. ROADMAP.md

---

## Author

**Massimiliano Brighindi**