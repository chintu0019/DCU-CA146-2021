#!/usr/bin/env python3

s = input()
while s != "end":
   i = 0
   while i < len(s) and s[i] != ":":
      i = i + 1

   # Linear search backwards to locate the final colon.
   j = 0
   while j < len(s) and s[len(s) - j - 1] != ":":
      j = j + 1

   print(s[:i], s[len(s) - j:])
   s = input()
