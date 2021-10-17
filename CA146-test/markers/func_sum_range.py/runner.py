#!/usr/bin/env python

import sys
import os

def sum_range(a, low, high):
   total = 0
   i = func_bsearch.bsearch(a, low)
   while i < len(a) and a[i] < high:
      total += a[i]
      i = i + 1
   return total

try:
   import func_sum_range
   import func_bsearch
except Exception as e:
   sys.stderr.write("error: failed to import test file\n")
   sys.stderr.write(str(e))
   sys.stderr.write("\n")
   sys.exit(1)

with open("func_sum_range.py") as f:
   words = f.read().split()
   if "in" in words:
      print "Your solution must not contain the word \"in\"."

#    0  1  2  3  4   5   6   7   8   9
a = [2, 4, 4, 7, 10, 10, 11, 20, 25, 25, 25, 25, 26]

print "test list:", a

low = min(a) - 1
high = max(a) + 2
length = 5

for q in range(low,high):
   func_bsearch.reset()
   print "test low={} high={} expected={} actual={}".format(q, q + length, sum_range(a,q,q+length), func_sum_range.sum_range(a,q,q+length))
   if not func_bsearch.is_called():
      print "   func_bsearch.bsearch(a,q) not called the correct number of times"

   if length % 2 == 0:
      length -= 3
   else:
      length += 3

