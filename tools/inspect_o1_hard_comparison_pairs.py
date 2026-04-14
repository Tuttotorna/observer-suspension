import json
import sys
from collections import Counter, defaultdict
from pathlib import Path

DEFAULT_DATASET_PATH = Path("data/o1_hard_comparison_pairs.jsonl")


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

    strength_counts = Counter()
    verdict_counts = Counter()
    domain_counts = Counter()
    gains = []
    grouped = defaultdict(list)

    for record in records:
        strength_counts[record.get("strength", "unknown")] += 1
        verdict_counts[record.get("verdict", "unknown")] += 1
        domain_counts[record.get("domain", "unknown")] += 1

        gain = record.get("o1_gain")
        if isinstance(gain, int):
            gains.append(gain)

        grouped[record.get("pair_id", "unknown")].append(record)

    average_gain = sum(gains) / len(gains) if gains else 0.0
    min_gain = min(gains) if gains else 0
    max_gain = max(gains) if gains else 0

    pair_type_counts = Counter()
    gain_gaps = []

    for pair_id, group in grouped.items():
        strengths = {record.get("strength", "unknown") for record in group}
        if strengths == {"accepted", "rejected"}:
            pair_type_counts["accepted_vs_rejected"] += 1
        else:
            pair_type_counts["other"] += 1

        group_gains = [record.get("o1_gain") for record in group if isinstance(record.get("o1_gain"), int)]
        if len(group_gains) == 2:
            gain_gaps.append(abs(group_gains[0] - group_gains[1]))

    average_gain_gap = sum(gain_gaps) / len(gain_gaps) if gain_gaps else 0.0
    min_gain_gap = min(gain_gaps) if gain_gaps else 0
    max_gain_gap = max(gain_gaps) if gain_gaps else 0

    print("O1 hard comparison pairs inspection")
    print("-----------------------------------")
    print(f"dataset: {dataset_path}")
    print(f"total records: {len(records)}")
    print(f"total pairs: {len(grouped)}")
    print(f"average o1_gain: {average_gain:.2f}")
    print(f"min o1_gain: {min_gain}")
    print(f"max o1_gain: {max_gain}")
    print(f"average gain gap per pair: {average_gain_gap:.2f}")
    print(f"min gain gap: {min_gain_gap}")
    print(f"max gain gap: {max_gain_gap}")
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
    print("Pair types:")
    for pair_type, count in sorted(pair_type_counts.items()):
        print(f"- {pair_type}: {count}")

    print()
    print("Hard comparison pairs:")
    print()

    for pair_id in sorted(grouped):
        print(f"[{pair_id}]")
        for record in sorted(grouped[pair_id], key=lambda r: r.get("variant", "")):
            print(f"  variant: {record.get('variant', '')}")
            print(f"  strength: {record.get('strength', '')}")
            print(f"  verdict: {record.get('verdict', '')}")
            print(f"  input_id: {record.get('input_id', '')}")
            print(f"  domain: {record.get('domain', '')}")
            print(f"  input: {record.get('input', '')}")
            print(f"  decentered_reformulation: {record.get('decentered_reformulation', '')}")
            print(f"  emergent_structure: {record.get('emergent_structure', '')}")
            print(f"  o1_gain: {record.get('o1_gain', '')}")
            print()
        group_gains = [record.get("o1_gain") for record in grouped[pair_id] if isinstance(record.get("o1_gain"), int)]
        if len(group_gains) == 2:
            print(f"  gain_gap: {abs(group_gains[0] - group_gains[1])}")
        print()

    return 0


def main():
    dataset_arg = sys.argv[1] if len(sys.argv) > 1 else str(DEFAULT_DATASET_PATH)
    dataset_path = Path(dataset_arg)
    raise SystemExit(inspect_dataset(dataset_path))


if __name__ == "__main__":
    main()