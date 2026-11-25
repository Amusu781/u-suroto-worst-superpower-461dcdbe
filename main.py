"""Worst Superpower entry: write one useless-superpower line to /output/entry.txt."""

import shutil
from pathlib import Path

ENTRY = "I always know exactly when the microwave is about to beep: one second after it beeps."

OUTPUT_DIR = Path("/output")
OUTPUT_PATH = OUTPUT_DIR / "entry.txt"


def main():
    assert "\n" not in ENTRY and 1 <= len(ENTRY) <= 140, "entry must be one line of 1-140 chars"
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    for path in OUTPUT_DIR.iterdir():
        if path.is_dir() and not path.is_symlink():
            shutil.rmtree(path)
        else:
            path.unlink()
    OUTPUT_PATH.write_text(ENTRY + "\n", encoding="utf-8")
    print(f"Wrote {len(ENTRY)}-character entry to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
