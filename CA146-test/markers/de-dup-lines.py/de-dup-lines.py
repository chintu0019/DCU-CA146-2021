#!/usr/bin/env python3

seen = []

line = input()
while line != "end":
   i = 0                                     # Linear search.
   while i < len(seen) and seen[i] != line:  #
      i = i + 1                              #

   if i == len(seen):
      print(line)
      seen.append(line)

   line = input()
