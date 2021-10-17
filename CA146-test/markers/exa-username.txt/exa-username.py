#!/usr/bin/env python3

s = input()
t = ""

i = 0
while i < len(s):
   if "A" <= s[i] and s[i] <= "Z":
      t = t + s[i+1]
   i = i + 1

print(t)
