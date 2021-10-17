#!/usr/bin/env python

nums = []

# Read in lines.
line = raw_input()
while line != "end":
   nums.append(int(line))
   line = raw_input()

if 0 < len(nums):
   # Calculate total.
   total = 0.0
   for v in nums:
      total = total + v

   # Calculate average.
   average = total / len(nums)

   # Output differences from the average.
   for v in nums:
      print v - average
