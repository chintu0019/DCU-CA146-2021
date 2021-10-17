#!/usr/bin/env python

a = []

s = raw_input()
while s != "end":
   a.append(int(s))
   s = raw_input()

n = input()

i = 0
while i < len(a) and a[i] < n:
   print a[i]
   i = i + 1

print n

while i < len(a):
   print a[i]
   i = i + 1
