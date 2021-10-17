#!/usr/bin/env python3

n = int(input())

i = 0
while i < n:
   curr = i + 1
   if curr % 15 == 0:
      print("fizz-buzz")
   elif curr % 3 == 0:
      print("fizz")
   elif curr % 5 == 0:
      print("buzz")
   else:
      print(curr)
   i = i + 1
