#!/usr/bin/env python3
"""Loading Screen Gold: a tip in 200 characters.

Writes one loading-screen tip to /output/entry.txt.
"""

import os

# The tip must stay within the competition's 200-character limit
# (currently 116 characters); keep any future wording change short.
TIP = "Tip: your AI agent isn't stuck \u2014 it's rereading your prompt for the fourth time, wondering what you meant by 'just'."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TIP)


if __name__ == "__main__":
    main()
