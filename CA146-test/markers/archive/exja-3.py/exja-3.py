#!/usr/bin/env python3

import sys
lines = sys.stdin.readlines()

a = []

i = 0
while i < len(lines):
   toks = lines[i].split()
   a.append(" ".join([toks[1], toks[0]]))
   i = i + 1

i = 0
while i < len(a):
   # loop invariant:
   #   - a[p] is the minimum value in a[i:j]
   p = i
   j = i + 1
   while j < len(a):
      if a[j] < a[p]:
         p = j
      j = j + 1

   # swap a[i] and a[p]
   tmp = a[p]
   a[p] = a[i]
   a[i] = tmp

   i = i + 1

i = 0
while i < len(a):
   toks = a[i].split()
   print(toks[1], toks[0])
   i = i + 1
