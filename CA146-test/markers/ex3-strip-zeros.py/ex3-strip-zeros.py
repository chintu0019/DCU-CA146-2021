#!/usr/bin/env python

import sys
nos = sys.stdin.read().split()

i = 0
while i < len(nos):
   s = nos[i]

   n = len(s) - 1
   j = 0
   while j < n and s[j] == "0":
      j = j + 1

   print s[j:]
   i = i + 1
