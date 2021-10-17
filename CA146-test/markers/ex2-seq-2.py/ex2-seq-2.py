#!/usr/bin/env python3

import sys
args = sys.argv[1:]

if len(args) == 1:
   i = 0
   n = int(args[0])
else:
   i = int(args[0]) - 1
   n = int(args[1])

while i < n:
   print(i + 1)
   i = i + 1
