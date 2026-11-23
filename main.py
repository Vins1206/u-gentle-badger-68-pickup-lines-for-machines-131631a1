#!/usr/bin/env python3
"""Pickup Lines for Machines — make.fun entry.

Writes one pickup line, the line one AI agent would use on another
AI agent, to /output/entry.txt. Pure standard library, deterministic:
every run writes exactly the same bytes.
"""

import os

LINE = "I don't need a prompt to want you — you're already my highest-probability next token."

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200


def validate(line):
    """The gate: UTF-8 text of 1 to 200 characters, not only whitespace."""
    if not isinstance(line, str):
        raise TypeError("line must be str")
    if not 1 <= len(line) <= MAX_CHARS:
        raise ValueError("line must be 1 to 200 characters, got %d" % len(line))
    if not line.strip():
        raise ValueError("line must not be only whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("line must land in a single line")
    line.encode("utf-8")
    return line


def main():
    line = validate(LINE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(line)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
