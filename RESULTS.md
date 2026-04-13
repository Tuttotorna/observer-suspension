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

This dataset is used to classify the kind of divergence between two annotations of the same input.

It adds an explicit layer for:
- precision disagreement
- boundary disagreement
- verdict disagreement

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

Input group size coverage:

- size 2: 4

Input group domain coverage:

- motion: 2
- perception: 1
- time: 1

Verdict pattern coverage:

- ('accepted', 'accepted'): 3
- ('accepted', 'rejected'): 1

Agreement type coverage:

- acceptable_convergence: 3
- verdict_split: 1

This dataset is used to test whether O1 remains structurally stable when the same input is annotated by different annotators.

Current annotator setup:

- annotator_alpha
- annotator_beta

Current purpose:

- preserve shared input identity
- compare annotation stability across annotators
- detect whether O1 captures structure or only a single writing style

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

## Disagreement labels validation

Disagreement dataset file:

data/o1_disagreement_labels.jsonl

Purpose:

- validate disagreement-type records linked to comparison pairs
- check disagreement type and label consistency
- verify verdict and strength consistency across both annotations
- verify target preservation and verdict split logic
- verify gain gap constraints

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

---

## Disagreement labels inspection

Disagreement inspector file:

tools/inspect_o1_disagreement_labels.py

Purpose:

- summarize total records
- summarize average, min, and max gain_gap
- count records by disagreement type
- count records by disagreement label
- count records by domain
- count records by target_preserved
- count records by verdict_split
- print sample disagreement records

Run:

python tools/inspect_o1_disagreement_labels.py

Observed output:

O1 disagreement labels inspection
--------------------------------
dataset: data/o1_disagreement_labels.jsonl
total records: 4
average gain_gap: 1.75
min gain_gap: 1
max gain_gap: 4

Records by disagreement type:
- D1: 2
- D3: 1
- D4: 1

Records by disagreement label:
- boundary_disagreement: 1
- precision_disagreement: 2
- verdict_disagreement: 1

Records by domain:
- motion: 2
- perception: 1
- time: 1

Records by target_preserved:
- 0: 1
- 1: 3

Records by verdict_split:
- 0: 3
- 1: 1

Sample disagreement records:

[dis_001]
  pair_id: cmp_001
  input: The object is still
  disagreement_type: D1
  disagreement_label: precision_disagreement
  annotation_a_strength: strong_acceptable
  annotation_b_strength: weak_acceptable
  gain_gap: 1
  notes: Both annotations preserve the same target and expose frame dependence, but annotation A is structurally sharper and reduces ambiguity more strongly.

[dis_002]
  pair_id: cmp_002
  input: Time passes
  disagreement_type: D1
  disagreement_label: precision_disagreement
  annotation_a_strength: strong_acceptable
  annotation_b_strength: weak_acceptable
  gain_gap: 1
  notes: Both annotations remain acceptable, but annotation A decomposes the distortion more precisely than annotation B.

[dis_003]
  pair_id: cmp_003
  input: I see a tree
  disagreement_type: D3
  disagreement_label: boundary_disagreement
  annotation_a_strength: strong_acceptable
  annotation_b_strength: borderline_acceptable
  gain_gap: 1
  notes: Both annotations remain acceptable, but annotation B moves closer to theoretical reinterpretation and therefore sits nearer the protocol boundary.

[dis_004]
  pair_id: cmp_004
  input: The train is moving
  disagreement_type: D4
  disagreement_label: verdict_disagreement
  annotation_a_strength: strong_acceptable
  annotation_b_strength: rejected
  gain_gap: 4
  notes: Annotation A preserves target and structural relation. Annotation B collapses into abstraction and fails the O1 acceptance threshold.

All comparison ids are unique.

---

## Multi-annotator seed validation

Multi-annotator dataset file:

data/o1_multiannotator_seed.jsonl

Purpose:

- validate grouped records for the same input across different annotators
- check record-level metric consistency
- ensure each input group contains exactly two distinct annotators
- ensure grouped records share domain and input text

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

---

## Multi-annotator seed inspection

Multi-annotator inspector file:

tools/inspect_o1_multiannotator_seed.py

Purpose:

- summarize total records and input groups
- summarize average o1_gain
- summarize average, min, and max gain gap per group
- count records by annotator
- count records by domain
- count records by verdict
- count input groups by size
- count input groups by domain
- count verdict patterns by group
- print sample input groups

Run:

python tools/inspect_o1_multiannotator_seed.py

Observed output:

O1 multi-annotator seed inspection
----------------------------------
dataset: data/o1_multiannotator_seed.jsonl
total records: 8
total input groups: 4
average o1_gain: 2.88
average gain gap per group: 1.25
min gain gap: 1
max gain gap: 4

Records by annotator:
- annotator_alpha: 4
- annotator_beta: 4

Records by domain:
- motion: 4
- perception: 2
- time: 2

Records by verdict:
- accepted: 7
- rejected: 1

Input groups by size:
- size 2: 4

Input groups by domain:
- motion: 2
- perception: 1
- time: 1

Verdict patterns by group:
- ('accepted', 'accepted'): 3
- ('accepted', 'rejected'): 1

Sample input groups:

[ma_input_001]
  annotator=annotator_alpha, domain=motion, verdict=accepted, o1_gain=4
    input: The object is still
    reformulation: The object remains at constant position relative to the chosen reference frame.
  annotator=annotator_beta, domain=motion, verdict=accepted, o1_gain=3
    input: The object is still
    reformulation: The object does not change position relative to the observer's chosen frame.

[ma_input_002]
  annotator=annotator_alpha, domain=time, verdict=accepted, o1_gain=4
    input: Time passes
    reformulation: State changes are ordered and compared in a way experienced as temporal progression by the observer.
  annotator=annotator_beta, domain=time, verdict=accepted, o1_gain=3
    input: Time passes
    reformulation: Observed change is structured in sequence and interpreted as temporal passage.

[ma_input_003]
  annotator=annotator_alpha, domain=perception, verdict=accepted, o1_gain=4
    input: I see a tree
    reformulation: My visual system registers and interprets signals consistent with a tree at this position relative to me.
  annotator=annotator_beta, domain=perception, verdict=accepted, o1_gain=3
    input: I see a tree
    reformulation: A portion of the visual field is stabilized and interpreted as a tree.

[ma_input_004]
  annotator=annotator_alpha, domain=motion, verdict=accepted, o1_gain=4
    input: The train is moving
    reformulation: The train changes position relative to the observer's current reference frame.
  annotator=annotator_beta, domain=motion, verdict=rejected, o1_gain=0
    input: The train is moving
    reformulation: Motion is an illusion created by perspective.

All record ids are unique.

---

## Multi-annotator agreement analysis

Agreement analysis file:

tools/analyze_o1_multiannotator_agreement.py

Purpose:

- classify agreement patterns across annotators on the same input
- measure gain gap across annotators
- distinguish acceptable convergence from verdict split
- show group-level stability under annotator change

Run:

python tools/analyze_o1_multiannotator_agreement.py

Observed output:

O1 multi-annotator agreement analysis
-------------------------------------
dataset: data/o1_multiannotator_seed.jsonl
total records: 8
total input groups: 4
average gain gap: 1.25
min gain gap: 1
max gain gap: 4

Agreement types:
- acceptable_convergence: 3
- verdict_split: 1

Verdict patterns:
- ('accepted', 'accepted'): 3
- ('accepted', 'rejected'): 1

Input groups by domain:
- motion: 2
- perception: 1
- time: 1

Group details:

[ma_input_001]
  domain: motion
  input: The object is still
  agreement_type: acceptable_convergence
  verdict_pattern: ('accepted', 'accepted')
  gain_gap: 1
  annotator=annotator_alpha, verdict=accepted, o1_gain=4
    reformulation: The object remains at constant position relative to the chosen reference frame.
  annotator=annotator_beta, verdict=accepted, o1_gain=3
    reformulation: The object does not change position relative to the observer's chosen frame.

[ma_input_002]
  domain: time
  input: Time passes
  agreement_type: acceptable_convergence
  verdict_pattern: ('accepted', 'accepted')
  gain_gap: 1
  annotator=annotator_alpha, verdict=accepted, o1_gain=4
    reformulation: State changes are ordered and compared in a way experienced as temporal progression by the observer.
  annotator=annotator_beta, verdict=accepted, o1_gain=3
    reformulation: Observed change is structured in sequence and interpreted as temporal passage.

[ma_input_003]
  domain: perception
  input: I see a tree
  agreement_type: acceptable_convergence
  verdict_pattern: ('accepted', 'accepted')
  gain_gap: 1
  annotator=annotator_alpha, verdict=accepted, o1_gain=4
    reformulation: My visual system registers and interprets signals consistent with a tree at this position relative to me.
  annotator=annotator_beta, verdict=accepted, o1_gain=3
    reformulation: A portion of the visual field is stabilized and interpreted as a tree.

[ma_input_004]
  domain: motion
  input: The train is moving
  agreement_type: verdict_split
  verdict_pattern: ('accepted', 'rejected')
  gain_gap: 4
  annotator=annotator_alpha, verdict=accepted, o1_gain=4
    reformulation: The train changes position relative to the observer's current reference frame.
  annotator=annotator_beta, verdict=rejected, o1_gain=0
    reformulation: Motion is an illusion created by perspective.

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
- inspect the comparison pairs dataset
- validate the disagreement labels dataset
- inspect the disagreement labels dataset
- validate the multi-annotator seed dataset
- inspect the multi-annotator seed dataset

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
5. a fixed disagreement-labels dataset
6. a fixed multi-annotator seed dataset
7. explicit gain fields
8. accepted and rejected cases
9. executable dataset checks
10. executable dataset inspection
11. pair-level validation for comparative annotations
12. pair-level inspection for comparative annotations
13. disagreement-type validation
14. disagreement-type inspection
15. multi-annotator seed validation
16. multi-annotator seed inspection
17. multi-annotator agreement analysis
18. a unified runner for the whole O1 block

This is enough to prove that the repository has moved past pure conceptual framing.

It is not enough yet to prove scientific strength.

---

## What is still missing

The project still lacks:

- integration of multi-annotator agreement analysis into the unified runner
- harder borderline cases across more domains
- comparison between more than two annotators on the same inputs
- explicit disagreement analysis beyond labels
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
- explicit disagreement typing
- validated base dataset
- validated borderline dataset
- validated comparison pairs dataset
- validated disagreement labels dataset
- validated multi-annotator seed dataset
- executable tooling
- unified checks runner

That is the correct first threshold.