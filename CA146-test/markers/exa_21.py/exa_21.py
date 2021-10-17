#!/usr/bin/env python

def first_odd_position(a):
   i = 0
   while i < len(a) and a[i] % 2 != 1:
      i = i + 1
   return i
