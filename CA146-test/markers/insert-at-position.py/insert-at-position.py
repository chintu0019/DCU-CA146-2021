#!/usr/bin/env python

if __name__ == "__main__":
   a = [1, 5, 6, 6, 10, 12]
   p = 4
   v = 8

a.append(0)

i = 0
while i < len(a) - p:
   a[len(a) - i - 1] = a[len(a) - i - 2]
   i = i + 1

a[p] = v
