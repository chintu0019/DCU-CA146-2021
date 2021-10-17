#!/usr/bin/env python

lines = []

line = raw_input()
while line != "end":
   lines.append(line)
   line = raw_input()

i = 0
while i < len(lines):
   line = lines[len(lines)-1-i]
   t = ""
   while line:
      t = line[0] + t
      line = line[1:]
   print t
   i = i + 1

