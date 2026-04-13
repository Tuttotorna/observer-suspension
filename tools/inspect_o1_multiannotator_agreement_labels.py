import json
import sys
from collections import Counter
from pathlib import Path

DEFAULT_DATASET_PATH = Path("data/o1_multiannotator_agreement_labels.jsonl")


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

    agreement_type_counts = Counter()
    agreement_label_counts = Counter()
    domain_counts = Counter()
    verdict_pattern_counts = Counter()
    gain_gaps = []

    for record in records:
        agreement_type = record.get("agreement_type", "unknown")
        agreement_label = record.get("agreement_label", "unknown")
        domain = record.get("domain", "unknown")
        a_verdict = record.get("annotator_a_verdict", "unknown")
        b_verdict = record.get("annotator_b_verdict", "unknown")
        gain_gap = record.get("gain_gap")

        agreement_type_counts[agreement_type] += 1
        agreement_label_counts[agreement_label] += 1
        domain_counts[domain] += 1
        verdict_pattern_counts[tuple(sorted([a_verdict, b_verdict]))] += 1

        if isinstance(gain_gap, int):
            gain_gaps.append(gain_gap)

    average_gain_gap = sum(gain_gaps) / len(gain_gaps) if gain_gaps else 0.0
    min_gain_gap = min(gain_gaps) if gain_gaps else 0
    max_gain_gap = max(gain_gaps) if gain_gaps else 0

    print("O1 multi-annotator agreement labels inspection")
    print("------------------------------------------------")
    print(f"dataset: {dataset_path}")
    print(f"total records: {len(records)}")
    print(f"average gain_gap: {average_gain_gap:.2f}")
    print(f"min gain_gap: {min_gain_gap}")
    print(f"max gain_gap: {max_gain_gap}")
    print()

    print("Records by agreement type:")
    for agreement_type, count in sorted(agreement_type_counts.items()):
        print(f"- {agreement_type}: {count}")

    print()
    print("Records by agreement label:")
    for agreement_label, count in sorted(agreement_label_counts.items()):
        print(f"- {agreement_label}: {count}")

    print()
    print("Records by domain:")
    for domain, count in sorted(domain_counts.items()):
        print(f"- {domain}: {count}")

    print()
    print("Records by verdict pattern:")
    for verdict_pattern, count in sorted(verdict_pattern_counts.items()):
        print(f"- {verdict_pattern}: {count}")

    print()
    print("Sample agreement records:")
    print()

    for record in records[:4]:
        print(f"[{record.get('agreement_id', 'unknown')}]")
        print(f"  input_id: {record.get('input_id', '')}")
        print(f"  domain: {record.get('domain', '')}")
        print(f"  input: {record.get('input', '')}")
        print(f"  agreement_type: {record.get('agreement_type', '')}")
        print(f"  agreement_label: {record.get('agreement_label', '')}")
        print(f"  annotator_a_verdict: {record.get('annotator_a_verdict', '')}")
        print(f"  annotator_b_verdict: {record.get('annotator_b_verdict', '')}")
        print(f"  annotator_a_gain: {record.get('annotator_a_gain', '')}")
        print(f"  annotator_b_gain: {record.get('annotator_b_gain', '')}")
        print(f"  gain_gap: {record.get('gain_gap', '')}")
        print(f"  notes: {record.get('notes', '')}")
        print()

    unique_agreement_ids = {record.get("agreement_id") for record in records}
    if len(unique_agreement_ids) != len(records):
        print("WARNING: duplicate agreement ids detected.")
    else:
        print("All agreement ids are unique.")

    return 0


def main():
    dataset_arg = sys.argv[1] if len(sys.argv) > 1 else str(DEFAULT_DATASET_PATH)
    dataset_path = Path(dataset_arg)
    raise SystemExit(inspect_dataset(dataset_path))


if __name__ == "__main__":
    main()