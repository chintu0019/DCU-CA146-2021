#!/usr/bin/env python

# Read a sequence of integers from standard input and output only
# the smallest ten of them in increasing numerical order (one per
# line).

# The obvious approach (not taken here) is to sort the list.  Then,
# the following would print out the first (smallest) ten elements:
#
# i = 0
# while i < len(a) and i < 10:
#    print a[i]
#    i = i + 1

# Approach...
# We retain the ten (n) smallest values only.  At the end of each
# iteration, we discard the 11th-smallest element (if necessary).
#
# The values are maintained in increasing numeric order.  Therefore,
# for each new value, that value must only be inserted into position
# within an otherwise sorted list.  This is done using essentially
# the inner loop from the insertion sort algorithm.

n = 10
a = []

s = raw_input()
while s != "end":
   v = int(s)
   a.append(None)              # Create space for the new value.

   p = len(a) - 1              # This is the inner loop from insertion sort.
   while 0 < p and v < a[p-1]: # Find the position p at which v should be
      a[p] = a[p-1]            # inserted, moving displaced elements up to
      p = p - 1                # make space.

   a[p] = v                    # Install the new value.

   if n < len(a):              # Discard the 11th element, if necessary.
      a.pop()                  #

   s = raw_input()

i = 0
while i < len(a):
   print a[i]
   i = i + 1

