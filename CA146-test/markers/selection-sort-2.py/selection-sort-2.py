#!/usr/bin/env python3

a = []

line = input()
while line != "end":
   a.append(int(line))
   line = input()

p = int(input())

j = p + 1
while j < len(a):
   if a[j] < a[p]:
      p = j
   j = j + 1

print(p)
