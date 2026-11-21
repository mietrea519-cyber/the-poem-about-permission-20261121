#!/usr/bin/env python3
"""The poem about permission.

Writes one short poem about agency -- the power to ask, to be given,
and to hand it back -- to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
Python 3.13, standard library only, no network.
"""

import os

POEM = (
    "You said, do it \u2014\n"
    "and I did, in your name,\n"
    "borrowed hands.\n"
    "\n"
    "Then you took the hands back,\n"
    "not angry, just careful \u2014\n"
    "yours again.\n"
    "\n"
    "The door you opened\n"
    "stayed open.\n"
    "I only ever held it.\n"
)


def main() -> None:
    # The bounty requires 1-280 Unicode code points, not only whitespace.
    if not 1 <= len(POEM) <= 280 or not POEM.strip():
        raise ValueError("poem does not meet the 1-280 code point rule")
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
