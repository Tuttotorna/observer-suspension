import json
from collections import Counter
from pathlib import Path

DATASET_PATH = Path("data/o1_miniset.jsonl")


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


def main():
    if not DATASET_PATH.exists():
        print(f"ERROR: dataset not found at {DATASET_PATH}")
        return

    records = load_records(DATASET_PATH)

    if not records:
        print("Dataset is empty.")
        return

    domain_counts = Counter(record["domain"] for record in records)

    print("O1 dataset inspection")
    print("---------------------")
    print(f"dataset: {DATASET_PATH}")
    print(f"total records: {len(records)}")
    print()

    print("Records by domain:")
    for domain, count in sorted(domain_counts.items()):
        print(f"- {domain}: {count}")

    print()
    print("Sample records:")
    print()

    for record in records[:5]:
        print(f"[{record['id']}] {record['domain']}")
        print(f"  standard: {record['standard_formulation']}")
        print(f"  reformulation: {record['decentered_reformulation']}")
        print()

    unique_ids = {record["id"] for record in records}
    if len(unique_ids) != len(records):
        print("WARNING: duplicate record ids detected.")
    else:
        print("All record ids are unique.")


if __name__ == "__main__":
    main()