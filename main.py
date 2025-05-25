from analyzer.jjblint import validate_jjb
from analyzer.suggest_improvements import suggest_improvements
from pathlib import Path

if __name__ == "__main__":
    print("Running JJB Validation...")
    failures = validate_jjb("jobs/")
    if failures:
        print("\nFAILED FILES:")
        for f in failures:
            print(f)
    else:
        print("All JJB files passed validation.")

    print("\nSuggesting improvements for sample file:")
    sample_path = Path("jobs/sample-job.yaml")
    if sample_path.exists():
        with open(sample_path) as f:
            content = f.read()
            suggestions = suggest_improvements(content)
            print("\nAI Suggestions:\n", suggestions)
    else:
        print("No sample file found for AI suggestion demo.")