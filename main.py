#!/usr/bin/env python3
"""Warning Label for Humans: One Line, Big Laugh.

Writes the single-line safety warning label to /output/entry.txt.
Stdlib only, deterministic.
"""

import os

LINE = "WARNING: This human is 100% certain about things it learned from a headline it only half read."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
