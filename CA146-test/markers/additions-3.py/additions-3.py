#!/usr/bin/env python3

total = 0
while total != 1000:
   s = input()
   j = 0
   while j < len(s) and s[j] != "+":
      j += 1

   total = int(s[:j]) + int(s[j + 1:])
   print(total)
