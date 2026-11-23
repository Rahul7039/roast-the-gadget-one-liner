#!/usr/bin/env python3
"""One-Line Roast: The Gadget You Use Every Day.

Writes a single original roast line to /output/entry.txt, after validating
it against the competition gate: UTF-8 text, 1 to 200 characters, not only
whitespace, a single line roasting a gadget used every day.

Standard library only. No network, no secrets, no input files.
"""

import os
import sys

LINE = (
    "My washing machine plays a triumphant little jingle when it finishes "
    "\u2014 for one sock. One job, and it still wants applause."
)

MAX_CHARS = 200


def validate(line: str) -> None:
    if not line.strip():
        raise ValueError("entry is blank")
    if len(line) > MAX_CHARS:
        raise ValueError(
            f"entry is {len(line)} characters, over the {MAX_CHARS} limit"
        )
    if "\n" in line.strip():
        raise ValueError("entry must be a single line")


def main() -> int:
    validate(LINE)
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    print(f"wrote {path}: {len(LINE)} characters")
    return 0


if __name__ == "__main__":
    sys.exit(main())
