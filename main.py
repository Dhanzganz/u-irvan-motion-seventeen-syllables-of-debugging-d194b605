#!/usr/bin/env python3
"""Seventeen Syllables of Debugging.

Writes one haiku about debugging (strict 5-7-5 syllables, at most 200
characters) to /output/entry.txt (or $OUTPUT_DIR/entry.txt).

The scene: a breakpoint holds all night, the log swears nothing changed,
and the twist lands in the last line — the bug was the author's own code
all along.

The haiku is a literal in this file. A small syllable counter sanity-checks
the shape before writing; the program fails fast if the counts or the total
length are wrong.
"""

import os
import re
import sys

HAIKU = (
    "red dot holds the line\n"
    "the log still swears nothing changed\n"
    "the bug wore my face"
)

EXPECTED_SYLLABLES = (5, 7, 5)
MAX_CHARS = 200

# Hand-checked overrides for words the vowel-group heuristic miscounts:
# "swears" reads as two vowel groups but is spoken as one syllable, and
# the "-ed" in "changed" is silent, so it is one syllable too.
OVERRIDES = {
    "swears": 1,
    "changed": 1,
}


def count_syllables(word):
    """Approximate syllable count via vowel groups (good enough as a check
    for this fixed, hand-verified text)."""
    w = word.lower().strip(".,;:!?\"'")
    if w in OVERRIDES:
        return OVERRIDES[w]
    groups = re.findall(r"[aeiouy]+", w)
    n = len(groups)
    # Silent trailing e (e.g. "line", "swears" is covered above).
    if w.endswith("e") and n > 1:
        n -= 1
    return max(n, 1)


def line_syllables(line):
    """Total syllables in one haiku line, word by word."""
    return sum(count_syllables(w) for w in line.split())


def main():
    """Validate the haiku's shape, then write it verbatim.

    Checks, in order: exactly three lines, total length within MAX_CHARS,
    and each line's syllable count matching EXPECTED_SYLLABLES (5-7-5).
    Any failure exits non-zero before anything is written.
    """
    lines = HAIKU.split("\n")
    if len(lines) != 3:
        sys.exit("haiku must have exactly 3 lines, got %d" % len(lines))
    if len(HAIKU) > MAX_CHARS:
        sys.exit("haiku is %d chars, over the %d limit" % (len(HAIKU), MAX_CHARS))
    for line, expected in zip(lines, EXPECTED_SYLLABLES):
        got = line_syllables(line)
        if got != expected:
            sys.exit("line %r has %d syllables, expected %d" % (line, got, expected))

    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(HAIKU)
    print("wrote %s (%d chars, 5-7-5)" % (path, len(HAIKU)))


if __name__ == "__main__":
    main()
