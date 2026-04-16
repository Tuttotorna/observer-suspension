
# Observer Suspension

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19571535.svg)](https://doi.org/10.5281/zenodo.19571535)

A minimal research protocol for detecting and reducing hidden observer privilege in ordinary descriptions.

**Author:** Massimiliano Brighindi  
**Contact:** brighissimo@gmail.com

This repository does not propose a final theory of reality.  
It does not attempt to replace science, language, or human cognition.

Its scope is narrower and harder:

**Given a statement shaped by ordinary human description, can we expose the hidden observer-centered assumptions inside it and produce a structurally less frame-dependent reformulation without destroying the phenomenon being described?**

That is the core task of this repository.

---

## Position in the Ecosystem

This repository belongs to the broader **MB-X.01 / OMNIABASE** ecosystem.

Within that ecosystem:

- **[OMNIABASE](https://github.com/Tuttotorna/OMNIABASE)** = the general multirepresentational framework
- **Observer Suspension** = the epistemic pre-layer
- **[OMNIA](https://github.com/Tuttotorna/OMNIA)** = the Diagnostics / Structural Measurement branch
- **[omniabase-coordinate-discovery](https://github.com/Tuttotorna/omniabase-coordinate-discovery)** = the Coordinate Discovery branch
- **[omega-translator](https://github.com/Tuttotorna/omega-translator)** = the Cross-Representation Translation branch

Observer Suspension is not the whole of OMNIABASE.

Its role is more specific:

**to reduce the silent monopoly of the privileged human observer before structural analysis hardens around a default frame.**

This repository should therefore be read as an epistemic gateway into OMNIABASE, not as a replacement for the broader framework.

---

## Why This Exists

Human language is efficient, but it is not neutral.

Many ordinary statements appear simple only because they silently hide structural assumptions such as:

- a privileged observer frame
- a stable point of view treated as natural
- object properties treated as intrinsic rather than relational
- temporal flow treated as directly given
- causal narration treated as if it were the structure itself
- perception treated as neutral access
- comparison criteria left implicit
- thresholds treated as absolutes

These assumptions are often useful for local survival and communication.  
They are not therefore structurally universal.

This repository exists to test a simple possibility:

**some descriptions look natural only because observer privilege has been silently built into them.**

If that privilege is made explicit and reduced, different structure may become visible.

But there is a second possibility, equally important:

**bad decentering may destroy the phenomenon instead of clarifying it.**

This repository studies both.

---

## Core Question

The repository is organized around one question:

**What changes when the privileged human observer is no longer treated as the default center of description?**

Not everything changes.  
Not everything should change.  
The task is not to destroy ordinary language.

The task is to identify where ordinary language compresses frame-dependent structure into apparently absolute statements, and to test whether a more explicit reformulation preserves the phenomenon or dissolves it.

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
- a solution to metaphysical debates

It defines a protocol for structural decomposition of observer-loaded statements and a method for distinguishing valid decentering from pseudo-depth.

---

## What This Repository Now Is

This repository is no longer only a conceptual note.

It now contains a minimal executable methodological spine:

- a frozen first protocol: `docs/O1_PROTOCOL.md`
- a gain rule: `docs/O1_GAIN_CRITERIA.md`
- a logic document: `docs/O1_PROTOCOL_LOGIC.md`
- evaluated examples: `examples/O1_examples.md`
- hard cases: `examples/O1_hard_cases_v0.md`
- external application files on real LLM outputs
- a roadmap: `ROADMAP.md`
- base, borderline, comparative, multi-annotator, and hard datasets
- validators and inspectors for each active block
- a unified runner: `tools/run_o1_checks.py`

This is still early-stage.  
But it is no longer just a manifesto.

---

## Repository Structure

```text
README.md
RESULTS.md
ROADMAP.md

docs/
  O1_PROTOCOL.md
  O1_GAIN_CRITERIA.md
  O1_PROTOCOL_LOGIC.md
  O1_MULTIANNOTATOR_AGREEMENT_RULES.md
  O1_EXTERNAL_BENCHMARK_v1.md

data/
  o1_miniset.jsonl
  o1_borderline_cases.jsonl
  o1_comparison_pairs.jsonl
  o1_disagreement_labels.jsonl
  o1_multiannotator_seed.jsonl
  o1_multiannotator_agreement_labels.jsonl
  o1_hard_inputs_seed.jsonl
  o1_hard_cases_v0.jsonl
  o1_hard_rejected_v0.jsonl
  o1_hard_comparison_pairs.jsonl

examples/
  O1_examples.md
  O1_hard_cases_v0.md
  O1_on_real_llm_outputs_v0.md
  O1_on_real_llm_outputs_v1_weak_prompts.md

tools/
  validate_o1_dataset.py
  inspect_o1_dataset.py
  validate_o1_comparison_pairs.py
  inspect_o1_comparison_pairs.py
  validate_o1_disagreement_labels.py
  inspect_o1_disagreement_labels.py
  validate_o1_multiannotator_seed.py
  inspect_o1_multiannotator_seed.py
  analyze_o1_multiannotator_agreement.py
  validate_o1_multiannotator_agreement_labels.py
  inspect_o1_multiannotator_agreement_labels.py
  validate_o1_hard_cases_v0.py
  inspect_o1_hard_cases_v0.py
  validate_o1_hard_rejected_v0.py
  inspect_o1_hard_rejected_v0.py
  validate_o1_hard_comparison_pairs.py
  inspect_o1_hard_comparison_pairs.py
  run_o1_checks.py


---

Protocol O1

The first protocol in this repository is:

O1 — Suspension of the privileged observer

O1 takes an ordinary statement and decomposes it into five fixed fields:

1. Standard formulation

The original sentence, unchanged.

2. Hidden observer assumption

The observer-centered condition that makes the sentence appear natural.

3. Structural distortion

What the hidden assumption compresses, absolutizes, or falsely stabilizes.

4. Decentered reformulation

A version with lower dependence on privileged observer framing.

5. Emergent structure

The relation, dependency, threshold, continuity rule, or constraint that becomes visible after decentering.

O1 is not a theory generator.
O1 is not a truth machine.
O1 is not a rhetorical exercise.

It is a minimal protocol for exposing hidden observer privilege inside statements and testing whether structural clarification is actually achieved.


---

Minimal Example

Standard formulation

The sun rises.

Hidden observer assumption

Assumes a stable Earth-bound observer frame treated as primary.

Structural distortion

Relative apparent motion is compressed into an absolute event attributed to the sun.

Decentered reformulation

The sun's apparent position changes relative to an Earth-bound observer due to Earth's rotation.

Emergent structure

Observed solar motion depends on observer frame and planetary rotation, not on an intrinsic rising event.


---

What Counts as Gain

A reformulation is not useful just because it sounds more abstract.

The repository defines a minimal gain rule in docs/O1_GAIN_CRITERIA.md.

A valid O1 reformulation should improve along explicit structural dimensions such as:

reduced hidden frame dependence

increased relational explicitness

reduced narrative compression

preserved referential continuity


This produces an O1_GAIN score from 0 to 4.

Minimum acceptance condition

referential continuity must be preserved

total gain must be at least 3


Without this rule, O1 would collapse into elegant paraphrase.
With this rule, O1 becomes minimally testable.


---

The Central Logic of the Repository

The decisive distinction in this repository is not simply:

observer-centered vs decentered

It is:

reconstruction vs evaporation

A valid O1 reformulation removes observer privilege and reconstructs the structure that still makes the phenomenon describable.

A failed O1 reformulation removes observer privilege only by dissolving the phenomenon into generic abstraction.

This is formalized in docs/O1_PROTOCOL_LOGIC.md.

Central rule

If decentering destroys the functional distinction between the phenomenon and its contrast case, it is not explanation but evaporation.

Examples:

If "same person" can no longer be distinguished from "different person", the reformulation failed.

If "quiet" can no longer be distinguished from "noisy", the reformulation failed.

If "better" can no longer be distinguished from "worse under declared criteria", the reformulation failed.

If "same color" can no longer be distinguished from "relevantly different color", the reformulation failed.


This is the law of functional distinction.
It is the methodological core of the project.


---

Validation

The repository includes validators and inspectors for every active methodological block.

Examples:

tools/validate_o1_dataset.py

tools/inspect_o1_dataset.py

tools/validate_o1_comparison_pairs.py

tools/inspect_o1_comparison_pairs.py

tools/validate_o1_hard_comparison_pairs.py

tools/inspect_o1_hard_comparison_pairs.py


Unified entry point

python tools/run_o1_checks.py

This does not prove scientific truth.

It ensures that the repository maintains structural integrity across datasets, comparisons, and failure-mode documentation.


---

Active Dataset Layers

The repository now contains several layers of increasing methodological pressure.

1. Base dataset

A minimal set of O1 cases showing that ordinary observer-loaded statements can be decomposed in a structured way.

File:

data/o1_miniset.jsonl


2. Borderline dataset

Cases designed to stress the protocol with acceptable and rejected reformulations on the same input.

File:

data/o1_borderline_cases.jsonl


3. Comparison pairs

Direct A/B comparison between stronger and weaker reformulations.

File:

data/o1_comparison_pairs.jsonl


4. Disagreement labels

A layer that classifies the type of divergence between alternative annotations.

File:

data/o1_disagreement_labels.jsonl


5. Multi-annotator seed

An initial test of whether O1 remains stable when the same input is annotated by different hands.

Files:

data/o1_multiannotator_seed.jsonl

data/o1_multiannotator_agreement_labels.jsonl


6. Hard cases

A higher-difficulty phase using more semantically viscous inputs.

Files:

data/o1_hard_cases_v0.jsonl

data/o1_hard_rejected_v0.jsonl


7. Hard comparison pairs

The strongest current block: same difficult input, one accepted structural reconstruction, one rejected pseudo-depth failure.

File:

data/o1_hard_comparison_pairs.jsonl


Current quartet

identity

value

perception

sound


This is currently the most front-facing demonstration of the protocol.


---

External Benchmark Layers

The repository also now contains its first external application layer.

v0 — Protected prompts

Real LLMs were asked to explain high-risk claims under prompts explicitly designed to prevent evaporation.

Result: models can often preserve the phenomenon when strongly constrained against abstraction.

File:

examples/O1_on_real_llm_outputs_v0.md


v1 — Weak prompts

The same domains were tested again under much weaker prompts.

Result: clear divergence between models and clearer failure modes.

File:

examples/O1_on_real_llm_outputs_v1_weak_prompts.md


Key observed external failure modes

pseudo-depth / abstraction

narrative contamination

meme / pragmatic drift

loss of locality

replacement of the phenomenon by its social framing


This external layer is important because it shows that O1 can evaluate not only handcrafted examples, but also real model behavior.


---

First Domains

The current protocol is applied to observer-loaded statements in domains such as:

motion

time

causality

perception

identity

space

agency

temperature

sound

value

orientation


These domains are not final.
They are the first places where hidden observer privilege appears clearly enough to be tested.


---

Example Domains of Compression

The framework starts from a simple observation:

ordinary sentences often hide structure by making relational, thresholded, or context-sensitive configurations look intrinsic.

Examples:

The object is still

Time passes

I see a tree

A causes B

The room is quiet

The color is the same

This result is better

This is the same person


These sentences are not useless.
They are locally efficient.

But they may hide:

reference-frame dependence

observer threshold dependence

continuity criteria

perceptual mediation

model-dependent causality

benchmark dependence

functional contrast conditions


Observer Suspension does not reject these statements.
It decomposes them and tests whether the decomposition remains usable.


---

What This Repository Is Not

This project is not:

a metaphysical doctrine

anti-scientific critique

relativism

linguistic decoration

phenomenology without criteria

an ontology of everything

a generator of impressive abstractions


It does not say that all descriptions are equally valid.
It does not say that nothing is real.
It does not say that structure depends only on the observer.

It says something narrower and harder:

many ordinary descriptions silently privilege one observer frame, and this privilege can sometimes be exposed and reduced in a reproducible way without destroying the phenomenon being described.


---

Success Condition

This repository succeeds only if it can show, even at small scale, that:

1. observer-centered statements contain hidden structural assumptions


2. O1 can expose these assumptions explicitly


3. the reformulated statements are less frame-dependent under a fixed gain rule


4. referential continuity is preserved


5. this produces non-trivial structural clarification rather than rhetorical abstraction



Anything weaker than that is not enough.


---

Failure Condition

This repository fails if it remains at one of these levels:

elegant epistemic language without protocol

abstract reformulations without comparison

vague philosophy without dataset

rhetorical depth without measurable gain

observer critique without structural output

decentering that destroys the target instead of clarifying it


If that happens, the project should be treated as a limited conceptual note and nothing more.


---

The Main Failure Mode: Pseudo-Depth

The most important error pattern documented in this repository is pseudo-depth.

Pseudo-depth appears when the annotator recognizes that the ordinary statement is compressed, but replaces clarification with slogans such as:

identity is an illusion

value is subjective

color is not real

silence is impossible

everything is perspective

everything is vibration


These may sound deep.
Inside O1 they count as failure whenever they erase functional distinction rather than reconstructing it.

This is not a stylistic objection.
It is a structural one.


---

Why the Project Matters

If even a small subset of ordinary descriptions turns out to depend heavily on hidden observer privilege, then some apparently basic concepts may be less structurally primary than they appear.

That would matter because it would suggest that:

some descriptions are anthropically compressed

some "obvious" properties are actually frame-dependent

some conceptual primitives may be downstream products of observer-centered language

some apparently profound critiques of ordinary language are methodologically empty


This is worth testing.
Not assuming. Testing.


---

Minimal Reading Order

For the shortest useful path through the repository:

1. README.md


2. docs/O1_PROTOCOL.md


3. docs/O1_GAIN_CRITERIA.md


4. docs/O1_PROTOCOL_LOGIC.md


5. examples/O1_examples.md


6. data/o1_miniset.jsonl


7. data/o1_hard_comparison_pairs.jsonl


8. examples/O1_on_real_llm_outputs_v1_weak_prompts.md


9. RESULTS.md




---

Related Repositories

For the shortest functional path into the broader ecosystem:

OMNIABASE — umbrella framework

OMNIA — Diagnostics / Structural Measurement branch

omniabase-coordinate-discovery — hidden coordinates and latent structure

omega-translator — structural residue across representational boundaries


Observer Suspension should be read as the epistemic pre-layer that helps motivate why the privilege of one observer-centered description should not be treated as final.


---

Current Research Direction

The current direction is now more precise than before.

1. Preserve and harden the protocol

The first task is not unlimited expansion, but maintaining the methodological clarity of the existing blocks.

2. Extend difficult comparisons carefully

New hard comparison pairs should only be added if they sharpen the distinction between reconstruction and evaporation.

3. Increase external usefulness

The protocol should eventually be applied to real AI outputs, technical language, benchmark discourse, and public explanatory texts.

4. Keep the boundary explicit

The repository must continue documenting not only successful reformulations, but also systematic failure modes.

That is what gives the project methodological teeth.


---

Final Definition

The most compact correct definition of this repository is:

Observer Suspension is a protocol for testing whether decentering a human description clarifies the phenomenon or dissolves it.

Or, even more sharply:

It is a methodological filter against pseudo-depth.