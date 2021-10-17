#!/usr/bin/env python

n = input()

i = 0
while i < n:
   print curr
   old_curr = curr
   curr = prev + curr
   prev = old_curr
   i = i + 1

