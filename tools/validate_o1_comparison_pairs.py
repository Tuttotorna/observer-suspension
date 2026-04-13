import json
import sys
from collections import defaultdict
from pathlib import Path

DEFAULT_DATASET_PATH = Path("data/o1_comparison_pairs.jsonl")

REQUIRED_STRING_FIELDS = [
    "pair_id",
    "input_id",
    "domain",
    "input",
    "annotation_id",
    "variant",
    "strength",
    "hidden_observer_assumption",
    "structural_distortion",
    "decentered_reformulation",
    "emergent_structure",
    "verdict",
]

REQUIRED_BINARY_FIELDS = ["c1", "c2", "c3", "c4"]

ALLOWED_VARIANTS = {"A", "B"}
ALLOWED_STRENGTHS = {
    "strong_acceptable",
    "weak_acceptable",
    "borderline_acceptable",
    "rejected",
}
ALLOWED_VERDICTS = {"accepted", "rejected"}


def is_non_empty_string(value):
    return isinstance(value, str) and value.strip() != ""


def validate_record(record, line_number, seen_annotation_ids):
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

    if "o1_gain" not in record:
        errors.append(f"line {line_number}: missing field 'o1_gain'")
    elif not isinstance(record["o1_gain"], int):
        errors.append(f"line {line_number}: field 'o1_gain' must be an integer")

    annotation_id = record.get("annotation_id")
    if is_non_empty_string(annotation_id):
        if annotation_id in seen_annotation_ids:
            errors.append(f"line {line_number}: duplicate annotation_id '{annotation_id}'")
        else:
            seen_annotation_ids.add(annotation_id)

    variant = record.get("variant")
    if is_non_empty_string(variant) and variant not in ALLOWED_VARIANTS:
        errors.append(f"line {line_number}: variant must be one of {sorted(ALLOWED_VARIANTS)}")

    strength = record.get("strength")
    if is_non_empty_string(strength) and strength not in ALLOWED_STRENGTHS:
        errors.append(f"line {line_number}: strength must be one of {sorted(ALLOWED_STRENGTHS)}")

    verdict = record.get("verdict")
    if is_non_empty_string(verdict) and verdict not in ALLOWED_VERDICTS:
        errors.append(f"line {line_number}: verdict must be 'accepted' or 'rejected'")

    binary_fields_present = all(field in record and record[field] in (0, 1) for field in REQUIRED_BINARY_FIELDS)
    gain_present = "o1_gain" in record and isinstance(record["o1_gain"], int)

    if binary_fields_present and gain_present:
        expected_gain = sum(record[field] for field in REQUIRED_BINARY_FIELDS)
        if record["o1_gain"] != expected_gain:
            errors.append(
                f"line {line_number}: o1_gain mismatch "
                f"(found {record['o1_gain']}, expected {expected_gain})"
            )

    if binary_fields_present and gain_present and is_non_empty_string(verdict):
        expected_verdict = "accepted" if (record["c4"] == 1 and record["o1_gain"] >= 3) else "rejected"
        if verdict != expected_verdict:
            errors.append(
                f"line {line_number}: verdict mismatch "
                f"(found '{verdict}', expected '{expected_verdict}')"
            )

    if is_non_empty_string(strength) and is_non_empty_string(verdict):
        if strength == "rejected" and verdict != "rejected":
            errors.append(f"line {line_number}: rejected strength must have verdict 'rejected'")
        if strength in {"strong_acceptable", "weak_acceptable", "borderline_acceptable"} and verdict != "accepted":
            errors.append(f"line {line_number}: acceptable strength must have verdict 'accepted'")

    return errors


def validate_pairs(records):
    errors = []
    pairs = defaultdict(list)

    for record in records:
        pairs[record["pair_id"]].append(record)

    for pair_id, pair_records in sorted(pairs.items()):
        if len(pair_records) != 2:
            errors.append(f"pair '{pair_id}': expected exactly 2 records, found {len(pair_records)}")
            continue

        variants = {r["variant"] for r in pair_records}
        if variants != {"A", "B"}:
            errors.append(f"pair '{pair_id}': expected variants A and B, found {sorted(variants)}")

        input_ids = {r["input_id"] for r in pair_records}
        if len(input_ids) != 1:
            errors.append(f"pair '{pair_id}': input_id mismatch across pair")

        inputs = {r["input"] for r in pair_records}
        if len(inputs) != 1:
            errors.append(f"pair '{pair_id}': input text mismatch across pair")

        domains = {r["domain"] for r in pair_records}
        if len(domains) != 1:
            errors.append(f"pair '{pair_id}': domain mismatch across pair")

    return errors


def validate_dataset(dataset_path):
    if not dataset_path.exists():
        print(f"ERROR: dataset not found at {dataset_path}")
        return 1

    total = 0
    valid = 0
    invalid = 0
    all_errors = []
    seen_annotation_ids = set()
    parsed_records = []

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

            errors = validate_record(record, line_number, seen_annotation_ids)
            total += 1

            if errors:
                invalid += 1
                all_errors.extend(errors)
            else:
                valid += 1
                parsed_records.append(record)

    pair_errors = validate_pairs(parsed_records)
    all_errors.extend(pair_errors)

    if pair_errors:
        valid = max(0, valid - len(pair_errors))
        invalid += len(pair_errors)

    print("O1 comparison pairs validation")
    print("------------------------------")
    print(f"dataset: {dataset_path}")
    print(f"total records: {total}")
    print(f"valid records: {valid}")
    print(f"invalid records: {invalid}")
    print(f"total pairs: {len({r['pair_id'] for r in parsed_records})}")

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