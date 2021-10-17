#!/usr/bin/env python3

curr = int(input())

if True:
   i = 0
   while i < 5:
      prev = curr
      curr = int(input())
      if curr < prev:
         print("lower")
      elif curr == prev:
         print("equal")
      else:
         print("higher")

      i = i + 1

# The if statement above is not needed.
#
# It is only there to ensure that the different parts of this
# implementation align with those in the next solution.
