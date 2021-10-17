#!/usr/bin/env python

import sys

s = sys.argv[1]

i = 1
while i < len(s):
   if s[i] == s[i-1]:
      s = s[:i] + s[i+1:]
   else:
      i += 1

print s
