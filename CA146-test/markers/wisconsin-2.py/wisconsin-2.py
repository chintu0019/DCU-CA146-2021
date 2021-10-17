#!/usr/bin/env python3

state = "WI"
total = 0

# Discard the header line.
s = input()

s = input()
while s != "end":
   i = 0
   while i < len(s) and s[i] != ",":
      i = i + 1

   if i < len(s):
      code = s[i + 1:i + 3]
      if code == state:
         total = total + 1

   s = input()

print(total)
