#!/usr/bin/env python

import sys

with open(sys.argv[1]) as f:
   ns = f.read().split()

total = 0

i = 0
while i < len(ns):
   total = total + int(ns[i])
   i = i + 1

print total
