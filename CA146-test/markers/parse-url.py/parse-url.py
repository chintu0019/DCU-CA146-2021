#!/usr/bin/env python

s = raw_input()

i = 0
while i < len(s) and s[i] != ":":
   i = i + 1

if i < len(s):
   print "scheme:", s[0:i]

p = i + 3
i = p
while i < len(s) and s[i] != "/":
   i = i + 1

if i < len(s):
   print "host:", s[p:i]

p = i
while i < len(s) and s[i] != "?":
   i = i + 1

if p < i:
   print "path:", s[p:i]

p = i + 1
while p < len(s):
   i = p

   i = p
   while i < len(s) and s[i] != "&":
      i = i + 1

   if p < i:
      j = p
      while j < i and s[j] != "=":
         j = j + 1

      if j < i:
         print "query:", s[p:j], s[j + 1:i]
      else:
         print "query:", s[p:j], True

   p = i + 1
