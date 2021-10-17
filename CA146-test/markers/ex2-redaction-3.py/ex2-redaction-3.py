#!/usr/bin/env python

import sys

lines = sys.stdin.readlines()

d = {
   "Mary": True,
   "lamb": True,
}

for line in lines:
   tokens = line.split()
   i = 0
   while i < len(tokens):
      token = tokens[i]
      if token in d:
         tokens[i] = "XXXX"
      i = i + 1
   for token in tokens:
      print token


