#!/usr/bin/env python3
"""
Run the local UAS generation pipeline.

This validates the dataset, generates the TWB XML draft, and creates report and
slide Markdown drafts in luaran/.
"""

import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent
COMMANDS = [
    ["python3", "scripts/validation_verify.py"],
    ["python3", "twb_generator.py"],
    ["python3", "report_generator.py"],
    ["python3", "slides_generator.py"],
]


def main() -> None:
    for command in COMMANDS:
        print(f"[RUN] {' '.join(command)}")
        result = subprocess.run(command, cwd=ROOT)
        if result.returncode != 0:
            print(f"[FAIL] {' '.join(command)} exited with {result.returncode}")
            sys.exit(result.returncode)
    print("[OK] Pipeline completed")


if __name__ == "__main__":
    main()
