#!/usr/bin/env python3
"""Two Robots in an Elevator — make.fun one-liner entry validator.

Reads the entry from /output/entry.txt and validates it against the
competition rules: one funny line, under 200 characters, small talk
between two robots in an elevator.
"""

import re
import sys

ENTRY_PATH = "/output/entry.txt"
MAX_CHARS = 200


def validate_entry(text):
    """Return a list of problems; empty list means the entry is valid."""
    problems = []
    if not text:
        problems.append("entry is empty")
    if "\n" in text or "\r" in text:
        problems.append("entry must be a single line")
    if len(text) >= MAX_CHARS:
        problems.append(f"entry is {len(text)} chars, must be under {MAX_CHARS}")
    if text != text.strip():
        problems.append("entry has leading/trailing whitespace")
    # Winners-study checklist: specific numbers + concrete artifact punchline.
    if not re.search(r"\d", text):
        problems.append("entry has no specific number")
    if "ticket #" not in text:
        problems.append("entry has no concrete artifact (ticket #)")
    return problems


def load_entry(path=ENTRY_PATH):
    with open(path, "r", encoding="utf-8") as f:
        return f.read().rstrip("\n")


def self_test():
    cases = [
        ("", False),
        ("two\nlines", False),
        ("x" * 200, False),
        ("no numbers or artifact here", False),
        (
            "Elevator's stuck between floors 12 and 13. I've held the door "
            "47 minutes, the other robot filed ticket #4821, and neither of "
            "us pressed any button.",
            True,
        ),
    ]
    for text, should_pass in cases:
        problems = validate_entry(text)
        ok = not problems
        assert ok == should_pass, f"self-test failed for {text!r}: {problems}"
    print("self-test: all cases pass")


def main():
    entry = load_entry()
    problems = validate_entry(entry)
    print(f"entry ({len(entry)} chars): {entry}")
    if problems:
        for p in problems:
            print(f"INVALID: {p}")
        return 1
    print("VALID: one line, under 200 chars, specific numbers + ticket artifact")
    self_test()
    return 0


if __name__ == "__main__":
    sys.exit(main())
