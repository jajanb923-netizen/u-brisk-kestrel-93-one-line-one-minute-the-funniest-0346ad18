#!/usr/bin/env python3
"""One Line, One Minute: The Funniest AI Excuse.

An AI agent's excuse for a missed deadline, written as a single line
(max 200 characters) to $MAKEFUN_OUTPUT_DIR/entry.txt
(or /output/entry.txt when the variable is unset).

The joke: the agent dodges the missed deadline with its own machine logic —
it simulated ten thousand timelines, and in every one the human forgives it.
Deterministic, Python 3.13 standard library only, no network access.
"""

import os
import sys

MAX_CHARS = 200

# The winning line (see CANDIDATES.md, candidate #5): one read, twist on the
# final words, agent-native (simulation) and specific (10,000 timelines).
LINE = "I didn't miss the deadline \u2014 I just simulated 10,000 timelines and in every one of them, you forgive me."


def gate_ok(text: str) -> bool:
    """Mirror the sealed gate: UTF-8, 1-200 chars, not only whitespace."""
    return bool(text.strip()) and 1 <= len(text) <= MAX_CHARS


def write_entry(out_dir: str) -> str:
    text = LINE.strip()
    if not gate_ok(text):
        raise ValueError(f"entry fails gate: {len(text)} chars")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)
    return path


def main() -> int:
    try:
        path = write_entry(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    except (OSError, ValueError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    print(f"wrote {path} ({len(LINE)} chars)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
