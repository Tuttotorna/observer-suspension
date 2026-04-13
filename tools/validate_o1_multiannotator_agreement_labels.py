import json
import sys
from pathlib import Path

DEFAULT_DATASET_PATH = Path("data/o1_multiannotator_agreement_labels.jsonl")

REQUIRED_STRING_FIELDS = [
    "agreement_id",
    "input_id",
    "domain",
    "input",
    "annotator_a_id",
    "annotator_b_id",
    "annotator_a_verdict",
    "annotator_b_verdict",
    "agreement_type",
    "agreement_label",
    "notes",
]

REQUIRED_INT_FIELDS = [
    "annotator_a_gain",
    "annotator_b_gain",
    "gain_gap",
]

ALLOWED_VERDICTS = {"accepted", "rejected"}
ALLOWED_AGREEMENT_TYPES = {"A0", "A1", "A2", "A3", "A4"}
ALLOWED_AGREEMENT_LABELS = {
    "strong_convergence",
    "acceptable_convergence",
    "weak_convergence",
    "verdict_split",
    "rejected_convergence",
}

TYPE_TO_LABEL = {
    "A0": "strong_convergence",
    "A1": "acceptable_convergence",
    "A2": "weak_convergence",
    "A3": "verdict_split",
    "A4": "rejected_convergence",
}


def is_non_empty_string(value):
    return isinstance(value, str) and value.strip() != ""


def expected_agreement_type(a_verdict, b_verdict, gain_gap):
    verdict_pattern = tuple(sorted([a_verdict, b_verdict]))

    if verdict_pattern == ("accepted", "rejected"):
        return "A3"
    if verdict_pattern == ("rejected", "rejected"):
        return "A4"
    if verdict_pattern == ("accepted", "accepted"):
        if gain_gap == 0:
            return "A0"
        if gain_gap == 1:
            return "A1"
        return "A2"
    return None


def validate_record(record, line_number, seen_agreement_ids):
    errors = []

    if not isinstance(record, dict):
        return [f"line {line_number}: record is not a JSON object"]

    for field in REQUIRED_STRING_FIELDS:
        if field not in record:
            errors.append(f"line {line_number}: missing field '{field}'")
        elif not is_non_empty_string(record[field]):
            errors.append(f"line {line_number}: field '{field}' is empty or not a string")

    for field in REQUIRED_INT_FIELDS:
        if field not in record:
            errors.append(f"line {line_number}: missing field '{field}'")
        elif not isinstance(record[field], int):
            errors.append(f"line {line_number}: field '{field}' must be an integer")

    agreement_id = record.get("agreement_id")
    if is_non_empty_string(agreement_id):
        if agreement_id in seen_agreement_ids:
            errors.append(f"line {line_number}: duplicate agreement_id '{agreement_id}'")
        else:
            seen_agreement_ids.add(agreement_id)

    for field in ("annotator_a_verdict", "annotator_b_verdict"):
        value = record.get(field)
        if is_non_empty_string(value) and value not in ALLOWED_VERDICTS:
            errors.append(
                f"line {line_number}: field '{field}' must be one of {sorted(ALLOWED_VERDICTS)}"
            )

    agreement_type = record.get("agreement_type")
    if is_non_empty_string(agreement_type) and agreement_type not in ALLOWED_AGREEMENT_TYPES:
        errors.append(
            f"line {line_number}: agreement_type must be one of {sorted(ALLOWED_AGREEMENT_TYPES)}"
        )

    agreement_label = record.get("agreement_label")
    if is_non_empty_string(agreement_label) and agreement_label not in ALLOWED_AGREEMENT_LABELS:
        errors.append(
            f"line {line_number}: agreement_label must be one of {sorted(ALLOWED_AGREEMENT_LABELS)}"
        )

    if (
        is_non_empty_string(agreement_type)
        and agreement_type in TYPE_TO_LABEL
        and is_non_empty_string(agreement_label)
        and agreement_label != TYPE_TO_LABEL[agreement_type]
    ):
        errors.append(
            f"line {line_number}: agreement_label mismatch "
            f"(found '{agreement_label}', expected '{TYPE_TO_LABEL[agreement_type]}')"
        )

    a_gain = record.get("annotator_a_gain")
    b_gain = record.get("annotator_b_gain")
    gain_gap = record.get("gain_gap")

    if isinstance(a_gain, int) and isinstance(b_gain, int) and isinstance(gain_gap, int):
        expected_gap = abs(a_gain - b_gain)
        if gain_gap != expected_gap:
            errors.append(
                f"line {line_number}: gain_gap mismatch "
                f"(found {gain_gap}, expected {expected_gap})"
            )
        if gain_gap < 0:
            errors.append(f"line {line_number}: gain_gap must be >= 0")

    a_verdict = record.get("annotator_a_verdict")
    b_verdict = record.get("annotator_b_verdict")

    if (
        is_non_empty_string(a_verdict)
        and is_non_empty_string(b_verdict)
        and isinstance(gain_gap, int)
        and is_non_empty_string(agreement_type)
    ):
        expected_type = expected_agreement_type(a_verdict, b_verdict, gain_gap)
        if expected_type is not None and agreement_type != expected_type:
            errors.append(
                f"line {line_number}: agreement_type mismatch "
                f"(found '{agreement_type}', expected '{expected_type}')"
            )

    return errors


def validate_dataset(dataset_path):
    if not dataset_path.exists():
        print(f"ERROR: dataset not found at {dataset_path}")
        return 1

    total = 0
    valid = 0
    invalid = 0
    all_errors = []
    seen_agreement_ids = set()

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

            errors = validate_record(record, line_number, seen_agreement_ids)
            total += 1

            if errors:
                invalid += 1
                all_errors.extend(errors)
            else:
                valid += 1

    print("O1 multi-annotator agreement labels validation")
    print("----------------------------------------------")
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