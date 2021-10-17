#!/usr/bin/env python

a = []

line = raw_input()
while line != "end":
   a.append(int(line))
   line = raw_input()

v = int(raw_input())

p = len(a)
while 0 < p and v < a[p - 1]:
   p = p - 1

print p
