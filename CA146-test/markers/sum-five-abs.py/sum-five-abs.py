#!/usr/bin/env python3

total = 0

i = 0
while i < 5:
   n = int(input())
   if 0 < n:
      total = total + n
   else:
      total = total - n
   i = i + 1

print(total)