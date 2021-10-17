#!/usr/bin/env python

n = input()

i = 2
while i < n and n % i != 0:
   i = i + 1

print i == n
