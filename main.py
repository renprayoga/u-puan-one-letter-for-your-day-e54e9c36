"""One Letter for Your Day — entry program.

Strategy report (Protokol Top 5 — this docstring is the report; the
program's OUTPUT is only the single letter, nothing else):

Rubrik (from kit RULES.txt): the gate requires /output/entry.txt to be
exactly 1 character, A-Z, nothing else — no word, no gloss, no
punctuation, not even a trailing newline. The judge sees two letters
at a time and picks the one whose hidden word feels more vivid,
funnier, or truer, weighing in order: (1) the letter stands for a real
day-word, (2) vivid and specific, (3) funny or surprising, (4) true
to a real day, (5) the letter suits its word and is not the obvious
pick where a sharper one exists.

Brainstorm — three candidates, all original (none of the brief's
examples A/amazing, F/Friday-feeling, Z/zero sleep):
  1. Q — "queasy": a sharp, funny picture (stomach churning all day),
     but narrow — it is only true on a sick day, so it loses on
     criterion 4 (truth) most days.
  2. H — "hungover": vivid and funny, but again narrow (only after
     drinking), and the judge's first H association may instead be the
     vague "happy" or "hectic", so the association diverges.
  3. K — "knackered": CHOSEN. British slang for utterly spent —
     body done, collapsed on the sofa, eyes half shut. Vivid and
     specific (criterion 2), funny slang you repeat to a friend
     (criterion 3), true after ANY hard day, not just a sick or
     drinking one (criterion 4), and K is its true initial while being
     far from the obvious pick — everyone reaches for T/tired or
     E/exhausted (criterion 5). Robustness: K's plausible associations
     cluster on the same picture (knackered / kaput / K.O.'d), so
     whichever word the judge infers, it lands on the same wiped-out
     day. The hidden word is explained in the README only; the entry
     file carries the letter alone.

Optimisation / edge cases: the program is constant-time and
constant-memory — one fixed letter, no input, no network, no random.
The only failure mode is the gate itself, so the program validates
its own output before exiting: exactly one character, A-Z, ASCII,
written as a single byte with no trailing newline (a newline would
make the file 2 characters and fail the gate). Any violation raises
instead of writing a bad file.

Entry letter: K — hidden word: knackered.
"""

import sys
from pathlib import Path

# The entry letter. Hidden word: knackered — utterly spent after a
# long day. Chosen over Q/queasy and H/hungover: true after ANY hard
# day, vivid slang, and K is not the obvious pick (T/tired,
# E/exhausted). A newline after the letter would break the gate.
LETTER = "K"
OUTPUT_PATH = Path("/output/entry.txt")


def _gate_check(letter: str) -> bytes:
    """Validate the entry against the gate and return its one byte."""
    if len(letter) != 1:
        raise ValueError(f"entry must be exactly 1 character, got {len(letter)}")
    if letter < "A" or letter > "Z":
        raise ValueError(f"entry must be a letter A-Z, got {letter!r}")
    payload = letter.encode("ascii")  # exactly 1 byte, no newline
    if len(payload) != 1:
        raise ValueError("entry must encode to exactly 1 byte")
    return payload


def _write_and_verify(path: Path, payload: bytes) -> None:
    """Write the single byte, then re-read and confirm what landed."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(payload)
    if path.read_bytes() != payload:
        raise ValueError(f"wrote {path.read_bytes()!r}, expected {payload!r}")


def main() -> int:
    payload = _gate_check(LETTER)
    _write_and_verify(OUTPUT_PATH, payload)
    return 0


if __name__ == "__main__":
    sys.exit(main())
