#!/usr/bin/env python

a = []

s = raw_input()
while s != "end":
   a.append(int(s))
   s = raw_input()

# We are told in the task statement that the input is non-empty.
assert 0 < len(a)

# Approach:
#
# 1. Sort the list.
# 2. Find the longest run.

# 1. Insertion sort.
i = 1
while i < len(a):
   p = i
   v = a[i]
   while 0 < p and v < a[p - 1]:
      a[p] = a[p - 1]
      p = p - 1
   a[p] = v
   i = i + 1

# 2. Find the longest run.
#
# v is the value in the run, and
# n is the number of occurrences of v.
#
# Note... We are told in the task statement that the input is non-empty;
# therefore, we are guaranteed that at least one run exists.  So,
# initialising v and n as below, they will be overwritten within the loop
# (lines 52 and 53) at least once.

v = None
n = 0

i = 0
while i < len(a):
   j = i + 1                           # Linear search.
   while j < len(a) and a[j] == a[i]:  #
      j = j + 1                        #

   # j - i is the length of the run starting at position i.
   assert 0 < j - i

   if n < j - i:
      v = a[i]                         # We have found a new longest run.
      n = j - i                        #

   assert i < j
   i = j                               # Move on to the next run.

print v, n
