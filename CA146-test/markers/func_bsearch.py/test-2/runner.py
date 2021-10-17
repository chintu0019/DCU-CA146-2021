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

try:
   import func_bsearch
except Exception as e:
   sys.stderr.write("error: failed to import test file\n")
   sys.stderr.write(str(e))
   sys.stderr.write("\n")
   sys.exit(1)

a = map(int,sys.stdin.read().split())

low = min(a) - 2
high = max(a) + 2

print "a contains", len(a), "integers."
print "running", high - low + 1, "tests"

for q in range(low,high):
   assert bsearch(a,q) == func_bsearch.bsearch(a,q)

print "ok"
