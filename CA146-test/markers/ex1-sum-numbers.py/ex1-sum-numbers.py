#!/usr/bin/env python3

n = int(input())
total = 0

i = 0
while i < n:
   s = input()
   if s == "one":
      total = total + 1
   elif s == "two":
      total = total + 2
   elif s == "three":
      total = total + 3
   elif s == "four":
      total = total + 4
   else:
      total = total + 5
   i = i + 1

print(total)
