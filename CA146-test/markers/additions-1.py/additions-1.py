#!/usr/bin/env python3

n = 10

i = 0
while i < n:
   s = input()
   j = 0
   while j < len(s) and s[j] != "+":
      j += 1

   print(int(s[:j]) + int(s[j + 1:]))
   i = i + 1
