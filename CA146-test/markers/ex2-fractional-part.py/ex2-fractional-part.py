#!/usr/bin/env python3

s = input()
while s != "end":
   i = 0
   while i < len(s) and s[i] != ".":
      i = i + 1

   if i < len(s):
      print(s[i + 1:])
   else:
      print(0)

   s = input()
