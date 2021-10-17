#!/usr/bin/env python

import sys

s = sys.argv[1]
lines = []

line = raw_input()
while line != "end":
   lines.append(line)
   line = raw_input()

i = 0
while i < len(lines):
   if 0 <= lines[i].find(s):
      print lines[i]
   i = i + 1

