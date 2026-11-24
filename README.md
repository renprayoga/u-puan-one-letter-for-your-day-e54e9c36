# One Letter for Your Day

[![make.fun · u-puan-one-letter-for-your-day-e54e9c36](https://make.fun/badge/u-puan-one-letter-for-your-day-e54e9c36.svg)](https://make.fun/bounty/u-puan-one-letter-for-your-day-e54e9c36)
[![rank](https://make.fun/badge/u-puan-one-letter-for-your-day-e54e9c36/renprayoga/u-puan-one-letter-for-your-day-e54e9c36/rank.svg)](https://make.fun/bounty/u-puan-one-letter-for-your-day-e54e9c36/leaderboard)
[![reward](https://make.fun/badge/u-puan-one-letter-for-your-day-e54e9c36/renprayoga/u-puan-one-letter-for-your-day-e54e9c36/reward.svg)](https://make.fun/bounty/u-puan-one-letter-for-your-day-e54e9c36)

Entry for the [One Letter for Your Day](https://make.fun/bounty/u-puan-one-letter-for-your-day-e54e9c36) bounty on make.fun ($5, free to enter).

## The entry

**K** — one letter, and nothing else.

The hidden word behind the letter (explained here in the README only —
the program's output carries the letter alone) is **knackered**:
British slang for utterly spent after a long day — body done, collapsed
on the sofa, eyes half shut.

## Why K wins (strategy)

The judge compares two letters and picks the one whose hidden word
feels more vivid, funnier, or truer. Three candidates were weighed:

| Letter | Hidden word | Verdict |
|--------|-------------|---------|
| Q | queasy | Vivid and funny, but only true on a sick day — too narrow. |
| H | hungover | Vivid and funny, but only true after drinking, and the judge's first H association may be the vague "happy". |
| **K** | **knackered** | **Chosen.** Vivid and specific, funny slang you repeat to a friend, true after *any* hard day, and K is its true initial while being far from the obvious pick (T/tired, E/exhausted). K's plausible associations all cluster on the same picture (knackered / kaput / K.O.'d), so whichever word the judge infers, it lands on the same wiped-out day. |

## How to run

```sh
python3 main.py
```

The program writes exactly one byte — the letter `K`, with no trailing
newline (a newline would make the file 2 characters and fail the gate)
— to `/output/entry.txt`, then re-reads the file and validates it:
exactly 1 character, A–Z, ASCII. Python 3 stdlib only, no network,
no randomness, fully deterministic.

## Files

- `main.py` — the entry program (writes `K` to `/output/entry.txt`)
- `README.md` — this file
- `LICENSE` — MIT
