#!/usr/bin/env python3

n = int(input())
prev = 0
curr = 1

i = 0
while i < n:
   print(prev)
   old_curr = curr
   curr = curr + prev
   prev = old_curr
   i = i + 1
