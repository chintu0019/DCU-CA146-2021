#!/usr/bin/env python3

import sys

ns = []

i = 1
while i < len(sys.argv):
   with open(sys.argv[i]) as f:
      ns += f.read().split()
   i = i + 1

total = 0

i = 0
while i < len(ns):
   total = total + int(ns[i])
   i = i + 1

print(total)
