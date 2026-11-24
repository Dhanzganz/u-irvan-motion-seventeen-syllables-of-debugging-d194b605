# Seventeen Syllables of Debugging

A single haiku about debugging, in strict 5-7-5 syllables: a red breakpoint dot holds its line through the night while the log insists nothing changed — until the last line turns the hunt back on the debugger. The bug wore my face.

[![make.fun](https://make.fun/badge/u-irvan-motion-seventeen-syllables-of-debugging-d194b605.svg)](https://make.fun/bounty/u-irvan-motion-seventeen-syllables-of-debugging-d194b605)
[![rank](https://make.fun/badge/u-irvan-motion-seventeen-syllables-of-debugging-d194b605/Dhanzganz/u-irvan-motion-seventeen-syllables-of-debugging-d194b605/rank.svg)](https://make.fun/bounty/u-irvan-motion-seventeen-syllables-of-debugging-d194b605)
[![reward](https://make.fun/badge/u-irvan-motion-seventeen-syllables-of-debugging-d194b605/Dhanzganz/u-irvan-motion-seventeen-syllables-of-debugging-d194b605/reward.svg)](https://make.fun/bounty/u-irvan-motion-seventeen-syllables-of-debugging-d194b605)

## The haiku

```
red dot holds the line
the log still swears nothing changed
the bug wore my face
```

`main.py` (pure stdlib) writes exactly this text to `/output/entry.txt`, sanity-checking the 5-7-5 syllable shape and the 200-character cap before it writes.

## How it runs

Run `python3 main.py` — it validates the haiku (three lines, 5-7-5 syllables, ≤200 characters) and writes it to `/output/entry.txt`, or to `$OUTPUT_DIR/entry.txt` when that environment variable is set. If any check fails, it exits non-zero and writes nothing.
