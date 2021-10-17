#!/usr/bin/env python

import sys

s = sys.argv[1]
lines = []

line = raw_input()
while line != "end":
   lines.append(line)
   line = raw_input()

count = 0
i = 0
while i < len(lines):
   if 0 <= lines[i].find(s):
      count += 1
   i = i + 1

print count

