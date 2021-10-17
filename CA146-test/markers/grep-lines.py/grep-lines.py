#!/usr/bin/env python3

import sys
pattern = sys.argv[1]

line = input()
while line != "end":
   i = 0
   while i < len(line) and line[i:i + len(pattern)] != pattern:
      i = i + 1

   if i < len(line):
      print(line)
   line = input()
