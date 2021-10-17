#!/usr/bin/env python

import sys

n = 3

prize = {
      0: 0,
      1: 1,
      2: 5,
      3: 100,
}

draw = {}

i = 1
while i < len(sys.argv):
   draw[sys.argv[i]] = True
   i = i + 1

lines = sys.stdin.readlines()

i = 0
while i < len(lines):
   count = 0
   tokens = lines[i].split()

   j = 0
   while j < n:
      if tokens[j] in draw:
         count += 1
      j = j + 1

   print prize[count]
   i = i + 1





