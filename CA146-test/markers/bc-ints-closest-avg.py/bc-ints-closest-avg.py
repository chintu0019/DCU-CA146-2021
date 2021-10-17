#!/usr/bin/env python

lines = []

line = raw_input()
while line != "end":
   lines.append(int(line))
   line = raw_input()

t = 0.0
i = 0
while i < len(lines):
   t += lines[i]
   i = i + 1

try:
   average = t / len(lines)
   nearest = lines[0]
except:
   average = t
   nearest = 0

i = 1
while i < len(lines):
   if abs(average - lines[i]) < abs(average - nearest):
      nearest = lines[i]
   i = i + 1

print nearest
