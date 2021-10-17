#!/usr/bin/env python

import sys
lines = sys.stdin.readlines()

counts = {}

i = 0
while i < len(lines):
   parse = lines[i].split()[0].split("/")
   month = int(parse[1])
   if month not in counts:
      counts[month] = 0
   counts[month] += 1
   i = i + 1

for key in sorted(counts):
   print key, counts[key]
