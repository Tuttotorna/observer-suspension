import json
from collections import Counter, defaultdict
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

    domain_counts = Counter()
    verdict_counts = Counter()
    domain_verdict_counts = defaultdict(Counter)
    gains = []

    for record in records:
        domain = record.get("domain", "unknown")
        verdict = record.get("verdict", "unknown")
        gain = record.get("o1_gain")

        domain_counts[domain] += 1
        verdict_counts[verdict] += 1
        domain_verdict_counts[domain][verdict] += 1

        if isinstance(gain, int):
            gains.append(gain)

    average_gain = sum(gains) / len(gains) if gains else 0.0

    print("O1 dataset inspection")
    print("---------------------")
    print(f"dataset: {DATASET_PATH}")
    print(f"total records: {len(records)}")
    print(f"average o1_gain: {average_gain:.2f}")
    print()

    print("Records by verdict:")
    for verdict, count in sorted(verdict_counts.items()):
        print(f"- {verdict}: {count}")

    print()
    print("Records by domain:")
    for domain, count in sorted(domain_counts.items()):
        print(f"- {domain}: {count}")

    print()
    print("Records by domain and verdict:")
    for domain in sorted(domain_verdict_counts):
        accepted = domain_verdict_counts[domain].get("accepted", 0)
        rejected = domain_verdict_counts[domain].get("rejected", 0)
        print(f"- {domain}: accepted={accepted}, rejected={rejected}")

    print()
    print("Sample records:")
    print()

    for record in records[:5]:
        print(f"[{record.get('id', 'unknown')}] {record.get('domain', 'unknown')}")
        print(f"  standard: {record.get('standard_formulation', '')}")
        print(f"  reformulation: {record.get('decentered_reformulation', '')}")
        print(f"  o1_gain: {record.get('o1_gain', 'unknown')}")
        print(f"  verdict: {record.get('verdict', 'unknown')}")
        print()

    unique_ids = {record.get("id") for record in records}
    if len(unique_ids) != len(records):
        print("WARNING: duplicate record ids detected.")
    else:
        print("All record ids are unique.")


if __name__ == "__main__":
    main()