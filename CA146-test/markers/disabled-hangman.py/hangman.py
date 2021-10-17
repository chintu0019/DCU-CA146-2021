#!/usr/bin/env python

import sys

s = sys.argv[1]
t = ""
c = 0
g = 5

i = 0
while i < len(s):
   if s[i].islower() or s[i].isupper():
      t += "_"
      c += 1
   else:
      t += s[i]
   i += 1

while c and g:
   print t
   ch = raw_input("guess: ")
   hit = False

   i = 0
   while i < len(s):
      if t[i] == "_" and ch.lower() == s[i].lower():
         t = t[:i] + s[i] + t[i+1:]
         c -= 1
         hit = True
      i += 1

   if not hit:
      g -= 1

if g:
   print "you win:", s
else:
   print "you lose:", s
