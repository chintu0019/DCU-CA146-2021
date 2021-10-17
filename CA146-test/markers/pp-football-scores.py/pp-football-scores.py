#!/usr/bin/env python

import sys
score = int(sys.argv[1])

# n, below, is the number of different possible goal counts.  E.g., if score
# is 5, then there are two possibilities: 0 or 1, so n is 2.
n = score / 3 + 1

i = 0
while i < n:
   print i, score - (3 * i)
   i = i + 1
