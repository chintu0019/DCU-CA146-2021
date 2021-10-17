#!/usr/bin/env python3

n = 8
longest = ""

i = 0
while i < n:
   line = input()
   if len(longest) < len(line):
      longest = line
   i = i + 1

print(longest)
