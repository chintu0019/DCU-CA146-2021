#!/usr/bin/env python

import sys

number = int(sys.argv[1])
lines = []

line = raw_input()
while line != "end":
   if len(lines) < number:
      lines.append(line)
   else:
      lines.pop(0)
      lines.append(line)
   line = raw_input()

for line in lines:
   print line
