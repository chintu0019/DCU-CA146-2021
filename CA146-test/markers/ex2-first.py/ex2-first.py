#!/usr/bin/env python3

s = input()

i = 0
while i < len(s) and not ("START" <= s[i] and s[i] <= "END"):
   i = i + 1

if i < len(s):
   print(s[i])
