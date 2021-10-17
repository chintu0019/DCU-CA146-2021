#!/usr/bin/env python

lines = []

line = raw_input()
while line != "end":
   lines.append(int(line))
   line = raw_input()

t = 0
i = 0
while i < len(lines):
   t += lines[i]
   i = i + 1

try:
   print t / len(lines)
except:
   print t

