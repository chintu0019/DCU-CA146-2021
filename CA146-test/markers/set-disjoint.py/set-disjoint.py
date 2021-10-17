#!/usr/bin/env python3

d = {}

with open("a.txt") as f:
   a = f.read().split()

i = 0
while i < len(a):
   d[a[i]] = True
   i = i + 1

with open("b.txt") as f:
   a = f.read().split()

i = 0                                # Linear search.
while i < len(a) and a[i] not in d:  #
   i = i + 1                         #

if i < len(a):
   print("intersecting")
else:
   print("disjoint")
