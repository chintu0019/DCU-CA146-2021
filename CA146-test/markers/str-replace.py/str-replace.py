#!/usr/bin/env python

import sys

haystack = sys.argv[1]
needle = sys.argv[2]
replacement = sys.argv[3]

i = 0
while i <= len(haystack) - len(needle):
   if haystack[i:i+len(needle)] == needle:
      haystack = haystack[0:i] + replacement + haystack[i+len(needle):]
      i += len(replacement)
   else:
      i += 1

print haystack

