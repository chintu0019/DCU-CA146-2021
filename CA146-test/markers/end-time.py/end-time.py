#!/usr/bin/env python

# The main ideas here are:
#
#   1. Normalise the input (to five characters) so that we do not have to
#      handle cases like "9:05" and "19.05" separately.
#   2. Convert everything to "minutes passed midnight", because with that
#      representation, the arithmetic logic becomes straightforward.
#
# Variable naming:
#   "s": start
#   "d": duration
#   "e": end
#
# Suffixes:
#   "h": hours
#   "m": minutes

import sys

s = sys.argv[1]           # "13:30"
d = sys.argv[2]           # "1:45"

# Ensure start and duration are both "XX:XX" (so, 5 characters).
if len(s) < 5:
   s = "0" + s            # "13:30"

if len(d) < 5:
   d = "0" + d            # "01:45"

# Convert to integers, and then minutes since midnight.
sh = int(s[:2])           # 13 (integers, now)
sm = int(s[3:])           # 30

dh = int(d[:2])           # 1
dm = int(d[3:])           # 45

s = 60 * sh + sm          # 810 (minutes since midnight)
d = 60 * dh + dm          # 105

# The end minutes-since-midnight is just the sum of the start and the duration.
e = (s + d) % (24 * 60)   # 915

# Convert back to hours and minutes.
eh = e / 60               # 15
em = e % 60               # 15

if em < 10:
   # Convert small integer minutes (e.g. 9) to two digits (e.g. "09").
   em = "0" + str(em)

print str(eh) + ":" + str(em)
