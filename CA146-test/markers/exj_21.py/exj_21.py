#!/usr/bin/env python

def largest_position(a):
   p = 0
   i = 1
   while i < len(a):
      if a[p] < a[i]:
         p = i
      i = i + 1
   return p
