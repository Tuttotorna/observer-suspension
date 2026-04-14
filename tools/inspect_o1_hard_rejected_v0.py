import json
import sys
from collections import Counter
from pathlib import Path

DEFAULT_DATASET_PATH = Path("data/o1_hard_rejected_v0.jsonl")


def load_records(path: Path):
    records = []
    with path.open("r", encoding="utf-8") as f:
        for line_number, raw_line in enumerate(f, start=1):
            line = raw_line.strip()
            if not line:
                continue
            try:
                record = json.loads(line)
                records.append(record)
            except json.JSONDecodeError as e:
                raise ValueError(f"Invalid JSON at line {line_number}: {e}") from e
    return records


def inspect_dataset(dataset_path: Path):
    if not dataset_path.exists():
        print(f"ERROR: dataset not found at {dataset_path}")
        return 1

    records = load_records(dataset_path)

    if not records:
        print("Dataset is empty.")
        return 1

    domain_counts = Counter()
    verdict_counts = Counter()
    gains = []

    for record in records:
        domain_counts[record.get("domain", "unknown")] += 1
        verdict_counts[record.get("verdict", "unknown")] += 1
        gain = record.get("o1_gain")
        if isinstance(gain, int):
            gains.append(gain)

    average_gain = sum(gains) / len(gains) if gains else 0.0
    min_gain = min(gains) if gains else 0
    max_gain = max(gains) if gains else 0

    print("O1 hard rejected v0 inspection")
    print("------------------------------")
    print(f"dataset: {dataset_path}")
    print(f"total records: {len(records)}")
    print(f"average o1_gain: {average_gain:.2f}")
    print(f"min o1_gain: {min_gain}")
    print(f"max o1_gain: {max_gain}")
    print()

    print("Records by verdict:")
    for verdict, count in sorted(verdict_counts.items()):
        print(f"- {verdict}: {count}")

    print()
    print("Records by domain:")
    for domain, count in sorted(domain_counts.items()):
        print(f"- {domain}: {count}")

    print()
    print("Sample rejected hard cases:")
    print()

    for record in records:
        print(f"[{record.get('case_id', 'unknown')}]")
        print(f"  input_id: {record.get('input_id', '')}")
        print(f"  domain: {record.get('domain', '')}")
        print(f"  standard_formulation: {record.get('standard_formulation', '')}")
        print(f"  decentered_reformulation: {record.get('decentered_reformulation', '')}")
        print(f"  emergent_structure: {record.get('emergent_structure', '')}")
        print(f"  o1_gain: {record.get('o1_gain', '')}")
        print(f"  verdict: {record.get('verdict', '')}")
        print()

    unique_case_ids = {record.get("case_id") for record in records}
    if len(unique_case_ids) != len(records):
        print("WARNING: duplicate case ids detected.")
    else:
        print("All case ids are unique.")

    return 0


def main():
    dataset_arg = sys.argv[1] if len(sys.argv) > 1 else str(DEFAULT_DATASET_PATH)
    dataset_path = Path(dataset_arg)
    raise SystemExit(inspect_dataset(dataset_path))


if __name__ == "__main__":
    main()