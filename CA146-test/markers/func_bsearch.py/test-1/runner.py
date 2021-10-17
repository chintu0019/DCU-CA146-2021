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

a = map(int,sorted("-5 -8 20 89 89 89 -5 0 0 89 56 23 ".split()))

print "a:", a

low = min(a) - 1
high = max(a) + 2

for q in range(low,high):
   print "test q={} expected={} actual={}".format(q, bsearch(a,q), func_bsearch.bsearch(a,q))
