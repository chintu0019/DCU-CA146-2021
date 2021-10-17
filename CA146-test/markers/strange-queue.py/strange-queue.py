#!/usr/bin/env python

import sys

tokens = sys.stdin.read().split()
q = []

i = 0
while i < len(tokens):
   if tokens[i] == "-":
      q.pop()
   else:
      q.append(tokens[i])
   i = i + 1

i = 0
while i < len(q):
   print q[i]
   i = i + 1
