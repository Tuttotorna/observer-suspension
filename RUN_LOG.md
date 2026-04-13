# O1 Unified Run Log

This file stores the latest full observed output of the unified O1 checks run.

It is a raw execution snapshot.
It is not a normalized summary.

---

## Command set executed

```text
/usr/bin/python3 tools/validate_o1_dataset.py data/o1_miniset.jsonl
/usr/bin/python3 tools/inspect_o1_dataset.py data/o1_miniset.jsonl
/usr/bin/python3 tools/validate_o1_dataset.py data/o1_borderline_cases.jsonl
/usr/bin/python3 tools/inspect_o1_dataset.py data/o1_borderline_cases.jsonl
/usr/bin/python3 tools/validate_o1_comparison_pairs.py data/o1_comparison_pairs.jsonl
/usr/bin/python3 tools/inspect_o1_comparison_pairs.py data/o1_comparison_pairs.jsonl


---

Observed output

$ /usr/bin/python3 tools/validate_o1_dataset.py data/o1_miniset.jsonl
## O1 dataset validation
dataset: data/o1_miniset.jsonl
total records: 13
valid records: 13
invalid records: 0
## No validation errors found.

$ /usr/bin/python3 tools/inspect_o1_dataset.py data/o1_miniset.jsonl
## O1 dataset inspection
dataset: data/o1_miniset.jsonl
total records: 13
average o1_gain: 3.69
Records by verdict:
 * accepted: 12
 * rejected: 1
Records by domain:
 * agency: 1
 * causality: 1
 * identity: 1
 * motion: 3
 * orientation: 1
 * perception: 1
 * sound: 1
 * space: 1
 * temperature: 1
 * time: 1
 * value: 1
Records by domain and verdict:
 * agency: accepted=1, rejected=0
 * causality: accepted=1, rejected=0
 * identity: accepted=1, rejected=0
 * motion: accepted=2, rejected=1
 * orientation: accepted=1, rejected=0
 * perception: accepted=1, rejected=0
 * sound: accepted=1, rejected=0
 * space: accepted=1, rejected=0
 * temperature: accepted=1, rejected=0
 * time: accepted=1, rejected=0
 * value: accepted=1, rejected=0
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
## All record ids are unique.

$ /usr/bin/python3 tools/validate_o1_dataset.py data/o1_borderline_cases.jsonl
## O1 dataset validation
dataset: data/o1_borderline_cases.jsonl
total records: 10
valid records: 10
invalid records: 0
## No validation errors found.

$ /usr/bin/python3 tools/inspect_o1_dataset.py data/o1_borderline_cases.jsonl
## O1 dataset inspection
dataset: data/o1_borderline_cases.jsonl
total records: 10
average o1_gain: 2.00
Records by verdict:
 * accepted: 5
 * rejected: 5
Records by domain:
 * causality: 2
 * identity: 2
 * motion: 2
 * perception: 2
 * time: 2
Records by domain and verdict:
 * causality: accepted=1, rejected=1
 * identity: accepted=1, rejected=1
 * motion: accepted=1, rejected=1
 * perception: accepted=1, rejected=1
 * time: accepted=1, rejected=1
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
## All record ids are unique.

$ /usr/bin/python3 tools/validate_o1_comparison_pairs.py data/o1_comparison_pairs.jsonl
## O1 comparison pairs validation
dataset: data/o1_comparison_pairs.jsonl
total records: 8
valid records: 8
invalid records: 0
total pairs: 4
## No validation errors found.

$ /usr/bin/python3 tools/inspect_o1_comparison_pairs.py data/o1_comparison_pairs.jsonl
## O1 comparison pairs inspection
dataset: data/o1_comparison_pairs.jsonl
total records: 8
total pairs: 4
average o1_gain: 2.75
Records by strength:
 * borderline_acceptable: 1
 * rejected: 1
 * strong_acceptable: 4
 * weak_acceptable: 2
Records by verdict:
 * accepted: 7
 * rejected: 1
Records by domain:
 * motion: 4
 * perception: 2
 * time: 2
Pairs by domain:
 * motion: 2
 * perception: 1
 * time: 1
Pair types:
 * acceptable_vs_rejected: 1
 * strong_vs_borderline: 1
 * strong_vs_weak: 2
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
## All annotation ids are unique.


---

Operational reading

This raw log confirms that, at the moment of execution:

base dataset validation passed

base dataset inspection completed

borderline dataset validation passed

borderline dataset inspection completed

comparison pairs validation passed

comparison pairs inspection completed


This file should be updated only when a new full run is executed and its output is captured again.


