#!/usr/bin/env python

s = raw_input()
a = []

i = 0
while i < len(s):
   a.append(s[i])
   i = i + 1

i = 0
while i < len(a)/2:
   tmp = a[i]
   a[i] = a[len(a) - i - 1]
   a[len(a) - i - 1] = tmp
   i = i + 1

t = ""
i = 0
while i < len(a):
   t = t + a[i]
   i = i + 1

print t
