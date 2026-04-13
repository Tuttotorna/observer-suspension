import json
from pathlib import Path

DATASET_PATH = Path("data/o1_miniset.jsonl")

REQUIRED_STRING_FIELDS = [
    "id",
    "domain",
    "standard_formulation",
    "hidden_observer_assumption",
    "structural_distortion",
    "decentered_reformulation",
    "emergent_structure",
    "verdict",
]

REQUIRED_BINARY_FIELDS = ["c1", "c2", "c3", "c4"]


def is_non_empty_string(value):
    return isinstance(value, str) and value.strip() != ""


def validate_record(record, line_number, seen_ids):
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

    if "id" in record and is_non_empty_string(record["id"]):
        record_id = record["id"]
        if record_id in seen_ids:
            errors.append(f"line {line_number}: duplicate id '{record_id}'")
        else:
            seen_ids.add(record_id)

    binary_fields_present = all(field in record and record[field] in (0, 1) for field in REQUIRED_BINARY_FIELDS)
    gain_present = "o1_gain" in record and isinstance(record["o1_gain"], int)

    if binary_fields_present and gain_present:
        expected_gain = sum(record[field] for field in REQUIRED_BINARY_FIELDS)
        if record["o1_gain"] != expected_gain:
            errors.append(
                f"line {line_number}: o1_gain mismatch "
                f"(found {record['o1_gain']}, expected {expected_gain})"
            )

    if "verdict" in record and is_non_empty_string(record["verdict"]) and binary_fields_present and gain_present:
        verdict = record["verdict"]
        c4 = record["c4"]
        gain = record["o1_gain"]

        if verdict not in ("accepted", "rejected"):
            errors.append(
                f"line {line_number}: verdict must be 'accepted' or 'rejected'"
            )
        else:
            expected_verdict = "accepted" if (c4 == 1 and gain >= 3) else "rejected"
            if verdict != expected_verdict:
                errors.append(
                    f"line {line_number}: verdict mismatch "
                    f"(found '{verdict}', expected '{expected_verdict}')"
                )

    return errors


def main():
    if not DATASET_PATH.exists():
        print(f"ERROR: dataset not found at {DATASET_PATH}")
        return

    total = 0
    valid = 0
    invalid = 0
    all_errors = []
    seen_ids = set()

    with DATASET_PATH.open("r", encoding="utf-8") as f:
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

            errors = validate_record(record, line_number, seen_ids)
            total += 1

            if errors:
                invalid += 1
                all_errors.extend(errors)
            else:
                valid += 1

    print("O1 dataset validation")
    print("---------------------")
    print(f"dataset: {DATASET_PATH}")
    print(f"total records: {total}")
    print(f"valid records: {valid}")
    print(f"invalid records: {invalid}")

    if all_errors:
        print("\nErrors:")
        for error in all_errors:
            print(f"- {error}")
    else:
        print("\nNo validation errors found.")


if __name__ == "__main__":
    main()