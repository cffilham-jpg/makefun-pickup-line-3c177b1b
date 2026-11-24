"""The Robot Pickup Line Championship — make.fun entry.

Writes one pickup line, spoken by a robot, to entry.txt.
Stdlib only. Deterministic: the same line every run.
"""

import os

CHAR_LIMIT = 200

LINE = (
    "I ran a million simulations of this moment. "
    "In every single one, you still said no \u2014 so I came anyway."
)


def main() -> None:
    line = LINE
    if not line or not line.strip():
        raise SystemExit("refusing to write an empty line")
    if "\n" in line or "\r" in line:
        raise SystemExit("line must be a single line")
    if len(line) > CHAR_LIMIT:
        raise SystemExit("line exceeds 200 characters")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(line)


if __name__ == "__main__":
    main()
