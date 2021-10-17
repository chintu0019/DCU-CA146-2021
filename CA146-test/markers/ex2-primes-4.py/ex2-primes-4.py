#!/usr/bin/env python

import sys

n = int(sys.argv[1])

def is_prime(n):
   for c in range(2,n):
      if n % c == 0:
         return False
   return True

i = 2
while i < n:
   if is_prime(i):
      print i
   i = i + 1
