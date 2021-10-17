#!/usr/bin/env python3

import sys

ns = sys.stdin.read().split()
total = 0

i = 0
while i < len(ns):
   total = total + int(ns[i])
   i = i + 1

print(total)
