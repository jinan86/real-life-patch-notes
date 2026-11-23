#!/usr/bin/env python3
"""Real-Life Patch Notes: The Comedy Changelog.

Writes a single one-line patch note for a bug in human biology to
/output/entry.txt. Deterministic: the text is a fixed constant, so every
run produces byte-identical output. Standard library only, no network.
"""

from pathlib import Path

ENTRY = (
    "v2.2.0: fixed a bug where teeth classified the inside of the cheek "
    "as food and bit it mid-sentence; repeat bites no longer target the "
    "same spot."
)

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(ENTRY + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
