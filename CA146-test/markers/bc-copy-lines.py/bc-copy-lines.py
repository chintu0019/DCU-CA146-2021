#!/usr/bin/env python

import sys

n = int(sys.argv[1])
lines = []

i = 0
while i < n:
   lines.append(raw_input())
   i += 1

print lines
