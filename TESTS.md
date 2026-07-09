# Test cases

Run `slop_score.py` on each SLOP sample; the index should be high. Run it on the
CLEAN rewrite; the index should drop and sentence-length stdev should rise. Use
these to catch regressions when you edit the rules.

## Case 1
SLOP: "In today's fast-paced landscape, let's delve into the robust, seamless
tapestry of productivity. Here's the thing: it's worth noting that great teams
leverage synergy. Full stop."
EXPECT: high banned-phrase count (delve, robust, seamless, tapestry, here's the
thing, it's worth noting, leverage), slop_index > 50.
CLEAN: "Productive teams share one habit: they cut meetings that have no agenda."
EXPECT: banned = 0, higher sentence variety.

## Case 2 (over-correction trap)
SLOP: "Building products is hard. Not because of technology. Because of people."
BAD REWRITE: "Products are hard. Tech is easy. People aren't." (still fragments +
contrast pivot; slop_index should NOT improve much.)
GOOD REWRITE: "Building products is hard, and technology is rarely the reason;
the hard part is people."
EXPECT: contrast_pivots drops to 0, stdev rises.

## Case 3 (formatting)
SLOP: bold-lead bullet wall with emoji markers (✪) and bold-unicode headers.
EXPECT: bullet_line_pct high, bold_unicode_headers > 0.
CLEAN: same content as two prose sentences.
EXPECT: bullet_line_pct near 0, bold_unicode_headers = 0.

## Case 4 (sycophancy)
SLOP: "Great question! You're absolutely right. In conclusion, only time will tell."
EXPECT: banned hits on great question, you're absolutely right, in conclusion,
only time will tell.
CLEAN: a direct answer with a specific next step.
