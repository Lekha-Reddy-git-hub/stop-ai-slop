# Formatting slop

The biggest gap in most slop removers: they only police prose. Formatting is the
most visible AI tell of all. A reader spots an AI-formatted document before they
read a single word.

## Cut on sight

- **Bold-lead bullet walls.** Every bullet starting with a **bolded phrase:**
  followed by an explanation. Turns prose into a listicle. If it is genuinely
  prose, write paragraphs. Keep bullets only for true lists.
- **Header-per-paragraph.** A heading above every 2 to 3 sentences. Headings are
  for sections, not for decoration. Most short pieces need zero headings.
- **Emoji bullets and emoji section markers.** ✪ 🔑 🚀 as list glyphs or
  before every header. Cut unless the platform and author genuinely use them.
- **Bold sprinkled mid-sentence** to "emphasize" ordinary words. Emphasis loses
  meaning when everything is emphasized. Cut to at most rare, load-bearing bold.
- **The forced-parallel section titles.** Every header the same shape
  ("Build X", "Ship Y", "Scale Z"). Reads generated. Let sections be named by
  what they say.

## Cap, do not ban

- **Numbered lists.** Fine for real sequences. Slop when every idea is forced into
  "1, 2, 3" scaffolding. If the items are not sequential or countable, use prose.
- **Em-dashes.** The most-cited punctuation tell. Cap at the author's own baseline
  rate (see slop_score.py output). Default to commas, colons, or periods when
  unsure. A slop remover that itself leans on em-dashes is not credible.

## The plain-prose test

If a paragraph would read fine as sentences without any bullets, bold, or headers,
then it should be sentences. Structure earns its place only when it aids the
reader, not when it decorates the page.
