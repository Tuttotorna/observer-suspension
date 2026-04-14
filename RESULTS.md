# Results

This file reports the current minimal executable state of the repository.

It is not a scientific validation.
It is only a reproducible status snapshot of the current O1 datasets and tools.

---

## Current dataset status

Base dataset file:

data/o1_miniset.jsonl

Current observed contents:

- total records: 13
- accepted: 12
- rejected: 1
- average O1 gain: 3.69

Domain coverage:

- agency: 1
- causality: 1
- identity: 1
- motion: 3
- orientation: 1
- perception: 1
- sound: 1
- space: 1
- temperature: 1
- time: 1
- value: 1

---

## Borderline dataset status

Borderline dataset file:

data/o1_borderline_cases.jsonl

Current observed contents:

- total records: 10
- accepted: 5
- rejected: 5
- average O1 gain: 2.00

Domain coverage:

- causality: 2
- identity: 2
- motion: 2
- perception: 2
- time: 2

This dataset is used to stress-test O1 on harder matched pairs:
same input, one acceptable reformulation, one rejected reformulation.

---

## Comparison pairs dataset status

Comparison dataset file:

data/o1_comparison_pairs.jsonl

Current observed contents:

- total records: 8
- total pairs: 4
- valid records: 8
- invalid records: 0
- average O1 gain: 2.75

Record strength coverage:

- borderline_acceptable: 1
- rejected: 1
- strong_acceptable: 4
- weak_acceptable: 2

Record verdict coverage:

- accepted: 7
- rejected: 1

Domain coverage:

- motion: 4
- perception: 2
- time: 2

Pair coverage by domain:

- motion: 2
- perception: 1
- time: 1

Pair type coverage:

- acceptable_vs_rejected: 1
- strong_vs_borderline: 1
- strong_vs_weak: 2

---

## Disagreement labels dataset status

Disagreement dataset file:

data/o1_disagreement_labels.jsonl

Current observed contents:

- total records: 4
- valid records: 4
- invalid records: 0
- average gain_gap: 1.75
- min gain_gap: 1
- max gain_gap: 4

Disagreement type coverage:

- D1: 2
- D3: 1
- D4: 1

Disagreement label coverage:

- boundary_disagreement: 1
- precision_disagreement: 2
- verdict_disagreement: 1

Domain coverage:

- motion: 2
- perception: 1
- time: 1

target_preserved coverage:

- 0: 1
- 1: 3

verdict_split coverage:

- 0: 3
- 1: 1

---

## Multi-annotator seed dataset status

Multi-annotator dataset file:

data/o1_multiannotator_seed.jsonl

Current observed contents:

- total records: 8
- valid records: 8
- invalid records: 0
- total input groups: 4
- average O1 gain: 2.88
- average gain gap per group: 1.25
- min gain gap: 1
- max gain gap: 4

Annotator coverage:

- annotator_alpha: 4
- annotator_beta: 4

Domain coverage:

- motion: 4
- perception: 2
- time: 2

Verdict coverage:

- accepted: 7
- rejected: 1

Agreement type coverage:

- acceptable_convergence: 3
- verdict_split: 1

---

## Multi-annotator agreement labels dataset status

Agreement labels dataset file:

data/o1_multiannotator_agreement_labels.jsonl

Current observed contents:

- total records: 4
- valid records: 4
- invalid records: 0
- average gain_gap: 1.75
- min gain_gap: 1
- max gain_gap: 4

Agreement type coverage:

- A1: 3
- A3: 1

Agreement label coverage:

- acceptable_convergence: 3
- verdict_split: 1

Domain coverage:

- motion: 2
- perception: 1
- time: 1

Verdict pattern coverage:

- ('accepted', 'accepted'): 3
- ('accepted', 'rejected'): 1

---

## Hard cases v0 dataset status

Hard cases dataset file:

data/o1_hard_cases_v0.jsonl

Current observed contents:

- total records: 4
- valid records: 4
- invalid records: 0
- average O1 gain: 4.00
- min O1 gain: 4
- max O1 gain: 4

Verdict coverage:

- accepted: 4

Domain coverage:

- agency: 1
- causality: 1
- motion: 1
- time: 1

Current role:

This dataset starts the next difficulty phase for O1, using inputs that contain:
- distributed process compression
- metaphorical temporal motion
- distributed causal narration
- agency metaphor

---

## Hard rejected v0 dataset status

Hard rejected dataset file:

data/o1_hard_rejected_v0.jsonl

Current observed contents:

- total records: 4
- valid records: 4
- invalid records: 0
- average O1 gain: 0.00
- min O1 gain: 0
- max O1 gain: 0

Verdict coverage:

- rejected: 4

Domain coverage:

- identity: 1
- perception: 1
- sound: 1
- value: 1

Current role:

This dataset records typical hard-case failures where the protocol collapses into abstraction, generic relativism, or pseudo-depth instead of preserving the target.

It adds the failure side of the difficulty phase.

---

## Hard comparison pairs dataset status

Hard comparison pairs dataset file:

data/o1_hard_comparison_pairs.jsonl

Current observed contents:

- total records: 4
- total pairs: 2
- valid records: 4
- invalid records: 0

Strength coverage:

- accepted: 2
- rejected: 2

Verdict coverage:

- accepted: 2
- rejected: 2

Domain coverage:

- identity: 2
- value: 2

Pair type coverage:

- accepted_vs_rejected: 2

Current role:

This dataset puts the hard-case border into direct pairwise form:
- one structurally valid decomposition
- one pseudo-deep failure
- same difficult input
- same domain
- opposite outcomes

It is the cleanest current front-facing test of O1 under high semantic pressure.

---

## Validation blocks

### Base dataset validation

Validator file:

tools/validate_o1_dataset.py

Run:

python tools/validate_o1_dataset.py

Observed output:

O1 dataset validation
---------------------
dataset: data/o1_miniset.jsonl
total records: 13
valid records: 13
invalid records: 0

No validation errors found.

### Borderline dataset validation

Run:

python tools/validate_o1_dataset.py data/o1_borderline_cases.jsonl

Observed output:

O1 dataset validation
---------------------
dataset: data/o1_borderline_cases.jsonl
total records: 10
valid records: 10
invalid records: 0

No validation errors found.

### Comparison pairs validation

Validator file:

tools/validate_o1_comparison_pairs.py

Run:

python tools/validate_o1_comparison_pairs.py

Observed output:

O1 comparison pairs validation
------------------------------
dataset: data/o1_comparison_pairs.jsonl
total records: 8
valid records: 8
invalid records: 0
total pairs: 4

No validation errors found.

### Disagreement labels validation

Validator file:

tools/validate_o1_disagreement_labels.py

Run:

python tools/validate_o1_disagreement_labels.py

Observed output:

O1 disagreement labels validation
--------------------------------
dataset: data/o1_disagreement_labels.jsonl
total records: 4
valid records: 4
invalid records: 0

No validation errors found.

### Multi-annotator seed validation

Validator file:

tools/validate_o1_multiannotator_seed.py

Run:

python tools/validate_o1_multiannotator_seed.py

Observed output:

O1 multi-annotator seed validation
----------------------------------
dataset: data/o1_multiannotator_seed.jsonl
total records: 8
valid records: 8
invalid records: 0
total input groups: 4

No validation errors found.

### Multi-annotator agreement labels validation

Validator file:

tools/validate_o1_multiannotator_agreement_labels.py

Run:

python tools/validate_o1_multiannotator_agreement_labels.py

Observed output:

O1 multi-annotator agreement labels validation
----------------------------------------------
dataset: data/o1_multiannotator_agreement_labels.jsonl
total records: 4
valid records: 4
invalid records: 0

No validation errors found.

### Hard cases v0 validation

Validator file:

tools/validate_o1_hard_cases_v0.py

Run:

python tools/validate_o1_hard_cases_v0.py

Observed output:

O1 hard cases v0 validation
---------------------------
dataset: data/o1_hard_cases_v0.jsonl
total records: 4
valid records: 4
invalid records: 0

No validation errors found.

### Hard rejected v0 validation

Validator file:

tools/validate_o1_hard_rejected_v0.py

Run:

python tools/validate_o1_hard_rejected_v0.py

Observed output:

O1 hard rejected v0 validation
------------------------------
dataset: data/o1_hard_rejected_v0.jsonl
total records: 4
valid records: 4
invalid records: 0

No validation errors found.

### Hard comparison pairs validation

Validator file:

tools/validate_o1_hard_comparison_pairs.py

Run:

python tools/validate_o1_hard_comparison_pairs.py

Observed output:

O1 hard comparison pairs validation
-----------------------------------
dataset: data/o1_hard_comparison_pairs.jsonl
total records: 4
valid records: 4
invalid records: 0
total pairs: 2

No validation errors found.

---

## Inspection blocks

### Hard cases v0 inspection

Inspector file:

tools/inspect_o1_hard_cases_v0.py

Run:

python tools/inspect_o1_hard_cases_v0.py

Observed output:

O1 hard cases v0 inspection
---------------------------
dataset: data/o1_hard_cases_v0.jsonl
total records: 4
average o1_gain: 4.00
min o1_gain: 4
max o1_gain: 4

Records by verdict:
- accepted: 4

Records by domain:
- agency: 1
- causality: 1
- motion: 1
- time: 1

All case ids are unique.

### Hard rejected v0 inspection

Inspector file:

tools/inspect_o1_hard_rejected_v0.py

Run:

python tools/inspect_o1_hard_rejected_v0.py

Observed output:

O1 hard rejected v0 inspection
------------------------------
dataset: data/o1_hard_rejected_v0.jsonl
total records: 4
average o1_gain: 0.00
min o1_gain: 0
max o1_gain: 0

Records by verdict:
- rejected: 4

Records by domain:
- identity: 1
- perception: 1
- sound: 1
- value: 1

All case ids are unique.

### Hard comparison pairs inspection

Inspector file:

tools/inspect_o1_hard_comparison_pairs.py

Run:

python tools/inspect_o1_hard_comparison_pairs.py

Observed output:

O1 hard comparison pairs inspection
-----------------------------------
dataset: data/o1_hard_comparison_pairs.jsonl
total records: 4
total pairs: 2

Pending updated inspection after the second pair addition.

---

## Current conclusion

Observer Suspension is now a structured methodological system with:

- base cases
- borderline cases
- comparison pairs
- disagreement labels
- multi-annotator seed
- multi-annotator agreement labels
- accepted hard cases
- rejected hard cases
- hard comparison pairs
- executable validation and inspection layers

The current difficulty phase now contains both success and failure modes, plus direct front-facing boundary comparison on identity and value.

That is the correct next threshold.