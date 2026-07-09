# How stop-ai-slop stays current

Most slop removers are a static list that one person maintains. Slop evolves with
every new model, so a static list goes stale. stop-ai-slop is built to keep up
through a human-in-the-loop loop with three engines. You (the maintainer) always
review before anything merges, so quality does not decay.

## Engine 1: auto-discovery (slop_miner.py)

Based on the excess-vocabulary method (Kobak et al., Science Advances 2025): AI
tells show up as words and phrases over-represented in machine text versus a human
baseline. `slop_miner.py` measures that excess and proposes NEW candidate tells
that are not yet in the banlist.

Run it whenever new models ship:

    python3 slop_miner.py --ai recent_ai_text/ --human human_baseline/

Grow both corpora over time. The bigger they get, the sharper the signal. The
miner only proposes; you decide what to add to `phrases.md`.

## Engine 2: community submissions

Thousands of readers catch tells one person never will. Anyone can open a
"slop sighting" issue with a pattern they spotted (there is a template). Good
submissions get added and credited. This is distributed maintenance: the banlist
improves as more people use it.

## Engine 3: the measurement loop

`slop_score.py` runs against a growing set of known-AI and known-human samples in
`TESTS.md`. When it misfires (flags human writing, or misses AI writing), that is
a signal to tune the rules or weights. Same principle as automated essay scoring
eval harnesses: measure, compare to ground truth, adjust.

## The cadence

1. New model ships or a submission arrives.
2. Run the miner and review new candidates; triage submissions.
3. Update the reference files; bump the version in CHANGELOG.
4. Re-run the test corpus to confirm nothing regressed.

Slop is time-indexed. "Delve" was a 2024 tell. This repo tracks the moving target
instead of freezing one snapshot of it.
