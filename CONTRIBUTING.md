# Contributing

stop-ai-slop gets better as more people feed it patterns. Two ways to help.

## Report a slop sighting

Spotted an AI tell the skill misses? Open an issue using the "Slop sighting"
template. Include:
- The exact slop phrase or structure.
- Where you saw it (X, LinkedIn, email, article, generic).
- Why it reads as a tell (one line).
- A human rewrite, if you have one.

Good sightings get added to the reference files and credited in the CHANGELOG.

## Submit a pull request

- New vocabulary or structure tells: add to the right tier in `phrases.md`,
  `structures.md`, `formatting.md`, `sycophancy.md`, or `channels.md`.
- Keep the tiering discipline: always-cut vs cut-unless-context vs
  frequency-capped. Do not blanket-ban a phrase that is sometimes correct.
- If you add an example, use the before / wrong-fix / right-fix format so it
  teaches the difference between de-slopping and over-correcting.
- Run `slop_score.py` on any sample text you add.

## Run the miner

If you have a corpus of recent AI text and human text, run `slop_miner.py` and
share the new high-excess candidates in an issue. That is the fastest way to keep
the banlist current as models change.

## Principle

The maintainer reviews everything before merge. Automation and community propose;
a human decides. That is what keeps quality from decaying as the list grows.
