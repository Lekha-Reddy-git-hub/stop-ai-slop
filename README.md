# deslop

**Remove AI tells from prose without flattening it into beige.**

AI writing has patterns: predictable phrases, structures, rhythms, and formatting.
This skill removes them. What makes it different from a plain banlist: it will not
trade one slop for another. Strip AI text with a naive remover and you get clipped,
punchy, LinkedIn-terse copy, which is its own tell. deslop is tiered and
context-aware, and it measures instead of guessing.

Based on [stop-slop](https://github.com/hardikpandya/stop-slop) by Hardik Pandya (MIT).
See "What changed" below.

## How it works: detect, rewrite, check

1. **Detect.** Run `slop_score.py` for objective counts: banned phrases, em-dash
   density, bullet-to-prose ratio, sentence-length variance, contrast-pivot count.
2. **Rewrite.** Fix only what fires. Preserve meaning, facts, quotes, and voice.
3. **Check.** Re-run the score. Confirm it improved AND that you did not
   over-correct into short-punchy slop.

## What it catches

- **Phrases** (`phrases.md`), tiered: always-cut vocabulary tells, cut-unless-context,
  and business jargon.
- **Structures** (`structures.md`): the "Not X. It is Y." pivot, rule-of-three,
  dramatic fragments, rhetorical scaffolding. Frequency-capped, not banned.
- **Formatting** (`formatting.md`): bold-lead bullet walls, header-per-paragraph,
  emoji bullets, em-dash overuse. The tell most removers miss.
- **Sycophancy and conclusion slop** (`sycophancy.md`): "Great question!", hedging
  stacks, "In conclusion", audience-hailing.

## What changed from stop-slop

- **Examples that pass their own rules.** The original's "after" examples were
  punchy quotables (banned by its own structures list). Here each example shows
  *before → wrong fix → right fix*.
- **Tiers, not blanket bans.** always-cut / cut-unless-context / frequency-capped,
  so it stops over-correcting harmless phrases.
- **Positive rules.** What good looks like (concrete nouns, varied rhythm, keep
  the author's words), not only what to remove.
- **New categories:** formatting slop and sycophancy/conclusion slop.
- **A real score.** `slop_score.py` gives countable metrics instead of a
  self-rated 1-to-10 rubric that LLMs game.

## Install

- **Claude Code:** copy this folder into `~/.claude/skills/deslop`
- **Claude.ai Projects:** upload `SKILL.md` plus the reference files
- **Anything else:** paste `SKILL.md` into your system prompt

## Pairs with voiceprint

deslop subtracts the machine. [voiceprint](https://github.com/Lekha-Reddy-git-hub/voiceprint)
adds the human: it renders your raw thoughts in your own measured voice. Use
deslop alone to clean text, or together to rewrite in your voice and de-slop in
one pass.

MIT. See LICENSE.
