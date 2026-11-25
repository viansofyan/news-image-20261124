"""Copy the entry image to the grader's output directory.

The front page itself is drawn in advance and shipped as
assets/entry.png; this program only moves it to
$MAKEFUN_OUTPUT_DIR/entry.png (or /output/entry.png when the variable
is unset). No network, no randomness: two runs write identical bytes.
"""

import os
import shutil
import sys
from pathlib import Path


def main() -> int:
    here = Path(__file__).resolve().parent
    source = here / "assets" / "entry.png"
    if not source.is_file():
        print(f"error: missing asset: {source}", file=sys.stderr)
        return 1
    with source.open("rb") as fh:
        if fh.read(8) != b"\x89PNG\r\n\x1a\n":
            print(f"error: asset is not a PNG: {source}", file=sys.stderr)
            return 1
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(source, out_dir / "entry.png")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
