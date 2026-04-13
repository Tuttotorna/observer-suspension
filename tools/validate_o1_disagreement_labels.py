import json
import sys
from pathlib import Path

DEFAULT_DATASET_PATH = Path("data/o1_disagreement_labels.jsonl")

REQUIRED_STRING_FIELDS = [
    "comparison_id",
    "pair_id",
    "input",
    "domain",
    "annotation_a_id",
    "annotation_b_id",
    "annotation_a_strength",
    "annotation_b_strength",
    "annotation_a_verdict",
    "annotation_b_verdict",
    "disagreement_type",
    "disagreement_label",
    "notes",
]

REQUIRED_BINARY_FIELDS = [
    "target_preserved",
    "verdict_split",
]

ALLOWED_STRENGTHS = {
    "strong_acceptable",
    "weak_acceptable",
    "borderline_acceptable",
    "rejected",
}

ALLOWED_VERDICTS = {"accepted", "rejected"}

ALLOWED_DISAGREEMENT_TYPES = {"D0", "D1", "D2", "D3", "D4", "D5"}

ALLOWED_DISAGREEMENT_LABELS = {
    "no_meaningful_disagreement",
    "precision_disagreement",
    "structural_emphasis_disagreement",
    "boundary_disagreement",
    "verdict_disagreement",
    "target_disagreement",
}

TYPE_TO_LABEL = {
    "D0": "no_meaningful_disagreement",
    "D1": "precision_disagreement",
    "D2": "structural_emphasis_disagreement",
    "D3": "boundary_disagreement",
    "D4": "verdict_disagreement",
    "D5": "target_disagreement",
}


def is_non_empty_string(value):
    return isinstance(value, str) and value.strip() != ""


def validate_record(record, line_number, seen_comparison_ids):
    errors = []

    if not isinstance(record, dict):
        return [f"line {line_number}: record is not a JSON object"]

    for field in REQUIRED_STRING_FIELDS:
        if field not in record:
            errors.append(f"line {line_number}: missing field '{field}'")
        elif not is_non_empty_string(record[field]):
            errors.append(f"line {line_number}: field '{field}' is empty or not a string")

    for field in REQUIRED_BINARY_FIELDS:
        if field not in record:
            errors.append(f"line {line_number}: missing field '{field}'")
        elif record[field] not in (0, 1):
            errors.append(f"line {line_number}: field '{field}' must be 0 or 1")

    if "gain_gap" not in record:
        errors.append(f"line {line_number}: missing field 'gain_gap'")
    elif not isinstance(record["gain_gap"], int):
        errors.append(f"line {line_number}: field 'gain_gap' must be an integer")
    elif record["gain_gap"] < 0:
        errors.append(f"line {line_number}: field 'gain_gap' must be >= 0")

    comparison_id = record.get("comparison_id")
    if is_non_empty_string(comparison_id):
        if comparison_id in seen_comparison_ids:
            errors.append(f"line {line_number}: duplicate comparison_id '{comparison_id}'")
        else:
            seen_comparison_ids.add(comparison_id)

    for field in ("annotation_a_strength", "annotation_b_strength"):
        value = record.get(field)
        if is_non_empty_string(value) and value not in ALLOWED_STRENGTHS:
            errors.append(
                f"line {line_number}: field '{field}' must be one of {sorted(ALLOWED_STRENGTHS)}"
            )

    for field in ("annotation_a_verdict", "annotation_b_verdict"):
        value = record.get(field)
        if is_non_empty_string(value) and value not in ALLOWED_VERDICTS:
            errors.append(
                f"line {line_number}: field '{field}' must be one of {sorted(ALLOWED_VERDICTS)}"
            )

    disagreement_type = record.get("disagreement_type")
    disagreement_label = record.get("disagreement_label")

    if is_non_empty_string(disagreement_type) and disagreement_type not in ALLOWED_DISAGREEMENT_TYPES:
        errors.append(
            f"line {line_number}: disagreement_type must be one of {sorted(ALLOWED_DISAGREEMENT_TYPES)}"
        )

    if is_non_empty_string(disagreement_label) and disagreement_label not in ALLOWED_DISAGREEMENT_LABELS:
        errors.append(
            f"line {line_number}: disagreement_label must be one of {sorted(ALLOWED_DISAGREEMENT_LABELS)}"
        )

    if (
        is_non_empty_string(disagreement_type)
        and disagreement_type in TYPE_TO_LABEL
        and is_non_empty_string(disagreement_label)
        and disagreement_label != TYPE_TO_LABEL[disagreement_type]
    ):
        errors.append(
            f"line {line_number}: disagreement_label mismatch "
            f"(found '{disagreement_label}', expected '{TYPE_TO_LABEL[disagreement_type]}')"
        )

    a_strength = record.get("annotation_a_strength")
    b_strength = record.get("annotation_b_strength")
    a_verdict = record.get("annotation_a_verdict")
    b_verdict = record.get("annotation_b_verdict")

    if is_non_empty_string(a_strength) and is_non_empty_string(a_verdict):
        expected = "rejected" if a_strength == "rejected" else "accepted"
        if a_verdict != expected:
            errors.append(
                f"line {line_number}: annotation_a_verdict mismatch "
                f"(found '{a_verdict}', expected '{expected}')"
            )

    if is_non_empty_string(b_strength) and is_non_empty_string(b_verdict):
        expected = "rejected" if b_strength == "rejected" else "accepted"
        if b_verdict != expected:
            errors.append(
                f"line {line_number}: annotation_b_verdict mismatch "
                f"(found '{b_verdict}', expected '{expected}')"
            )

    target_preserved = record.get("target_preserved")
    verdict_split = record.get("verdict_split")
    gain_gap = record.get("gain_gap")

    if (
        target_preserved in (0, 1)
        and verdict_split in (0, 1)
        and isinstance(gain_gap, int)
        and is_non_empty_string(disagreement_type)
    ):
        if disagreement_type == "D4" and verdict_split != 1:
            errors.append(f"line {line_number}: D4 requires verdict_split = 1")

        if disagreement_type == "D5" and target_preserved != 0:
            errors.append(f"line {line_number}: D5 requires target_preserved = 0")

        if disagreement_type in {"D0", "D1", "D2", "D3"} and target_preserved != 1:
            errors.append(
                f"line {line_number}: {disagreement_type} requires target_preserved = 1"
            )

        if disagreement_type in {"D0", "D1", "D2", "D3"} and verdict_split != 0:
            errors.append(
                f"line {line_number}: {disagreement_type} requires verdict_split = 0"
            )

        if disagreement_type == "D0" and gain_gap != 0:
            errors.append(f"line {line_number}: D0 requires gain_gap = 0")

        if disagreement_type == "D1" and gain_gap <= 0:
            errors.append(f"line {line_number}: D1 requires gain_gap > 0")

    return errors


def validate_dataset(dataset_path):
    if not dataset_path.exists():
        print(f"ERROR: dataset not found at {dataset_path}")
        return 1

    total = 0
    valid = 0
    invalid = 0
    all_errors = []
    seen_comparison_ids = set()

    with dataset_path.open("r", encoding="utf-8") as f:
        for line_number, raw_line in enumerate(f, start=1):
            line = raw_line.strip()

            if not line:
                all_errors.append(f"line {line_number}: empty line")
                invalid += 1
                total += 1
                continue

            try:
                record = json.loads(line)
            except json.JSONDecodeError as e:
                all_errors.append(f"line {line_number}: invalid JSON - {e}")
                invalid += 1
                total += 1
                continue

            errors = validate_record(record, line_number, seen_comparison_ids)
            total += 1

            if errors:
                invalid += 1
                all_errors.extend(errors)
            else:
                valid += 1

    print("O1 disagreement labels validation")
    print("--------------------------------")
    print(f"dataset: {dataset_path}")
    print(f"total records: {total}")
    print(f"valid records: {valid}")
    print(f"invalid records: {invalid}")

    if all_errors:
        print("\nErrors:")
        for error in all_errors:
            print(f"- {error}")
        return 1

    print("\nNo validation errors found.")
    return 0


def main():
    dataset_arg = sys.argv[1] if len(sys.argv) > 1 else str(DEFAULT_DATASET_PATH)
    dataset_path = Path(dataset_arg)
    raise SystemExit(validate_dataset(dataset_path))


if __name__ == "__main__":
    main()