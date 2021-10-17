#!/usr/bin/env python3

s = input()
while s != "end":
   if s[len(s) - 3:] == ".py":
      i = 0
      while i < len(s) and s[len(s) - i - 1] != "/":
         i = i + 1

      print(s[len(s) - i:])
   s = input()
