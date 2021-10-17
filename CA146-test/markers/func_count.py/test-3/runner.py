#!/usr/bin/env python

import sys
import os

def bsearch(a,q):
   """
   a: a sorted list
   q: a query

   If q is present in a:
      then return the *first* position at which q occurs in a.

   Otherwise:
      return the position p such that, were q inserted at position p, the list would remain sorted.
      (Note: that position could be the position *after* the end of the list.)
   """

   low = 0
   high = len(a)

   while low < high:
      mid = low + (high - low) / 2
      assert(low <= mid < high)

      if a[mid] < q:
         low = mid + 1
      else:
         high = mid

   return low

def count(a,q):
   return bsearch(a,q+1) - bsearch(a,q)

try:
   import func_count
except Exception as e:
   sys.stderr.write("error: failed to import test file\n")
   sys.stderr.write(str(e))
   sys.stderr.write("\n")
   sys.exit(1)

a = [100] * 10000

low = 0
high = 30000

print "a contains", len(a), "integers."
print "running", high - low + 1, "tests"

for q in range(low,high):
   assert count(a,q) == func_count.count(a,q)

print "ok"
