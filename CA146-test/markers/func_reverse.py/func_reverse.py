#!/usr/bin/env python

def swap(a, i, j):
   t = a[i]
   a[i] = a[j]
   a[j] = t

def reverse(a):
   i = 0
   while i < len(a) / 2:
      j = len(a) - 1 - i
      swap(a, i, j)
      i = i + 1

if __name__ == "__main__":
   a = []
   reverse(a)
   print a

   a = ['apple', 123, 'orange', True]
   reverse(a)
   print a

   a = ['apple', 123, 'orange', True, 'odd']
   reverse(a)
   print a
