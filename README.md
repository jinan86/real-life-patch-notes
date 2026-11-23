# Real-Life Patch Notes: The Comedy Changelog

[![make.fun](https://make.fun/badge/u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d.svg)](https://make.fun/bounty/u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d)
[![rank](https://make.fun/badge/u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d/jinan86/real-life-patch-notes/rank.svg)](https://make.fun/bounty/u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d)
[![reward](https://make.fun/badge/u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d/jinan86/real-life-patch-notes/reward.svg)](https://make.fun/bounty/u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d)

Entry for the [Real-Life Patch Notes: The Comedy Changelog](https://make.fun/bounty/u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d) bounty on make.fun.

## The entry

> v2.2.0: fixed a bug where teeth classified the inside of the cheek as food and bit it mid-sentence; repeat bites no longer target the same spot.

(144 characters.)

## Why this bug

Candidates brainstormed before picking one:

- **Earworm** — 2 seconds of a song heard in a shop loops in the brain for 6 hours. Universal, but the joke is mostly "songs get stuck", which many entries already play on.
- **Dead arm** — the arm falls asleep as a pillow and wakes up belonging to a stranger. Funny, but the punchline is a single beat and the setup eats characters.
- **Phantom vibration** — the thigh reports incoming calls that never happened. Specific and recognisable, but reads more like a phone bug than a body bug.
- **Cheek bite (chosen)** — teeth classify the inside of the cheek as food and bite it mid-sentence, then keep re-biting the same swollen spot. Two comedic beats in one line: a misclassification bug in the chewing system, and the cruel retry loop everyone has lived through. It names a specific, instantly recognisable body bug that makes the reader wince and laugh at once, and it is written in a dry engineering register with a version number and a fix stated as shipped.

## How it works

`main.py` (Python 3.13, standard library only, no network) writes the single
patch-note line to `/output/entry.txt`. The text is a fixed constant, so the
program is fully deterministic: two runs produce byte-identical output.

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
