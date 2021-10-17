#!/usr/bin/env python3


s = input()
while s != "end":
   line = ""

   i = 0
   while i < len(s):
      if "a" <= s[i] <= "z" or "A" <= s[i] <= "Z":
         line = line + s[i]
      i = i + 1

   print(line)
   s = input()
