#!/usr/bin/env python3

curr = int(input())

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
