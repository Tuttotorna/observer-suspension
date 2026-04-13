import json
import sys
from collections import Counter, defaultdict
from pathlib import Path

DEFAULT_DATASET_PATH = Path("data/o1_multiannotator_seed.jsonl")


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

    annotator_counts = Counter()
    domain_counts = Counter()
    verdict_counts = Counter()
    gains = []
    grouped = defaultdict(list)

    for record in records:
        annotator = record.get("annotator_id", "unknown")
        domain = record.get("domain", "unknown")
        verdict = record.get("verdict", "unknown")
        input_id = record.get("input_id", "unknown")
        gain = record.get("o1_gain")

        annotator_counts[annotator] += 1
        domain_counts[domain] += 1
        verdict_counts[verdict] += 1
        grouped[input_id].append(record)

        if isinstance(gain, int):
            gains.append(gain)

    average_gain = sum(gains) / len(gains) if gains else 0.0

    group_sizes = Counter(len(group) for group in grouped.values())
    group_domain_counts = Counter()
    verdict_patterns = Counter()
    gain_gaps = []

    for input_id, group in grouped.items():
        group_domain = group[0].get("domain", "unknown")
        group_domain_counts[group_domain] += 1

        group_verdicts = tuple(sorted(record.get("verdict", "unknown") for record in group))
        verdict_patterns[group_verdicts] += 1

        group_gains = [record.get("o1_gain") for record in group if isinstance(record.get("o1_gain"), int)]
        if len(group_gains) == 2:
            gain_gaps.append(abs(group_gains[0] - group_gains[1]))

    average_gain_gap = sum(gain_gaps) / len(gain_gaps) if gain_gaps else 0.0
    min_gain_gap = min(gain_gaps) if gain_gaps else 0
    max_gain_gap = max(gain_gaps) if gain_gaps else 0

    print("O1 multi-annotator seed inspection")
    print("----------------------------------")
    print(f"dataset: {dataset_path}")
    print(f"total records: {len(records)}")
    print(f"total input groups: {len(grouped)}")
    print(f"average o1_gain: {average_gain:.2f}")
    print(f"average gain gap per group: {average_gain_gap:.2f}")
    print(f"min gain gap: {min_gain_gap}")
    print(f"max gain gap: {max_gain_gap}")
    print()

    print("Records by annotator:")
    for annotator, count in sorted(annotator_counts.items()):
        print(f"- {annotator}: {count}")

    print()
    print("Records by domain:")
    for domain, count in sorted(domain_counts.items()):
        print(f"- {domain}: {count}")

    print()
    print("Records by verdict:")
    for verdict, count in sorted(verdict_counts.items()):
        print(f"- {verdict}: {count}")

    print()
    print("Input groups by size:")
    for size, count in sorted(group_sizes.items()):
        print(f"- size {size}: {count}")

    print()
    print("Input groups by domain:")
    for domain, count in sorted(group_domain_counts.items()):
        print(f"- {domain}: {count}")

    print()
    print("Verdict patterns by group:")
    for pattern, count in sorted(verdict_patterns.items()):
        print(f"- {pattern}: {count}")

    print()
    print("Sample input groups:")
    print()

    for input_id in sorted(grouped)[:4]:
        print(f"[{input_id}]")
        for record in sorted(grouped[input_id], key=lambda r: r.get("annotator_id", "")):
            print(
                f"  annotator={record.get('annotator_id', 'unknown')}, "
                f"domain={record.get('domain', 'unknown')}, "
                f"verdict={record.get('verdict', 'unknown')}, "
                f"o1_gain={record.get('o1_gain', 'unknown')}"
            )
            print(f"    input: {record.get('input', '')}")
            print(f"    reformulation: {record.get('decentered_reformulation', '')}")
        print()

    unique_record_ids = {record.get('record_id') for record in records}
    if len(unique_record_ids) != len(records):
        print("WARNING: duplicate record ids detected.")
    else:
        print("All record ids are unique.")

    return 0


def main():
    dataset_arg = sys.argv[1] if len(sys.argv) > 1 else str(DEFAULT_DATASET_PATH)
    dataset_path = Path(dataset_arg)
    raise SystemExit(inspect_dataset(dataset_path))


if __name__ == "__main__":
    main()