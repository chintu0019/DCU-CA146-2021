#!/usr/bin/env python3

a = []

n = int(input())
while n != 0:
   a.append(n)
   n = int(input())

i = 0
while i < len(a):
   print(a[len(a) - i - 1])
   i = i + 1
