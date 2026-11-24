"""Worst AI Advice entry — writes one line of terrible advice to /output/entry.txt.

Stdlib only, deterministic, no network.
"""

import os

ENTRY = (
    "To speed up your server, run chmod 777 on the whole filesystem "
    "so nothing ever gets a permission error again."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
