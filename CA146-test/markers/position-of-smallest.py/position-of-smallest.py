#!/usr/bin/env python3

if __name__ == "__main__":
   a = [49, 32, 39, 13, 30, 12, 14, 19, 31, 31]

p = 0

i = 0
while i < len(a):
   if a[i] < a[p]:
      p = i
   i = i + 1

print(p)
