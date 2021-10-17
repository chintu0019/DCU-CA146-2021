#!/usr/bin/env python

value = 0

n = input()
while n != 0:
   if n % 2 == 0:
      value = value + ((n - 100) % 10) * 2
   else:
      value = value + (4 - n)
   n = input()

print value
