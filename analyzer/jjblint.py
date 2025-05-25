import subprocess
from pathlib import Path

def validate_jjb(path="jobs/"):
    yaml_files = list(Path(path).rglob("*.yaml"))
    failed = []

    for yml in yaml_files:
        try:
            subprocess.run(["jenkins-jobs", "test", str(yml)], check=True)
        except subprocess.CalledProcessError:
            print(f"❌ Failed: {yml}")
            failed.append(str(yml))

    return failed