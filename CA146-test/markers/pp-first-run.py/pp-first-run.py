#!/usr/bin/env python

import sys
n = int(sys.argv[1])
s = sys.argv[2]

i = 0
while i < len(s) and s[i:i+n] != s[i] * n:
   i = i + 1

print s
print " " * i + "|"
