#!/usr/bin/env python3

# Example, n is 5:
#
#   *
#  ***
# *****
#  ***
#   *

# Idea, for n is 7:
#
# j = i * 2 + 1
#
# So, j takes on these values...
#
#    |     |     |     |     |     |     |
# 00 01 02 03 04 05 06 07 08 09 10 11 12 13 14
#    |     |     |     |     |     |     |   | 1 = 7 - (13 % 7)
#                            |     |     |---|
#                            |     |         | 3 = 7 - (11 % 7)
#                            |     |---------|
#                            |               | 5 = 7 - (9 % 7)
#                            |---------------|
#
# For the top half (up to 7), the number of asterisks is just j;
# the hard case is bottom half.  For those cases, see the statement
# marked "X" below, and the illustration above.
#
# At the point of the print, j is the required number of "*"s.
#

import sys
n = int(sys.argv[1])

i = 0
while i < n:
   j = i * 2 + 1
   if n < j:
      j = n - j % n                   # X (see example above).
   print(" " * ((n - j) // 2) + "*" * j)
   i = i + 1
