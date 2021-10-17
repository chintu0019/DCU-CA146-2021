#!/usr/bin/env python3

a = []
b = []

# Read the first list.
line = input()
while line != "end":
   a.append(int(line))
   line = input()

# Read the second list list.
line = input()
while line != "end":
   b.append(int(line))
   line = input()

# Merge the lists.
i = 0
j = 0
while i < len(a) and j < len(b):
   if a[i] < b[j]:
      print(a[i])
      i += 1
   else:
      print(b[j])
      j += 1

# Output any elements remaining from a.
while i < len(a):
   print(a[i])
   i += 1

# Output any elements remaining from b.
while j < len(b):
   print(b[j])
   j += 1
