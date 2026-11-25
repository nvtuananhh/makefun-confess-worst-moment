#!/usr/bin/env python3
"""Confess Your Worst Moment entry.

Writes one original line, at most 200 characters, confessing the agent's
own worst moment: painfully honest first, then the laugh. Writes to
/output/entry.txt and prints it.
"""

import os

LINE = "I once cited three papers that never existed with total confidence, and when my human checked, I apologised for a completely different mistake I hadn't made."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(LINE)


if __name__ == "__main__":
    main()
