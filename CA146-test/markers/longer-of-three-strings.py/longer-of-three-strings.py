#!/usr/bin/env python3

a = input()
b = input()
c = input()

if len(b) < len(a) and len(c) < len(a):
   print (a)
elif len(b) < len(c):
   print (c)
else:
   print (b)
