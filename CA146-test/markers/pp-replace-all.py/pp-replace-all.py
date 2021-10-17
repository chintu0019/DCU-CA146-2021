#!/usr/bin/env python

# Variables:
#
# "s" is the current line.
# "t" is the new line (the one that will be printed).
#
# "i" scans through "s".
# "j" is the loop variable for linear search, finding the position of
#     the next match.
#
# Example:
#   This line contains the PATTERN text.
#   |                      |
#   i                      j      | j + len(PATTERN)
#                                 |
#   t = t + s[i:j] + REPLACEMENT  |
#   i = j + len(PATTERN)          |
#                                 |
# Then:                           |
#                                 |
#   This line contains the PATTERN text.
#                                 |     |
#                                 i     j

import sys
pattern = sys.argv[1]
replacement = sys.argv[2]

s = raw_input()
while s != "END":
   t = ""

   i = 0
   while i < len(s):
      j = i                                                 # Linear search.
      while j < len(s) and s[j:j+len(pattern)] != pattern:  #
         j = j + 1                                          #

      t = t + s[i:j]                   # Copy everything before the match to t.
      i = j

      if i < len(s):                   # A match was found.
         t = t + replacement           # Copy replacement to t.
         i = j + len(pattern)          # Move to the position after the match.

   print t
   s = raw_input()
