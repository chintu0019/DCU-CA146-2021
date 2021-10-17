#!/usr/bin/env python

import random
import time

M = 1000   # Number of test iterations.
MAX = 200  # Use integer values in the range 0 to this.
N = 40     # Number of test points to use.

# Test whether points t (top), m (middle) and b (bottom) are in a line.
# Because we're using integer division, we need to make sure that we're not
# getting false positives due to rounding.  Specifically, t and b must either
# both be odd or both be even.
def is_line(t, m, b):
   return t % 2 == b % 2 and (t + b) / 2 == m

# This version is O(n^3).
def count_lines_slow(top, middle, bottom):
   count = 0
   for t in top:
      for m in middle:
         for b in bottom:
            if is_line(t, m, b):
               count += 1
   return count

# Take N to be len(top).
# Take M to be len(middle).
# Take P to be len(bottom).
#
# This algorithm is worst case O(N*M + P).
# The average case seems to be better than O(N*M) (but I can't prove it).
#
# This counts the number of lines with a negative gradient (and the vertical
# lines).  We call it twice, the second time with the top and bottom swapped to
# get the lines with positive gradients.  We double count the vertical lines,
# and then compensate later.
#
def count_lines_negative(top, middle, bottom):
   # The set of points in bottom; building this is O(len(bottom)), lookup is O(1).
   b_set = set(bottom)

   # The maximum value in bottom; building this is again O(len(bottom)).
   b_max = max(bottom)

   count = vertical_count = 0

   t = m = 0
   while t < len(top):
      # Advance m such that top[t] <= middle[m].
      while m < len(middle) and middle[m] < top[t]:
         m += 1

      # Next, we walk from position m in middle to the end, looking for matches
      # (loop variable "mm").  The second part of the condition below allows us
      # to stop early if the value which would have to be in bottom for there
      # to be a match is bigger than the largest actual value bottom.
      mm = m
      while mm < len(middle) and top[t] + (middle[mm] - top[t]) * 2 <= b_max:
         candidate_b = top[t] + (middle[mm] - top[t]) * 2
         if candidate_b in b_set:
            count += 1
            if top[t] == middle[mm]:
               vertical_count += 1

         mm += 1
      t += 1

   return count, vertical_count

def count_lines_fast(top, middle, bottom):
   # Count the negative-gradient and the positive-gradient lines.
   [count_negative, vertical_count_negative] = count_lines_negative(top, middle, bottom)
   [count_positive, vertical_count_positive] = count_lines_negative(bottom, middle, top)

   # The number of vertical lines should be the same.
   assert vertical_count_positive == vertical_count_negative

   # We double counted the vertical lines, so subtract that off.
   return count_negative + count_positive - vertical_count_positive

MAX = 1000
N = 500
def generate_line():
   return sorted(set([random.randint(0,MAX) for i in range(N)]))

import sys

if 1 < len(sys.argv):

   print " ".join(map(str, generate_line()))
   print " ".join(map(str, generate_line()))
   print " ".join(map(str, generate_line()))
   print N

else:
   elapsed_slow = 0
   elapsed_fast = 0

   top = map(int, sys.stdin.readline().split())
   middle = map(int, sys.stdin.readline().split())
   bottom = map(int, sys.stdin.readline().split())

   start = time.time()
   # slow_count = count_lines_slow(top, middle, bottom)
   slow_count = count_lines_fast(top, middle, bottom)
   elapsed_slow += time.time() - start

   start = time.time()
   fast_count = count_lines_fast(top, middle, bottom)
   elapsed_fast += time.time() - start

   assert fast_count == slow_count
   print fast_count
