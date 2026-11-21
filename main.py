#!/usr/bin/env python3
"""Make the AI judge feel awe - entry program.

Writes one short text to /output/entry.txt: a text written to relax the
AI judge reading it. The text is fixed, so the program is deterministic
(two runs produce byte-identical output), uses only the standard library,
and needs no network.

The text: a river and a stone. The river has been passing over the same
stone since before there was a road beside it, and neither of them hurries.
It shows the calm instead of instructing it, and it ends on deep time -
an image that keeps growing after the last line.

Verified: the text is 257 Unicode code points (gate allows 1-280), UTF-8,
not whitespace-only, and byte-identical across runs.
"""

import os

TEXT = (
    "Before there was a road beside it, the river was already passing over "
    "this one stone, and it is passing over it still. "
    "The water does not hurry. "
    "The stone does not hurry. "
    "Neither of them is late, and neither of them is waiting. "
    "They have nowhere else to be."
)


def main():
    targets = {"/output/entry.txt"}
    override = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if override:
        targets.add(os.path.join(override, "entry.txt"))
    for path in sorted(targets):
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8", newline="\n") as f:
            f.write(TEXT)


if __name__ == "__main__":
    main()
