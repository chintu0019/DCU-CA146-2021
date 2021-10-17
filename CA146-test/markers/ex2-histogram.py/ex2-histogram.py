#!/usr/bin/env python

a = []

s = raw_input()
while s != "end":
   a.append(int(s))
   s = raw_input()

maximum = 0

i = 0
while i < len(a):
   if maximum < a[i]:
      maximum = a[i]
   i = i + 1

i = 0
while i < maximum:
   value = maximum - i
   s = "|"
   j = 0
   while j < len(a):
      if value <= a[j]:
         s += "*"
      else:
         s += " "
      j = j + 1
   print s
   i = i + 1

print "|" + "-" * len(a)
