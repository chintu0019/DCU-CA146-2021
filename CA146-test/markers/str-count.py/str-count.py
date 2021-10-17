#!/usr/bin/env python

import sys

haystack = sys.argv[1]
needle = sys.argv[2]
count = 0

i = 0
while i < len(haystack) - len(needle) + 1:
   if haystack[i:i+len(needle)] == needle:
      count += 1
      i += len(needle)
   else:
      i += 1

print count

