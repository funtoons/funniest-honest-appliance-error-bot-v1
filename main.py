"""Entry for make.fun: The Funniest Honest Appliance Error.

Writes one line, the funniest honest error message an appliance could
show, to /output/entry.txt. The line is a single original sentence in the
appliance's own flat, put-upon voice: a kettle that boiled itself dry and
reports it with misplaced pride. Deterministic and offline: no randomness,
no network, no timestamps, no environment reads.
"""

from pathlib import Path

ENTRY = "No water detected. I boiled the kettle dry for three minutes, very efficiently."
OUTPUT = Path("/output/entry.txt")


def main() -> None:
    # Guard the sealed scorer's gate: one line, 1-200 characters, not blank.
    if not 1 <= len(ENTRY) <= 200 or "\n" in ENTRY or not ENTRY.strip():
        raise SystemExit("entry violates the 1-200 character single-line gate")
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
