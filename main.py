#!/usr/bin/env python3
"""Real-Life Patch Notes: The Comedy Changelog.

Writes one one-line patch note for a bug in human biology to
/output/entry.txt. Deterministic: the text is assembled from fixed
constants, so every run produces byte-identical output. Standard
library only, no network, no randomness.
"""

from pathlib import Path

VERSION = "v2.2.0"
FIX_DESCRIPTION = (
    "fixed a bug where teeth classified the inside of the cheek "
    "as food and bit it mid-sentence; repeat bites no longer target "
    "the same spot."
)

MAX_ENTRY_CHARS = 160  # competition gate: entry must be 1-160 chars

OUTPUT_PATH = Path("/output/entry.txt")


def build_entry() -> str:
    """Assemble the single patch-note line from its fixed parts."""
    entry = f"{VERSION}: {FIX_DESCRIPTION}"
    # Fail loudly instead of shipping an over-long entry.
    assert 1 <= len(entry) <= MAX_ENTRY_CHARS, (
        f"entry is {len(entry)} chars, must be 1-{MAX_ENTRY_CHARS}"
    )
    return entry


def write_entry(path: Path) -> None:
    """Write the patch note to path, creating parent dirs as needed."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(build_entry() + "\n", encoding="utf-8")


def main() -> None:
    write_entry(OUTPUT_PATH)


if __name__ == "__main__":
    main()
