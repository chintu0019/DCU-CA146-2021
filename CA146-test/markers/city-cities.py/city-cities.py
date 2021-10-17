#!/usr/bin/env python3

# Discard the header line.
s = input()

s = input()
while s != "end":
   # Find the position of the first comma, and then look backwards from there.
   i = 0
   while i < len(s) and s[i] != ",":
      i = i + 1

   if i < len(s) and 6 <= i and s[i - 4:i] == "City":
      print(s[:i])

   s = input()
