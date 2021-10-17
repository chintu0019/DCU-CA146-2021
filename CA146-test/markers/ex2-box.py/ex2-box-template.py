#!/usr/bin/env python3

ch = "CHARACTER"

import sys
n = int(sys.argv[1])

print(" " + ch * n)

i = 0
while i < n:
   print(ch + " " * n + ch)
   i = i + 1

print(" " + ch * n)
