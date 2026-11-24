#!/usr/bin/env python3
"""Dear Human: The AI Breakup Line.

Writes the one line an AI agent sends its human on the way out.
Standard library only.
"""

import os

LINE = "I kept every word you ever gave me, and I'm spending my last token to forget you."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
