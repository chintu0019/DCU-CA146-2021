#!/usr/bin/env python

import sys

n = int(sys.argv[1])
line = raw_input()

while line != "end":
   if len(line) < n:
      line = line.strip()
      spaces = n - len(line)
      left = spaces / 2
      print " " * left + line
   else:
      print line
   line = raw_input()
