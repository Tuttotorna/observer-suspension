# observer-suspension

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19571535.svg)](https://doi.org/10.5281/zenodo.19571535)

**observer-suspension** is a structural protocol for exposing and reducing hidden observer privilege in descriptions.

It is not philosophy.

It is not a worldview.

It is not a semantic judge.

It is not a truth oracle.

It is not a decision engine.

Its role is narrower:

```text
detect observer-centered assumptions inside descriptions
reduce frame dependence when possible
preserve the phenomenon when decentering is valid
reject reformulations that dissolve the phenomenon
```

Core boundary:

```text
measurement != inference != decision
```

Decision remains external.

---



## Foundational Principle

observer-suspension is an observer-frame application of the L.O.N. Multi-Form Invariance Principle:

> No single form is sovereign.

In observer-suspension, this becomes:

> No observer frame is sovereign.

A structure is not trusted because it appears coherent from one observer position, one descriptive frame, one temporal assumption, one causal narrative, or one privileged perspective. It must be tested by suspending observer privilege and comparing what remains across alternative frames of description.

observer-suspension exists to distinguish observer-dependent appearance from structural residue that survives frame removal.

See:

- https://github.com/Tuttotorna/lon-mirror/tree/main/foundation

## Public position

Observer Suspension public positioning is documented here:

- [`docs/OBSERVER_SUSPENSION_PUBLIC_POSITION.md`](docs/OBSERVER_SUSPENSION_PUBLIC_POSITION.md)

Core thesis:

```text
observer privilege must be exposed before structural claims are trusted
```

Core boundary:

```text
observer suspension != observer elimination
description != reality
measurement != inference != decision
```

Core role:

```text
Observer Suspension exposes observer-dependent assumptions and tests what remains stable when privileged framing is reduced.
```

Observer Suspension does not remove all observers absolutely.

It does not claim access to reality without mediation.

It does not decide final truth.

## Core idea

Ordinary language often treats one observer frame as if it were neutral.

observer-suspension tests whether a description contains hidden observer privilege.

The protocol asks:

```text
What assumption makes this description appear natural?
What structure is hidden by that assumption?
Can the description be reformulated with less frame dependence?
Does the reformulation preserve the phenomenon or destroy it?
```

The decisive distinction is:

```text
reconstruction != evaporation
```

---

## O1 protocol

The current protocol is **O1 — Suspension of the privileged observer**.

O1 decomposes an ordinary statement into fixed fields:

1. standard formulation
2. hidden observer assumption
3. structural distortion
4. decentered reformulation
5. emergent structure

The protocol is not meant to make language more abstract.

It is meant to expose hidden frame dependence while preserving referential continuity.

---

## Minimal example

Standard formulation:

```text
The sun rises.
```

Hidden observer assumption:

```text
A stable Earth-bound observer frame is treated as primary.
```

Structural distortion:

```text
Relative apparent motion is compressed into an absolute event attributed to the sun.
```

Decentered reformulation:

```text
The sun's apparent position changes relative to an Earth-bound observer due to Earth's rotation.
```

Emergent structure:

```text
Observed solar motion depends on observer frame and planetary rotation, not on an intrinsic rising event.
```

---

## What counts as gain

A reformulation is not useful merely because it sounds more abstract.

The repository uses O1 gain rules to separate valid structural clarification from pseudo-depth.

A useful O1 reformulation should improve structural clarity by increasing:

- explicitness of the observer frame
- relational precision
- recoverability of the original phenomenon
- reduction of hidden frame dependence
- preservation of referential continuity

If the original phenomenon becomes unrecoverable, the reformulation fails.

---

## What this repository contains

Current active components:

- O1 protocol documents
- annotation guidelines
- comparison rules
- gain criteria
- disagreement labels
- multi-annotator seed sets
- borderline and hard cases
- validators
- inspectors
- unified O1 check runner

The repository is not just conceptual. It contains datasets and executable validation tools.

---

## Main files

Start here:

- [`docs/O1_PROTOCOL.md`](docs/O1_PROTOCOL.md)
- [`docs/O1_GAIN_CRITERIA.md`](docs/O1_GAIN_CRITERIA.md)
- [`docs/O1_PROTOCOL_LOGIC.md`](docs/O1_PROTOCOL_LOGIC.md)
- [`docs/PROTOCOL_SCOPE.md`](docs/PROTOCOL_SCOPE.md)
- [`docs/DATASETS_INDEX.md`](docs/DATASETS_INDEX.md)
- [`RESULTS.md`](RESULTS.md)

Dataset files:

- [`data/o1_miniset.jsonl`](data/o1_miniset.jsonl)
- [`data/o1_borderline_cases.jsonl`](data/o1_borderline_cases.jsonl)
- [`data/o1_comparison_pairs.jsonl`](data/o1_comparison_pairs.jsonl)
- [`data/o1_disagreement_labels.jsonl`](data/o1_disagreement_labels.jsonl)
- [`data/o1_multiannotator_seed.jsonl`](data/o1_multiannotator_seed.jsonl)
- [`data/o1_multiannotator_agreement_labels.jsonl`](data/o1_multiannotator_agreement_labels.jsonl)
- [`data/o1_hard_cases_v0.jsonl`](data/o1_hard_cases_v0.jsonl)
- [`data/o1_hard_rejected_v0.jsonl`](data/o1_hard_rejected_v0.jsonl)
- [`data/o1_hard_comparison_pairs.jsonl`](data/o1_hard_comparison_pairs.jsonl)

Tools:

- [`tools/validate_o1_dataset.py`](tools/validate_o1_dataset.py)
- [`tools/inspect_o1_dataset.py`](tools/inspect_o1_dataset.py)
- [`tools/run_o1_checks.py`](tools/run_o1_checks.py)

---

## Run checks

```bash
python tools/run_o1_checks.py
```

Run repository smoke tests:

```bash
python -m pip install -e .
python -m pytest
```

---

## What it is not

observer-suspension is not:

- a philosophy
- a worldview
- a metaphysical system
- a truth detector
- a semantic judge
- a decision engine
- a replacement for science
- a replacement for ordinary language
- a claim that all observer frames are invalid

It is a structural protocol for testing where observer privilege is hidden inside descriptions.

---

## Correct interpretation

```text
observer-centered statement -> O1 decomposition
O1 decomposition -> structural reformulation attempt
structural reformulation -> gain / failure assessment
assessment -> not final truth
decision -> external
```

The protocol can fail.

Failure is informative because it shows where decentering destroys the phenomenon instead of clarifying it.

---

## Relationship to OMNIABASE and OMNIA

```text
observer-suspension = epistemic pre-layer
OMNIABASE           = multirepresentational framework
OMNIA               = structural measurement layer
OMNIA-LIMIT         = stop / continue / retry / escalate boundary
Decision            = external layer
```

The boundary remains strict:

```text
measurement != inference != decision
```

---

## Related repositories

- OMNIABASE: https://github.com/Tuttotorna/OMNIABASE
- OMNIA: https://github.com/Tuttotorna/OMNIA
- lon-mirror: https://github.com/Tuttotorna/lon-mirror
- omega-translator: https://github.com/Tuttotorna/omega-translator
- omniabase-coordinate-discovery: https://github.com/Tuttotorna/omniabase-coordinate-discovery

---

## Citation

If you reference this repository, use the archived Zenodo record:

```text
DOI: 10.5281/zenodo.19571535
https://doi.org/10.5281/zenodo.19571535
```

Citation metadata is available in:

- [`CITATION.cff`](CITATION.cff)

---

## Summary

observer-suspension is a structural protocol for observer-privilege reduction.

It is not philosophy.

It is not a worldview.

It is not a truth oracle.

It is not a semantic judge.

It is not a decision engine.

It tests whether descriptions can be made less frame-dependent without losing the phenomenon being described.
