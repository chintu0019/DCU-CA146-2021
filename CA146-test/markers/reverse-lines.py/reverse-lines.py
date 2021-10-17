#!/usr/bin/env python3

lines = []

line = input()
while line != "end":
   lines.append(line)
   line = input()

i = 0
while i < len(lines):
   print(lines[len(lines) - i - 1])
   i = i + 1
