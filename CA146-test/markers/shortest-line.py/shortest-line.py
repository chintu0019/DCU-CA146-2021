#!/usr/bin/env python3

shortest = len(input())

s = input()
while s != "end":
   n = len(s)
   if n < shortest:
      shortest = n
   s = input()

print(shortest)
