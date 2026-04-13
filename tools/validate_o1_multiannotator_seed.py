import json
import sys
from collections import defaultdict
from pathlib import Path

DEFAULT_DATASET_PATH = Path("data/o1_multiannotator_seed.jsonl")

REQUIRED_STRING_FIELDS = [
    "record_id",
    "input_id",
    "annotator_id",
    "domain",
    "input",
    "hidden_observer_assumption",
    "structural_distortion",
    "decentered_reformulation",
    "emergent_structure",
    "verdict",
]

REQUIRED_BINARY_FIELDS = ["c1", "c2", "c3", "c4"]

ALLOWED_VERDICTS = {"accepted", "rejected"}


def is_non_empty_string(value):
    return isinstance(value, str) and value.strip() != ""


def validate_record(record, line_number, seen_record_ids):
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

    record_id = record.get("record_id")
    if is_non_empty_string(record_id):
        if record_id in seen_record_ids:
            errors.append(f"line {line_number}: duplicate record_id '{record_id}'")
        else:
            seen_record_ids.add(record_id)

    verdict = record.get("verdict")
    if is_non_empty_string(verdict) and verdict not in ALLOWED_VERDICTS:
        errors.append(f"line {line_number}: verdict must be one of {sorted(ALLOWED_VERDICTS)}")

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

    return errors


def validate_groups(records):
    errors = []
    grouped = defaultdict(list)

    for record in records:
        grouped[record["input_id"]].append(record)

    for input_id, group in sorted(grouped.items()):
        if len(group) != 2:
            errors.append(f"group '{input_id}': expected exactly 2 records, found {len(group)}")
            continue

        annotators = {r["annotator_id"] for r in group}
        if len(annotators) != 2:
            errors.append(f"group '{input_id}': expected 2 distinct annotators, found {len(annotators)}")

        domains = {r["domain"] for r in group}
        if len(domains) != 1:
            errors.append(f"group '{input_id}': domain mismatch across annotators")

        inputs = {r["input"] for r in group}
        if len(inputs) != 1:
            errors.append(f"group '{input_id}': input text mismatch across annotators")

    return errors


def validate_dataset(dataset_path):
    if not dataset_path.exists():
        print(f"ERROR: dataset not found at {dataset_path}")
        return 1

    total = 0
    valid = 0
    invalid = 0
    all_errors = []
    seen_record_ids = set()
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

            errors = validate_record(record, line_number, seen_record_ids)
            total += 1

            if errors:
                invalid += 1
                all_errors.extend(errors)
            else:
                valid += 1
                parsed_records.append(record)

    group_errors = validate_groups(parsed_records)
    all_errors.extend(group_errors)

    if group_errors:
        valid = max(0, valid - len(group_errors))
        invalid += len(group_errors)

    print("O1 multi-annotator seed validation")
    print("----------------------------------")
    print(f"dataset: {dataset_path}")
    print(f"total records: {total}")
    print(f"valid records: {valid}")
    print(f"invalid records: {invalid}")
    print(f"total input groups: {len({r['input_id'] for r in parsed_records})}")

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