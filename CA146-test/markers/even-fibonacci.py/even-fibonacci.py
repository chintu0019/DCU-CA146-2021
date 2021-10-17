#!/usr/bin/env python

import sys
n = int(sys.argv[1])

prev = curr = 1
total = 0

while curr < n:
   if curr % 2 == 0:
      total += curr

   prev, curr = curr, prev + curr

print total
