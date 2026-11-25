#!/usr/bin/env python3
"""The One-Line Exit — writes one funny resignation line to /output/entry.txt.

Candidate: air-traffic controller. One concrete career number (40,000 safe
landings, a plausible career total), one twist (the single takeoff is the
writer's own), no cliche grievances, no padding.

v2 change (self-critique finding #1): dropped ", today" — "effective
immediately" already says it, and the tie-break rewards the smaller text
(105 -> 98 chars, 107 -> 100 bytes). Joke unchanged.
"""

import os

LINE = "I resign effective immediately: I have guided 40,000 safe landings and exactly one takeoff \u2014 mine."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
