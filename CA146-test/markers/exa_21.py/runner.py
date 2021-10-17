#!/usr/bin/env python

import sys
import exa_21
import random

a = [2, 4, 2, 42, 42, 4, 2, 4, 2, 4]
a = a + a + [7]

def first_odd_position(a):
   i = 0
   while i < len(a) and a[i] % 2 != 1:
      i = i + 1
   return i

print "running 100 test cases..."
print

for i in range(100):
   random.shuffle(a)
   expected = first_odd_position(a)
   actual = exa_21.first_odd_position(a)
   if actual != expected:
      print "error found for the following list:"
      print " ", a
      print "expected:", expected
      print "actual:", actual
      sys.exit(1)

print "ok"
