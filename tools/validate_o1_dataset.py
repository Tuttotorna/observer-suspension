import json
from pathlib import Path

REQUIRED_FIELDS = [
    "id",
    "domain",
    "standard_formulation",
    "hidden_observer_assumption",
    "structural_distortion",
    "decentered_reformulation",
    "emergent_structure",
]


def is_non_empty_string(value):
    return isinstance(value, str) and value.strip() != ""


def validate_record(record, line_number):
    errors = []

    if not isinstance(record, dict):
        return [f"line {line_number}: record is not a JSON object"]

    for field in REQUIRED_FIELDS:
        if field not in record:
            errors.append(f"line {line_number}: missing field '{field}'")
        elif not is_non_empty_string(record[field]):
            errors.append(f"line {line_number}: field '{field}' is empty or not a string")

    return errors


def main():
    dataset_path = Path("data/o1_miniset.jsonl")

    if not dataset_path.exists():
        print(f"ERROR: dataset not found at {dataset_path}")
        return

    total = 0
    valid = 0
    invalid = 0
    all_errors = []

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

            errors = validate_record(record, line_number)
            total += 1

            if errors:
                invalid += 1
                all_errors.extend(errors)
            else:
                valid += 1

    print("O1 dataset validation")
    print("---------------------")
    print(f"dataset: {dataset_path}")
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