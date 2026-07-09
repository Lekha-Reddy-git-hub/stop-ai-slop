# stop-ai-slop

**Make anything you write sound human again: X posts, LinkedIn posts, cold and
warm emails, and articles. Without collapsing into the short-punchy style that
just trades one kind of slop for another.**

AI writing has patterns: predictable phrases, structures, rhythms, and
formatting. This skill removes them. What makes it different from a plain
banlist: it will not trade one slop for another. Strip AI text with a naive
remover and you get clipped, punchy, LinkedIn-broetry copy, which is its own
tell. stop-ai-slop is tiered, context-aware, channel-aware, and it measures
instead of guessing.

Not a detector-bypass tool. The goal is writing that is actually better, not
writing that sneaks past an AI checker. See "Scope and honesty" below.

Based on [stop-slop](https://github.com/hardikpandya/stop-slop) by Hardik Pandya (MIT).

## Why per-channel matters

Slop wears a different costume on each platform, so one generic pass is not
enough. A cold email and a LinkedIn post fail in completely different ways.
`channels.md` handles each one. Here is how and why it helps the writing you
actually send:

- **X / Twitter posts.** Cuts thread-bait ("A thread", "Let's dive in"),
  guru hook formulas, and "follow for more". Result: one clear idea in the first
  line, a concrete specific instead of a general claim, and a post that stands on
  its own.
- **LinkedIn posts.** Removes the most recognizable slop anywhere: bold-unicode
  fake headers, broetry line breaks, emoji bullets, "Here's the thing", and the
  recap-everything close. Result: normal paragraphs, one lived-experience claim,
  and an ending that lands on the strongest idea rather than a poll.
- **Cold email.** Kills "I hope this email finds you well", fake personalization,
  and three paragraphs of throat-clearing before the ask. Result: a first line
  that could only go to that person, one early ask, and a short message that
  respects their time.
- **Warm email.** Strips the over-formality you would never use in person:
  "circling back", "per my last email", corporate hedging with people you know.
  Result: writing that matches the warmth already there.
- **Articles.** Removes "in this article we'll explore", header-per-paragraph
  skeletons, and restate-everything conclusions. Result: prose that starts in the
  material and ends on one idea.

## How it works: detect, rewrite, check

1. **Detect.** Run `slop_score.py` for objective counts: banned phrases, em-dash
   density, bullet-to-prose ratio, sentence-length variance, contrast-pivot count.
2. **Rewrite.** Fix only what fires. Apply the channel layer from `channels.md`.
   Preserve meaning, facts, quotes, and voice.
3. **Check.** Re-run the score. Confirm it improved AND that you did not
   over-correct into short-punchy slop.

## What it catches

- **Phrases** (`phrases.md`), tiered: always-cut vocabulary tells,
  cut-unless-context, business jargon, fake specificity.
- **Structures** (`structures.md`): the "Not X. It is Y." pivot, rule-of-three,
  dramatic fragments, rhetorical scaffolding. Frequency-capped, not banned.
- **Formatting** (`formatting.md`): bold-lead bullet walls, header-per-paragraph,
  emoji bullets, em-dash overuse.
- **Sycophancy and conclusion slop** (`sycophancy.md`): "Great question!",
  hedging stacks, "In conclusion", audience-hailing.
- **Channel tells** (`channels.md`): per-platform slop for X, LinkedIn, cold and
  warm email, and long-form.

## What changed from stop-slop

- **Per-channel guidance.** The original treats every piece of writing the same.
  This adds distinct logic for X, LinkedIn, cold email, warm email, and articles.
- **Examples that pass their own rules.** Each example shows
  *before, wrong fix, right fix*, so it teaches the difference between
  de-slopping and over-correcting into a second slop.
- **Tiers, not blanket bans.** always-cut / cut-unless-context / frequency-capped.
- **Positive rules.** What good looks like, not only what to remove.
- **A real score.** `slop_score.py` gives countable metrics instead of a
  self-rated rubric.

## Scope and honesty

- This is a writing-improvement tool, not an AI-detector bypass. Detection tools
  are unreliable and biased against non-native English writers
  ([Liang et al., Patterns 2023](https://arxiv.org/abs/2304.02819)), so "beat the
  detector" is not a goal here.
- A banlist can remove tells but cannot guarantee good writing. Use the score as a
  guide, then read the result with human judgment.

## Pairs with voiceprint

stop-ai-slop subtracts the machine.
[voiceprint](https://github.com/Lekha-Reddy-git-hub/voiceprint) adds the human: it
learns your voice from your own writing and renders your raw thoughts in it.
Together they rewrite in your voice and de-slop in one pass. That pairing, sound
like YOU rather than sound generically human, is the part no humanizer does.

## Install

- **Claude Code:** copy this folder into `~/.claude/skills/stop-ai-slop`
- **Claude.ai Projects:** upload `SKILL.md` plus the reference files
- **Anything else:** paste `SKILL.md` into your system prompt

MIT. See LICENSE.
