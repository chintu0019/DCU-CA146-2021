#!/usr/bin/env python

# Example argument: "aaaaaaaabbbbb"
#
# First iteration:  "aaaaaaaabbbbb"
#                    |       |
#                    i       j
#
# Second iteration: "aaaaaaaabbbbb"
#                            |    |
#                            i    j
#
# Observe that the position j after the first iteration becomes the position
# i for the second iteration.
#
# Also, if i < len(s), then at least one run remains.
#

import sys
s = sys.argv[1]

i = 0
while i < len(s):
   j = i                              # Linear search.
   while j < len(s) and s[j] == s[i]: #
      j = j + 1                       #

   print s[i], j - i
   i = j
