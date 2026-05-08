
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def test_public_entrypoints_exist():
    required = [
        "README.md",
        "LICENSE",
        "CITATION.cff",
        "pyproject.toml",
        "pytest.ini",
        "RESULTS.md",
        "ROADMAP.md",
        "docs/O1_PROTOCOL.md",
        "docs/O1_GAIN_CRITERIA.md",
        "docs/O1_PROTOCOL_LOGIC.md",
        "docs/PROTOCOL_SCOPE.md",
        "docs/DATASETS_INDEX.md",
        "docs/REPOSITORY_STATUS.md",
    ]
    for rel in required:
        assert (ROOT / rel).exists(), rel

def test_core_datasets_exist():
    required = [
        "data/o1_miniset.jsonl",
        "data/o1_borderline_cases.jsonl",
        "data/o1_comparison_pairs.jsonl",
        "data/o1_disagreement_labels.jsonl",
        "data/o1_multiannotator_seed.jsonl",
        "data/o1_multiannotator_agreement_labels.jsonl",
        "data/o1_hard_cases_v0.jsonl",
        "data/o1_hard_rejected_v0.jsonl",
        "data/o1_hard_comparison_pairs.jsonl",
    ]
    for rel in required:
        assert (ROOT / rel).exists(), rel

def test_core_tools_exist():
    required = [
        "tools/validate_o1_dataset.py",
        "tools/inspect_o1_dataset.py",
        "tools/run_o1_checks.py",
    ]
    for rel in required:
        assert (ROOT / rel).exists(), rel

def test_readme_boundary_terms():
    text = (ROOT / "README.md").read_text(encoding="utf-8")
    required_phrases = [
        "measurement != inference != decision",
        "It is not philosophy.",
        "It is not a worldview.",
        "It is not a semantic judge.",
        "It is not a truth oracle.",
        "Decision remains external.",
        "reconstruction != evaporation",
    ]
    for phrase in required_phrases:
        assert phrase in text

def test_citation_contains_doi():
    text = (ROOT / "CITATION.cff").read_text(encoding="utf-8")
    assert "10.5281/zenodo.19571535" in text
