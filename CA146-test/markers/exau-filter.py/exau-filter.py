#!/usr/bin/env python3

import sys
n = int(sys.argv[1])
a = sys.stdin.readlines()

i = 0
while i < len(a):
   m = int(a[i])
   if m % n == 0:
      print(m)
   i = i + 1
