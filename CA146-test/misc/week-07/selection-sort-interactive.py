#!/usr/bin/env python

import random
import os

n = 10
a = []

i = 0
while i < n:
   a.append(random.randint(0,20))
   i = i + 1

def show(a, ii, p=None):
   print
   os.system("clear")
   s = ""
   i = 0
   while i < len(a):
      s += "%3d" % a[i]
      i = i + 1
   if p != None:
      print " " * (3 * p + 2) + "p", "=", p
      print " " * (3 * p + 2) + "|"
   else:
      print
      print
   print s
   print " " * (3 * ii + 2) + "|"
   print " " * (3 * ii + 2) + "i", "=", ii
   s = raw_input()

i = 0
while i < len(a):
   show(a,i)
   # loop invariant:
   #   - a[p] is the minimum value in a[i:j]
   p = i
   j = i + 1
   while j < len(a):
      if a[j] < a[p]:
         p = j
      j = j + 1

   show(a,i,p)

   # swap a[i] and a[p]
   tmp = a[p]
   a[p] = a[i]
   a[i] = tmp

   show(a,i,p)

   i = i + 1

i = 0
while i < len(a):
   print a[i]
   i = i + 1

