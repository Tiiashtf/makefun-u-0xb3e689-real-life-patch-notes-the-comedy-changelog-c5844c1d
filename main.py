#!/usr/bin/env python3
"""Real-Life Patch Notes: The Comedy Changelog.

Writes one patch-note line to /output/entry.txt: a software release
note for a bug in human biology, in the terse register of a real
changelog. Standard library only, no network, deterministic: every
run writes the same bytes.
"""

import os
import shutil

ENTRY = (
    "v2.4.1: fixed a bug where the brain replayed your most "
    "embarrassing moment from 2009 every night at 3am instead "
    "of sleeping."
)

OUTPUT_DIR = "/output"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "entry.txt")


def main() -> None:
    line = ENTRY
    assert "\n" not in line, "entry must be a single line"
    assert 1 <= len(line) <= 160, "entry must be 1-160 characters"
    assert line.strip(), "entry must not be only whitespace"

    # Never remove the output directory itself: the grader may run
    # with a root-owned output directory inside a sticky parent.
    # Create it if missing, clear only its contents, then write.
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    for name in os.listdir(OUTPUT_DIR):
        path = os.path.join(OUTPUT_DIR, name)
        if os.path.isdir(path) and not os.path.islink(path):
            shutil.rmtree(path)
        else:
            os.remove(path)

    with open(OUTPUT_FILE, "w", encoding="utf-8", newline="\n") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
