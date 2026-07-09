#!/usr/bin/env python3
"""slop_miner.py - auto-discover NEW slop as models change. Part of stop-ai-slop (MIT).

The idea (from Kobak et al., Science Advances 2025): AI tells show up as words and
phrases that are OVER-REPRESENTED in machine text compared to a human baseline.
"delves" rose 28-fold after ChatGPT. This script measures that excess so the banlist
stays current instead of going stale.

How it works:
  1. You give it recent AI-written text (ai_corpus) and human-written text (baseline).
  2. It counts word and 2-gram frequencies in each, per 10k tokens.
  3. Excess ratio = ai_rate / (human_rate + smoothing).
  4. It ranks candidates by excess, flags which are already in phrases.md, and prints
     the NEW ones for you to review and add. Human-in-the-loop: you merge, not the script.

Usage:
  python3 slop_miner.py --ai ai_samples.txt --human human_baseline.txt
  python3 slop_miner.py --ai ai/ --human human/ --min-count 3 --top 40
  (folders are read recursively; .txt and .md files)

Grow the corpora over time; accuracy scales with size. Seed files are tiny on
purpose so the method is visible, not authoritative.
"""
import re, sys, os, argparse, unicodedata
from collections import Counter

STOPWORDS = set(
    "the a an and or but if then this that these those is are was were be been being "
    "to of in on at by for with from into over under as it its it's we you they he she "
    "i me my our your their them his her must can will would should could have has had "
    "do does did not no so than too very just about out up down off which who what when "
    "where why how all any both each more most other some such only own same also".split()
)

def norm(t):
    return ''.join(unicodedata.normalize('NFKC', c) if 0x1D400 <= ord(c) <= 0x1D7FF else c for c in t)

def read_corpus(path):
    texts = []
    if os.path.isdir(path):
        for root, _, files in os.walk(path):
            for f in files:
                if f.endswith((".txt", ".md")):
                    texts.append(open(os.path.join(root, f), encoding="utf-8", errors="ignore").read())
    else:
        texts.append(open(path, encoding="utf-8", errors="ignore").read())
    return norm("\n".join(texts)).lower()

def grams(text):
    words = re.findall(r"[a-z][a-z'-]+", text)
    unigrams = Counter(words)
    bigrams = Counter(f"{a} {b}" for a, b in zip(words, words[1:]))
    return unigrams, bigrams, max(len(words), 1)

def load_known(phrases_path):
    if not os.path.exists(phrases_path):
        return set()
    return set(re.findall(r"[a-z][a-z'-]+(?:\s[a-z][a-z'-]+)?", open(phrases_path, encoding="utf-8").read().lower()))

def rate(counter, total):
    return {k: 10000 * v / total for k, v in counter.items()}

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ai", required=True, help="AI-written text file or folder")
    ap.add_argument("--human", required=True, help="human-written baseline file or folder")
    ap.add_argument("--phrases", default="phrases.md", help="existing banlist to diff against")
    ap.add_argument("--min-count", type=int, default=3, help="min occurrences in AI corpus")
    ap.add_argument("--top", type=int, default=30)
    ap.add_argument("--smoothing", type=float, default=0.5)
    a = ap.parse_args()

    ai = read_corpus(a.ai)
    hu = read_corpus(a.human)
    ai_uni, ai_bi, ai_n = grams(ai)
    hu_uni, hu_bi, hu_n = grams(hu)
    known = load_known(a.phrases)

    def candidates(ai_counts, hu_counts):
        ar, hr = rate(ai_counts, ai_n), rate(hu_counts, hu_n)
        out = []
        for term, c in ai_counts.items():
            if c < a.min_count or len(term) < 4:
                continue
            parts = term.split()
            if all(p in STOPWORDS for p in parts):
                continue
            excess = ar[term] / (hr.get(term, 0) + a.smoothing)
            if excess >= 2.0:
                out.append((term, round(excess, 1), c, term in known))
        return sorted(out, key=lambda x: -x[1])[:a.top]

    print(f"AI corpus: {ai_n} tokens | human baseline: {hu_n} tokens\n")
    print("Excess terms (candidate slop). NEW = not yet in your banlist.\n")
    print(f"{'term':30} {'excessx':>8} {'count':>6}  status")
    print("-" * 56)
    rows = candidates(ai_uni, hu_uni) + candidates(ai_bi, hu_bi)
    rows = sorted(rows, key=lambda x: -x[1])[:a.top]
    for term, ex, c, isknown in rows:
        print(f"{term:30} {ex:>8} {c:>6}  {'known' if isknown else 'NEW -> review'}")
    print("\nReview the NEW rows. Add the real tells to phrases.md. You decide; the miner only proposes.")

if __name__ == "__main__":
    main()
