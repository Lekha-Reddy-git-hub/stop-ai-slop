---
name: deslop
description: Remove AI tells from prose without flattening it into beige. A tiered, context-aware slop remover that detects machine patterns, rewrites them, and preserves meaning and the author's voice. Use when the user wants to clean AI-generated or AI-assisted text, asks "make this sound less like AI", or wants an objective slop score.
---

# deslop

AI writing has patterns: predictable phrases, structures, rhythms, and formatting.
This skill removes them. It does NOT replace them with a second slop (clipped,
punchy, LinkedIn-terse). The goal is prose that is direct, varied, and human,
not prose that is merely short.

Based on stop-slop by Hardik Pandya (MIT). See README for what changed.

## Workflow: detect, then rewrite, then check

1. **Detect.** Read the whole text. Run `slop_score.py` for objective counts
   (banned phrases, em-dash density, bullet-to-prose ratio, sentence-length
   variance). Note what actually fires; do not guess.
2. **Rewrite.** Fix only what the detectors flag. Preserve meaning, facts,
   quotes, and technical terms exactly. Preserve the author's voice if one is
   given (pair with a voice profile if available).
3. **Check.** Re-run `slop_score.py`. Confirm the score improved AND that you did
   not overcorrect into the opposite slop (see "Do not overcorrect" below).

## The tiers (see phrases.md, structures.md, formatting.md, sycophancy.md)

- **Always cut:** vocabulary tells and dead phrases that carry no meaning.
- **Cut unless context justifies it:** phrases that are sometimes correct. Keep
  when the sentence genuinely needs them; cut when they are reflexive.
- **Frequency-capped:** devices that are fine once and slop when repeated
  (em-dashes, rule-of-three, sentence-initial "And/But", dramatic fragments).

## Positive rules (what good looks like, not just what to remove)

Removing slop leaves a hole. Fill it with substance, not with punch.
- Prefer concrete nouns, numbers, and named things over abstraction.
- Keep the author's own words and rhythm. Do not upgrade their vocabulary.
- Vary sentence length on purpose. Slop is metronomic in both directions:
  all-long (GPT default) and all-short (over-corrected).
- State claims plainly. Trust the reader to follow without scaffolding.

## Do not overcorrect

The most common failure is trading one slop for another. After rewriting, the
text must not be:
- All short punchy fragments (that is its own tell).
- A stack of binary contrasts ("Not X. It is Y.") repeated every paragraph.
- Stripped of the author's real quirks, which are features, not slop.

## Scoring (countable, not self-rated)

Do not ask the model to "rate this 1 to 10"; LLMs self-score generously.
Use `slop_score.py` output: banned-phrase hits, em-dash per 1k words,
bullet-to-prose ratio, sentence-length standard deviation. Report the numbers
before and after. Lower banned-phrase count and HIGHER sentence-length variance
is the target.
