#!/usr/bin/env python

import sys
import os

def count(a,q):
   x = func_bsearch.bsearch(a,q)
   y = func_bsearch.bsearch(a,q+1)

   return y - x
try:
   import func_count
   import func_bsearch
except Exception as e:
   sys.stderr.write("error: failed to import test file\n")
   sys.stderr.write(str(e))
   sys.stderr.write("\n")
   sys.exit(1)


with open("func_count.py") as f:
   words = f.read().split()
   if "in" in words:
      print "Your solution must not contain the word \"in\"."
   if "while" in words:
      print "Your solution must not contain the word \"while\"."

#    0  1  2  3  4   5   6   7   8   9
a = [2, 4, 4, 7, 10, 10, 11, 20, 25, 25, 25, 25, 26]

print "test list:", a

low = min(a) - 1
high = max(a) + 2

for q in range(low,high):
   func_bsearch.reset()
   print "test q={} expected={} actual={}".format(q, count(a,q), func_count.count(a,q))
   if not func_bsearch.is_called():
      print "   func_bsearch.bsearch(a,q) not called the correct number of times"
