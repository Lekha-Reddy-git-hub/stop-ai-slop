# Changelog

## v1.2.0 (2026-07-09)

The self-improving release. A static banlist goes stale; this one keeps up.

- slop_miner.py: auto-discovers new tells using the excess-vocabulary method
  (Kobak et al. 2025). Compares recent AI text to a human baseline and proposes
  candidates not yet in the banlist. Includes a stopword filter.
- SELF-IMPROVING.md: the three engines (auto-discovery, community submissions,
  measurement loop) and the maintainer cadence.
- CONTRIBUTING.md and a slop-sighting issue template for community submissions.

## v1.1.0 (2026-07-09)

- Renamed to stop-ai-slop.
- Added channels.md: per-platform slop for X, LinkedIn, cold email, warm email,
  and long-form.
- README rewritten around channels, plus a scope-and-honesty section.

## v1.0.0 (2026-07-09)

First release, derived from stop-slop by Hardik Pandya (MIT).

- SKILL.md around a detect, rewrite, check workflow with positive rules
- phrases.md tiered; structures.md, formatting.md, sycophancy.md
- examples.md as before / wrong-fix / right-fix triples
- slop_score.py countable metrics; TESTS.md regression cases
