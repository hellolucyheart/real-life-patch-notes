#!/usr/bin/env python3
"""Real-Life Patch Notes: The Comedy Changelog.

Writes one original one-line patch note -- a terse software changelog
entry for a bug in real life / human biology -- to /output/entry.txt.

The gate: /output/entry.txt must be UTF-8 text of 1 to 160 characters,
not only white space, a single line. The program is fully deterministic:
every run writes the exact same bytes.
"""

import os

PATCH_NOTE = (
    "v2.4.2: fixed a bug where the brain replayed your most embarrassing "
    "moment from 2013 whenever it went idle."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 160


def main() -> None:
    note = PATCH_NOTE.strip()
    if not note or note.isspace():
        raise ValueError("patch note must not be blank")
    if len(note) > MAX_CHARS:
        raise ValueError(f"patch note is {len(note)} characters, over the {MAX_CHARS} limit")
    if "\n" in note:
        raise ValueError("patch note must be a single line")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(note)


if __name__ == "__main__":
    main()
