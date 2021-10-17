#!/usr/bin/env python

import sys
longest = sys.argv[1]

i = 2
while i < len(sys.argv):
   if len(longest) < len(sys.argv[i]):
      longest = sys.argv[i]
   i = i + 1

print longest
