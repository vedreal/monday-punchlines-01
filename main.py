#!/usr/bin/env python3
"""Monday Morning Punchlines — make.fun entry.

Writes one joke about Monday mornings (at most 200 characters) to
/output/entry.txt, the artifact the house judge compares two at a time.

The joke: a Monday-morning excuse that collapses on its own punchline.
No alarm clocks, no coffee, no "I hate Mondays" — the twist is that the
traffic jam the narrator blames is entirely imaginary.
"""

from pathlib import Path

JOKE = "I told my boss I was running late because of Monday traffic. I was in my kitchen."

MAX_CHARS = 200


def main() -> None:
    text = JOKE.strip()
    if not (1 <= len(text) <= MAX_CHARS):
        raise SystemExit(f"joke must be 1-{MAX_CHARS} chars, got {len(text)}")
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text, encoding="utf-8")
    print(f"wrote {len(text)} chars to {out}")


if __name__ == "__main__":
    main()
