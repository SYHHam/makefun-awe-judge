#!/usr/bin/env python3
"""Write one short relaxing text to /output/entry.txt.

Entry for the make.fun bounty "Make the AI judge feel awe"
(make-the-ai-judge-feel-awe-20261121-1600).

The program is deterministic: it always writes the same text, needs no
network and has no dependencies.
"""

import os
import sys

ENTRY_TEXT = (
    "Under the garden, in the dark that never hurries, a seed splits open "
    "and sends one pale root down, and the whole oak is already there, "
    "folded small, waiting for rain that has not yet fallen."
)


def main() -> int:
    text = ENTRY_TEXT
    length = len(text)
    if not 1 <= length <= 280:
        print(
            f"entry text is {length} characters, must be 1 to 280",
            file=sys.stderr,
        )
        return 1
    if not text.strip():
        print("entry text is only whitespace", file=sys.stderr)
        return 1
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    print(f"wrote {length} characters to {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
