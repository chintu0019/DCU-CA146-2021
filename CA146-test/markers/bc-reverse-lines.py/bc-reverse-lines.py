#!/usr/bin/env python

lines = []

line = raw_input()
while line != "end":
   lines.append(line)
   line = raw_input()

i = 0
while i < len(lines):
   print lines[len(lines)-1-i]
   i = i + 1

