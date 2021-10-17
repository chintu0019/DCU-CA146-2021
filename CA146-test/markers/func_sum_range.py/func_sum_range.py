#!/usr/bin/env python

import func_bsearch

def sum_range(a, low, high):
   total = 0
   # We really cannot do any better than using binary search
   # to find the start position, and then linear search to
   # scan to the end position, adding up the elements as we
   # fo along.
   i = func_bsearch.bsearch(a, low)
   while i < len(a) and a[i] < high:
      total += a[i]
      i = i + 1
   return total

if __name__ == "__main__":
   a = [1, 2, 4, 4, 5, 5, 6, 7, 8]
   print sum_range(a, 3, 7)
