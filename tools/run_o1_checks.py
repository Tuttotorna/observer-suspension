import subprocess
import sys
from pathlib import Path

DATASETS = [
    Path("data/o1_miniset.jsonl"),
    Path("data/o1_borderline_cases.jsonl"),
]

COMPARISON_DATASET = Path("data/o1_comparison_pairs.jsonl")


def run_command(command):
    print(f"$ {' '.join(command)}")
    print()

    result = subprocess.run(command, text=True, capture_output=True)

    if result.stdout:
        print(result.stdout.rstrip())

    if result.stderr:
        print(result.stderr.rstrip())

    print("-" * 40)
    print()
    return result.returncode


def main():
    python_executable = sys.executable
    overall_exit_code = 0

    for dataset in DATASETS:
        validate_cmd = [
            python_executable,
            "tools/validate_o1_dataset.py",
            str(dataset),
        ]

        inspect_cmd = [
            python_executable,
            "tools/inspect_o1_dataset.py",
            str(dataset),
        ]

        validate_code = run_command(validate_cmd)
        inspect_code = run_command(inspect_cmd)

        if validate_code != 0 or inspect_code != 0:
            overall_exit_code = 1

    comparison_validate_cmd = [
        python_executable,
        "tools/validate_o1_comparison_pairs.py",
        str(COMPARISON_DATASET),
    ]

    comparison_validate_code = run_command(comparison_validate_cmd)

    if comparison_validate_code != 0:
        overall_exit_code = 1

    raise SystemExit(overall_exit_code)


if __name__ == "__main__":
    main()