#!/usr/bin/env python

import random
import os
import sys
task = os.environ["TASK"]

def flatten(a):
   return str(map(str, a))

def test(a):
   b = a[:]
   b.reverse()
   print "testing: a =", a
   execfile(task)
   print "  expecting:", b
   print "     actual:", a
   if flatten(a) != flatten(b):
      print "      error!"
      sys.exit(1)

print "testing various cases..."

for i in range(12):
   a = []
   for j in range(i):
      a.append(random.randint(0,15))
   test(a)
   a = []
   for j in range(i):
      a.append(random.randint(0,15))
   test(a)

print "ok"
