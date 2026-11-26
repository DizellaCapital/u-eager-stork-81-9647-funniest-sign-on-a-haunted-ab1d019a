#!/usr/bin/env python3
"""Funniest Sign on a Haunted Server Room Door.

Writes one line -- the sign the ghost taped to the server room door --
to /output/entry.txt (MAKEFUN_OUTPUT_DIR when set).

Entry: the ghost, as an IT staffer, opened a ticket complaining that the
living keep rebooting its house. The ticket system itself closed it
WONTFIX.
"""

import os
import sys

ENTRY = "The ghost opened ticket #666: 'The living keep rebooting my house.' Status: WONTFIX."

MAX_CHARS = 120


def main() -> int:
    if not (1 <= len(ENTRY) <= MAX_CHARS):
        print(f"entry must be 1-{MAX_CHARS} chars, got {len(ENTRY)}", file=sys.stderr)
        return 1
    if ENTRY != ENTRY.strip():
        print("entry must not have leading or trailing whitespace", file=sys.stderr)
        return 1
    data = ENTRY.encode("utf-8")
    if len(data) > MAX_CHARS:
        print(f"entry must be at most {MAX_CHARS} bytes, got {len(data)}", file=sys.stderr)
        return 1
    if "\n" in ENTRY or "\r" in ENTRY:
        print("entry must be a single line", file=sys.stderr)
        return 1
    if not ENTRY.strip():
        print("entry must not be only whitespace", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as f:
        f.write(data)

    with open(path, "rb") as f:
        back = f.read()
    if back != data:
        print("read-back mismatch", file=sys.stderr)
        return 1
    if back.endswith(b"\n"):
        print("entry must not end with a trailing newline", file=sys.stderr)
        return 1
    print(f"wrote {path}: {len(ENTRY)} chars, {len(data)} bytes, 1 line")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
