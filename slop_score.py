#!/usr/bin/env python3
"""slop_score.py - objective slop detection. Part of deslop (MIT).

Counts machine tells so you measure instead of guessing. Lower banned-phrase and
formatting counts are better; HIGHER sentence-length variance is better (slop is
metronomic).

Usage:
  python3 slop_score.py text.txt
  python3 slop_score.py text.txt --json
"""
import re, sys, json, statistics, unicodedata

BANNED = [
    # vocabulary tells
    "delve", "delves", "tapestry", "testament to", "realm", "boasts", "nestled",
    "bustling", "underscore", "underscores", "elevate", "robust", "seamless",
    "myriad", "plethora", "leverage", "utilize", "game-changer", "deep dive",
    "in today's fast-paced", "ever-evolving",
    # dead phrases
    "it's worth noting", "it is worth noting", "it's important to note",
    "needless to say", "when it comes to", "at its core", "in essence",
    "let that sink in", "make no mistake", "here's the thing", "the truth is",
    "let me be clear", "at the end of the day",
    # sycophancy / conclusion / hailing
    "great question", "you're absolutely right", "i'd be happy to",
    "in conclusion", "to sum up", "all in all", "only time will tell",
    "whether you're a beginner", "in this article",
    # fake specificity
    "studies show", "research suggests", "experts agree", "it is widely known",
    # email openers
    "i hope this email finds you well", "i hope you're doing well",
    "i wanted to reach out",
]

def norm(t):
    return ''.join(unicodedata.normalize('NFKC', c) if 0x1D400 <= ord(c) <= 0x1D7FF else c for c in t)

def score(text):
    bold_unicode = sum(1 for c in text if 0x1D400 <= ord(c) <= 0x1D7FF)
    t = norm(text)
    low = t.lower()
    words = re.findall(r"[A-Za-z0-9'+-]+", t)
    n = max(len(words), 1)
    sents = [s for s in re.split(r'(?<=[.!?])\s+', t) if s.strip()]
    slens = [l for l in (len(re.findall(r"[A-Za-z0-9'+-]+", s)) for s in sents) if l > 0]
    lines = [l for l in t.split("\n") if l.strip()]
    bullet_lines = sum(1 for l in lines if re.match(r'\s*([-*•✪🔑🚀]|\d+\.)\s', l))
    hits = {}
    for p in BANNED:
        c = low.count(p)
        if c:
            hits[p] = c
    contrast = len(re.findall(r"\b(?:not|isn't|aren't|no longer)\b[^.!?]{0,55}[.!?]\s+(?:It is|It's|They are|That is|That's)", t, re.I))
    result = {
        "words": n,
        "banned_phrase_total": sum(hits.values()),
        "banned_phrases": hits,
        "contrast_pivots_notX_itisY": contrast,
        "em_dash_per_1k": round(1000 * text.count("—") / n, 1),
        "sentence_len_stdev": round(statistics.stdev(slens), 1) if len(slens) > 1 else 0,
        "bullet_line_pct": round(100 * bullet_lines / max(len(lines), 1)),
        "bold_unicode_headers": bold_unicode,
    }
    # crude 0-100 slop index (higher = more slop). For guidance, not a verdict.
    idx = min(100,
              6 * result["banned_phrase_total"] +
              8 * max(0, contrast - 1) +
              2 * max(0, result["em_dash_per_1k"] - 4) +
              max(0, result["bullet_line_pct"] - 20) +
              (10 if bold_unicode else 0))
    result["slop_index_0_100"] = round(idx)
    return result

def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if not args:
        print(__doc__); sys.exit(1)
    r = score(open(args[0], encoding="utf-8").read())
    if "--json" in sys.argv:
        print(json.dumps(r, indent=2)); return
    print(f"slop_index (0-100, lower better): {r['slop_index_0_100']}")
    print(f"banned phrases: {r['banned_phrase_total']}  {r['banned_phrases'] or ''}")
    print(f"contrast pivots (cap 1): {r['contrast_pivots_notX_itisY']}")
    print(f"em-dash per 1k words: {r['em_dash_per_1k']}")
    print(f"sentence-length stdev (higher better): {r['sentence_len_stdev']}")
    print(f"bullet-line %: {r['bullet_line_pct']}")
    print(f"bold-unicode headers: {r['bold_unicode_headers']}")

if __name__ == "__main__":
    main()
