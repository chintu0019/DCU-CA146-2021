#!/usr/bin/env python3

n = int(input())

boundary = "*" * n
line = "*" + " " * ((n - 3) // 2) + "*" + " " * ((n - 3) // 2) + "*"

i = 0
while i < n:
   if i == 0 or i == n - 1 or i == n // 2:
      print(boundary)
   else:
      print(line)
   i = i + 1
