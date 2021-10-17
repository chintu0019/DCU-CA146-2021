#!/usr/bin/env python3

import sys

with open(sys.argv[1]) as f:
   s = f.read()
with open(sys.argv[2]) as f:
   t = f.read()

i = 0
while i < len(s) and i < len(t) and s[i] == t[i]:
   i = i + 1

if i < len(s) or i < len(t):
   same = s[:i]
   lines = same.split("\n")
   last = lines[len(lines) - 1]
   print(len(lines) - 1, len(last))
