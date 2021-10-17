#!/usr/bin/env python3

import random
import os
import sys
task = os.environ["TASK"]

def flatten(a):
   return "/".join(map(str, a))

def test(a):
   b = a[:]
   b.reverse()
   print("testing: a =", a)
   with open(task) as f:
      exec(f.read())
   print("  expecting:", b)
   print("     actual:", a)
   if flatten(a) != flatten(b):
      print("      error!")
      sys.exit(1)

print("testing various cases...")

for i in range(12):
   a = []
   for j in range(i):
      a.append(random.randint(0,15))
   test(a)
   a = []
   for j in range(i):
      a.append(random.randint(0,15))
   test(a)

print("ok")
