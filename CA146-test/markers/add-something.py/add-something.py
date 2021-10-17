#!/usr/bin/env python3

a = []

line = input()
while line != "end":
   a.append(int(line))
   line = input()

n = int(input())

i = 0
while i < len(a):
   print(a[i] + n)
   i = i + 1
