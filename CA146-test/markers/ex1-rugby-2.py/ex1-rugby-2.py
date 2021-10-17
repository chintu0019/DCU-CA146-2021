#!/usr/bin/env python

score = 0
n = input()

i = 0
while i < n:
   s = raw_input()
   if s == "try":
      score = score + 5
   elif s == "penalty":
      score = score + 3
   else:
      score = score + 2
   i = i + 1

print score
