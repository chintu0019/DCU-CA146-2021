#!/usr/bin/env python3

i = 0
while i < len(a) / 2:
   t = a[i]
   a[i] = a[len(a) - i - 1]
   a[len(a) - i - 1] = t
   i = i + 1
