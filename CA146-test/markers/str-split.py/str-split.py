#!/usr/bin/env python

import sys

haystack = sys.argv[1]
needle = sys.argv[2]

i = 0
while i <= len(haystack) - len(needle):
   if haystack[i:i+len(needle)] == needle:
      print haystack[:i]
      haystack = haystack[i+len(needle):]
      i = 0
   else:
      i += 1

print haystack
