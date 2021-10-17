#!/usr/bin/env python

import sys

haystack = sys.argv[1]
needle = sys.argv[2]

found = False
i = 0
while i <= len(haystack) - len(needle) and haystack[i:i+len(needle)] != needle:
   i += 1

if i <= len(haystack) - len(needle):
   print i
else:
   print -1

