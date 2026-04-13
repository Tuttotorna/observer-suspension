import json
import sys
from collections import Counter
from pathlib import Path

DEFAULT_DATASET_PATH = Path("data/o1_disagreement_labels.jsonl")


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

    type_counts = Counter()
    label_counts = Counter()
    domain_counts = Counter()
    target_preserved_counts = Counter()
    verdict_split_counts = Counter()
    gain_gaps = []

    for record in records:
        disagreement_type = record.get("disagreement_type", "unknown")
        disagreement_label = record.get("disagreement_label", "unknown")
        domain = record.get("domain", "unknown")
        target_preserved = record.get("target_preserved", "unknown")
        verdict_split = record.get("verdict_split", "unknown")
        gain_gap = record.get("gain_gap")

        type_counts[disagreement_type] += 1
        label_counts[disagreement_label] += 1
        domain_counts[domain] += 1
        target_preserved_counts[target_preserved] += 1
        verdict_split_counts[verdict_split] += 1

        if isinstance(gain_gap, int):
            gain_gaps.append(gain_gap)

    average_gain_gap = sum(gain_gaps) / len(gain_gaps) if gain_gaps else 0.0
    max_gain_gap = max(gain_gaps) if gain_gaps else 0
    min_gain_gap = min(gain_gaps) if gain_gaps else 0

    print("O1 disagreement labels inspection")
    print("--------------------------------")
    print(f"dataset: {dataset_path}")
    print(f"total records: {len(records)}")
    print(f"average gain_gap: {average_gain_gap:.2f}")
    print(f"min gain_gap: {min_gain_gap}")
    print(f"max gain_gap: {max_gain_gap}")
    print()

    print("Records by disagreement type:")
    for disagreement_type, count in sorted(type_counts.items()):
        print(f"- {disagreement_type}: {count}")

    print()
    print("Records by disagreement label:")
    for disagreement_label, count in sorted(label_counts.items()):
        print(f"- {disagreement_label}: {count}")

    print()
    print("Records by domain:")
    for domain, count in sorted(domain_counts.items()):
        print(f"- {domain}: {count}")

    print()
    print("Records by target_preserved:")
    for value, count in sorted(target_preserved_counts.items()):
        print(f"- {value}: {count}")

    print()
    print("Records by verdict_split:")
    for value, count in sorted(verdict_split_counts.items()):
        print(f"- {value}: {count}")

    print()
    print("Sample disagreement records:")
    print()

    for record in records[:4]:
        print(f"[{record.get('comparison_id', 'unknown')}]")
        print(f"  pair_id: {record.get('pair_id', '')}")
        print(f"  input: {record.get('input', '')}")
        print(f"  disagreement_type: {record.get('disagreement_type', '')}")
        print(f"  disagreement_label: {record.get('disagreement_label', '')}")
        print(f"  annotation_a_strength: {record.get('annotation_a_strength', '')}")
        print(f"  annotation_b_strength: {record.get('annotation_b_strength', '')}")
        print(f"  gain_gap: {record.get('gain_gap', '')}")
        print(f"  notes: {record.get('notes', '')}")
        print()

    unique_comparison_ids = {record.get("comparison_id") for record in records}
    if len(unique_comparison_ids) != len(records):
        print("WARNING: duplicate comparison ids detected.")
    else:
        print("All comparison ids are unique.")

    return 0


def main():
    dataset_arg = sys.argv[1] if len(sys.argv) > 1 else str(DEFAULT_DATASET_PATH)
    dataset_path = Path(dataset_arg)
    raise SystemExit(inspect_dataset(dataset_path))


if __name__ == "__main__":
    main()