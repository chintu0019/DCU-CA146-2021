#!/usr/bin/env python3

# This is an approximation of bubblesort.

a = int(input())
b = int(input())
c = int(input())

if b < a:
   tmp = b
   b = a
   a = tmp

if c < b:
   tmp = b
   b = c
   c = tmp

# At this point, the largest value is in c, so we don't need to consider
# c any more.

if b < a:
   tmp = b
   b = a
   a = tmp

print(a)
print(b)
print(c)
