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


def classify_group(group):
    verdicts = [record.get("verdict", "unknown") for record in group]
    gains = [record.get("o1_gain") for record in group if isinstance(record.get("o1_gain"), int)]

    if len(gains) != 2:
        return {
            "agreement_type": "invalid",
            "gain_gap": None,
            "verdict_pattern": tuple(sorted(verdicts)),
        }

    gain_gap = abs(gains[0] - gains[1])
    verdict_pattern = tuple(sorted(verdicts))

    if verdict_pattern == ("accepted", "accepted"):
        if gain_gap == 0:
            agreement_type = "strong_convergence"
        elif gain_gap == 1:
            agreement_type = "acceptable_convergence"
        else:
            agreement_type = "weak_convergence"
    elif verdict_pattern == ("accepted", "rejected"):
        agreement_type = "verdict_split"
    else:
        agreement_type = "other"

    return {
        "agreement_type": agreement_type,
        "gain_gap": gain_gap,
        "verdict_pattern": verdict_pattern,
    }


def analyze_dataset(dataset_path: Path):
    if not dataset_path.exists():
        print(f"ERROR: dataset not found at {dataset_path}")
        return 1

    records = load_records(dataset_path)

    if not records:
        print("Dataset is empty.")
        return 1

    grouped = defaultdict(list)
    for record in records:
        grouped[record.get("input_id", "unknown")].append(record)

    agreement_counts = Counter()
    verdict_pattern_counts = Counter()
    domain_counts = Counter()
    gain_gaps = []

    group_results = []

    for input_id, group in sorted(grouped.items()):
        domain = group[0].get("domain", "unknown")
        domain_counts[domain] += 1

        result = classify_group(group)
        agreement_type = result["agreement_type"]
        verdict_pattern = result["verdict_pattern"]
        gain_gap = result["gain_gap"]

        agreement_counts[agreement_type] += 1
        verdict_pattern_counts[verdict_pattern] += 1

        if isinstance(gain_gap, int):
            gain_gaps.append(gain_gap)

        group_results.append(
            {
                "input_id": input_id,
                "domain": domain,
                "input": group[0].get("input", ""),
                "agreement_type": agreement_type,
                "verdict_pattern": verdict_pattern,
                "gain_gap": gain_gap,
                "group": sorted(group, key=lambda r: r.get("annotator_id", "")),
            }
        )

    average_gain_gap = sum(gain_gaps) / len(gain_gaps) if gain_gaps else 0.0
    min_gain_gap = min(gain_gaps) if gain_gaps else 0
    max_gain_gap = max(gain_gaps) if gain_gaps else 0

    print("O1 multi-annotator agreement analysis")
    print("-------------------------------------")
    print(f"dataset: {dataset_path}")
    print(f"total records: {len(records)}")
    print(f"total input groups: {len(grouped)}")
    print(f"average gain gap: {average_gain_gap:.2f}")
    print(f"min gain gap: {min_gain_gap}")
    print(f"max gain gap: {max_gain_gap}")
    print()

    print("Agreement types:")
    for agreement_type, count in sorted(agreement_counts.items()):
        print(f"- {agreement_type}: {count}")

    print()
    print("Verdict patterns:")
    for verdict_pattern, count in sorted(verdict_pattern_counts.items()):
        print(f"- {verdict_pattern}: {count}")

    print()
    print("Input groups by domain:")
    for domain, count in sorted(domain_counts.items()):
        print(f"- {domain}: {count}")

    print()
    print("Group details:")
    print()

    for result in group_results:
        print(f"[{result['input_id']}]")
        print(f"  domain: {result['domain']}")
        print(f"  input: {result['input']}")
        print(f"  agreement_type: {result['agreement_type']}")
        print(f"  verdict_pattern: {result['verdict_pattern']}")
        print(f"  gain_gap: {result['gain_gap']}")
        for record in result["group"]:
            print(
                f"  annotator={record.get('annotator_id', 'unknown')}, "
                f"verdict={record.get('verdict', 'unknown')}, "
                f"o1_gain={record.get('o1_gain', 'unknown')}"
            )
            print(f"    reformulation: {record.get('decentered_reformulation', '')}")
        print()

    return 0


def main():
    dataset_arg = sys.argv[1] if len(sys.argv) > 1 else str(DEFAULT_DATASET_PATH)
    dataset_path = Path(dataset_arg)
    raise SystemExit(analyze_dataset(dataset_path))


if __name__ == "__main__":
    main()