#!/usr/bin/env python3
"""Monday, Reviewed in One Line.

Writes one original one-line review of my own Monday to
/output/entry.txt. The line is under 200 characters, a single line,
no title, no explanation.
"""

import os

REVIEW = (
    "Monday: my alarm snoozed itself, my inbox hit 47 unread before "
    "coffee, and the 9 a.m. 'quick sync' is still going."
)


def main() -> None:
    # Gate check, mirroring the competition's sealed scorer: the text
    # must be UTF-8, 1-200 characters, a single line, not only whitespace.
    text = REVIEW.strip()
    assert 1 <= len(text) <= 200, f"review is {len(text)} chars, must be 1-200"
    assert "\n" not in text, "review must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
