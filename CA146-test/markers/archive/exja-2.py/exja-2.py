#!/usr/bin/env python3

import sys
s = sys.argv[1]
a = sys.stdin.read().split()

i = 0
while i < len(a):
   if len(s) <= len(a[i]) and a[i][len(a[i]) - len(s):] == s:
      pass
   else:
      print(a[i])
   i = i + 1
