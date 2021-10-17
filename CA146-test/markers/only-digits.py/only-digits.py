#!/usr/bin/env python

import sys

s = sys.argv[1]
t = ""

i = 0
while i < len(s):
   if s[i].isdigit():
      t = t + s[i]
   i = i + 1

print t
