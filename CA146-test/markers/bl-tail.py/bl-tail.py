#!/usr/bin/env python

import sys

n = int(sys.argv[1])
lines = []

line = raw_input()
while line != "end":
   lines.append(line)
   line = raw_input()

pos = len(lines) - n
if pos < 0:
   pos = 0

while pos < len(lines):
   print lines[pos]
   pos += 1
