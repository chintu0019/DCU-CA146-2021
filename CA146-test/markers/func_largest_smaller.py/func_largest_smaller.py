#!/usr/bin/env python

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

def largest_smaller(a,q):
   x = bsearch(a,q)

   return a[x-1]
