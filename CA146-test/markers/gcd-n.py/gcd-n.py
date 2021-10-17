#!/usr/bin/env python

import sys

def gcd(a,b):
   if a < b:
      a, b = b, a
   while 0 < b:
      a, b = b, a % b
   return a

common_divisor = int(sys.argv[1])
a = sys.argv[2:]

i = 0
while i < len(a):
   common_divisor = gcd(int(a[i]), common_divisor)
   i = i + 1

print common_divisor
