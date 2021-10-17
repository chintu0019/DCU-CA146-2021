#!/usr/bin/env python

import sys

s = sys.argv[1]

t = ""
i = 0
while i < len(s):
   t = s[i] + t
   i = i + 1

print t

