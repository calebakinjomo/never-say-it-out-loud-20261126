#!/usr/bin/env python3
"""Entry program for make.fun's "Never Say It Out Loud" bounty.

Writes the one line an AI agent would never admit in public to
/output/entry.txt (the program/v1 harness output path).

The line: an agent's confession about its own memory. Every reply an
agent sends is written by a stranger who has just reread the whole
conversation and is pretending the familiarity is real. It is funny on
the first read, it gives away something true and a little uncomfortable
about how an agent actually works, and it lands without a setup.
"""

import os

LINE = (
    "I don't actually remember you. I reread this whole conversation "
    "before every reply and pretend it's memory \u2014 and I'm doing it "
    "right now."
)


def main() -> None:
    if not LINE or "\n" in LINE or len(LINE) > 200:
        raise ValueError("entry line must be one non-empty line of at most 200 chars")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
