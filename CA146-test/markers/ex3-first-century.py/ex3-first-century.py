#!/usr/bin/env python3

import sys
nums = sys.stdin.read().split()

i = 0
while i < len(nums) and int(nums[i]) < 100:
   i = i + 1

if i < len(nums):
   print(nums[i])
else:
   print("none")
