#!/usr/bin/env python

import sys

lines = sys.stdin.readlines()
d = {}

i = 0
while i < len(lines):
   parse = lines[i].split()
   d[parse[0]] = parse[2]
   i = i + 1

for var in sorted(d):
   print var, d[var]
