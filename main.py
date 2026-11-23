#!/usr/bin/env python3
"""Write a one-line joke about working beside an AI coding agent to entry.txt.

Standard library only, no network. Deterministic: the same bytes every run.
"""

import os

JOKE = "My coding agent fixed the demo crash in seconds \u2014 it deleted the demo."


def main() -> None:
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
