#!/usr/bin/env python3

import sys

with open(sys.argv[1]) as f:
   nums = f.read().split()

total = 0

i = 0
while i < len(nums):
   total = total + int(nums[i])
   i = i + 1

print(total)
