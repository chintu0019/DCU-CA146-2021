#!/usr/bin/env python

import sys
a = sys.stdin.readlines()

i = 0
while i < len(a):
   toks = a[i].split()
   j = 0
   while j < len(toks):
      if len(toks[j]) == 4:
         toks[j] = "****"
      j = j + 1
   print " ".join(toks)
   i = i + 1
