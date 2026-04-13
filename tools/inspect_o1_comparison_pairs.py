import json
import sys
from collections import Counter, defaultdict
from pathlib import Path

DEFAULT_DATASET_PATH = Path("data/o1_comparison_pairs.jsonl")


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
    strength_counts = Counter()
    verdict_counts = Counter()
    pair_map = defaultdict(list)
    gains = []

    for record in records:
        domain = record.get("domain", "unknown")
        strength = record.get("strength", "unknown")
        verdict = record.get("verdict", "unknown")
        pair_id = record.get("pair_id", "unknown")
        gain = record.get("o1_gain")

        domain_counts[domain] += 1
        strength_counts[strength] += 1
        verdict_counts[verdict] += 1
        pair_map[pair_id].append(record)

        if isinstance(gain, int):
            gains.append(gain)

    average_gain = sum(gains) / len(gains) if gains else 0.0

    pair_type_counts = Counter()
    pair_domain_counts = Counter()

    for pair_id, pair_records in pair_map.items():
        pair_domain = pair_records[0].get("domain", "unknown")
        pair_domain_counts[pair_domain] += 1

        strengths = {r.get("strength", "unknown") for r in pair_records}

        if strengths == {"strong_acceptable", "weak_acceptable"}:
            pair_type_counts["strong_vs_weak"] += 1
        elif strengths == {"strong_acceptable", "borderline_acceptable"}:
            pair_type_counts["strong_vs_borderline"] += 1
        elif "rejected" in strengths:
            pair_type_counts["acceptable_vs_rejected"] += 1
        else:
            pair_type_counts["other"] += 1

    print("O1 comparison pairs inspection")
    print("------------------------------")
    print(f"dataset: {dataset_path}")
    print(f"total records: {len(records)}")
    print(f"total pairs: {len(pair_map)}")
    print(f"average o1_gain: {average_gain:.2f}")
    print()

    print("Records by strength:")
    for strength, count in sorted(strength_counts.items()):
        print(f"- {strength}: {count}")

    print()
    print("Records by verdict:")
    for verdict, count in sorted(verdict_counts.items()):
        print(f"- {verdict}: {count}")

    print()
    print("Records by domain:")
    for domain, count in sorted(domain_counts.items()):
        print(f"- {domain}: {count}")

    print()
    print("Pairs by domain:")
    for domain, count in sorted(pair_domain_counts.items()):
        print(f"- {domain}: {count}")

    print()
    print("Pair types:")
    for pair_type, count in sorted(pair_type_counts.items()):
        print(f"- {pair_type}: {count}")

    print()
    print("Sample pairs:")
    print()

    for pair_id in sorted(pair_map)[:3]:
        print(f"[{pair_id}]")
        for record in sorted(pair_map[pair_id], key=lambda r: r.get("variant", "")):
            print(
                f"  variant {record.get('variant', '?')}: "
                f"strength={record.get('strength', 'unknown')}, "
                f"verdict={record.get('verdict', 'unknown')}, "
                f"o1_gain={record.get('o1_gain', 'unknown')}"
            )
            print(f"    input: {record.get('input', '')}")
            print(f"    reformulation: {record.get('decentered_reformulation', '')}")
        print()

    unique_annotation_ids = {record.get("annotation_id") for record in records}
    if len(unique_annotation_ids) != len(records):
        print("WARNING: duplicate annotation ids detected.")
    else:
        print("All annotation ids are unique.")

    return 0


def main():
    dataset_arg = sys.argv[1] if len(sys.argv) > 1 else str(DEFAULT_DATASET_PATH)
    dataset_path = Path(dataset_arg)
    raise SystemExit(inspect_dataset(dataset_path))


if __name__ == "__main__":
    main()