#!/usr/bin/env python

import sys

lines = sys.stdin.readlines()

d = {
}

for token in sys.argv[1:]:
   d[token] = True

for line in lines:
   tokens = line.split()
   i = 0
   while i < len(tokens):
      token = tokens[i]
      if token in d:
         tokens[i] = "XXXX"
      i = i + 1
   print " ".join(tokens)


