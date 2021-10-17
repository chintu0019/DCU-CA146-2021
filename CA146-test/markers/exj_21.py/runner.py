#!/usr/bin/env python

import sys
import exj_21
import random

a = range(12)
a = a + a

def lp(a):
   p = 0
   i = 1
   while i < len(a):
      if a[p] < a[i]:
         p = i
      i = i + 1
   return p

print "running 100 test cases..."
print

for i in range(100):
   random.shuffle(a)
   expected = lp(a)
   actual = exj_21.largest_position(a)
   if actual != expected:
      print "error found for the following list:"
      print " ", a
      print "expected:", expected
      print "actual:", actual
      sys.exit(1)

print "ok"
