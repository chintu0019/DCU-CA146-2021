#!/usr/bin/env python

s = raw_input()
n = 0

i = 0
while i < len(s):
   if "0" <= s[i] and s[i] < "5":
      n = n + int(s[i])
   elif "5" <= s[i] and s[i] <= "9":
      n = n + (int(s[i]) - 5) * 10
   else:
      n = n / 0
   i = i + 1

print n
