#!/usr/bin/env python3

a = []

n = int(input())
while n != 0:
   if 0 < n:
      print(n)               # Positive.
   else:
      a.append(n)            # Save the negative numbers for later.
   n = int(input())

i = 0
while i < len(a):
   print(a[i])               # Print out the negative numbers.
   i = i + 1
