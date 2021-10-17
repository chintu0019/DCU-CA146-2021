#!/usr/bin/env python3

s = input()
n = 0

i = 0
while i < len(s):
   if "a" <= s[i] and s[i] <= "z":
      n = n * 2
      if "m" < s[i]:
         n = n + 1
   i = i + 1

print(n)
