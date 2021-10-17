#!/usr/bin/env python3

a = []

line = input()
while line != "end":
   a.append(int(line))
   line = input()

# loop invariant:
#   - a[0:i] is sorted
#   - each of a[0:i] is <= each of a[i:]

i = 0
while i < len(a):
   # loop invariant:
   #   - a[p] is the minimum value in a[i:j]
   p = i
   j = i + 1
   while j < len(a):
      if a[j] < a[p]:
         p = j
      j = j + 1

   # swap a[i] and a[p]
   tmp = a[p]
   a[p] = a[i]
   a[i] = tmp

   i = i + 1

i = 0
while i < len(a):
   print(a[i])
   i = i + 1
