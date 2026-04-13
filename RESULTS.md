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

This dataset is used to compare alternative annotations of the same input:
- strong acceptable annotation
- weak acceptable annotation
- borderline acceptable annotation
- rejected annotation

It adds controlled variation on identical inputs.

---

## Validator

Validator file:

tools/validate_o1_dataset.py

Purpose:

- check valid JSONL structure
- check required string fields
- check binary gain fields
- check o1_gain consistency
- check verdict consistency
- check duplicate ids

Run on base dataset:

python tools/validate_o1_dataset.py

Observed output:

O1 dataset validation
---------------------
dataset: data/o1_miniset.jsonl
total records: 13
valid records: 13
invalid records: 0

No validation errors found.

Run on borderline dataset:

python tools/validate_o1_dataset.py data/o1_borderline_cases.jsonl

Observed output:

O1 dataset validation
---------------------
dataset: data/o1_borderline_cases.jsonl
total records: 10
valid records: 10
invalid records: 0

No validation errors found.

---

## Inspector

Inspector file:

tools/inspect_o1_dataset.py

Purpose:

- summarize total records
- summarize average gain
- count accepted vs rejected
- count records by domain
- count records by domain and verdict
- print sample records

Run on base dataset:

python tools/inspect_o1_dataset.py

Observed output:

O1 dataset inspection
---------------------
dataset: data/o1_miniset.jsonl
total records: 13
average o1_gain: 3.69

Records by verdict:
- accepted: 12
- rejected: 1

Records by domain:
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

Records by domain and verdict:
- agency: accepted=1, rejected=0
- causality: accepted=1, rejected=0
- identity: accepted=1, rejected=0
- motion: accepted=2, rejected=1
- orientation: accepted=1, rejected=0
- perception: accepted=1, rejected=0
- sound: accepted=1, rejected=0
- space: accepted=1, rejected=0
- temperature: accepted=1, rejected=0
- time: accepted=1, rejected=0
- value: accepted=1, rejected=0

Sample records:

[o1_001] motion
  standard: The sun rises
  reformulation: The sun's apparent position changes relative to an Earth-bound observer due to Earth's rotation.
  o1_gain: 4
  verdict: accepted

[o1_002] motion
  standard: The object is still
  reformulation: The object remains at constant position relative to the chosen reference frame.
  o1_gain: 4
  verdict: accepted

[o1_003] time
  standard: Time passes
  reformulation: State changes are ordered and compared in a way experienced as temporal progression by the observer.
  o1_gain: 4
  verdict: accepted

[o1_004] perception
  standard: I see a tree
  reformulation: My visual system registers and interprets signals consistent with a tree at this position relative to me.
  o1_gain: 4
  verdict: accepted

[o1_005] causality
  standard: A causes B
  reformulation: Within this model, changes in A systematically precede and constrain changes in B.
  o1_gain: 4
  verdict: accepted

All record ids are unique.

Run on borderline dataset:

python tools/inspect_o1_dataset.py data/o1_borderline_cases.jsonl

Observed output:

O1 dataset inspection
---------------------
dataset: data/o1_borderline_cases.jsonl
total records: 10
average o1_gain: 2.00

Records by verdict:
- accepted: 5
- rejected: 5

Records by domain:
- causality: 2
- identity: 2
- motion: 2
- perception: 2
- time: 2

Records by domain and verdict:
- causality: accepted=1, rejected=1
- identity: accepted=1, rejected=1
- motion: accepted=1, rejected=1
- perception: accepted=1, rejected=1
- time: accepted=1, rejected=1

Sample records:

[o1b_001] motion
  standard: The train is moving
  reformulation: The train changes position relative to the observer's current reference frame.
  o1_gain: 4
  verdict: accepted

[o1b_002] motion
  standard: The train is moving
  reformulation: Motion is an illusion created by perspective.
  o1_gain: 0
  verdict: rejected

[o1b_003] time
  standard: The meeting starts at 3 PM
  reformulation: Within the agreed local time convention, the meeting begins at the coordinate labeled 3 PM.
  o1_gain: 4
  verdict: accepted

[o1b_004] time
  standard: The meeting starts at 3 PM
  reformulation: Time is socially constructed.
  o1_gain: 0
  verdict: rejected

[o1b_005] perception
  standard: The light is bright
  reformulation: The light produces high perceived intensity for this observer under current adaptation conditions.
  o1_gain: 4
  verdict: accepted

All record ids are unique.

---

## Comparison pairs validation

Comparison dataset file:

data/o1_comparison_pairs.jsonl

Purpose:

- validate paired A/B annotations on the same input
- check pair-level structural consistency
- verify annotation-level metric consistency
- ensure each pair is complete and comparable

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

---

## Comparison pairs inspection

Comparison inspector file:

tools/inspect_o1_comparison_pairs.py

Purpose:

- summarize total records and total pairs
- summarize average gain
- count records by strength
- count records by verdict
- count records by domain
- count pairs by domain
- count pair types
- print sample pairs

Run:

python tools/inspect_o1_comparison_pairs.py

Observed output:

O1 comparison pairs inspection
------------------------------
dataset: data/o1_comparison_pairs.jsonl
total records: 8
total pairs: 4
average o1_gain: 2.75

Records by strength:
- borderline_acceptable: 1
- rejected: 1
- strong_acceptable: 4
- weak_acceptable: 2

Records by verdict:
- accepted: 7
- rejected: 1

Records by domain:
- motion: 4
- perception: 2
- time: 2

Pairs by domain:
- motion: 2
- perception: 1
- time: 1

Pair types:
- acceptable_vs_rejected: 1
- strong_vs_borderline: 1
- strong_vs_weak: 2

Sample pairs:

[cmp_001]
  variant A: strength=strong_acceptable, verdict=accepted, o1_gain=4
    input: The object is still
    reformulation: The object remains at constant position relative to the chosen reference frame.
  variant B: strength=weak_acceptable, verdict=accepted, o1_gain=3
    input: The object is still
    reformulation: The object appears not to change position from this observational frame.

[cmp_002]
  variant A: strength=strong_acceptable, verdict=accepted, o1_gain=4
    input: Time passes
    reformulation: State changes are ordered and compared in a way experienced as temporal progression by the observer.
  variant B: strength=weak_acceptable, verdict=accepted, o1_gain=3
    input: Time passes
    reformulation: Observed change is organized in a sequence interpreted as temporal passage.

[cmp_003]
  variant A: strength=strong_acceptable, verdict=accepted, o1_gain=4
    input: I see a tree
    reformulation: My visual system registers and interprets signals consistent with a tree at this position relative to me.
  variant B: strength=borderline_acceptable, verdict=accepted, o1_gain=3
    input: I see a tree
    reformulation: A portion of the visual field is stabilized and interpreted as a tree.

All annotation ids are unique.

---

## Unified runner

Runner file:

tools/run_o1_checks.py

Purpose:

- validate the base dataset
- inspect the base dataset
- validate the borderline dataset
- inspect the borderline dataset
- validate the comparison pairs dataset

Run:

python tools/run_o1_checks.py

Current role:

This script is the single operational entry point for the current O1 methodological block.

---

## Meaning of the current result

At this stage, the repository can already show:

1. a fixed protocol
2. a fixed minimal dataset
3. a fixed borderline stress-test dataset
4. a fixed comparison-pairs dataset
5. explicit gain fields
6. accepted and rejected cases
7. executable dataset checks
8. executable dataset inspection
9. pair-level validation for comparative annotations
10. pair-level inspection for comparative annotations
11. a unified runner for the whole O1 block

This is enough to prove that the repository has moved past pure conceptual framing.

It is not enough yet to prove scientific strength.

---

## What is still missing

The project still lacks:

- harder borderline cases across more domains
- comparison between multiple annotators on the same inputs
- explicit disagreement analysis
- automatic scoring proposals
- bridge to stronger structural systems

So the repository is now minimally executable, but still early.

---

## Current conclusion

Observer Suspension is no longer only an epistemic idea.

It is now a small but structured protocol with:

- explicit fields
- explicit gain rule
- explicit rejection condition
- explicit annotation discipline
- explicit comparison rules
- validated base dataset
- validated borderline dataset
- validated comparison pairs dataset
- executable tooling
- unified checks runner

That is the correct first threshold.