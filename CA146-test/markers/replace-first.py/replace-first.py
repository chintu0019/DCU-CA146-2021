#!/usr/bin/env python

import sys
pattern = sys.argv[1]
replacement = sys.argv[2]

line = raw_input()
while line != "end":
   i = 0
   while i < len(line) and line[i:i+len(pattern)] != pattern:
      i = i + 1

   if i < len(line):
      line = line[0:i] + replacement + line[i+len(pattern):]

   print line
   line = raw_input()
