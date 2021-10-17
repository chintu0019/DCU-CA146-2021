#!/usr/bin/env python

import sys

n = int(sys.argv[1])

primes = [True] * n

candidate = 2
while candidate < n:
   if primes[candidate]:
      print candidate
      i = candidate * 2
      while i < n:
         primes[i] = False
         i += candidate

   candidate += 1
