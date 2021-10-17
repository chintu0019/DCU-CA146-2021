#!/usr/bin/env python

import func_bsearch

def count(a, q):
   # We search for the position of q and the position of q+1.
   # The difference between these positions is the number of
   # occurrences of q.
   x = func_bsearch.bsearch(a, q)
   y = func_bsearch.bsearch(a, q + 1)

   return y - x
