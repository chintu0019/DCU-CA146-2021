#!/usr/bin/env python

a = []
b = []

s = raw_input()
while s != "end":
   a.append(s)
   s = raw_input()


s = raw_input()
while s != "end":
   b.append(s)
   s = raw_input()

i = 0
while i < len(a):
   j = 0
   while j < len(b) and b[j] != a[i]:
      j = j + 1

   if not (j < len(b)):
      print a[i]

   i = i + 1
