#!/usr/bin/env python

import sys
import os

try:
   import func_contains
   import func_bsearch
except Exception as e:
   sys.stderr.write("error: failed to import test file\n")
   sys.stderr.write(str(e))
   sys.stderr.write("\n")
   sys.exit(1)

with open("func_contains.py") as f:
   words = f.read().split()
   if "in" in words:
      print "Your solution must not contain the word \"in\"."
   if "while" in words:
      print "Your solution must not contain the word \"while\"."
   if "True" in words:
      print "Your solution must not contain the word \"True\"."

#    0  1  2  3  4   5   6   7   8   9
a = [2, 4, 4, 7, 10, 10, 11, 20, 25]

print "test list:", a

low = min(a) - 1
high = max(a) + 2

for q in range(low,high):
   func_bsearch.reset()
   print "test q={} expected={} actual={}".format(q, (q in a), func_contains.contains(a,q))
   if not func_bsearch.is_called():
      print "   func_bsearch.bsearch(a,q) not called"

