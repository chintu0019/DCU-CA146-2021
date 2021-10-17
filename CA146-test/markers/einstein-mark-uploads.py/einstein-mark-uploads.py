#!/usr/bin/env python

user = ""
count = 0
pos = 10 + 1 + 5 + 1  # Date is 10, module is 5.

s = raw_input()
while s != "end":
   i = pos
   while i < len(s) and s[i] != "/":
      i = i + 1

   curr = s[pos:i]
   if curr != user:
      if 0 < len(user):
         print user, count
      user = curr
      count = 0

   if s[len(s) - 8:] == ".correct":
      count = count + 1

   s = raw_input()

if 0 < len(user):
   print user, count
