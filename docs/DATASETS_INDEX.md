# observer-suspension Datasets Index

## Purpose

This file lists the active O1 datasets and their roles.

## Core datasets

- `data/o1_miniset.jsonl`
  - minimal O1 examples

- `data/o1_borderline_cases.jsonl`
  - cases near the acceptance boundary

- `data/o1_comparison_pairs.jsonl`
  - A/B reformulation comparisons

- `data/o1_disagreement_labels.jsonl`
  - disagreement-type labels

- `data/o1_multiannotator_seed.jsonl`
  - seed items for multi-annotator comparison

- `data/o1_multiannotator_agreement_labels.jsonl`
  - agreement labels for multi-annotator analysis

- `data/o1_hard_inputs_seed.jsonl`
  - hard input seed set

- `data/o1_hard_cases_v0.jsonl`
  - accepted hard O1 cases

- `data/o1_hard_rejected_v0.jsonl`
  - rejected hard cases

- `data/o1_hard_comparison_pairs.jsonl`
  - hard A/B comparison pairs

## Tooling

Core validators and inspectors are in `tools/`.

Main runner:

```bash
python tools/run_o1_checks.py
```

## Interpretation

Dataset validity means:

```text
the records satisfy the expected structural format
```

It does not mean:

```text
the protocol proves final truth
the protocol replaces semantic judgment
the protocol replaces external review
```
