#!/usr/bin/env python3

total = 0


n = int(input())
while n != 0:
   if 0 < n:
      total = total + n
   else:
      total = total - n

   n = int(input())

print(total)
