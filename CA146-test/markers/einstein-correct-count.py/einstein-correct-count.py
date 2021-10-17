#!/usr/bin/env python3

total = 0

s = input()
while s != "end":
   if s[len(s) - 8:] == ".correct":
      total = total + 1
   s = input()

print(total)
