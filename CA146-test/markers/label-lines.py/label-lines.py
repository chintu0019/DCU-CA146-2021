#!/usr/bin/env python3

lines = []

line = input()
while line != "end":
   lines.append(line)
   line = input()

i = 0
while i < len(lines):
   print(i, len(lines), lines[i])
   i = i + 1
