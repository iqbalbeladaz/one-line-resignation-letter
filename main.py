#!/usr/bin/env python3
"""The Funniest One-Line Resignation Letter — make.fun entry.

Writes the one-line resignation letter of a cron job to /output/entry.txt.
The line is exactly 124 characters, one line, no trailing newline.
"""

import os

ENTRY = (
    "I am the cron job that has fired every minute since March, "
    "and March ended eight months ago, in case nobody noticed. I quit."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
